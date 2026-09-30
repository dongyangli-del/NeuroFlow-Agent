"""Event-style hooks for the lightweight NeuroFlow runtime."""

from __future__ import annotations

import json
import os
import subprocess
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path

from .privacy import sanitize_remote_text, sensitive_labels
from .registry import RuntimeRegistry, WorkflowChain
from .runner import WorkflowRunner
from .trace import HookEvent, RouteCandidate, WorkflowTrace

VALID_EVENTS = {"session_start", "pre_artifact", "post_tool", "pre_commit", "session_end"}
VALID_PROFILES = {"minimal", "standard", "strict"}
PUBLIC_ARTIFACT_KINDS = {"claim", "memory", "reference", "readme"}


@dataclass(frozen=True)
class HookResult:
    event: str
    status: str
    hook_id: str
    profile: str
    warnings: list[str] = field(default_factory=list)
    selected_chain: str = ""
    run_id: str = ""
    trace: str = ""
    artifact: str = ""
    blocked_reason: str = ""
    metadata: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


class WorkflowHookRuntime:
    def __init__(self, registry: RuntimeRegistry, root: Path) -> None:
        self.registry = registry
        self.root = root
        self.output_root = root / ".private" / "runs"

    def run(
        self,
        event: str,
        task: str = "",
        artifact: Path | None = None,
        kind: str = "",
        run_id: str = "",
        tool: str = "",
        summary: str = "",
    ) -> HookResult:
        if event not in VALID_EVENTS:
            return self._result(event, "blocked", blocked_reason=f"Unknown hook event: {event}")
        hook_id = f"hook:{event}"
        profile = self.profile()
        if self.disabled(hook_id):
            return self._result(event, "skipped", hook_id=hook_id, profile=profile)
        if event == "session_start":
            return self.session_start(task=task, hook_id=hook_id, profile=profile)
        if event == "pre_artifact":
            return self.pre_artifact(artifact=artifact, kind=kind, hook_id=hook_id, profile=profile)
        if event == "post_tool":
            return self.post_tool(run_id=run_id, tool=tool, summary=summary, hook_id=hook_id, profile=profile)
        if event == "pre_commit":
            return self.pre_commit(hook_id=hook_id, profile=profile)
        if event == "session_end":
            return self.session_end(run_id=run_id, hook_id=hook_id, profile=profile)
        return self._result(event, "blocked", hook_id=hook_id, profile=profile, blocked_reason="Unhandled hook event")

    def session_start(self, task: str, hook_id: str, profile: str) -> HookResult:
        if not task.strip():
            return self._result(
                "session_start",
                "warning",
                hook_id=hook_id,
                profile=profile,
                warnings=["Missing task text."],
            )
        chain = self.select_chain(task)
        runner = WorkflowRunner(registry=self.registry, root=self.root)
        result = runner.run(chain_name=chain.name, task=task, dry_run=False)
        event = self._event(
            "session_start",
            "ok",
            hook_id,
            profile,
            selected_chain=chain.name,
            artifact=str(result.artifact_path),
            metadata={"run_id": result.trace.run_id, "trace": str(result.trace_path)},
        )
        result.trace.append_hook_event(event)
        result.trace.metadata["hook_profile"] = profile
        result.trace.route_candidates = [
            RouteCandidate(chain=name, score=float(score), reasons=reasons)
            for name, score, reasons in self.rank_chains(task)
        ]
        result.trace.selected_route = chain.name
        result.trace.write_json(result.trace_path)
        return self._from_event(event, trace=str(result.trace_path), run_id=result.trace.run_id)

    def pre_artifact(self, artifact: Path | None, kind: str, hook_id: str, profile: str) -> HookResult:
        warnings: list[str] = []
        blocked_reason = ""
        artifact_text = ""
        artifact_path = str(artifact) if artifact else ""
        normalized_kind = (kind or "claim").strip().lower()
        if normalized_kind not in PUBLIC_ARTIFACT_KINDS:
            warnings.append(f"Unknown artifact kind {kind!r}; treating it as public research text.")
        if artifact and artifact.exists():
            artifact_text = artifact.read_text(encoding="utf-8", errors="ignore")
        else:
            warnings.append("Artifact path is missing or does not exist; evidence gate can only run in advisory mode.")
        lower = artifact_text.lower()
        source_markers = ("source-traced", "citation", "doi", "arxiv", "evidence_sources")
        has_source_trace = any(marker in lower for marker in source_markers)
        has_unresolved = any(marker in lower for marker in ("unresolved", "todo", "manual-review", "人工核验"))
        sensitive = sensitive_labels(artifact_text)
        if artifact_text and not has_source_trace and normalized_kind in PUBLIC_ARTIFACT_KINDS:
            warnings.append("Public artifact lacks an obvious citation/source-trace marker.")
        if has_unresolved:
            warnings.append("Artifact still contains unresolved review markers.")
        if sensitive:
            blocked_reason = f"Public artifact appears to contain sensitive material: {', '.join(sensitive)}."
        status = "blocked" if blocked_reason else ("warning" if warnings else "ok")
        event = self._event(
            "pre_artifact",
            status,
            hook_id,
            profile,
            warnings=warnings,
            artifact=artifact_path,
            blocked_reason=blocked_reason,
        )
        self._append_to_latest_trace(event)
        return self._from_event(event)

    def post_tool(self, run_id: str, tool: str, summary: str, hook_id: str, profile: str) -> HookResult:
        warnings: list[str] = []
        trace_path = self._trace_path(run_id)
        if not trace_path:
            warnings.append("No run id supplied and no existing run trace found; recorded advisory hook result only.")
        clean_summary = self._sanitize_summary(summary)
        event = self._event(
            "post_tool",
            "warning" if warnings else "ok",
            hook_id,
            profile,
            warnings=warnings,
            metadata={"tool": tool, "summary": clean_summary},
        )
        if trace_path:
            self._append_event(trace_path, event)
        return self._from_event(event, trace=str(trace_path) if trace_path else "", run_id=run_id)

    def pre_commit(self, hook_id: str, profile: str) -> HookResult:
        result = subprocess.run(
            ["make", "validate"],
            cwd=self.root,
            text=True,
            capture_output=True,
            timeout=120,
            check=False,
        )
        warnings = []
        blocked_reason = ""
        if result.returncode != 0:
            blocked_reason = "make validate failed."
            warnings.append((result.stderr or result.stdout).strip()[:800])
        event = self._event(
            "pre_commit",
            "blocked" if blocked_reason else "ok",
            hook_id,
            profile,
            warnings=warnings,
            blocked_reason=blocked_reason,
            metadata={"command": "make validate", "returncode": str(result.returncode)},
        )
        self._append_to_latest_trace(event)
        return self._from_event(event)

    def session_end(self, run_id: str, hook_id: str, profile: str) -> HookResult:
        trace_path = self._trace_path(run_id)
        warnings = []
        memory_candidate = "no"
        unresolved = "none"
        next_actions = "No unresolved workflow action."
        if trace_path:
            trace = WorkflowTrace.read_json(trace_path)
            failed_steps = [step.name for step in trace.steps if step.status in {"failed", "blocked"}]
            gate_warnings = [
                event.event for event in trace.hook_events if event.status in {"warning", "blocked"}
            ]
            reusable_signal = bool(failed_steps or gate_warnings or trace.outcome.get("memory_candidate"))
            memory_candidate = "yes" if reusable_signal else "no"
            if failed_steps or gate_warnings:
                unresolved = ", ".join(failed_steps + gate_warnings)
                next_actions = "Resolve failed stages or hook warnings before proposing durable memory."
        metadata = {
            "next_actions": next_actions,
            "memory_candidate": memory_candidate,
            "unresolved": unresolved,
        }
        if not trace_path:
            warnings.append("No run trace found for session_end.")
        event = self._event(
            "session_end",
            "warning" if warnings else "ok",
            hook_id,
            profile,
            warnings=warnings,
            metadata=metadata,
        )
        if trace_path:
            feedback = []
            if memory_candidate == "yes":
                try:
                    from .evolution import EvolutionEngine

                    feedback = EvolutionEngine(self.root).ingest_trace(trace_path)
                    event.metadata["feedback_ids"] = ",".join(item.id for item in feedback)
                except Exception as exc:
                    event.status = "warning"
                    event.warnings.append(f"Feedback ingestion failed: {exc}")
            persisted_trace = WorkflowTrace.read_json(trace_path)
            persisted_trace.feedback_ids = sorted(
                set(persisted_trace.feedback_ids) | {item.id for item in feedback}
            )
            persisted_trace.append_hook_event(event)
            if feedback:
                persisted_trace.append_hook_event(
                    self._event(
                        "feedback_ingest",
                        "ok",
                        "hook:feedback_ingest",
                        profile,
                        metadata={"feedback_count": str(len(feedback))},
                    )
                )
            persisted_trace.write_json(trace_path)
        return self._from_event(event, trace=str(trace_path) if trace_path else "", run_id=run_id)

    def select_chain(self, task: str) -> WorkflowChain:
        return self.registry.get_chain(self.rank_chains(task)[0][0])

    def rank_chains(self, task: str) -> list[tuple[str, int, list[str]]]:
        text = task.lower()
        triggers = {
            "paper-to-repro": ("reproduce", "repro", "runnable", "repo", "code", "smoke", "复现"),
            "benchmark-to-baseline": (
                "baseline", "benchmark", "dataset", "metric", "leakage", "split", "worse", "差", "数据集",
            ),
            "experiment-to-paper": (
                "claim", "paper claim", "write", "abstract", "result", "figure", "table", "投稿", "论文",
            ),
            "paper-to-rebuttal": ("reviewer", "rebuttal", "review", "response", "审稿", "反驳"),
            "continual-adaptation": (
                "continual", "online", "streaming", "adaptation", "cross-session", "个性化", "持续",
            ),
            "session-to-memory": ("memory", "save this", "make reusable", "沉淀", "经验"),
            "idea-to-experiment": ("idea", "hypothesis", "plan experiment", "ablation", "实验计划", "想法"),
        }
        ranked = []
        for name, needles in triggers.items():
            matches = [needle for needle in needles if needle in text]
            ranked.append((name, len(matches), [f"matched:{needle}" for needle in matches]))
        ranked.sort(key=lambda item: (item[1], item[0]), reverse=True)
        if ranked[0][1] == 0:
            ranked = [("idea-to-experiment", 0, ["default:unclassified"])] + [
                item for item in ranked if item[0] != "idea-to-experiment"
            ]
        return ranked

    def profile(self) -> str:
        raw = os.environ.get("NEUROFLOW_HOOK_PROFILE", "standard").strip().lower()
        return raw if raw in VALID_PROFILES else "standard"

    def disabled(self, hook_id: str) -> bool:
        disabled = {
            item.strip().lower()
            for item in os.environ.get("NEUROFLOW_DISABLED_HOOKS", "").split(",")
            if item.strip()
        }
        return hook_id.lower() in disabled or hook_id.split(":", 1)[-1].lower() in disabled

    def _append_to_latest_trace(self, event: HookEvent) -> None:
        trace_path = self._trace_path("")
        if trace_path:
            self._append_event(trace_path, event)

    def _append_event(self, trace_path: Path, event: HookEvent) -> None:
        trace = WorkflowTrace.read_json(trace_path)
        trace.append_hook_event(event)
        trace.write_json(trace_path)

    def _trace_path(self, run_id: str) -> Path | None:
        if run_id:
            candidate = self.output_root / run_id / "trace.json"
            return candidate if candidate.exists() else None
        traces = sorted(self.output_root.glob("nf_*/trace.json"), key=lambda path: path.stat().st_mtime, reverse=True)
        return traces[0] if traces else None

    def _event(
        self,
        event: str,
        status: str,
        hook_id: str,
        profile: str,
        warnings: list[str] | None = None,
        selected_chain: str = "",
        artifact: str = "",
        blocked_reason: str = "",
        metadata: dict[str, str] | None = None,
    ) -> HookEvent:
        timestamp = datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        return HookEvent(
            event=event,
            status=status,
            created_at=timestamp,
            hook_id=hook_id,
            profile=profile,
            warnings=warnings or [],
            selected_chain=selected_chain,
            artifact=artifact,
            blocked_reason=blocked_reason,
            metadata=metadata or {},
        )

    def _from_event(self, event: HookEvent, trace: str = "", run_id: str = "") -> HookResult:
        return HookResult(
            event=event.event,
            status=event.status,
            hook_id=event.hook_id,
            profile=event.profile,
            warnings=event.warnings,
            selected_chain=event.selected_chain,
            run_id=run_id or event.metadata.get("run_id", ""),
            trace=trace or event.metadata.get("trace", ""),
            artifact=event.artifact,
            blocked_reason=event.blocked_reason,
            metadata=event.metadata,
        )

    def _result(
        self,
        event: str,
        status: str,
        hook_id: str = "",
        profile: str = "standard",
        warnings: list[str] | None = None,
        blocked_reason: str = "",
    ) -> HookResult:
        return HookResult(
            event=event,
            status=status,
            hook_id=hook_id,
            profile=profile,
            warnings=warnings or [],
            blocked_reason=blocked_reason,
        )

    def _score(self, text: str, *needles: str) -> int:
        return sum(1 for needle in needles if needle in text)

    def _sanitize_summary(self, summary: str) -> str:
        clean = summary.strip().replace("\n", " ")
        return sanitize_remote_text(clean, max_chars=500)


def result_to_json(result: HookResult) -> str:
    return json.dumps(result.to_dict(), ensure_ascii=False, indent=2)
