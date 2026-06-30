#!/usr/bin/env python3
"""CLI for the lightweight NeuroFlow runtime registry."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent
REPO_ROOT = SCRIPTS_ROOT.parent
if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_ROOT))

from neuroflow_runtime import WorkflowHookRuntime, WorkflowRunner, build_registry  # noqa: E402
from neuroflow_runtime.hooks import result_to_json  # noqa: E402


def print_registry(kind: str) -> None:
    registry = build_registry(REPO_ROOT)
    if kind in {"chains", "all"}:
        print("Workflow chains:")
        for name, chain in sorted(registry.chains().items()):
            print(f"- {name}: {' -> '.join(chain.stages)} [{chain.artifact}]")
    if kind in {"skills", "all"}:
        print("Skills:")
        for name, manifest in sorted(registry.skills().items()):
            print(f"- {name}: {manifest.status}, {manifest.verification_status}")


def run_chain(args: argparse.Namespace) -> None:
    registry = build_registry(REPO_ROOT)
    runner = WorkflowRunner(registry=registry, root=REPO_ROOT)
    output_root = Path(args.output_root).expanduser().resolve() if args.output_root else None
    result = runner.run(
        chain_name=args.chain,
        task=args.task,
        output_root=output_root,
        dry_run=args.dry_run,
    )
    payload = {
        "run_id": result.trace.run_id,
        "chain": result.trace.chain,
        "status": result.trace.status,
        "run_dir": str(result.run_dir),
        "trace": str(result.trace_path),
        "artifact": str(result.artifact_path),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def run_hook(args: argparse.Namespace) -> None:
    registry = build_registry(REPO_ROOT)
    runtime = WorkflowHookRuntime(registry=registry, root=REPO_ROOT)
    artifact = Path(args.artifact).expanduser().resolve() if args.artifact else None
    result = runtime.run(
        event=args.event,
        task=args.task,
        artifact=artifact,
        kind=args.kind,
        run_id=args.run_id,
        tool=args.tool,
        summary=args.summary,
    )
    print(result_to_json(result))
    if result.status == "blocked":
        raise SystemExit(2)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="NeuroFlow runtime registry")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List registered skills or workflow chains")
    list_parser.add_argument("--kind", choices=("chains", "skills", "all"), default="all")

    run_parser = subparsers.add_parser("run", help="Create a traceable workflow run scaffold")
    run_parser.add_argument("--chain", required=True, help="Workflow chain name")
    run_parser.add_argument("--task", required=True, help="User task or run objective")
    run_parser.add_argument("--output-root", default="", help="Override output root; defaults to .private/runs")
    run_parser.add_argument("--dry-run", action="store_true", help="Mark trace as dry-run")

    hook_parser = subparsers.add_parser("hook", help="Run a lightweight NeuroFlow workflow hook")
    hook_parser.add_argument(
        "--event",
        required=True,
        choices=("session_start", "pre_artifact", "post_tool", "pre_commit", "session_end"),
    )
    hook_parser.add_argument("--task", default="", help="Natural-language task for session_start")
    hook_parser.add_argument("--artifact", default="", help="Artifact path for pre_artifact")
    hook_parser.add_argument("--kind", default="", help="Artifact kind: claim, memory, reference, or readme")
    hook_parser.add_argument("--run-id", default="", help="Existing runtime run id")
    hook_parser.add_argument("--tool", default="", help="Tool name for post_tool")
    hook_parser.add_argument("--summary", default="", help="Short tool result summary for post_tool")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "list":
        print_registry(args.kind)
    elif args.command == "run":
        run_chain(args)
    elif args.command == "hook":
        run_hook(args)
    else:
        parser.error(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()
