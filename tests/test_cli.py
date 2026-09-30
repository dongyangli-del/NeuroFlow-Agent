from __future__ import annotations

import json
from pathlib import Path

from neuroflow_runtime.cli import app
from typer.testing import CliRunner


def test_failed_executed_workflow_returns_nonzero_exit() -> None:
    result = CliRunner().invoke(
        app,
        [
            "run",
            "--chain",
            "idea-to-experiment",
            "--task",
            "Create an experiment",
            "--execute",
            "--provider",
            "mock",
        ],
        env={"NEUROFLOW_EXECUTOR_MOCK_RESPONSE": "insufficient evidence"},
    )
    assert result.exit_code == 1
    payload = json.loads(result.stdout)
    assert payload["status"] == "failed"


def test_registry_eval_kb_and_evolution_commands(tmp_path: Path) -> None:
    runner = CliRunner()
    assert runner.invoke(app, ["list", "--kind", "chains"]).exit_code == 0

    eval_result = runner.invoke(app, ["eval", "list", "--partition", "protected"])
    assert eval_result.exit_code == 0
    assert len(json.loads(eval_result.stdout)) == 3

    assert runner.invoke(app, ["kb", "summary"]).exit_code == 0
    init_result = runner.invoke(app, ["evolve", "init"])
    assert init_result.exit_code == 0
    assert "***" not in json.loads(init_result.stdout)["database_url"]
    assert runner.invoke(app, ["evolve", "list"]).exit_code == 0

    report_result = runner.invoke(
        app,
        ["report", "evolution", "--output-dir", str(tmp_path / "report")],
    )
    assert report_result.exit_code == 0
    report_paths = json.loads(report_result.stdout)
    assert Path(report_paths["markdown"]).exists()
    assert Path(report_paths["html"]).exists()


def test_cli_dry_run_and_external_result_import(tmp_path: Path) -> None:
    runner = CliRunner()
    run_result = runner.invoke(
        app,
        [
            "run",
            "--chain",
            "paper-to-repro",
            "--task",
            "Build a reproduction contract",
            "--dry-run",
        ],
    )
    assert run_result.exit_code == 0
    run_payload = json.loads(run_result.stdout)
    artifact = tmp_path / "stage.md"
    artifact.write_text("citation source arxiv doi prior work uncertain\n", encoding="utf-8")
    import_result = runner.invoke(
        app,
        [
            "import-result",
            "--run-id",
            run_payload["run_id"],
            "--step",
            "1",
            "--artifact",
            str(artifact),
            "--status",
            "passed",
            "--metric",
            "tokens=12",
        ],
    )
    assert import_result.exit_code == 0
    assert json.loads(import_result.stdout)["step"] == 1


def test_cli_hook_routes_baseline_failure() -> None:
    result = CliRunner().invoke(
        app,
        [
            "hook",
            "--event",
            "session_start",
            "--task",
            "My EEG result is worse than the baseline",
        ],
    )
    assert result.exit_code == 0
    assert json.loads(result.stdout)["selected_chain"] == "benchmark-to-baseline"
