from __future__ import annotations

from pathlib import Path

from neuroflow_runtime.providers import MockProvider, ModelRequest, ModelResponse
from neuroflow_runtime.registry import build_registry
from neuroflow_runtime.runner import WorkflowRunner
from neuroflow_runtime.trace import WorkflowTrace

ROOT = Path(__file__).resolve().parents[1]


class CapturingWorkflowProvider:
    name = "capture"
    model = "capture"

    def __init__(self) -> None:
        self.prompts: list[str] = []

    async def generate(self, request: ModelRequest) -> ModelResponse:
        self.prompts.append(request.prompt)
        text = (
            "citation source arxiv doi prior work uncertain access license split metric baseline leakage "
            "ablation control statistic stop environment data weight command expected output sanity "
            "online offline safety calibration latency privacy target eval no-repo verification"
        )
        return ModelResponse(text=text, provider=self.name, model=self.model)


def test_executed_workflow_records_stage_outcomes(tmp_path: Path) -> None:
    response = (
        "citation source arxiv doi prior work uncertain access license split metric baseline leakage "
        "ablation control statistic stop environment data weight command expected output sanity "
        "online offline safety calibration latency privacy target eval no-repo verification"
    )
    runner = WorkflowRunner(build_registry(ROOT), ROOT)
    result = runner.run(
        "benchmark-to-baseline",
        "Audit a benchmark",
        output_root=tmp_path,
        execute=True,
        provider=MockProvider(response=response),
    )
    trace = WorkflowTrace.read_json(result.trace_path)
    assert trace.status == "passed"
    assert all(step.status == "passed" for step in trace.steps)
    assert trace.skill_versions["eeg-benchmark-hunter"]
    assert trace.route_candidates[0].reasons == ["explicit-chain"]
    assert trace.cost["input_tokens"] > 0
    assert len(trace.outcome["artifact_sha256"]) == 64
    assert result.artifact_path.exists()


def test_external_agent_result_can_be_imported(tmp_path: Path) -> None:
    runner = WorkflowRunner(build_registry(ROOT), ROOT)
    result = runner.run("benchmark-to-baseline", "Audit", output_root=tmp_path, dry_run=False)
    external = tmp_path / "external.md"
    external.write_text("access license split metric baseline leakage", encoding="utf-8")
    trace = runner.import_step_result(
        result.trace_path,
        step_index=1,
        artifact=external,
        status="passed",
        metrics={"tokens": 12},
    )
    assert trace.steps[0].status == "passed"
    assert trace.steps[0].output_hash
    assert trace.steps[0].metrics["tokens"] == 12
    assert "access license" in result.artifact_path.read_text(encoding="utf-8")


def test_three_representative_workflows_produce_complete_outcome_traces(tmp_path: Path) -> None:
    response = (
        "citation source arxiv doi prior work uncertain access license split metric baseline leakage "
        "ablation control statistic stop environment data weight command expected output sanity "
        "online offline safety calibration latency privacy target eval no-repo verification"
    )
    runner = WorkflowRunner(build_registry(ROOT), ROOT)
    tasks = [
        ("benchmark-to-baseline", "Audit an EEG visual reconstruction benchmark"),
        ("paper-to-repro", "Build a runnable reproduction contract"),
        ("experiment-to-paper", "Scope a result claim for a conference paper"),
    ]
    traces = []
    for chain, task in tasks:
        result = runner.run(chain, task, output_root=tmp_path, execute=True, provider=MockProvider(response=response))
        traces.append(WorkflowTrace.read_json(result.trace_path))
    assert len({trace.run_id for trace in traces}) == 3
    assert all(trace.status == "passed" and trace.completed_at for trace in traces)
    assert all(trace.outcome["completed_steps"] == trace.outcome["total_steps"] for trace in traces)


def test_workflow_provider_prompt_is_privacy_scrubbed(tmp_path: Path) -> None:
    provider = CapturingWorkflowProvider()
    credential = "sk-" + "b" * 26
    runner = WorkflowRunner(build_registry(ROOT), ROOT)
    result = runner.run(
        "paper-to-repro",
        f"Reproduce participant-P001 from /home/researcher/raw.csv using {credential}",
        output_root=tmp_path,
        execute=True,
        provider=provider,
    )
    assert result.trace.status == "passed"
    assert provider.prompts
    assert all("participant-P001" not in prompt for prompt in provider.prompts)
    assert all("/home/researcher" not in prompt for prompt in provider.prompts)
    assert all(credential not in prompt for prompt in provider.prompts)
