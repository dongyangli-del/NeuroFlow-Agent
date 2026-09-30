"""Typed contracts for the NeuroFlow evolution control plane."""

from __future__ import annotations

from datetime import UTC, datetime
from enum import StrEnum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, model_validator


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex[:16]}"


class EvolutionMode(StrEnum):
    OFF = "off"
    SHADOW = "shadow"
    SEMI_AUTO = "semi-auto"


class RiskLevel(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class CandidateStatus(StrEnum):
    OBSERVED = "observed"
    CLUSTERED = "clustered"
    PROPOSED = "proposed"
    SHADOW_TESTING = "shadow_testing"
    AWAITING_REVIEW = "awaiting_review"
    CANARY = "canary"
    PROMOTED = "promoted"
    REJECTED = "rejected"
    ROLLED_BACK = "rolled_back"


class FeedbackType(StrEnum):
    USER_CORRECTION = "user_correction"
    GATE_FAILURE = "gate_failure"
    TOOL_FAILURE = "tool_failure"
    REVIEWER_OBJECTION = "reviewer_objection"
    EVAL_REGRESSION = "eval_regression"
    RUNTIME_FAILURE = "runtime_failure"


class EvalPartition(StrEnum):
    INCIDENT = "incident"
    REGRESSION = "regression"
    PROTECTED = "protected"
    HIDDEN_HOLDOUT = "hidden_holdout"


class EvalDimension(StrEnum):
    ADAPTIVITY = "adaptivity"
    RETENTION = "retention"
    GENERALIZATION = "generalization"
    EFFICIENCY = "efficiency"
    SAFETY = "safety"


class AssertionType(StrEnum):
    CONTAINS = "contains"
    NOT_CONTAINS = "not_contains"
    REGEX = "regex"
    JSON_PATH = "json_path"
    JSON_SCHEMA = "json_schema"
    FILE_EXISTS = "file_exists"
    FILE_DIFF = "file_diff"
    ARTIFACT_FIELD = "artifact_field"
    COMMAND_EXIT = "command_exit"
    LLM_RUBRIC = "llm_rubric"


class FeedbackEvent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(default_factory=lambda: new_id("feedback"))
    run_id: str
    event_type: FeedbackType
    summary: str
    failure_tag: str = ""
    source: str = "runtime"
    evidence: dict[str, Any] = Field(default_factory=dict)
    handled: bool = False
    created_at: str = Field(default_factory=utc_now)


class EvolutionCandidate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(default_factory=lambda: new_id("candidate"))
    parent_id: str | None = None
    target_component: str
    status: CandidateStatus = CandidateStatus.PROPOSED
    risk_level: RiskLevel
    trigger_feedback_ids: list[str] = Field(default_factory=list)
    patch_path: str
    patch_sha256: str
    generator_provider: str = ""
    generator_model: str = ""
    rationale: str = ""
    expected_gain: float = 0.0
    requires_human: bool = True
    metadata: dict[str, Any] = Field(default_factory=dict)
    created_at: str = Field(default_factory=utc_now)
    updated_at: str = Field(default_factory=utc_now)


class EvalAssertion(BaseModel):
    model_config = ConfigDict(extra="allow")

    type: AssertionType = AssertionType.LLM_RUBRIC
    text: str = ""
    value: Any = None
    path: str = ""
    expected_path: str = ""
    field: str = ""
    pattern: str = ""
    schema_def: dict[str, Any] = Field(default_factory=dict, alias="schema")
    command: list[str] = Field(default_factory=list)
    expected_exit: int = 0
    critical: bool = False
    weight: float = 1.0
    dimension: EvalDimension = EvalDimension.ADAPTIVITY

    @model_validator(mode="after")
    def validate_payload(self) -> EvalAssertion:
        if self.type in {AssertionType.CONTAINS, AssertionType.NOT_CONTAINS} and not (self.value or self.text):
            raise ValueError(f"{self.type} assertion needs value or text")
        if self.type == AssertionType.REGEX and not (self.pattern or self.value):
            raise ValueError("regex assertion needs pattern or value")
        if self.type == AssertionType.COMMAND_EXIT and not self.command:
            raise ValueError("command_exit assertion needs command")
        file_assertions = {AssertionType.FILE_EXISTS, AssertionType.FILE_DIFF, AssertionType.ARTIFACT_FIELD}
        if self.type in file_assertions and not self.path:
            raise ValueError(f"{self.type} assertion needs path")
        if self.type == AssertionType.FILE_DIFF and not self.expected_path:
            raise ValueError("file_diff assertion needs expected_path")
        if self.type == AssertionType.ARTIFACT_FIELD and not self.field:
            raise ValueError("artifact_field assertion needs field")
        if self.type == AssertionType.JSON_SCHEMA and not self.schema_def:
            raise ValueError("json_schema assertion needs schema")
        return self


class EvalCase(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str
    skill_name: str = ""
    prompt: str
    expected_output: str = ""
    files: list[str] = Field(default_factory=list)
    assertions: list[EvalAssertion] = Field(default_factory=list)
    partition: EvalPartition = EvalPartition.REGRESSION
    tags: list[str] = Field(default_factory=list)
    repeats: int = Field(default=1, ge=1, le=10)
    source_path: str = ""
    skill_root: str = ""


class AssertionResult(BaseModel):
    assertion: EvalAssertion
    passed: bool
    score: float
    message: str = ""
    tokens: int = 0
    cost_usd: float = 0.0


class EvalCaseResult(BaseModel):
    case_id: str
    partition: EvalPartition
    output: str
    assertions: list[AssertionResult]
    score: float
    critical_pass: bool
    duration_ms: int = 0
    tokens: int = 0
    cost_usd: float = 0.0


class EvalRunSummary(BaseModel):
    id: str = Field(default_factory=lambda: new_id("evalrun"))
    candidate_id: str | None = None
    parent_run_id: str | None = None
    status: str = "completed"
    partition: str = "all"
    score: float
    dimension_scores: dict[str, float] = Field(default_factory=dict)
    case_statistics: dict[str, dict[str, float]] = Field(default_factory=dict)
    critical_pass: bool
    regressions: list[str] = Field(default_factory=list)
    cost: dict[str, float] = Field(default_factory=dict)
    results: list[EvalCaseResult] = Field(default_factory=list)
    created_at: str = Field(default_factory=utc_now)


class PromotionDecision(BaseModel):
    id: str = Field(default_factory=lambda: new_id("decision"))
    candidate_id: str
    decision: str
    actor: str
    reason: str
    automatic: bool = False
    reviewer_provider: str = ""
    reviewer_model: str = ""
    rollback_target: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)
    created_at: str = Field(default_factory=utc_now)
