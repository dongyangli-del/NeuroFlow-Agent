"""SQLite-backed persistence for evolution feedback, candidates, and decisions."""

from __future__ import annotations

import json
import os
import weakref
from pathlib import Path
from typing import Any

from alembic import command
from alembic.config import Config
from alembic.script import ScriptDirectory
from sqlalchemy import Boolean, Float, String, Text, create_engine, select, text
from sqlalchemy import inspect as sa_inspect
from sqlalchemy.engine import make_url
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy.pool import NullPool

from .models import EvalRunSummary, EvolutionCandidate, FeedbackEvent, PromotionDecision


def redact_database_url(database_url: str) -> str:
    return make_url(database_url).render_as_string(hide_password=True)


class Base(DeclarativeBase):
    pass


class FeedbackRow(Base):
    __tablename__ = "feedback_events"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    run_id: Mapped[str] = mapped_column(String(96), index=True)
    event_type: Mapped[str] = mapped_column(String(40))
    summary: Mapped[str] = mapped_column(Text)
    failure_tag: Mapped[str] = mapped_column(String(120), default="")
    source: Mapped[str] = mapped_column(String(80), default="runtime")
    evidence_json: Mapped[str] = mapped_column(Text, default="{}")
    handled: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[str] = mapped_column(String(32))


class CandidateRow(Base):
    __tablename__ = "evolution_candidates"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    parent_id: Mapped[str | None] = mapped_column(String(96), nullable=True)
    target_component: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(40))
    risk_level: Mapped[str] = mapped_column(String(24))
    trigger_feedback_json: Mapped[str] = mapped_column(Text, default="[]")
    patch_path: Mapped[str] = mapped_column(Text)
    patch_sha256: Mapped[str] = mapped_column(String(64))
    generator_provider: Mapped[str] = mapped_column(String(80), default="")
    generator_model: Mapped[str] = mapped_column(String(120), default="")
    rationale: Mapped[str] = mapped_column(Text, default="")
    expected_gain: Mapped[float] = mapped_column(Float, default=0.0)
    requires_human: Mapped[bool] = mapped_column(Boolean, default=True)
    metadata_json: Mapped[str] = mapped_column(Text, default="{}")
    created_at: Mapped[str] = mapped_column(String(32))
    updated_at: Mapped[str] = mapped_column(String(32))


class EvalRunRow(Base):
    __tablename__ = "eval_runs"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    candidate_id: Mapped[str | None] = mapped_column(String(64), nullable=True, index=True)
    parent_run_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    status: Mapped[str] = mapped_column(String(32))
    partition: Mapped[str] = mapped_column(String(32))
    score: Mapped[float] = mapped_column(Float, default=0.0)
    dimension_scores_json: Mapped[str] = mapped_column(Text, default="{}")
    critical_pass: Mapped[bool] = mapped_column(Boolean, default=False)
    regressions_json: Mapped[str] = mapped_column(Text, default="[]")
    cost_json: Mapped[str] = mapped_column(Text, default="{}")
    result_path: Mapped[str] = mapped_column(Text)
    created_at: Mapped[str] = mapped_column(String(32))


class PromotionRow(Base):
    __tablename__ = "promotion_decisions"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    candidate_id: Mapped[str] = mapped_column(String(64), index=True)
    decision: Mapped[str] = mapped_column(String(32))
    actor: Mapped[str] = mapped_column(String(120))
    reason: Mapped[str] = mapped_column(Text)
    automatic: Mapped[bool] = mapped_column(Boolean, default=False)
    reviewer_provider: Mapped[str] = mapped_column(String(80), default="")
    reviewer_model: Mapped[str] = mapped_column(String(120), default="")
    rollback_target: Mapped[str] = mapped_column(String(64), default="")
    metadata_json: Mapped[str] = mapped_column(Text, default="{}")
    created_at: Mapped[str] = mapped_column(String(32))


