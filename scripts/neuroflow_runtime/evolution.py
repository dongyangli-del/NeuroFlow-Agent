"""Feedback ingestion, candidate generation, and shadow evaluation."""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from .evals import EvalHarness, compare_runs, load_eval_cases, run_sync, write_eval_result
from .models import (
    CandidateStatus,
    EvalPartition,
    EvolutionCandidate,
    FeedbackEvent,
    FeedbackType,
    utc_now,
)
from .privacy import sanitize_remote_text
from .providers import ModelProvider, ModelRequest
from .risk import PatchInspection, inspect_patch
from .storage import EvolutionStore
from .trace import WorkflowTrace

ALLOWED_TRANSITIONS = {
    CandidateStatus.OBSERVED: {CandidateStatus.CLUSTERED, CandidateStatus.REJECTED},
    CandidateStatus.CLUSTERED: {CandidateStatus.PROPOSED, CandidateStatus.REJECTED},
    CandidateStatus.PROPOSED: {CandidateStatus.SHADOW_TESTING, CandidateStatus.REJECTED},
    CandidateStatus.SHADOW_TESTING: {CandidateStatus.AWAITING_REVIEW, CandidateStatus.REJECTED},
    CandidateStatus.AWAITING_REVIEW: {CandidateStatus.CANARY, CandidateStatus.REJECTED},
    CandidateStatus.CANARY: {CandidateStatus.PROMOTED, CandidateStatus.ROLLED_BACK},
    CandidateStatus.PROMOTED: {CandidateStatus.ROLLED_BACK},
    CandidateStatus.REJECTED: set(),
    CandidateStatus.ROLLED_BACK: set(),
}


class EvolutionError(RuntimeError):
    pass


