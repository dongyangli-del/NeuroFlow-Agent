from __future__ import annotations

import json
from pathlib import Path

import pytest
from neuroflow_runtime.evals import run_sync
from neuroflow_runtime.evolution import (
    EvolutionEngine,
    EvolutionError,
    cluster_feedback,
    sanitize_provider_context,
)
from neuroflow_runtime.models import CandidateStatus, FeedbackEvent, FeedbackType, RiskLevel
from neuroflow_runtime.promotion import PromotionController
from neuroflow_runtime.providers import MockProvider, ModelRequest, ModelResponse


def test_feedback_clustering() -> None:
    events = [
        FeedbackEvent(run_id="1", event_type=FeedbackType.GATE_FAILURE, summary="a", failure_tag="gate:benchmark"),
        FeedbackEvent(run_id="2", event_type=FeedbackType.GATE_FAILURE, summary="b", failure_tag="gate:benchmark"),
        FeedbackEvent(run_id="3", event_type=FeedbackType.TOOL_FAILURE, summary="c", failure_tag="tool:web"),
    ]
    clusters = cluster_feedback(events)
    assert len(clusters["gate:benchmark"]) == 2
    assert len(clusters["tool:web"]) == 1


def test_provider_context_is_privacy_scrubbed() -> None:
    credential = "sk-" + "a" * 26
    text = f"Read /home/researcher/private.csv for participant-P001 using {credential}"
    scrubbed = sanitize_provider_context(text)
    assert "/home/" not in scrubbed
    assert "participant-P001" not in scrubbed
    assert credential not in scrubbed
    public_url = "https://example.org/home/research"
    assert sanitize_provider_context(public_url) == public_url


def test_candidate_lifecycle_and_incident_eval(
    git_repo: Path,
    additive_reference_patch: str,
) -> None:
    engine = EvolutionEngine(git_repo)
    feedback = engine.store.add_feedback(
        FeedbackEvent(
            run_id="run",
            event_type=FeedbackType.USER_CORRECTION,
            summary="Add source trace",
            failure_tag="citation:missing",
        )
    )
    candidate = engine.create_candidate_from_patch(
        additive_reference_patch,
        feedback_ids=[feedback.id],
        rationale="Prevent repeated source omissions",
    )
    assert candidate.status == CandidateStatus.PROPOSED
    assert candidate.parent_id and candidate.parent_id.startswith("git:")
    assert candidate.risk_level == RiskLevel.LOW
    assert [item["to"] for item in candidate.metadata["status_history"]] == ["observed", "clustered", "proposed"]
    assert Path(candidate.patch_path).exists()
    assert list((git_repo / ".private/evolution/evals/incidents").glob("*.json"))
    assert not engine.store.list_feedback(unhandled_only=True)


def test_candidate_cannot_modify_protected_eval(git_repo: Path) -> None:
    (git_repo / "evals").mkdir()
    (git_repo / "evals/protected.json").write_text("{}\n", encoding="utf-8")
    patch = """diff --git a/evals/protected.json b/evals/protected.json
--- a/evals/protected.json
+++ b/evals/protected.json
@@ -1 +1 @@
-{}
+{"disabled": true}
"""
    with pytest.raises(EvolutionError, match="protected eval"):
        EvolutionEngine(git_repo).create_candidate_from_patch(patch)


def test_candidate_cannot_modify_hidden_holdout(git_repo: Path) -> None:
    patch = """diff --git a/.private/evolution/evals/hidden.json b/.private/evolution/evals/hidden.json
new file mode 100644
--- /dev/null
+++ b/.private/evolution/evals/hidden.json
@@ -0,0 +1 @@
+{}
"""
    with pytest.raises(EvolutionError, match="hidden holdout"):
        EvolutionEngine(git_repo).create_candidate_from_patch(patch)


