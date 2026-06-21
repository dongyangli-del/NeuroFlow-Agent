"""Executable lightweight NeuroFlow runner."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .registry import RuntimeRegistry
from .trace import TraceStep, WorkflowTrace


@dataclass(frozen=True)
class RunResult:
    run_dir: Path
    trace_path: Path
    artifact_path: Path
    trace: WorkflowTrace


class WorkflowRunner:
    def __init__(self, registry: RuntimeRegistry, root: Path) -> None:
        self.registry = registry
        self.root = root

    def run(
        self,
        chain_name: str,
        task: str,
        output_root: Path | None = None,
        dry_run: bool = False,
    ) -> RunResult:
        chain = self.registry.get_chain(chain_name)
        trace = WorkflowTrace.create(
            chain=chain.name,
            task=task,
            artifact=chain.artifact,
            stop_condition=chain.stop_condition,
        )

        for index, stage in enumerate(chain.stages, start=1):
            module = chain.modules[min(index - 1, len(chain.modules) - 1)]
            manifest = self.registry.skills().get(module)
            trace.steps.append(
                TraceStep(
                    index=index,
                    name=stage,
                    module=module,
                    required_reads=list(manifest.always_load if manifest else ()),
                    evidence_gates=list(chain.evidence_gates),
                    output=f"Plan or fill the {stage} section in {chain.artifact}.",
                )
            )

        if dry_run:
            trace.status = "dry-run"
        output_root = output_root or self.root / ".private" / "runs"
        run_dir = output_root / trace.run_id
        artifact_path = run_dir / "artifacts" / chain.artifact
        trace_path = run_dir / "trace.json"

        if not dry_run:
            self._write_artifact_stub(artifact_path, trace)
            trace.write_json(trace_path)
        else:
            # Dry runs still return the deterministic paths that would be used.
            run_dir.mkdir(parents=True, exist_ok=True)
            self._write_artifact_stub(artifact_path, trace)
            trace.write_json(trace_path)

        return RunResult(run_dir=run_dir, trace_path=trace_path, artifact_path=artifact_path, trace=trace)

    def _write_artifact_stub(self, path: Path, trace: WorkflowTrace) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            f"# {trace.artifact.removesuffix('.md').replace('_', ' ').title()}",
            "",
            f"Run ID: {trace.run_id}",
            f"Workflow chain: {trace.chain}",
            f"Task: {trace.task}",
            f"Status: {trace.status}",
            "",
            "## Work Order",
            "",
        ]
        for step in trace.steps:
            reads = ", ".join(step.required_reads) if step.required_reads else "none"
            gates = ", ".join(step.evidence_gates) if step.evidence_gates else "none"
            lines.extend(
                [
                    f"### {step.index}. {step.name}",
                    "",
                    f"- Module: `{step.module}`",
                    f"- Required reads: {reads}",
                    f"- Evidence gates: {gates}",
                    f"- Output: {step.output}",
                    "",
                ]
            )
        lines.extend(
            [
                "## Stop Condition",
                "",
                trace.stop_condition,
                "",
                "## Notes",
                "",
                "This file is a runtime scaffold. Fill it with inspected evidence before treating it as a research result.",
                "",
            ]
        )
        path.write_text("\n".join(lines), encoding="utf-8")
