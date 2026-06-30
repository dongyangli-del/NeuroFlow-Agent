"""Trace schema for lightweight NeuroFlow runs."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4


@dataclass
class TraceStep:
    index: int
    name: str
    module: str
    required_reads: list[str] = field(default_factory=list)
    evidence_gates: list[str] = field(default_factory=list)
    output: str = ""
    status: str = "planned"


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
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass
class WorkflowTrace:
    run_id: str
    chain: str
    task: str
    artifact: str
    status: str
    created_at: str
    stop_condition: str
    steps: list[TraceStep] = field(default_factory=list)
    hook_events: list[HookEvent] = field(default_factory=list)
    metadata: dict[str, str] = field(default_factory=dict)

    @classmethod
    def create(cls, chain: str, task: str, artifact: str, stop_condition: str) -> "WorkflowTrace":
        timestamp = datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        return cls(
            run_id=f"nf_{datetime.now(UTC).strftime('%Y%m%d_%H%M%S')}_{uuid4().hex[:8]}",
            chain=chain,
            task=task,
            artifact=artifact,
            status="planned",
            created_at=timestamp,
            stop_condition=stop_condition,
        )

    def to_dict(self) -> dict[str, object]:
        return asdict(self)

    @classmethod
    def from_dict(cls, payload: dict[str, object]) -> "WorkflowTrace":
        steps = [
            TraceStep(**step)
            for step in payload.get("steps", [])
            if isinstance(step, dict)
        ]
        hook_events = [
            HookEvent(**event)
            for event in payload.get("hook_events", [])
            if isinstance(event, dict)
        ]
        return cls(
            run_id=str(payload["run_id"]),
            chain=str(payload["chain"]),
            task=str(payload["task"]),
            artifact=str(payload["artifact"]),
            status=str(payload["status"]),
            created_at=str(payload["created_at"]),
            stop_condition=str(payload["stop_condition"]),
            steps=steps,
            hook_events=hook_events,
            metadata=dict(payload.get("metadata", {})),
        )

    @classmethod
    def read_json(cls, path: Path) -> "WorkflowTrace":
        return cls.from_dict(json.loads(path.read_text(encoding="utf-8")))

    def append_hook_event(self, event: HookEvent) -> None:
        self.hook_events.append(event)

    def write_json(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
