"""Event-style hooks for the lightweight NeuroFlow runtime."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path

from .registry import RuntimeRegistry, WorkflowChain
from .runner import WorkflowRunner
from .trace import HookEvent, WorkflowTrace

VALID_EVENTS = {"session_start", "pre_artifact", "post_tool", "pre_commit", "session_end"}
VALID_PROFILES = {"minimal", "standard", "strict"}
PUBLIC_ARTIFACT_KINDS = {"claim", "memory", "reference", "readme"}
PRIVATE_PATH_PATTERNS = (
    re.compile("/" + r"vePFS-[^\s)>\"]+"),
    re.compile("/" + r"home/ldy(?:/|\b)"),
    re.compile("/" + r"Users/[^/\s)>\"]+"),
)


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
            return self._result("session_start", "warning", hook_id=hook_id, profile=profile, warnings=["Missing task text."])
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
        has_source_trace = any(marker in lower for marker in ("source-traced", "citation", "doi", "arxiv", "evidence_sources"))
        has_unresolved = any(marker in lower for marker in ("unresolved", "todo", "manual-review", "人工核验"))
        leaks_private_path = any(pattern.search(artifact_text) for pattern in PRIVATE_PATH_PATTERNS)
        if artifact_text and not has_source_trace and normalized_kind in PUBLIC_ARTIFACT_KINDS:
            warnings.append("Public artifact lacks an obvious citation/source-trace marker.")
        if has_unresolved:
            warnings.append("Artifact still contains unresolved review markers.")
        if leaks_private_path:
            blocked_reason = "Public artifact appears to contain a private local path."
        status = "blocked" if blocked_reason else ("warning" if warnings else "ok")
        event = self._event("pre_artifact", status, hook_id, profile, warnings=warnings, artifact=artifact_path, blocked_reason=blocked_reason)
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
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
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
        metadata = {
            "next_actions": "Review warnings, fill artifact evidence sections, and decide whether neuro-memory should persist a finding.",
            "memory_candidate": "yes",
            "unresolved": "check artifact notes and hook warnings",
        }
        if not trace_path:
            warnings.append("No run trace found for session_end.")
        event = self._event("session_end", "warning" if warnings else "ok", hook_id, profile, warnings=warnings, metadata=metadata)
        if trace_path:
            self._append_event(trace_path, event)
        return self._from_event(event, trace=str(trace_path) if trace_path else "", run_id=run_id)

    def select_chain(self, task: str) -> WorkflowChain:
        text = task.lower()
        chain_scores = {
            "paper-to-repro": self._score(text, "reproduce", "repro", "runnable", "repo", "code", "smoke", "复现"),
            "benchmark-to-baseline": self._score(text, "baseline", "benchmark", "dataset", "metric", "leakage", "split", "worse", "差", "数据集"),
            "experiment-to-paper": self._score(text, "claim", "paper claim", "write", "abstract", "result", "figure", "table", "投稿", "论文"),
            "paper-to-rebuttal": self._score(text, "reviewer", "rebuttal", "review", "response", "审稿", "反驳"),
            "continual-adaptation": self._score(text, "continual", "online", "streaming", "adaptation", "cross-session", "个性化", "持续"),
            "session-to-memory": self._score(text, "memory", "save this", "make reusable", "沉淀", "经验"),
            "idea-to-experiment": self._score(text, "idea", "hypothesis", "plan experiment", "ablation", "实验计划", "想法"),
        }
        selected = max(chain_scores, key=lambda name: (chain_scores[name], name))
        if chain_scores[selected] == 0:
            selected = "idea-to-experiment"
        return self.registry.get_chain(selected)

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
        for pattern in PRIVATE_PATH_PATTERNS:
            clean = pattern.sub("[private-path]", clean)
        return clean[:500]


def result_to_json(result: HookResult) -> str:
    return json.dumps(result.to_dict(), ensure_ascii=False, indent=2)
