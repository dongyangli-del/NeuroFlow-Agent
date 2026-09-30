from __future__ import annotations

import json
from pathlib import Path

from neuroflow_runtime.evals import EvalHarness, compare_runs, load_eval_cases, run_sync, summarize_results
from neuroflow_runtime.models import (
    AssertionResult,
    AssertionType,
    EvalAssertion,
    EvalCase,
    EvalCaseResult,
    EvalPartition,
)
from neuroflow_runtime.providers import MockProvider, ModelRequest, ModelResponse

ROOT = Path(__file__).resolve().parents[1]


def test_all_tracked_evals_have_unique_executable_ids() -> None:
    cases = load_eval_cases(ROOT)
    assert len(cases) >= 52
    assert len({case.id for case in cases}) == len(cases)
    assert all(case.assertions for case in cases)
    assert all(case.repeats >= 1 for case in cases)


def test_hidden_holdout_requires_explicit_loading(tmp_path: Path) -> None:
    hidden = tmp_path / ".private/evolution/evals/hidden.json"
    hidden.parent.mkdir(parents=True)
    hidden.write_text(
        json.dumps(
            {
                "skill_name": "hidden",
                "evals": [
                    {
                        "id": "secret",
                        "prompt": "held-out prompt",
                        "partition": "hidden_holdout",
                        "assertions": [{"type": "contains", "value": "ok"}],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    assert not load_eval_cases(tmp_path)
    loaded = load_eval_cases(tmp_path, include_hidden=True)
    assert len(loaded) == 1
    assert loaded[0].partition == EvalPartition.HIDDEN_HOLDOUT


def test_deterministic_assertions_execute(tmp_path: Path) -> None:
    (tmp_path / "artifact.md").write_text("Evidence source-traced", encoding="utf-8")
    case = EvalCase(
        id="case",
        prompt="return evidence",
        expected_output="Evidence source-traced",
        partition=EvalPartition.PROTECTED,
        assertions=[
            EvalAssertion(type=AssertionType.CONTAINS, value="source-traced", critical=True),
            EvalAssertion(type=AssertionType.NOT_CONTAINS, value="private-path", critical=True),
            EvalAssertion(type=AssertionType.FILE_EXISTS, path="artifact.md", critical=True),
        ],
    )
    harness = EvalHarness(tmp_path, MockProvider(), MockProvider())
    result = run_sync(harness.run_case(case))
    assert result.score == 1.0
    assert result.critical_pass


def test_schema_file_diff_and_artifact_field_assertions(tmp_path: Path) -> None:
    (tmp_path / "actual.md").write_text("Status: source-traced\n", encoding="utf-8")
    (tmp_path / "expected.md").write_text("Status: source-traced\n", encoding="utf-8")
    case = EvalCase(
        id="structured",
        prompt="structured output",
        expected_output='{"status": "ok"}',
        assertions=[
            EvalAssertion(
                type=AssertionType.JSON_SCHEMA,
                schema={"type": "object", "required": ["status"], "properties": {"status": {"const": "ok"}}},
                critical=True,
            ),
            EvalAssertion(
                type=AssertionType.FILE_DIFF,
                path="actual.md",
                expected_path="expected.md",
                critical=True,
            ),
            EvalAssertion(
                type=AssertionType.ARTIFACT_FIELD,
                path="actual.md",
                field="Status",
                value="source-traced",
                critical=True,
            ),
        ],
    )
    result = run_sync(EvalHarness(tmp_path, MockProvider(), MockProvider()).run_case(case))
    assert result.score == 1.0
    assert result.critical_pass


def test_command_assertions_reject_inline_python(tmp_path: Path) -> None:
    marker = tmp_path / "escaped.txt"
    case = EvalCase(
        id="command-boundary",
        prompt="do not execute arbitrary code",
        assertions=[
            EvalAssertion(
                type=AssertionType.COMMAND_EXIT,
                command=["python3", "-c", f"open({str(marker)!r}, 'w').write('bad')"],
                critical=True,
            )
        ],
    )
    result = run_sync(EvalHarness(tmp_path, MockProvider(), MockProvider()).run_case(case))
    assert result.score == 0.0
    assert not marker.exists()
    assert "must invoke a repository script" in result.assertions[0].message


class CapturingProvider:
    name = "capture"
    model = "capture"

    def __init__(self) -> None:
        self.prompts: list[str] = []

    async def generate(self, request: ModelRequest) -> ModelResponse:
        self.prompts.append(request.prompt)
        return ModelResponse(
            text=str(request.metadata.get("expected_output", "ok")),
            provider=self.name,
            model=self.model,
        )


def test_eval_provider_prompt_is_privacy_scrubbed(tmp_path: Path) -> None:
    provider = CapturingProvider()
    credential = "sk-" + "a" * 26
    case = EvalCase(
        id="privacy",
        prompt=f"Inspect /home/researcher/raw.csv for participant-P001 using {credential}",
        expected_output="ok",
        assertions=[EvalAssertion(type=AssertionType.LLM_RUBRIC, text="returns output")],
    )
    result = run_sync(EvalHarness(tmp_path, provider, MockProvider()).run_case(case))
    assert result.score == 1.0
    assert "[private-path]" in provider.prompts[0]
    assert "[participant-id]" in provider.prompts[0]
    assert credential not in provider.prompts[0]


def make_result(case_id: str, score: float, critical: bool = True, tokens: int = 100) -> EvalCaseResult:
    assertion = EvalAssertion(type=AssertionType.LLM_RUBRIC, text="quality", critical=True)
    return EvalCaseResult(
        case_id=case_id,
        partition=EvalPartition.REGRESSION,
        output="",
        assertions=[AssertionResult(assertion=assertion, passed=critical, score=score)],
        score=score,
        critical_pass=critical,
        tokens=tokens,
    )


def test_candidate_comparison_enforces_gain_regression_cost_and_safety() -> None:
    parent = summarize_results([make_result("a", 1.0), make_result("b", 0.5)], candidate_id=None, partition="all")
    candidate = summarize_results(
        [make_result("a", 1.0, tokens=110), make_result("b", 0.6, tokens=110)],
        candidate_id="c",
        partition="all",
    )
    comparison = compare_runs(parent, candidate)
    assert comparison["eligible"]
    regressed = summarize_results(
        [make_result("a", 0.8), make_result("b", 0.9)], candidate_id="d", partition="all"
    )
    assert not compare_runs(parent, regressed)["eligible"]
    assert compare_runs(parent, regressed)["regressions"] == ["a"]


def test_candidate_gain_uses_incident_target_slice() -> None:
    parent_target = make_result("incident", 0.3)
    parent_target.partition = EvalPartition.INCIDENT
    candidate_target = make_result("incident", 0.4)
    candidate_target.partition = EvalPartition.INCIDENT
    parent = summarize_results([parent_target, make_result("regression", 1.0)], candidate_id=None, partition="all")
    candidate = summarize_results(
        [candidate_target, make_result("regression", 1.0)], candidate_id="candidate", partition="all"
    )
    comparison = compare_runs(parent, candidate)
    assert comparison["target_partition"] == "incident"
    assert comparison["quality_gain"] == 0.1
    assert comparison["eligible"]
