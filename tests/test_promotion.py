from __future__ import annotations

import subprocess
from pathlib import Path

import pytest
from neuroflow_runtime.evolution import EvolutionEngine
from neuroflow_runtime.models import CandidateStatus
from neuroflow_runtime.promotion import PromotionController, PromotionError
from neuroflow_runtime.providers import MockProvider


def eligible_candidate(git_repo: Path, patch: str):
    engine = EvolutionEngine(git_repo)
    candidate = engine.create_candidate_from_patch(patch)
    candidate.metadata.update(
        {
            "comparison": {"eligible": True},
            "reviewer": {"provider": "mock", "model": "reviewer"},
            "review_verdict": {"verdict": "pass", "source_trace_valid": True},
        }
    )
    engine.transition(candidate, CandidateStatus.SHADOW_TESTING)
    engine.transition(candidate, CandidateStatus.AWAITING_REVIEW)
    return engine, candidate


def test_low_risk_auto_promotion_and_rollback(
    git_repo: Path,
    additive_reference_patch: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    engine, candidate = eligible_candidate(git_repo, additive_reference_patch)
    monkeypatch.setenv("NEUROFLOW_EVOLUTION_MODE", "semi-auto")
    controller = PromotionController(git_repo, engine)
    result = controller.promote(
        candidate.id,
        automatic=True,
        executor=MockProvider("executor"),
        reviewer=MockProvider("reviewer"),
    )
    target = git_repo / "skills/example/references/evolved.md"
    assert result["status"] == "promoted"
    assert target.exists()
    rollback = controller.rollback(candidate.id, actor="tester", reason="test rollback")
    assert rollback["status"] == "rolled_back"
    assert not target.exists()


def test_auto_promotion_requires_independent_reviewer(
    git_repo: Path,
    additive_reference_patch: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    engine, candidate = eligible_candidate(git_repo, additive_reference_patch)
    monkeypatch.setenv("NEUROFLOW_EVOLUTION_MODE", "semi-auto")
    with pytest.raises(PromotionError, match="independent reviewer"):
        PromotionController(git_repo, engine).promote(
            candidate.id,
            automatic=True,
            executor=MockProvider("same"),
            reviewer=MockProvider("same"),
        )


def test_default_shadow_mode_blocks_automatic_promotion(
    git_repo: Path,
    additive_reference_patch: str,
) -> None:
    engine, candidate = eligible_candidate(git_repo, additive_reference_patch)
    with pytest.raises(PromotionError, match="semi-auto"):
        PromotionController(git_repo, engine).promote(
            candidate.id,
            automatic=True,
            executor=MockProvider("executor"),
            reviewer=MockProvider("reviewer"),
        )


def test_off_mode_blocks_existing_candidate_promotion(
    git_repo: Path,
    additive_reference_patch: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    engine, candidate = eligible_candidate(git_repo, additive_reference_patch)
    monkeypatch.setenv("NEUROFLOW_EVOLUTION_MODE", "off")
    with pytest.raises(PromotionError, match="disabled"):
        PromotionController(git_repo, engine).promote(candidate.id, actor="owner")


def test_high_risk_requires_human_approval(git_repo: Path) -> None:
    patch = """diff --git a/skills/example/SKILL.md b/skills/example/SKILL.md
--- a/skills/example/SKILL.md
+++ b/skills/example/SKILL.md
@@ -4,2 +4,3 @@ description: test
 ---
 # Example
+New policy.
"""
    engine, candidate = eligible_candidate(git_repo, patch)
    controller = PromotionController(git_repo, engine)
    with pytest.raises(PromotionError, match="human approval"):
        controller.promote(candidate.id, actor="tester")
    controller.review(candidate.id, approve=True, actor="owner", reason="approved")
    result = controller.promote(candidate.id, actor="owner")
    assert result["status"] == "promoted"


def test_high_risk_candidate_cannot_auto_promote(
    git_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    patch = """diff --git a/skills/example/SKILL.md b/skills/example/SKILL.md
--- a/skills/example/SKILL.md
+++ b/skills/example/SKILL.md
@@ -4,2 +4,3 @@ description: test
 ---
 # Example
+New policy.
"""
    engine, candidate = eligible_candidate(git_repo, patch)
    monkeypatch.setenv("NEUROFLOW_EVOLUTION_MODE", "semi-auto")
    with pytest.raises(PromotionError, match="Only low-risk"):
        PromotionController(git_repo, engine).promote(
            candidate.id,
            automatic=True,
            executor=MockProvider("executor"),
            reviewer=MockProvider("reviewer"),
        )


def test_promotion_blocks_stale_parent_revision(
    git_repo: Path,
    additive_reference_patch: str,
) -> None:
    engine, candidate = eligible_candidate(git_repo, additive_reference_patch)
    (git_repo / "unrelated.txt").write_text("new commit\n", encoding="utf-8")
    subprocess.run(["git", "add", "unrelated.txt"], cwd=git_repo, check=True)
    subprocess.run(["git", "commit", "-m", "advance head"], cwd=git_repo, check=True, stdout=subprocess.PIPE)
    with pytest.raises(PromotionError, match="HEAD changed"):
        PromotionController(git_repo, engine).promote(candidate.id, actor="owner")


def test_promotion_blocks_tampered_patch(
    git_repo: Path,
    additive_reference_patch: str,
) -> None:
    engine, candidate = eligible_candidate(git_repo, additive_reference_patch)
    Path(candidate.patch_path).write_text(additive_reference_patch + "\n# changed\n", encoding="utf-8")
    with pytest.raises(PromotionError, match="integrity"):
        PromotionController(git_repo, engine).promote(candidate.id, actor="owner")


def test_canary_failure_automatically_rolls_back_patch(
    git_repo: Path,
    additive_reference_patch: str,
) -> None:
    (git_repo / "Makefile").write_text("validate:\n\t@false\n", encoding="utf-8")
    subprocess.run(["git", "add", "Makefile"], cwd=git_repo, check=True)
    subprocess.run(["git", "commit", "-m", "failing canary"], cwd=git_repo, check=True, stdout=subprocess.PIPE)
    engine, candidate = eligible_candidate(git_repo, additive_reference_patch)
    controller = PromotionController(git_repo, engine)
    with pytest.raises(PromotionError, match="Canary validation failed"):
        controller.promote(candidate.id, actor="owner")
    assert not (git_repo / "skills/example/references/evolved.md").exists()
    assert engine.store.get_candidate(candidate.id).status == CandidateStatus.ROLLED_BACK
    assert engine.store.list_decisions(candidate.id)[0]["decision"] == "canary_failed_rollback"
