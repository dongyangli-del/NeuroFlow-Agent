"""Create the NeuroFlow evolution control-plane tables."""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op

revision = "0001_evolution_control_plane"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "feedback_events",
        sa.Column("id", sa.String(64), primary_key=True),
        sa.Column("run_id", sa.String(96), nullable=False, index=True),
        sa.Column("event_type", sa.String(40), nullable=False),
        sa.Column("summary", sa.Text(), nullable=False),
        sa.Column("failure_tag", sa.String(120), nullable=False, server_default=""),
        sa.Column("source", sa.String(80), nullable=False, server_default="runtime"),
        sa.Column("evidence_json", sa.Text(), nullable=False, server_default="{}"),
        sa.Column("handled", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("created_at", sa.String(32), nullable=False),
    )
    op.create_table(
        "evolution_candidates",
        sa.Column("id", sa.String(64), primary_key=True),
        sa.Column("parent_id", sa.String(96), nullable=True),
        sa.Column("target_component", sa.String(255), nullable=False),
        sa.Column("status", sa.String(40), nullable=False),
        sa.Column("risk_level", sa.String(24), nullable=False),
        sa.Column("trigger_feedback_json", sa.Text(), nullable=False, server_default="[]"),
        sa.Column("patch_path", sa.Text(), nullable=False),
        sa.Column("patch_sha256", sa.String(64), nullable=False),
        sa.Column("generator_provider", sa.String(80), nullable=False, server_default=""),
        sa.Column("generator_model", sa.String(120), nullable=False, server_default=""),
        sa.Column("rationale", sa.Text(), nullable=False, server_default=""),
        sa.Column("expected_gain", sa.Float(), nullable=False, server_default="0"),
        sa.Column("requires_human", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("metadata_json", sa.Text(), nullable=False, server_default="{}"),
        sa.Column("created_at", sa.String(32), nullable=False),
        sa.Column("updated_at", sa.String(32), nullable=False),
    )
    op.create_table(
        "eval_runs",
        sa.Column("id", sa.String(64), primary_key=True),
        sa.Column("candidate_id", sa.String(64), nullable=True, index=True),
        sa.Column("parent_run_id", sa.String(64), nullable=True),
        sa.Column("status", sa.String(32), nullable=False),
        sa.Column("partition", sa.String(32), nullable=False),
        sa.Column("score", sa.Float(), nullable=False, server_default="0"),
        sa.Column("dimension_scores_json", sa.Text(), nullable=False, server_default="{}"),
        sa.Column("critical_pass", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("regressions_json", sa.Text(), nullable=False, server_default="[]"),
        sa.Column("cost_json", sa.Text(), nullable=False, server_default="{}"),
        sa.Column("result_path", sa.Text(), nullable=False),
        sa.Column("created_at", sa.String(32), nullable=False),
    )
    op.create_table(
        "promotion_decisions",
        sa.Column("id", sa.String(64), primary_key=True),
        sa.Column("candidate_id", sa.String(64), nullable=False, index=True),
        sa.Column("decision", sa.String(32), nullable=False),
        sa.Column("actor", sa.String(120), nullable=False),
        sa.Column("reason", sa.Text(), nullable=False),
        sa.Column("automatic", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("reviewer_provider", sa.String(80), nullable=False, server_default=""),
        sa.Column("reviewer_model", sa.String(120), nullable=False, server_default=""),
        sa.Column("rollback_target", sa.String(64), nullable=False, server_default=""),
        sa.Column("metadata_json", sa.Text(), nullable=False, server_default="{}"),
        sa.Column("created_at", sa.String(32), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("promotion_decisions")
    op.drop_table("eval_runs")
    op.drop_table("evolution_candidates")
    op.drop_table("feedback_events")