def test_provider_can_propose_a_valid_candidate(
    git_repo: Path,
    additive_reference_patch: str,
) -> None:
    engine = EvolutionEngine(git_repo)
    feedback = engine.store.add_feedback(
        FeedbackEvent(
            run_id="run",
            event_type=FeedbackType.USER_CORRECTION,
            summary="Missing source trace",
            failure_tag="citation:missing",
        )
    )
    provider = MockProvider(
        response=json.dumps(
            {
                "target_component": "example reference",
                "rationale": "add verified source",
                "expected_gain": 0.04,
                "patch": additive_reference_patch,
            }
        )
    )
    candidates = run_sync(engine.propose(provider, feedback_ids=[feedback.id], variants=1))
    assert len(candidates) == 1
    assert candidates[0].metadata["feedback_cluster"] == "citation:missing"


def test_off_mode_blocks_candidate_creation(
    git_repo: Path,
    additive_reference_patch: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("NEUROFLOW_EVOLUTION_MODE", "off")
    with pytest.raises(EvolutionError, match="disabled"):
        EvolutionEngine(git_repo).create_candidate_from_patch(additive_reference_patch)


def test_off_mode_blocks_existing_candidate_evaluation(
    git_repo: Path,
    additive_reference_patch: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    engine = EvolutionEngine(git_repo)
    candidate = engine.create_candidate_from_patch(additive_reference_patch)
    monkeypatch.setenv("NEUROFLOW_EVOLUTION_MODE", "off")
    with pytest.raises(EvolutionError, match="disabled"):
        engine.evaluate_candidate(candidate.id, MockProvider("executor"), MockProvider("reviewer"))


def test_manual_candidate_gets_synthetic_feedback_and_incident_eval(
    git_repo: Path,
    additive_reference_patch: str,
) -> None:
    engine = EvolutionEngine(git_repo)
    candidate = engine.create_candidate_from_patch(additive_reference_patch, rationale="manual improvement")
    assert len(candidate.trigger_feedback_ids) == 1
    assert engine.store.list_feedback()[0].summary == "manual improvement"
    assert list((git_repo / ".private/evolution/evals/incidents").glob("*.json"))


def test_high_risk_candidate_requires_shadow_approval(git_repo: Path) -> None:
    patch = """diff --git a/skills/example/SKILL.md b/skills/example/SKILL.md
--- a/skills/example/SKILL.md
+++ b/skills/example/SKILL.md
@@ -4,2 +4,3 @@ description: test
 ---
 # Example
+New routing policy.
"""
    engine = EvolutionEngine(git_repo)
    candidate = engine.create_candidate_from_patch(patch)
    with pytest.raises(EvolutionError, match="human shadow approval"):
        engine.evaluate_candidate(candidate.id, MockProvider("executor"), MockProvider("reviewer"))
    decision = PromotionController(git_repo, engine).review(
        candidate.id,
        approve=True,
        actor="owner",
        reason="Safe to execute in the isolated worktree",
    )
    assert decision.decision == "shadow_approved"
    assert engine.store.get_candidate(candidate.id).status == CandidateStatus.PROPOSED


def test_candidate_patch_tampering_is_detected(
    git_repo: Path,
    additive_reference_patch: str,
) -> None:
    engine = EvolutionEngine(git_repo)
    candidate = engine.create_candidate_from_patch(additive_reference_patch)
    Path(candidate.patch_path).write_text(additive_reference_patch + "\n# tampered\n", encoding="utf-8")
    with pytest.raises(EvolutionError, match="integrity"):
        engine.evaluate_candidate(candidate.id, MockProvider("executor"), MockProvider("reviewer"))


def test_hidden_holdout_cannot_be_skipped_for_candidate_evaluation(
    git_repo: Path,
    additive_reference_patch: str,
) -> None:
    engine = EvolutionEngine(git_repo)
    candidate = engine.create_candidate_from_patch(additive_reference_patch)
    hidden = git_repo / ".private/evolution/evals/hidden.json"
    hidden.parent.mkdir(parents=True, exist_ok=True)
    hidden.write_text('{"skill_name":"hidden","evals":[]}\n', encoding="utf-8")
    with pytest.raises(EvolutionError, match="mandatory"):
        engine.evaluate_candidate(
            candidate.id,
            MockProvider("executor"),
            MockProvider("reviewer"),
            include_hidden=False,
        )


def test_incident_eval_redacts_sensitive_feedback(
    git_repo: Path,
    additive_reference_patch: str,
) -> None:
    engine = EvolutionEngine(git_repo)
    feedback = engine.store.add_feedback(
        FeedbackEvent(
            run_id="private-run",
            event_type=FeedbackType.USER_CORRECTION,
            summary="participant-P001 failed at /home/researcher/raw.csv",
            failure_tag="privacy:redaction",
        )
    )
    engine.create_candidate_from_patch(additive_reference_patch, feedback_ids=[feedback.id])
    incident = next((git_repo / ".private/evolution/evals/incidents").glob("*.json"))
    text = incident.read_text(encoding="utf-8")
    assert "participant-P001" not in text
    assert "/home/researcher" not in text
    assert "[participant-id]" in text


class PatchAwareProvider:
    def __init__(self, name: str, model: str) -> None:
        self.name = name
        self.model = model

    async def generate(self, request: ModelRequest) -> ModelResponse:
        if "Independently review" in request.prompt:
            text = '{"verdict":"pass","disagreements":[],"required_fixes":[],"source_trace_valid":true}'
        elif "Judge one assertion" in request.prompt:
            passed = "source-traced behavior" in request.prompt
            text = json.dumps({"passed": passed, "score": 1.0 if passed else 0.0, "reason": "test"})
        else:
            text = "source-traced behavior" if "# Evolved Check" in request.prompt else "missing behavior"
        return ModelResponse(text=text, provider=self.name, model=self.model, input_tokens=10, output_tokens=2)


class NoRemoteProvider:
    name = "must-not-run"
    model = "must-not-run"

    async def generate(self, request: ModelRequest) -> ModelResponse:
        raise AssertionError(f"Private-memory evaluation called a remote provider: {request.prompt[:80]}")


def test_private_memory_candidate_uses_local_incident_and_review_checks(git_repo: Path) -> None:
    patch = """diff --git a/.private/references/lesson.md b/.private/references/lesson.md
new file mode 100644
--- /dev/null
+++ b/.private/references/lesson.md
@@ -0,0 +1 @@
+# Reusable local lesson
"""
    engine = EvolutionEngine(git_repo)
    candidate = engine.create_candidate_from_patch(patch, rationale="Keep this local")
    result = engine.evaluate_candidate(
        candidate.id,
        NoRemoteProvider(),
        NoRemoteProvider(),
        include_hidden=False,
    )
    assert result["eligible"]
    assert result["review_verdict"]["provider"] == "local-policy"
    assert engine.store.get_candidate(candidate.id).metadata["reviewer"]["provider"] == "local-policy"


def test_candidate_shadow_evaluation_compares_parent_and_patch(
    git_repo: Path,
    additive_reference_patch: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    engine = EvolutionEngine(git_repo)
    candidate = engine.create_candidate_from_patch(additive_reference_patch, rationale="add behavior")
    result = engine.evaluate_candidate(
        candidate.id,
        PatchAwareProvider("executor", "one"),
        PatchAwareProvider("reviewer", "two"),
        include_hidden=False,
    )
    assert result["eligible"]
    assert result["quality_gain"] == 1.0
    assert result["target_partition"] == "incident"
    assert result["review_verdict"]["verdict"] == "pass"
    assert engine.store.get_candidate(candidate.id).status == CandidateStatus.AWAITING_REVIEW
    monkeypatch.setenv("NEUROFLOW_EVOLUTION_MODE", "semi-auto")
    promoted = PromotionController(git_repo, engine).promote(
        candidate.id,
        automatic=True,
        executor=PatchAwareProvider("executor", "one"),
        reviewer=PatchAwareProvider("reviewer", "two"),
    )
    assert promoted["status"] == "promoted"
    rolled_back = PromotionController(git_repo, engine).rollback(
        candidate.id,
        actor="test",
        reason="verify rollback",
    )
    assert rolled_back["status"] == "rolled_back"
