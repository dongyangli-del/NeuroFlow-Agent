"""Executable lightweight NeuroFlow runner."""

from __future__ import annotations

import asyncio
import hashlib
import shutil
from dataclasses import dataclass
from pathlib import Path

from .privacy import sanitize_remote_text
from .providers import ModelProvider, ModelRequest
from .registry import RuntimeRegistry
from .trace import GateResult, RouteCandidate, TraceStep, WorkflowTrace


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
        execute: bool = False,
        provider: ModelProvider | None = None,
    ) -> RunResult:
        if dry_run and execute:
            raise ValueError("--dry-run and --execute cannot be used together")
        if execute and provider is None:
            raise ValueError("Executing a workflow requires a model provider")
        chain = self.registry.get_chain(chain_name)
        trace = WorkflowTrace.create(
            chain=chain.name,
            task=task,
            artifact=chain.artifact,
            stop_condition=chain.stop_condition,
        )

        trace.skill_versions = {
            name: manifest.version for name, manifest in self.registry.skills().items() if manifest.version
        }
        trace.route_candidates = [RouteCandidate(chain=chain.name, score=1.0, reasons=["explicit-chain"])]
        for index, stage in enumerate(chain.stages, start=1):
            manifest = self.registry.skills().get(stage.module)
            trace.steps.append(
                TraceStep(
                    index=index,
                    name=stage.name,
                    module=stage.module,
                    required_reads=list(manifest.always_load if manifest else ()),
                    evidence_gates=list(stage.evidence_gates or chain.evidence_gates),
                    output=stage.output,
                )
            )

        output_root = output_root or self.root / ".private" / "runs"
        run_dir = output_root / trace.run_id
        artifact_path = run_dir / "artifacts" / chain.artifact
        trace_path = run_dir / "trace.json"
        run_dir.mkdir(parents=True, exist_ok=True)
        if dry_run:
            trace.status = "dry-run"
            self._write_artifact_stub(artifact_path, trace)
            trace.write_json(trace_path)
        elif execute:
            asyncio.run(self._execute(trace, artifact_path, trace_path, provider))
        else:
            self._write_artifact_stub(artifact_path, trace)
            trace.write_json(trace_path)

        return RunResult(run_dir=run_dir, trace_path=trace_path, artifact_path=artifact_path, trace=trace)

    def import_step_result(
        self,
        trace_path: Path,
        *,
        step_index: int,
        artifact: Path,
        status: str,
        failure_tag: str = "",
        error: str = "",
        metrics: dict[str, float] | None = None,
    ) -> WorkflowTrace:
        if status not in {"passed", "failed", "blocked", "skipped"}:
            raise ValueError("Imported result status must be passed, failed, blocked, or skipped")
        if not artifact.exists() or not artifact.is_file():
            raise ValueError(f"Imported stage artifact does not exist: {artifact}")
        trace = WorkflowTrace.read_json(trace_path)
        try:
            step = next(item for item in trace.steps if item.index == step_index)
        except StopIteration as exc:
            raise ValueError(f"Trace has no stage with index {step_index}") from exc
        text = artifact.read_text(encoding="utf-8", errors="ignore")
        output_dir = trace_path.parent / "stage_outputs"
        output_dir.mkdir(parents=True, exist_ok=True)
        stored = output_dir / f"{step.index:02d}-{_slug(step.name)}-external.md"
        shutil.copy2(artifact, stored)
        if not step.started_at:
            step.start()
        step.gate_results = [self._check_gate(gate, text) for gate in step.evidence_gates]
        failed_gates = [gate.gate for gate in step.gate_results if gate.status == "failed"]
        resolved_status = "failed" if status == "passed" and failed_gates else status
        step.finish(
            resolved_status,
            output_refs=[str(stored)],
            output_text=text,
            failure_tag=failure_tag or (f"gate:{failed_gates[0]}" if failed_gates else ""),
            error=error or (f"Failed evidence gates: {', '.join(failed_gates)}" if failed_gates else ""),
            metrics=metrics,
        )
        trace.status = "running"
        terminal = {"passed", "failed", "blocked", "skipped"}
        if all(item.status in terminal for item in trace.steps):
            successful = all(item.status in {"passed", "skipped"} for item in trace.steps)
            trace.finalize("passed" if successful else "failed")
        trace.write_json(trace_path)
        self._rebuild_artifact(trace_path, trace)
        return trace

    async def _execute(
        self,
        trace: WorkflowTrace,
        artifact_path: Path,
        trace_path: Path,
        provider: ModelProvider,
    ) -> None:
        sections = [
            f"# {trace.artifact.removesuffix('.md').replace('_', ' ').title()}",
            "",
            f"Run ID: {trace.run_id}",
            f"Workflow chain: {trace.chain}",
            f"Task: {trace.task}",
            "",
        ]
        previous_outputs: list[str] = []
        trace.status = "running"
        trace.write_json(trace_path)
        for step in trace.steps:
            step.start()
            step.input_refs = list(step.required_reads)
            trace.write_json(trace_path)
            prompt = self._stage_prompt(trace, step, previous_outputs)
            try:
                response = await provider.generate(
                    ModelRequest(
                        prompt=prompt,
                        system=(
                            "Execute exactly one NeuroFlow workflow stage. Ground claims in inspected references, "
                            "mark unresolved evidence, and return only the stage artifact."
                        ),
                        temperature=0.0,
                        max_tokens=6000,
                    )
                )
                output_dir = trace_path.parent / "stage_outputs"
                output_dir.mkdir(parents=True, exist_ok=True)
                output_path = output_dir / f"{step.index:02d}-{_slug(step.name)}.md"
                output_path.write_text(response.text, encoding="utf-8")
                step.gate_results = [self._check_gate(gate, response.text) for gate in step.evidence_gates]
                failed_gates = [gate.gate for gate in step.gate_results if gate.status == "failed"]
                status = "failed" if failed_gates else "passed"
                step.finish(
                    status,
                    output_refs=[str(output_path)],
                    output_text=response.text,
                    failure_tag=f"gate:{failed_gates[0]}" if failed_gates else "",
                    error=f"Failed evidence gates: {', '.join(failed_gates)}" if failed_gates else "",
                    metrics={
                        "input_tokens": float(response.input_tokens),
                        "output_tokens": float(response.output_tokens),
                        "cost_usd": response.cost_usd,
                    },
                )
                sections.extend([f"## {step.index}. {step.name}", "", response.text, ""])
                previous_outputs.append(response.text)
                if failed_gates:
                    break
            except Exception as exc:
                step.finish("failed", failure_tag="provider:error", error=str(exc))
                break
            finally:
                trace.write_json(trace_path)
        artifact_path.parent.mkdir(parents=True, exist_ok=True)
        artifact_path.write_text("\n".join(sections), encoding="utf-8")
        artifact_digest = hashlib.sha256(artifact_path.read_bytes()).hexdigest()
        passed = all(step.status == "passed" for step in trace.steps)
        trace.finalize(
            "passed" if passed else "failed",
            {
                "artifact_path": str(artifact_path),
                "artifact_sha256": artifact_digest,
                "completed_steps": sum(step.status == "passed" for step in trace.steps),
                "total_steps": len(trace.steps),
            },
        )
        trace.write_json(trace_path)

    def _stage_prompt(self, trace: WorkflowTrace, step: TraceStep, previous_outputs: list[str]) -> str:
        references = []
        manifest = self.registry.skills().get(step.module)
        skill_dir = manifest.path.parent if manifest else self.root
        for relative in step.required_reads:
            path = (skill_dir / relative).resolve()
            try:
                path.relative_to(self.root.resolve())
            except ValueError:
                continue
            if path.exists() and path.is_file():
                references.append(f"--- {path.relative_to(self.root)} ---\n{path.read_text(encoding='utf-8')[:20000]}")
        upstream = "\n\n".join(previous_outputs[-2:])
        return sanitize_remote_text(
            f"Original task:\n{trace.task}\n\nWorkflow stage: {step.name}\nOwner module: {step.module}\n"
            f"Required output: {step.output}\nEvidence gates: {', '.join(step.evidence_gates)}\n\n"
            f"Upstream artifacts:\n{upstream or 'none'}\n\nReferences:\n" + "\n\n".join(references)
        )

    def _check_gate(self, gate: str, output: str) -> GateResult:
        lower = output.lower()
        requirements = {
            "novelty": ("citation", "source", "arxiv", "doi", "uncertain", "prior work"),
            "benchmark": ("access", "license", "split", "metric", "baseline", "leakage"),
            "experiment": ("baseline", "metric", "ablation", "control", "statistic", "stop"),
            "reproduction": ("environment", "data", "weight", "command", "expected output", "sanity"),
            "closed loop": ("online", "offline", "safety", "calibration", "latency"),
            "memory": ("privacy", "target", "eval", "no-repo", "verification"),
        }
        tokens = requirements.get(gate, ())
        matches = [token for token in tokens if token in lower]
        minimum = max(1, len(tokens) // 2) if tokens else 0
        status = "passed" if len(matches) >= minimum else "failed"
        return GateResult(
            gate=gate,
            status=status,
            message=f"Matched {len(matches)}/{len(tokens)} required evidence markers: {', '.join(matches) or 'none'}",
        )

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
                "This file is a runtime scaffold. Fill it with inspected evidence before treating it as a "
                "research result.",
                "",
            ]
        )
        path.write_text("\n".join(lines), encoding="utf-8")

    def _rebuild_artifact(self, trace_path: Path, trace: WorkflowTrace) -> None:
        artifact_path = trace_path.parent / "artifacts" / trace.artifact
        lines = [
            f"# {trace.artifact.removesuffix('.md').replace('_', ' ').title()}",
            "",
            f"Run ID: {trace.run_id}",
            f"Workflow chain: {trace.chain}",
            f"Task: {trace.task}",
            "",
        ]
        for step in trace.steps:
            if not step.output_refs:
                continue
            output_path = Path(step.output_refs[-1])
            if output_path.exists():
                lines.extend([f"## {step.index}. {step.name}", "", output_path.read_text(encoding="utf-8"), ""])
        artifact_path.parent.mkdir(parents=True, exist_ok=True)
        artifact_path.write_text("\n".join(lines), encoding="utf-8")
        trace.outcome["artifact_path"] = str(artifact_path)
        trace.outcome["artifact_sha256"] = hashlib.sha256(artifact_path.read_bytes()).hexdigest()
        trace.write_json(trace_path)


def _slug(value: str) -> str:
    return "-".join(part for part in value.lower().replace("/", " ").split() if part)