class EvolutionStore:
    def __init__(self, root: Path, database_url: str | None = None) -> None:
        self.root = root
        default_path = root / ".private" / "evolution" / "neuroflow.db"
        default_path.parent.mkdir(parents=True, exist_ok=True)
        self.database_url = database_url or os.environ.get("NEUROFLOW_DATABASE_URL") or f"sqlite:///{default_path}"
        connect_args = {"check_same_thread": False} if self.database_url.startswith("sqlite") else {}
        engine_options: dict[str, Any] = {"future": True, "connect_args": connect_args}
        if self.database_url.startswith("sqlite") and self.database_url not in {"sqlite://", "sqlite:///:memory:"}:
            engine_options["poolclass"] = NullPool
        self.engine = create_engine(self.database_url, **engine_options)
        self.Session = sessionmaker(self.engine, expire_on_commit=False)
        self._finalizer = weakref.finalize(self, self.engine.dispose)

    @property
    def safe_database_url(self) -> str:
        return redact_database_url(self.database_url)

    def close(self) -> None:
        if self._finalizer.alive:
            self._finalizer()

    def initialize(self) -> None:
        if self.database_url in {"sqlite://", "sqlite:///:memory:"}:
            Base.metadata.create_all(self.engine)
            return
        config_path = self.root / "alembic.ini"
        migrations = self.root / "migrations"
        if config_path.exists() and migrations.exists():
            config = Config(str(config_path))
            config.set_main_option("script_location", str(migrations))
            config.set_main_option("sqlalchemy.url", self.database_url.replace("%", "%%"))
            tables = set(sa_inspect(self.engine).get_table_names())
            required = {"feedback_events", "evolution_candidates", "eval_runs", "promotion_decisions"}
            if required.issubset(tables) and "alembic_version" not in tables:
                command.stamp(config, "head")
                return
            if "alembic_version" in tables:
                with self.engine.connect() as connection:
                    current = connection.execute(text("SELECT version_num FROM alembic_version")).scalar_one_or_none()
                if current == ScriptDirectory.from_config(config).get_current_head():
                    return
            command.upgrade(config, "head")
            return
        Base.metadata.create_all(self.engine)

    def add_feedback(self, event: FeedbackEvent) -> FeedbackEvent:
        with self.Session.begin() as session:
            existing = session.scalar(
                select(FeedbackRow).where(
                    FeedbackRow.run_id == event.run_id,
                    FeedbackRow.event_type == event.event_type.value,
                    FeedbackRow.failure_tag == event.failure_tag,
                    FeedbackRow.summary == event.summary,
                )
            )
            if existing is not None:
                return _feedback_from_row(existing)
            session.merge(
                FeedbackRow(
                    id=event.id,
                    run_id=event.run_id,
                    event_type=event.event_type.value,
                    summary=event.summary,
                    failure_tag=event.failure_tag,
                    source=event.source,
                    evidence_json=_dump(event.evidence),
                    handled=event.handled,
                    created_at=event.created_at,
                )
            )
        return event

    def list_feedback(self, *, unhandled_only: bool = False) -> list[FeedbackEvent]:
        with self.Session() as session:
            statement = select(FeedbackRow).order_by(FeedbackRow.created_at)
            if unhandled_only:
                statement = statement.where(FeedbackRow.handled.is_(False))
            return [_feedback_from_row(row) for row in session.scalars(statement)]

    def mark_feedback_handled(self, ids: list[str]) -> None:
        if not ids:
            return
        with self.Session.begin() as session:
            for row in session.scalars(select(FeedbackRow).where(FeedbackRow.id.in_(ids))):
                row.handled = True

    def add_candidate(self, candidate: EvolutionCandidate) -> EvolutionCandidate:
        with self.Session.begin() as session:
            session.merge(_candidate_to_row(candidate))
        return candidate

    def get_candidate(self, candidate_id: str) -> EvolutionCandidate:
        with self.Session() as session:
            row = session.get(CandidateRow, candidate_id)
            if row is None:
                raise KeyError(f"Unknown evolution candidate: {candidate_id}")
            return _candidate_from_row(row)

    def list_candidates(self) -> list[EvolutionCandidate]:
        with self.Session() as session:
            rows = session.scalars(select(CandidateRow).order_by(CandidateRow.created_at.desc()))
            return [_candidate_from_row(row) for row in rows]

    def update_candidate(self, candidate: EvolutionCandidate) -> EvolutionCandidate:
        return self.add_candidate(candidate)

    def add_eval_run(self, summary: EvalRunSummary, result_path: Path) -> EvalRunSummary:
        with self.Session.begin() as session:
            session.merge(
                EvalRunRow(
                    id=summary.id,
                    candidate_id=summary.candidate_id,
                    parent_run_id=summary.parent_run_id,
                    status=summary.status,
                    partition=summary.partition,
                    score=summary.score,
                    dimension_scores_json=_dump(summary.dimension_scores),
                    critical_pass=summary.critical_pass,
                    regressions_json=_dump(summary.regressions),
                    cost_json=_dump(summary.cost),
                    result_path=str(result_path),
                    created_at=summary.created_at,
                )
            )
        return summary

    def list_eval_runs(self, candidate_id: str | None = None) -> list[dict[str, Any]]:
        with self.Session() as session:
            statement = select(EvalRunRow).order_by(EvalRunRow.created_at.desc())
            if candidate_id:
                statement = statement.where(EvalRunRow.candidate_id == candidate_id)
            return [_eval_run_dict(row) for row in session.scalars(statement)]

    def add_decision(self, decision: PromotionDecision) -> PromotionDecision:
        with self.Session.begin() as session:
            session.merge(
                PromotionRow(
                    id=decision.id,
                    candidate_id=decision.candidate_id,
                    decision=decision.decision,
                    actor=decision.actor,
                    reason=decision.reason,
                    automatic=decision.automatic,
                    reviewer_provider=decision.reviewer_provider,
                    reviewer_model=decision.reviewer_model,
                    rollback_target=decision.rollback_target,
                    metadata_json=_dump(decision.metadata),
                    created_at=decision.created_at,
                )
            )
        return decision

    def list_decisions(self, candidate_id: str | None = None) -> list[dict[str, Any]]:
        with self.Session() as session:
            statement = select(PromotionRow).order_by(PromotionRow.created_at.desc())
            if candidate_id:
                statement = statement.where(PromotionRow.candidate_id == candidate_id)
            return [_decision_dict(row) for row in session.scalars(statement)]