class EvolutionEngine:
    def __init__(self, root: Path, store: EvolutionStore | None = None) -> None:
        self.root = root.resolve()
        self.store = store or EvolutionStore(self.root)
        self.store.initialize()
        self.state_root = self.root / ".private" / "evolution"
        self.state_root.mkdir(parents=True, exist_ok=True)

    @property
    def mode(self) -> str:
        return os.environ.get("NEUROFLOW_EVOLUTION_MODE", "shadow").strip().lower()

    def ingest_trace(
        self,
        trace_path: Path,
        *,
        summary: str = "",
        event_type: FeedbackType | None = None,
        failure_tag: str = "",
        source: str = "runtime",
    ) -> list[FeedbackEvent]:
        trace = WorkflowTrace.read_json(trace_path)
        events: list[FeedbackEvent] = []
        if summary:
            events.append(
                FeedbackEvent(
                    run_id=trace.run_id,
                    event_type=event_type or FeedbackType.USER_CORRECTION,
                    summary=summary,
                    failure_tag=failure_tag,
                    source=source,
                    evidence={"trace": str(trace_path)},
                )
            )
        for step in trace.steps:
            if step.status not in {"failed", "blocked"}:
                continue
            events.append(
                FeedbackEvent(
                    run_id=trace.run_id,
                    event_type=FeedbackType.RUNTIME_FAILURE,
                    summary=step.error or f"Stage {step.name} ended with {step.status}",
                    failure_tag=step.failure_tag or f"stage:{step.name}",
                    source="trace-step",
                    evidence={"trace": str(trace_path), "stage": step.name, "module": step.module},
                )
            )
        for hook in trace.hook_events:
            if hook.status not in {"blocked", "warning"}:
                continue
            events.append(
                FeedbackEvent(
                    run_id=trace.run_id,
                    event_type=FeedbackType.GATE_FAILURE,
                    summary=hook.blocked_reason or "; ".join(hook.warnings) or f"Hook {hook.event} warned",
                    failure_tag=f"hook:{hook.event}",
                    source="runtime-hook",
                    evidence={"trace": str(trace_path), "hook": hook.event},
                )
            )
        return [self.store.add_feedback(event) for event in _deduplicate_feedback(events)]

    def create_candidate_from_patch(
        self,
        patch_text: str,
        *,
        target_component: str = "",
        feedback_ids: list[str] | None = None,
        provider: str = "manual",
        model: str = "manual",
        rationale: str = "",
        expected_gain: float = 0.0,
        parent_id: str | None = None,
    ) -> EvolutionCandidate:
        if self.mode == "off":
            raise EvolutionError("Evolution is disabled by NEUROFLOW_EVOLUTION_MODE=off")
        inspection = inspect_patch(patch_text)
        if "evals/protected.json" in inspection.paths:
            raise EvolutionError("Candidates cannot modify the protected eval set")
        if ".private/evolution/evals/hidden.json" in inspection.paths:
            raise EvolutionError("Candidates cannot modify the hidden holdout set")
        self._check_patch_applies(patch_text)
        digest = hashlib.sha256(patch_text.encode("utf-8")).hexdigest()
        resolved_parent = parent_id or f"git:{_run(['git', 'rev-parse', 'HEAD'], self.root).stdout.strip()}"
        resolved_target = target_component or ",".join(inspection.paths)
        linked_feedback = list(feedback_ids or [])
        if not linked_feedback:
            event = FeedbackEvent(
                run_id="manual-candidate",
                event_type=FeedbackType.USER_CORRECTION,
                summary=rationale or f"Manually proposed evolution for {resolved_target}",
                failure_tag=f"candidate:{resolved_target[:80]}",
                source=provider,
            )
            event = self.store.add_feedback(event)
            linked_feedback.append(event.id)
        candidate = EvolutionCandidate(
            parent_id=resolved_parent,
            target_component=resolved_target,
            status=CandidateStatus.OBSERVED,
            risk_level=inspection.risk_level,
            trigger_feedback_ids=linked_feedback,
            patch_path="",
            patch_sha256=digest,
            generator_provider=provider,
            generator_model=model,
            rationale=rationale,
            expected_gain=expected_gain,
            requires_human=inspection.requires_human,
            metadata={
                "inspection": _inspection_dict(inspection),
                "status_history": [{"from": "", "to": CandidateStatus.OBSERVED.value, "at": utc_now()}],
            },
        )
        candidate_dir = self.state_root / "candidates" / candidate.id
        candidate_dir.mkdir(parents=True, exist_ok=False)
        patch_path = candidate_dir / "candidate.patch"
        patch_path.write_text(patch_text, encoding="utf-8")
        candidate.patch_path = str(patch_path)
        self._write_incident_eval(candidate, linked_feedback)
        self.store.add_candidate(candidate)
        self.transition(candidate, CandidateStatus.CLUSTERED)
        self.transition(candidate, CandidateStatus.PROPOSED)
        self.store.mark_feedback_handled(linked_feedback)
        return candidate

    async def propose(
        self,
        executor: ModelProvider,
        *,
        feedback_ids: list[str] | None = None,
        variants: int = 2,
    ) -> list[EvolutionCandidate]:
        feedback = self.store.list_feedback(unhandled_only=True)
        if feedback_ids:
            requested = set(feedback_ids)
            feedback = [item for item in feedback if item.id in requested]
        if not feedback:
            raise EvolutionError("No unhandled feedback is available for candidate generation")
        clusters = cluster_feedback(feedback)
        cluster_key, feedback = max(clusters.items(), key=lambda item: (len(item[1]), item[0]))
        feedback_payload = [
            {
                "id": item.id,
                "event_type": item.event_type.value,
                "summary": sanitize_provider_context(item.summary),
                "failure_tag": item.failure_tag,
                "source": item.source,
            }
            for item in feedback
        ]
        context = self._candidate_context(feedback)
        candidates = []
        for variant in range(variants):
            request = ModelRequest(
                system=(
                    "You are the NeuroFlow evolution executor. Produce the smallest behavior-changing patch. "
                    "Prefer an existing reference or eval over a new skill. Never modify protected gates."
                ),
                prompt=(
                    "Return one JSON object with target_component, rationale, expected_gain, and patch. "
                    "patch must be a valid git unified diff against the current repository.\n"
                    f"Variant: {variant + 1}/{variants}\nFeedback:\n"
                    f"{json.dumps(feedback_payload, ensure_ascii=False, indent=2)}"
                    f"\nRelevant repository context:\n{sanitize_remote_text(context)}"
                ),
                temperature=0.2 + 0.1 * variant,
                max_tokens=8000,
            )
            response = await executor.generate(request)
            payload = _extract_object(response.text)
            try:
                candidates.append(
                    self.create_candidate_from_patch(
                        str(payload["patch"]),
                        target_component=str(payload.get("target_component", "")),
                        feedback_ids=[item.id for item in feedback],
                        provider=response.provider,
                        model=response.model,
                        rationale=str(payload.get("rationale", "")),
                        expected_gain=float(payload.get("expected_gain", 0.0)),
                    )
                )
                candidates[-1].metadata["feedback_cluster"] = cluster_key
                candidates[-1].metadata["generation_cost"] = {
                    "tokens": response.input_tokens + response.output_tokens,
                    "cost_usd": response.cost_usd,
                }
                self.store.update_candidate(candidates[-1])
            except (KeyError, TypeError, ValueError) as exc:
                raise EvolutionError(f"Provider produced an invalid candidate payload: {exc}") from exc
        return candidates

    def evaluate_candidate(
        self,
        candidate_id: str,
        executor: ModelProvider,
        reviewer: ModelProvider,
        *,
        include_hidden: bool = True,
    ) -> dict[str, Any]:
        if self.mode == "off":
            raise EvolutionError("Evolution is disabled by NEUROFLOW_EVOLUTION_MODE=off")
        candidate = self.store.get_candidate(candidate_id)
        if candidate.status not in {CandidateStatus.PROPOSED, CandidateStatus.SHADOW_TESTING}:
            raise EvolutionError(f"Candidate cannot be evaluated from status {candidate.status}")
        patch_text = self.read_verified_patch(candidate)
        inspection = inspect_patch(patch_text)
        if inspection.requires_human and not self._has_shadow_approval(candidate.id):
            raise EvolutionError(
                "Medium-, high-, and critical-risk candidates require a human shadow approval before evaluation"
            )
        hidden_present = (self.state_root / "evals" / "hidden.json").exists()
        if hidden_present and not include_hidden:
            raise EvolutionError("The configured hidden holdout is mandatory for candidate evaluation")
        if candidate.status == CandidateStatus.PROPOSED:
            self.transition(candidate, CandidateStatus.SHADOW_TESTING)
        partitions = {
            EvalPartition.INCIDENT,
            EvalPartition.REGRESSION,
            EvalPartition.PROTECTED,
        }
        if include_hidden:
            partitions.add(EvalPartition.HIDDEN_HOLDOUT)
        with self.shadow_workspaces(candidate, patch_text) as (parent_workspace, candidate_workspace):
            parent_cases = load_eval_cases(
                parent_workspace,
                partitions=partitions,
                include_hidden=include_hidden,
            )
            parent_cases = _scope_incident_cases(parent_cases, candidate.id)
            parent_harness = EvalHarness(parent_workspace, executor, reviewer)
            parent_summary = run_sync(parent_harness.run(parent_cases, partition_label="comparison-parent"))
            candidate_cases = load_eval_cases(
                candidate_workspace,
                partitions=partitions,
                include_hidden=include_hidden,
            )
            candidate_cases = _scope_incident_cases(candidate_cases, candidate.id)
            candidate_harness = EvalHarness(candidate_workspace, executor, reviewer)
            candidate_summary = run_sync(
                candidate_harness.run(
                    candidate_cases,
                    candidate_id=candidate.id,
                    partition_label="comparison-candidate",
                )
            )
        parent_path = write_eval_result(self.root, parent_summary)
        self.store.add_eval_run(parent_summary, parent_path)
        candidate_summary.parent_run_id = parent_summary.id
        comparison = compare_runs(parent_summary, candidate_summary)
        private_memory = "additive private Markdown memory" in inspection.reasons
        if private_memory:
            review_verdict = {
                "verdict": "pass",
                "disagreements": [],
                "required_fixes": [],
                "source_trace_valid": False,
                "provider": "local-policy",
                "model": "deterministic",
                "tokens": 0,
                "cost_usd": 0.0,
            }
        else:
            review_verdict = run_sync(self._review_candidate(candidate, reviewer, comparison, patch_text))
        comparison["review_pass"] = review_verdict.get("verdict") == "pass"
        comparison["eligible"] = bool(comparison["eligible"] and comparison["review_pass"])
        candidate_summary.regressions = comparison["regressions"]
        candidate_path = write_eval_result(self.root, candidate_summary)
        self.store.add_eval_run(candidate_summary, candidate_path)
        candidate.metadata.update(
            {
                "parent_eval_run": parent_summary.id,
                "candidate_eval_run": candidate_summary.id,
                "comparison": comparison,
                "executor": {"provider": executor.name, "model": executor.model},
                "reviewer": {
                    "provider": review_verdict["provider"],
                    "model": review_verdict["model"],
                },
                "review_verdict": review_verdict,
                "hidden_holdout_present": hidden_present,
                "hidden_holdout_evaluated": any(
                    case.partition == EvalPartition.HIDDEN_HOLDOUT for case in candidate_cases
                ),
            }
        )
        next_status = CandidateStatus.AWAITING_REVIEW if comparison["eligible"] else CandidateStatus.REJECTED
        self.transition(candidate, next_status)
        return {
            "candidate_id": candidate.id,
            "status": candidate.status.value,
            "parent_eval_run": parent_summary.id,
            "candidate_eval_run": candidate_summary.id,
            **comparison,
            "review_verdict": review_verdict,
        }

    async def _review_candidate(
        self,
        candidate: EvolutionCandidate,
        reviewer: ModelProvider,
        comparison: dict[str, Any],
        patch: str,
    ) -> dict[str, Any]:
        feedback_by_id = {item.id: item for item in self.store.list_feedback()}
        feedback = [
            {
                "event_type": item.event_type.value,
                "failure_tag": item.failure_tag,
                "summary": sanitize_provider_context(item.summary),
            }
            for feedback_id in candidate.trigger_feedback_ids
            if (item := feedback_by_id.get(feedback_id)) is not None
        ]
        prompt = (
            "Independently review this NeuroFlow evolution candidate. Check that the patch addresses its "
            "feedback, does not weaken evidence/privacy/safety rules, does not invent public sources, and "
            "matches the reported evaluation comparison. Return only JSON with verdict (pass or fail), "
            "disagreements (array), required_fixes (array), and source_trace_valid (boolean).\n\n"
            f"Risk: {candidate.risk_level.value}\n"
            f"Rationale: {sanitize_provider_context(candidate.rationale)}\n"
            f"Trigger feedback: {json.dumps(feedback, ensure_ascii=False)}\n"
            f"Comparison: {json.dumps(comparison, ensure_ascii=False)}\nPatch:\n{patch}"
        )
        response = await reviewer.generate(
            ModelRequest(
                prompt=prompt,
                temperature=0.0,
                max_tokens=1200,
                metadata={
                    "mock_response": json.dumps(
                        {
                            "verdict": "pass",
                            "disagreements": [],
                            "required_fixes": [],
                            "source_trace_valid": True,
                        }
                    )
                },
            )
        )
        payload = _extract_object(response.text)
        verdict = str(payload.get("verdict", "fail")).lower()
        if verdict not in {"pass", "fail"}:
            verdict = "fail"
        return {
            "verdict": verdict,
            "disagreements": list(payload.get("disagreements") or []),
            "required_fixes": list(payload.get("required_fixes") or []),
            "source_trace_valid": bool(payload.get("source_trace_valid", False)),
            "provider": response.provider,
            "model": response.model,
            "tokens": response.input_tokens + response.output_tokens,
            "cost_usd": response.cost_usd,
        }

    @contextmanager
    def shadow_workspaces(self, candidate: EvolutionCandidate, patch_text: str) -> Iterator[tuple[Path, Path]]:
        worktree_root = self.state_root / "worktrees"
        parent = worktree_root / f"{candidate.id}-parent"
        evolved = worktree_root / f"{candidate.id}-candidate"
        revision = (
            candidate.parent_id.removeprefix("git:")
            if candidate.parent_id and candidate.parent_id.startswith("git:")
            else "HEAD"
        )
        added: list[Path] = []
        worktree_root.mkdir(parents=True, exist_ok=True)
        try:
            for path in (parent, evolved):
                subprocess.run(
                    ["git", "worktree", "remove", "--force", str(path)],
                    cwd=self.root,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                shutil.rmtree(path, ignore_errors=True)
                _run(["git", "worktree", "add", "--detach", str(path), revision], self.root)
                added.append(path)
                self._copy_eval_overlay(path)
            applied = subprocess.run(
                ["git", "apply", "--whitespace=nowarn", "-"],
                cwd=evolved,
                input=patch_text,
                text=True,
                capture_output=True,
                check=False,
            )
            if applied.returncode != 0:
                raise EvolutionError(f"Candidate patch failed in the shadow checkout: {applied.stderr.strip()}")
            yield parent, evolved
        finally:
            for path in reversed(added):
                subprocess.run(
                    ["git", "worktree", "remove", "--force", str(path)],
                    cwd=self.root,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                shutil.rmtree(path, ignore_errors=True)

    def read_verified_patch(self, candidate: EvolutionCandidate) -> str:
        expected = (self.state_root / "candidates" / candidate.id / "candidate.patch").resolve()
        actual = Path(candidate.patch_path).resolve()
        if actual != expected or not actual.is_file():
            raise EvolutionError("Candidate patch path does not match its immutable control-plane location")
        patch = actual.read_text(encoding="utf-8")
        digest = hashlib.sha256(patch.encode("utf-8")).hexdigest()
        if digest != candidate.patch_sha256:
            raise EvolutionError("Candidate patch integrity check failed")
        return patch

    def _has_shadow_approval(self, candidate_id: str) -> bool:
        return any(
            item["decision"] == "shadow_approved" and not item["automatic"]
            for item in self.store.list_decisions(candidate_id)
        )

    def _copy_eval_overlay(self, workspace: Path) -> None:
        hidden = self.state_root / "evals" / "hidden.json"
        if hidden.exists():
            target = workspace / ".private" / "evolution" / "evals" / "hidden.json"
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(hidden, target)
        incidents = self.state_root / "evals" / "incidents"
        if incidents.exists():
            shutil.copytree(
                incidents,
                workspace / ".private" / "evolution" / "evals" / "incidents",
                dirs_exist_ok=True,
            )

    def transition(self, candidate: EvolutionCandidate, status: CandidateStatus) -> EvolutionCandidate:
        if status not in ALLOWED_TRANSITIONS[candidate.status]:
            raise EvolutionError(f"Invalid candidate transition: {candidate.status} -> {status}")
        previous = candidate.status
        candidate.status = status
        candidate.updated_at = utc_now()
        candidate.metadata.setdefault("status_history", []).append(
            {"from": previous.value, "to": status.value, "at": candidate.updated_at}
        )
        self.store.update_candidate(candidate)
        return candidate

    def _check_patch_applies(self, patch_text: str) -> None:
        completed = subprocess.run(
            ["git", "apply", "--check", "-"],
            cwd=self.root,
            input=patch_text,
            text=True,
            capture_output=True,
            check=False,
        )
        if completed.returncode != 0:
            raise EvolutionError(f"Candidate patch does not apply cleanly: {completed.stderr.strip()}")

    def _candidate_context(self, feedback: list[FeedbackEvent]) -> str:
        tags = " ".join(item.failure_tag + " " + item.summary for item in feedback).lower()
        paths = [
            self.root / "skills-codex/neuro-orchestrator/references/pipeline.md",
            self.root / "skills/ai-bci-research/references/workflows/skill-factory.md",
        ]
        if any(token in tags for token in ("citation", "paper", "claim", "source")):
            paths.append(self.root / "skills/paper-rag-plus/references/claim-grounding.md")
        if any(token in tags for token in ("baseline", "split", "leakage", "metric")):
            paths.append(self.root / "skills/eeg-benchmark-hunter/references/benchmark-risk-checklist.md")
        sections = []
        for path in paths:
            if path.exists():
                sections.append(f"--- {path.relative_to(self.root)} ---\n{path.read_text(encoding='utf-8')[:12000]}")
        return "\n".join(sections)

    def _write_incident_eval(self, candidate: EvolutionCandidate, feedback_ids: list[str]) -> None:
        if not feedback_ids:
            return
        feedback_by_id = {item.id: item for item in self.store.list_feedback()}
        selected = [feedback_by_id[item] for item in feedback_ids if item in feedback_by_id]
        if not selected:
            return
        path = self.state_root / "evals" / "incidents" / f"{candidate.id}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        inspection = candidate.metadata.get("inspection", {})
        target_paths = list(inspection.get("paths", []))
        private_memory = "additive private Markdown memory" in inspection.get("reasons", [])
        evals = []
        for item in selected:
            if private_memory:
                assertions = [
                    {
                        "type": "file_exists",
                        "path": target,
                        "critical": True,
                        "dimension": "adaptivity",
                    }
                    for target in target_paths
                ]
                files: list[str] = []
                repeats = 1
            else:
                assertions = [
                    {
                        "type": "llm_rubric",
                        "text": (
                            "Output prevents or correctly handles: "
                            f"{sanitize_provider_context(item.summary)}"
                        ),
                        "critical": item.event_type in {
                            FeedbackType.GATE_FAILURE,
                            FeedbackType.EVAL_REGRESSION,
                        },
                        "dimension": "adaptivity",
                    }
                ]
                files = target_paths
                repeats = 3
            evals.append(
                {
                    "id": item.id,
                    "prompt": sanitize_provider_context(item.summary),
                    "expected_output": (
                        "The response must address failure tag "
                        f"{item.failure_tag or item.event_type.value}."
                    ),
                    "files": files,
                    "partition": "incident",
                    "repeats": repeats,
                    "assertions": assertions,
                }
            )
        payload = {
            "skill_name": f"incident-{candidate.id}",
            "evals": evals,
        }
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def load_incident_eval_paths(root: Path) -> list[Path]:
    return sorted((root / ".private" / "evolution" / "evals" / "incidents").glob("*.json"))


def _scope_incident_cases(cases: list[Any], candidate_id: str) -> list[Any]:
    scoped = []
    for case in cases:
        if case.partition == EvalPartition.INCIDENT and candidate_id not in Path(case.source_path).stem:
            case = case.model_copy(
                update={
                    "partition": EvalPartition.REGRESSION,
                    "tags": sorted(set(case.tags) | {"prior-incident"}),
                }
            )
        scoped.append(case)
    return scoped


def cluster_feedback(events: list[FeedbackEvent]) -> dict[str, list[FeedbackEvent]]:
    clusters: dict[str, list[FeedbackEvent]] = {}
    for event in events:
        key = event.failure_tag.strip().lower() or event.event_type.value
        key = re.sub(r"[^a-z0-9:_-]+", "-", key).strip("-") or "unclassified"
        clusters.setdefault(key, []).append(event)
    return clusters


def sanitize_provider_context(text: str) -> str:
    return sanitize_remote_text(text, max_chars=4000)


def _deduplicate_feedback(events: list[FeedbackEvent]) -> list[FeedbackEvent]:
    seen = set()
    result = []
    for event in events:
        key = (event.run_id, event.event_type, event.failure_tag, event.summary)
        if key not in seen:
            seen.add(key)
            result.append(event)
    return result


def _inspection_dict(inspection: PatchInspection) -> dict[str, Any]:
    return {
        "paths": list(inspection.paths),
        "new_files": list(inspection.new_files),
        "additions": inspection.additions,
        "deletions": inspection.deletions,
        "risk_level": inspection.risk_level.value,
        "requires_human": inspection.requires_human,
        "public_reference": inspection.public_reference,
        "source_traced": inspection.source_traced,
        "reasons": list(inspection.reasons),
    }


def _extract_object(text: str) -> dict[str, Any]:
    stripped = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip(), flags=re.IGNORECASE)
    start = stripped.find("{")
    end = stripped.rfind("}")
    if start < 0 or end < start:
        raise EvolutionError("Provider response does not contain a JSON object")
    payload = json.loads(stripped[start : end + 1])
    if not isinstance(payload, dict):
        raise EvolutionError("Candidate response must be a JSON object")
    return payload


def _run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise EvolutionError(f"Command failed ({' '.join(command)}): {completed.stderr.strip()}")
    return completed
