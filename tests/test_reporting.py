from __future__ import annotations

from pathlib import Path

from neuroflow_runtime.evolution import EvolutionEngine
from neuroflow_runtime.reporting import build_report
from neuroflow_runtime.storage import EvolutionStore


def test_static_reports_are_generated(tmp_path: Path) -> None:
    store = EvolutionStore(tmp_path, "sqlite:///:memory:")
    store.initialize()
    paths = build_report(tmp_path, store, tmp_path / "reports")
    assert Path(paths["markdown"]).read_text(encoding="utf-8").startswith("# NeuroFlow Evolution Report")
    assert "<title>NeuroFlow Evolution Report</title>" in Path(paths["html"]).read_text(encoding="utf-8")


def test_report_contains_candidate_diff_and_rollback_command(
    git_repo: Path,
    additive_reference_patch: str,
) -> None:
    engine = EvolutionEngine(git_repo)
    candidate = engine.create_candidate_from_patch(additive_reference_patch, rationale="report test")
    paths = build_report(git_repo, engine.store, git_repo / ".private/reports")
    markdown = Path(paths["markdown"]).read_text(encoding="utf-8")
    html = Path(paths["html"]).read_text(encoding="utf-8")
    assert candidate.id in markdown
    assert "```diff" in markdown
    assert "Patch integrity: True" in markdown
    assert f"neuroflow evolve rollback {candidate.id}" in markdown
    assert "Candidate Diffs" in html
    assert "Patch integrity" in html
    assert "Cost" in html