def _dump(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def _load(value: str) -> Any:
    return json.loads(value or "null")


def _feedback_from_row(row: FeedbackRow) -> FeedbackEvent:
    return FeedbackEvent(
        id=row.id,
        run_id=row.run_id,
        event_type=row.event_type,
        summary=row.summary,
        failure_tag=row.failure_tag,
        source=row.source,
        evidence=_load(row.evidence_json),
        handled=row.handled,
        created_at=row.created_at,
    )


def _candidate_to_row(candidate: EvolutionCandidate) -> CandidateRow:
    return CandidateRow(
        id=candidate.id,
        parent_id=candidate.parent_id,
        target_component=candidate.target_component,
        status=candidate.status.value,
        risk_level=candidate.risk_level.value,
        trigger_feedback_json=_dump(candidate.trigger_feedback_ids),
        patch_path=candidate.patch_path,
        patch_sha256=candidate.patch_sha256,
        generator_provider=candidate.generator_provider,
        generator_model=candidate.generator_model,
        rationale=candidate.rationale,
        expected_gain=candidate.expected_gain,
        requires_human=candidate.requires_human,
        metadata_json=_dump(candidate.metadata),
        created_at=candidate.created_at,
        updated_at=candidate.updated_at,
    )


def _candidate_from_row(row: CandidateRow) -> EvolutionCandidate:
    return EvolutionCandidate(
        id=row.id,
        parent_id=row.parent_id,
        target_component=row.target_component,
        status=row.status,
        risk_level=row.risk_level,
        trigger_feedback_ids=_load(row.trigger_feedback_json),
        patch_path=row.patch_path,
        patch_sha256=row.patch_sha256,
        generator_provider=row.generator_provider,
        generator_model=row.generator_model,
        rationale=row.rationale,
        expected_gain=row.expected_gain,
        requires_human=row.requires_human,
        metadata=_load(row.metadata_json),
        created_at=row.created_at,
        updated_at=row.updated_at,
    )


def _eval_run_dict(row: EvalRunRow) -> dict[str, Any]:
    return {
        "id": row.id,
        "candidate_id": row.candidate_id,
        "parent_run_id": row.parent_run_id,
        "status": row.status,
        "partition": row.partition,
        "score": row.score,
        "dimension_scores": _load(row.dimension_scores_json),
        "critical_pass": row.critical_pass,
        "regressions": _load(row.regressions_json),
        "cost": _load(row.cost_json),
        "result_path": row.result_path,
        "created_at": row.created_at,
    }


def _decision_dict(row: PromotionRow) -> dict[str, Any]:
    return {
        "id": row.id,
        "candidate_id": row.candidate_id,
        "decision": row.decision,
        "actor": row.actor,
        "reason": row.reason,
        "automatic": row.automatic,
        "reviewer_provider": row.reviewer_provider,
        "reviewer_model": row.reviewer_model,
        "rollback_target": row.rollback_target,
        "metadata": _load(row.metadata_json),
        "created_at": row.created_at,
    }
