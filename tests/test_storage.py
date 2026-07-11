from __future__ import annotations

from pathlib import Path

from neuroflow_runtime.models import (
    CandidateStatus,
    EvolutionCandidate,
    FeedbackEvent,
    FeedbackType,
    RiskLevel,
)
from neuroflow_runtime.storage import EvolutionStore, redact_database_url


def test_store_round_trip(tmp_path: Path) -> None:
    store = EvolutionStore(tmp_path, "sqlite:///:memory:")
    store.initialize()
    feedback = store.add_feedback(
        FeedbackEvent(run_id="run", event_type=FeedbackType.USER_CORRECTION, summary="fix routing")
    )
    assert store.list_feedback(unhandled_only=True)[0].id == feedback.id
    candidate = EvolutionCandidate(
        target_component="routing",
        status=CandidateStatus.PROPOSED,
        risk_level=RiskLevel.HIGH,
        patch_path="/tmp/patch",
        patch_sha256="0" * 64,
    )
    store.add_candidate(candidate)
    loaded = store.get_candidate(candidate.id)
    assert loaded.risk_level == RiskLevel.HIGH
    assert loaded.status == CandidateStatus.PROPOSED
    store.mark_feedback_handled([feedback.id])
    assert not store.list_feedback(unhandled_only=True)


def test_database_url_redaction_hides_password() -> None:
    rendered = redact_database_url("postgresql+psycopg://researcher:secret@db.example/neuroflow")
    assert "secret" not in rendered
    assert "***" in rendered
