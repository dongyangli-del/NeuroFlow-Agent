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
class WorkflowTrace:
    run_id: str
    chain: str
    task: str
    artifact: str
    status: str
    created_at: str
    stop_condition: str
    steps: list[TraceStep] = field(default_factory=list)
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

    def write_json(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
