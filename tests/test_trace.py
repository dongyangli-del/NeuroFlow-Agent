from __future__ import annotations

from neuroflow_runtime.trace import GateResult, TraceStep, WorkflowTrace


def test_trace_v1_is_backward_compatible() -> None:
    trace = WorkflowTrace.from_dict(
        {
            "run_id": "nf_old",
            "chain": "paper-to-repro",
            "task": "old trace",
            "artifact": "REPRO.md",
            "status": "planned",
            "created_at": "2025-01-01T00:00:00Z",
            "stop_condition": "done",
            "steps": [{"index": 1, "name": "paper facts", "module": "paper-rag-plus"}],
            "hook_events": [],
            "metadata": {"legacy": "yes"},
        }
    )
    assert trace.schema_version == 1
    assert trace.selected_route == "paper-to-repro"
    assert trace.steps[0].status == "planned"


def test_trace_records_outcome_cost_and_failures() -> None:
    trace = WorkflowTrace.create("benchmark-to-baseline", "task", "AUDIT.md", "done")
    step = TraceStep(index=1, name="split", module="eeg-benchmark-hunter")
    step.start()
    step.gate_results.append(GateResult(gate="benchmark", status="failed"))
    step.finish("failed", output_text="bad", failure_tag="gate:benchmark", metrics={"tokens": 8})
    trace.steps.append(step)
    trace.finalize("failed", {"reason": "gate"})
    assert trace.failure_tags == ["gate:benchmark"]
    assert trace.cost["tokens"] == 8
    assert trace.outcome["reason"] == "gate"
    assert trace.completed_at
