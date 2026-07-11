from __future__ import annotations

from pathlib import Path

from neuroflow_runtime.hooks import WorkflowHookRuntime
from neuroflow_runtime.registry import build_registry
from neuroflow_runtime.storage import EvolutionStore
from neuroflow_runtime.trace import TraceStep, WorkflowTrace

ROOT = Path(__file__).resolve().parents[1]


def test_session_end_only_persists_reusable_failure(tmp_path: Path) -> None:
    trace = WorkflowTrace.create("benchmark-to-baseline", "task", "AUDIT.md", "done")
    step = TraceStep(index=1, name="split/leakage", module="eeg-benchmark-hunter")
    step.finish("failed", failure_tag="benchmark:leakage", error="subject split was omitted")
    trace.steps.append(step)
    trace_path = tmp_path / ".private" / "runs" / trace.run_id / "trace.json"
    trace.write_json(trace_path)
    runtime = WorkflowHookRuntime(build_registry(ROOT), tmp_path)
    result = runtime.session_end(trace.run_id, "hook:session_end", "standard")
    assert result.metadata["memory_candidate"] == "yes"
    feedback = EvolutionStore(tmp_path).list_feedback()
    assert len(feedback) == 1
    assert feedback[0].failure_tag == "benchmark:leakage"
    persisted = WorkflowTrace.read_json(trace_path)
    assert persisted.feedback_ids == [feedback[0].id]


def test_session_end_does_not_persist_empty_scaffold(tmp_path: Path) -> None:
    trace = WorkflowTrace.create("paper-to-repro", "task", "REPRO.md", "done")
    trace.steps.append(TraceStep(index=1, name="paper facts", module="paper-rag-plus"))
    trace_path = tmp_path / ".private" / "runs" / trace.run_id / "trace.json"
    trace.write_json(trace_path)
    runtime = WorkflowHookRuntime(build_registry(ROOT), tmp_path)
    result = runtime.session_end(trace.run_id, "hook:session_end", "standard")
    assert result.metadata["memory_candidate"] == "no"
    store = EvolutionStore(tmp_path)
    store.initialize()
    assert not store.list_feedback()


def test_public_artifact_blocks_participant_identifier(tmp_path: Path) -> None:
    artifact = tmp_path / "claim.md"
    artifact.write_text(
        "Source-traced claim for participant-P001. Evidence: https://example.org/source\n",
        encoding="utf-8",
    )
    runtime = WorkflowHookRuntime(build_registry(ROOT), tmp_path)
    result = runtime.pre_artifact(artifact, "claim", "hook:pre_artifact", "strict")
    assert result.status == "blocked"
    assert "participant identifier" in result.blocked_reason
