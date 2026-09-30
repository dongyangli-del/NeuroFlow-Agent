"""Trace schema for lightweight NeuroFlow runs."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from uuid import uuid4

STEP_STATUSES = {"planned", "running", "passed", "failed", "skipped", "blocked"}


def timestamp() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


@dataclass
class GateResult:
    gate: str
    status: str
    message: str = ""
    evidence_refs: list[str] = field(default_factory=list)
    checked_at: str = field(default_factory=timestamp)


@dataclass
class RouteCandidate:
    chain: str
    score: float
    reasons: list[str] = field(default_factory=list)


@dataclass
class TraceStep:
    index: int
    name: str
    module: str
    required_reads: list[str] = field(default_factory=list)
    evidence_gates: list[str] = field(default_factory=list)
    output: str = ""
    status: str = "planned"
    input_refs: list[str] = field(default_factory=list)
    output_refs: list[str] = field(default_factory=list)
    output_hash: str = ""
    gate_results: list[GateResult] = field(default_factory=list)
    started_at: str = ""
    completed_at: str = ""
    retry_count: int = 0
    failure_tag: str = ""
    error: str = ""
    metrics: dict[str, float] = field(default_factory=dict)

    def start(self) -> None:
        self.status = "running"
        self.started_at = timestamp()

    def finish(
        self,
        status: str,
        *,
        output_refs: list[str] | None = None,
        output_text: str = "",
        failure_tag: str = "",
        error: str = "",
        metrics: dict[str, float] | None = None,
    ) -> None:
        if status not in STEP_STATUSES:
            raise ValueError(f"Invalid step status: {status}")
        self.status = status
        self.completed_at = timestamp()
        self.output_refs = output_refs or self.output_refs
        if output_text:
            self.output_hash = hashlib.sha256(output_text.encode("utf-8")).hexdigest()
        self.failure_tag = failure_tag
        self.error = error
        if metrics:
            self.metrics.update(metrics)


@dataclass
class HookEvent:
    event: str
    status: str
    created_at: str
    hook_id: str = ""
    profile: str = "standard"
    warnings: list[str] = field(default_factory=list)
    selected_chain: str = ""
    artifact: str = ""
    blocked_reason: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkflowTrace:
    run_id: str
    chain: str
    task: str
    artifact: str
    status: str
    created_at: str
    stop_condition: str
    schema_version: int = 2
    steps: list[TraceStep] = field(default_factory=list)
    hook_events: list[HookEvent] = field(default_factory=list)
    skill_versions: dict[str, str] = field(default_factory=dict)
    route_candidates: list[RouteCandidate] = field(default_factory=list)
    selected_route: str = ""
    gate_results: list[GateResult] = field(default_factory=list)
    outcome: dict[str, Any] = field(default_factory=dict)
    feedback_ids: list[str] = field(default_factory=list)
    failure_tags: list[str] = field(default_factory=list)
    cost: dict[str, float] = field(default_factory=dict)
    completed_at: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def create(cls, chain: str, task: str, artifact: str, stop_condition: str) -> WorkflowTrace:
        created_at = timestamp()
        return cls(
            run_id=f"nf_{datetime.now(UTC).strftime('%Y%m%d_%H%M%S')}_{uuid4().hex[:8]}",
            chain=chain,
            task=task,
            artifact=artifact,
            status="planned",
            created_at=created_at,
            stop_condition=stop_condition,
            selected_route=chain,
        )

    def to_dict(self) -> dict[str, object]:
        return asdict(self)

    @classmethod
    def from_dict(cls, payload: dict[str, object]) -> WorkflowTrace:
        steps = []
        for raw_step in payload.get("steps", []):
            if not isinstance(raw_step, dict):
                continue
            raw = dict(raw_step)
            raw["gate_results"] = [
                GateResult(**gate) for gate in raw.get("gate_results", []) if isinstance(gate, dict)
            ]
            steps.append(TraceStep(**_known_fields(TraceStep, raw)))
        hook_events = [
            HookEvent(**_known_fields(HookEvent, event))
            for event in payload.get("hook_events", [])
            if isinstance(event, dict)
        ]
        route_candidates = [
            RouteCandidate(**candidate)
            for candidate in payload.get("route_candidates", [])
            if isinstance(candidate, dict)
        ]
        gate_results = [
            GateResult(**gate)
            for gate in payload.get("gate_results", [])
            if isinstance(gate, dict)
        ]
        return cls(
            run_id=str(payload["run_id"]),
            chain=str(payload["chain"]),
            task=str(payload["task"]),
            artifact=str(payload["artifact"]),
            status=str(payload["status"]),
            created_at=str(payload["created_at"]),
            stop_condition=str(payload["stop_condition"]),
            schema_version=int(payload.get("schema_version", 1)),
            steps=steps,
            hook_events=hook_events,
            skill_versions=dict(payload.get("skill_versions", {})),
            route_candidates=route_candidates,
            selected_route=str(payload.get("selected_route", payload.get("chain", ""))),
            gate_results=gate_results,
            outcome=dict(payload.get("outcome", {})),
            feedback_ids=list(payload.get("feedback_ids", [])),
            failure_tags=list(payload.get("failure_tags", [])),
            cost={str(key): float(value) for key, value in dict(payload.get("cost", {})).items()},
            completed_at=str(payload.get("completed_at", "")),
            metadata=dict(payload.get("metadata", {})),
        )

    @classmethod
    def read_json(cls, path: Path) -> WorkflowTrace:
        return cls.from_dict(json.loads(path.read_text(encoding="utf-8")))

    def append_hook_event(self, event: HookEvent) -> None:
        self.hook_events.append(event)

    def finalize(self, status: str, outcome: dict[str, Any] | None = None) -> None:
        self.status = status
        self.completed_at = timestamp()
        if outcome:
            self.outcome.update(outcome)
        self.failure_tags = sorted(
            {step.failure_tag for step in self.steps if step.failure_tag} | set(self.failure_tags)
        )
        totals: dict[str, float] = {}
        for step in self.steps:
            for key, value in step.metrics.items():
                totals[key] = totals.get(key, 0.0) + float(value)
        self.cost.update(totals)

    def write_json(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")


def _known_fields(model: type, payload: dict[str, Any]) -> dict[str, Any]:
    names = model.__dataclass_fields__
    return {key: value for key, value in payload.items() if key in names}
