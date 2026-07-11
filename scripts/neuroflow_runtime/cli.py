#!/usr/bin/env python3
"""CLI for NeuroFlow workflows and the semi-automatic evolution control plane."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Annotated

import typer

SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent
REPO_ROOT = SCRIPTS_ROOT.parent
if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_ROOT))

from neuroflow_runtime.evals import EvalHarness, load_eval_cases, run_sync, write_eval_result  # noqa: E402
from neuroflow_runtime.evolution import EvolutionEngine, EvolutionError  # noqa: E402
from neuroflow_runtime.hooks import WorkflowHookRuntime  # noqa: E402
from neuroflow_runtime.kb import kb_summary, search_kb  # noqa: E402
from neuroflow_runtime.models import EvalPartition, FeedbackType  # noqa: E402
from neuroflow_runtime.promotion import PromotionController, PromotionError  # noqa: E402
from neuroflow_runtime.providers import ProviderError, load_provider  # noqa: E402
from neuroflow_runtime.registry import build_registry  # noqa: E402
from neuroflow_runtime.reporting import build_report  # noqa: E402
from neuroflow_runtime.runner import WorkflowRunner  # noqa: E402
from neuroflow_runtime.storage import EvolutionStore  # noqa: E402

app = typer.Typer(no_args_is_help=True, help="NeuroFlow research workflow and evolution runtime")
kb_app = typer.Typer(no_args_is_help=True, help="Search public NeuroFlow knowledge maps")
eval_app = typer.Typer(no_args_is_help=True, help="Run executable skill and workflow evaluations")
evolve_app = typer.Typer(no_args_is_help=True, help="Manage semi-automatic workflow and skill evolution")
report_app = typer.Typer(no_args_is_help=True, help="Generate static operational reports")
app.add_typer(kb_app, name="kb")
app.add_typer(eval_app, name="eval")
app.add_typer(evolve_app, name="evolve")
app.add_typer(report_app, name="report")


def emit(payload: object) -> None:
    typer.echo(json.dumps(payload, ensure_ascii=False, indent=2))


def fail(exc: Exception) -> None:
    typer.echo(json.dumps({"error": str(exc)}, ensure_ascii=False, indent=2), err=True)
    raise typer.Exit(2)


@app.command("list")
def list_registry(
    kind: Annotated[str, typer.Option("--kind", help="chains, skills, or all")] = "all",
) -> None:
    if kind not in {"chains", "skills", "all"}:
        raise typer.BadParameter("kind must be chains, skills, or all")
    registry = build_registry(REPO_ROOT)
    if kind in {"chains", "all"}:
        typer.echo("Workflow chains:")
        for name, chain in sorted(registry.chains().items()):
            typer.echo(f"- {name}: {' -> '.join(chain.stage_names)} [{chain.artifact}]")
    if kind in {"skills", "all"}:
        typer.echo("Skills:")
        for name, manifest in sorted(registry.skills().items()):
            typer.echo(f"- {name}: {manifest.status}, {manifest.verification_status}")


@app.command("run")
def run_chain(
    chain: Annotated[str, typer.Option("--chain", help="Workflow chain name")],
    task: Annotated[str, typer.Option("--task", help="User task or run objective")],
    output_root: Annotated[str, typer.Option("--output-root")] = "",
    dry_run: Annotated[bool, typer.Option("--dry-run")] = False,
    execute: Annotated[bool, typer.Option("--execute", help="Execute stages through the configured provider")] = False,
    provider: Annotated[str, typer.Option("--provider", help="Override executor provider")] = "",
) -> None:
    try:
        registry = build_registry(REPO_ROOT)
        runner = WorkflowRunner(registry=registry, root=REPO_ROOT)
        target_root = Path(output_root).expanduser().resolve() if output_root else None
        executor = load_provider("executor", provider) if execute else None
        result = runner.run(
            chain_name=chain,
            task=task,
            output_root=target_root,
            dry_run=dry_run,
            execute=execute,
            provider=executor,
        )
        emit(
            {
                "run_id": result.trace.run_id,
                "chain": result.trace.chain,
                "status": result.trace.status,
                "run_dir": str(result.run_dir),
                "trace": str(result.trace_path),
                "artifact": str(result.artifact_path),
            }
        )
    except (KeyError, ProviderError, RuntimeError, ValueError) as exc:
        fail(exc)
    if execute and result.trace.status == "failed":
        raise typer.Exit(1)


@app.command("hook")
def run_hook(
    event: Annotated[str, typer.Option("--event")],
    task: Annotated[str, typer.Option("--task")] = "",
    artifact: Annotated[str, typer.Option("--artifact")] = "",
    kind: Annotated[str, typer.Option("--kind")] = "",
    run_id: Annotated[str, typer.Option("--run-id")] = "",
    tool: Annotated[str, typer.Option("--tool")] = "",
    summary: Annotated[str, typer.Option("--summary")] = "",
) -> None:
    registry = build_registry(REPO_ROOT)
    runtime = WorkflowHookRuntime(registry=registry, root=REPO_ROOT)
    artifact_path = Path(artifact).expanduser().resolve() if artifact else None
    result = runtime.run(
        event=event,
        task=task,
        artifact=artifact_path,
        kind=kind,
        run_id=run_id,
        tool=tool,
        summary=summary,
    )
    emit(result.to_dict())
    if result.status == "blocked":
        raise typer.Exit(2)


@app.command("import-result")
def import_result(
    run_id: Annotated[str, typer.Option("--run-id")],
    step: Annotated[int, typer.Option("--step", min=1)],
    artifact: Annotated[str, typer.Option("--artifact")],
    status: Annotated[str, typer.Option("--status")] = "passed",
    failure_tag: Annotated[str, typer.Option("--failure-tag")] = "",
    error: Annotated[str, typer.Option("--error")] = "",
    metric: Annotated[list[str] | None, typer.Option("--metric", help="Numeric key=value; repeatable")] = None,
) -> None:
    try:
        trace_path = REPO_ROOT / ".private" / "runs" / run_id / "trace.json"
        runner = WorkflowRunner(build_registry(REPO_ROOT), REPO_ROOT)
        trace = runner.import_step_result(
            trace_path,
            step_index=step,
            artifact=Path(artifact).expanduser().resolve(),
            status=status,
            failure_tag=failure_tag,
            error=error,
            metrics=_metrics(metric or []),
        )
        emit({"run_id": trace.run_id, "status": trace.status, "step": step, "trace": str(trace_path)})
    except (ValueError, OSError, KeyError) as exc:
        fail(exc)


@kb_app.command("search")
def kb_search(
    query: str,
    limit: Annotated[int, typer.Option("--limit")] = 8,
    as_json: Annotated[bool, typer.Option("--json")] = False,
) -> None:
    hits = search_kb(REPO_ROOT, query, limit=limit)
    payload = [
        {
            "score": hit.score,
            "path": str(hit.path),
            "line": hit.line,
            "heading": hit.heading,
            "snippet": hit.snippet,
        }
        for hit in hits
    ]
    if as_json:
        emit(payload)
        return
    if not hits:
        typer.echo("No knowledge-base hits found.")
        return
    for hit in hits:
        heading = f" [{hit.heading}]" if hit.heading else ""
        typer.echo(f"{hit.path}:{hit.line}{heading} score={hit.score}\n  {hit.snippet}")


@kb_app.command("summary")
def kb_show_summary() -> None:
    emit(kb_summary(REPO_ROOT))


@eval_app.command("list")
def eval_list(
    partition: Annotated[str, typer.Option("--partition")] = "",
    include_hidden: Annotated[bool, typer.Option("--include-hidden")] = False,
) -> None:
    partitions = _partitions(partition)
    cases = load_eval_cases(REPO_ROOT, partitions=partitions, include_hidden=include_hidden)
    emit(
        [
            {
                "id": case.id,
                "skill": case.skill_name,
                "partition": case.partition.value,
                "assertions": len(case.assertions),
                "repeats": case.repeats,
            }
            for case in cases
        ]
    )


@eval_app.command("run")
def eval_run(
    partition: Annotated[str, typer.Option("--partition")] = "",
    candidate: Annotated[str, typer.Option("--candidate")] = "",
    executor_provider: Annotated[str, typer.Option("--executor-provider")] = "",
    reviewer_provider: Annotated[str, typer.Option("--reviewer-provider")] = "",
    include_hidden: Annotated[bool | None, typer.Option("--include-hidden/--exclude-hidden")] = None,
) -> None:
    try:
        executor = load_provider("executor", executor_provider)
        reviewer = load_provider("reviewer", reviewer_provider)
        if candidate:
            engine = EvolutionEngine(REPO_ROOT)
            emit(
                engine.evaluate_candidate(
                    candidate,
                    executor,
                    reviewer,
                    include_hidden=True if include_hidden is None else include_hidden,
                )
            )
            return
        resolved_include_hidden = bool(include_hidden)
        cases = load_eval_cases(
            REPO_ROOT,
            partitions=_partitions(partition),
            include_hidden=resolved_include_hidden,
        )
        harness = EvalHarness(REPO_ROOT, executor, reviewer)
        summary = run_sync(harness.run(cases, partition_label=partition or "all"))
        path = write_eval_result(REPO_ROOT, summary)
        store = EvolutionStore(REPO_ROOT)
        store.initialize()
        store.add_eval_run(summary, path)
        emit(
            {
                "id": summary.id,
                "score": summary.score,
                "critical_pass": summary.critical_pass,
                "dimension_scores": summary.dimension_scores,
                "case_statistics": summary.case_statistics,
                "cases": len(summary.case_statistics),
                "repeated_results": len(summary.results),
                "result": str(path),
                "cost": summary.cost,
            }
        )
        if not summary.critical_pass:
            raise typer.Exit(1)
    except (EvolutionError, ProviderError, ValueError, KeyError) as exc:
        fail(exc)


@evolve_app.command("init")
def evolve_init() -> None:
    store = EvolutionStore(REPO_ROOT)
    store.initialize()
    emit({"database_url": store.safe_database_url, "status": "initialized"})


@evolve_app.command("ingest")
def evolve_ingest(
    run_id: Annotated[str, typer.Option("--run-id")] = "",
    trace: Annotated[str, typer.Option("--trace")] = "",
    summary: Annotated[str, typer.Option("--summary")] = "",
    event_type: Annotated[str, typer.Option("--event-type")] = "",
    failure_tag: Annotated[str, typer.Option("--failure-tag")] = "",
) -> None:
    try:
        trace_path = (
            Path(trace).expanduser().resolve()
            if trace
            else REPO_ROOT / ".private" / "runs" / run_id / "trace.json"
        )
        if not trace_path.exists():
            raise ValueError(f"Trace does not exist: {trace_path}")
        kind = FeedbackType(event_type) if event_type else None
        engine = EvolutionEngine(REPO_ROOT)
        events = engine.ingest_trace(
            trace_path,
            summary=summary,
            event_type=kind,
            failure_tag=failure_tag,
            source="cli",
        )
        emit([event.model_dump(mode="json") for event in events])
    except (ValueError, KeyError) as exc:
        fail(exc)


@evolve_app.command("propose")
def evolve_propose(
    feedback_id: Annotated[list[str] | None, typer.Option("--feedback-id")] = None,
    variants: Annotated[int, typer.Option("--variants", min=1, max=5)] = 2,
    provider: Annotated[str, typer.Option("--provider")] = "",
    patch: Annotated[
        str,
        typer.Option("--patch", help="Import a prepared unified diff instead of calling a model"),
    ] = "",
    target: Annotated[str, typer.Option("--target")] = "",
) -> None:
    try:
        engine = EvolutionEngine(REPO_ROOT)
        if patch:
            patch_text = Path(patch).read_text(encoding="utf-8")
            candidate = engine.create_candidate_from_patch(
                patch_text,
                target_component=target,
                feedback_ids=feedback_id or [],
            )
            emit(candidate.model_dump(mode="json"))
            return
        executor = load_provider("executor", provider)
        candidates = run_sync(engine.propose(executor, feedback_ids=feedback_id or [], variants=variants))
        emit([candidate.model_dump(mode="json") for candidate in candidates])
    except (EvolutionError, ProviderError, ValueError, OSError) as exc:
        fail(exc)


@evolve_app.command("list")
def evolve_list() -> None:
    store = EvolutionStore(REPO_ROOT)
    store.initialize()
    emit([candidate.model_dump(mode="json") for candidate in store.list_candidates()])


@evolve_app.command("review")
def evolve_review(
    candidate: str,
    approve: Annotated[bool, typer.Option("--approve/--reject")] = True,
    actor: Annotated[str, typer.Option("--actor")] = "human",
    reason: Annotated[str, typer.Option("--reason")] = "Human review completed.",
) -> None:
    try:
        controller = PromotionController(REPO_ROOT)
        decision = controller.review(candidate, approve=approve, actor=actor, reason=reason)
        emit(decision.model_dump(mode="json"))
    except (PromotionError, KeyError, ValueError) as exc:
        fail(exc)


@evolve_app.command("reject")
def evolve_reject(
    candidate: str,
    actor: Annotated[str, typer.Option("--actor")] = "human",
    reason: Annotated[str, typer.Option("--reason")] = "Candidate rejected by operator.",
) -> None:
    try:
        controller = PromotionController(REPO_ROOT)
        decision = controller.review(candidate, approve=False, actor=actor, reason=reason)
        emit(decision.model_dump(mode="json"))
    except (PromotionError, KeyError, ValueError) as exc:
        fail(exc)


@evolve_app.command("promote")
def evolve_promote(
    candidate: str,
    automatic: Annotated[bool, typer.Option("--auto")] = False,
    actor: Annotated[str, typer.Option("--actor")] = "human",
    executor_provider: Annotated[str, typer.Option("--executor-provider")] = "",
    reviewer_provider: Annotated[str, typer.Option("--reviewer-provider")] = "",
) -> None:
    try:
        executor = load_provider("executor", executor_provider) if automatic else None
        reviewer = load_provider("reviewer", reviewer_provider) if automatic else None
        controller = PromotionController(REPO_ROOT)
        emit(
            controller.promote(
                candidate,
                actor=actor,
                automatic=automatic,
                executor=executor,
                reviewer=reviewer,
            )
        )
    except (PromotionError, ProviderError, KeyError, ValueError) as exc:
        fail(exc)


@evolve_app.command("rollback")
def evolve_rollback(
    candidate: str,
    actor: Annotated[str, typer.Option("--actor")] = "human",
    reason: Annotated[str, typer.Option("--reason")] = "Operator requested rollback.",
) -> None:
    try:
        controller = PromotionController(REPO_ROOT)
        emit(controller.rollback(candidate, actor=actor, reason=reason))
    except (PromotionError, KeyError, ValueError) as exc:
        fail(exc)


@report_app.command("evolution")
def report_evolution(
    output_dir: Annotated[str, typer.Option("--output-dir")] = "",
) -> None:
    store = EvolutionStore(REPO_ROOT)
    store.initialize()
    destination = Path(output_dir).expanduser().resolve() if output_dir else None
    emit(build_report(REPO_ROOT, store, destination))


def _partitions(value: str) -> set[EvalPartition] | None:
    if not value:
        return None
    try:
        return {EvalPartition(item.strip()) for item in value.split(",") if item.strip()}
    except ValueError as exc:
        raise typer.BadParameter(f"Unknown eval partition in {value!r}") from exc


def _metrics(values: list[str]) -> dict[str, float]:
    metrics: dict[str, float] = {}
    for value in values:
        if "=" not in value:
            raise typer.BadParameter(f"Metric must be key=value, got {value!r}")
        key, raw = value.split("=", 1)
        metrics[key.strip()] = float(raw)
    return metrics


def main() -> None:
    app()


if __name__ == "__main__":
    main()
