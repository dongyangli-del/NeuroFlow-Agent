#!/usr/bin/env python3
"""Idempotently migrate NeuroFlow eval JSON files to executable schema v2."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def dimension(text: str) -> str:
    lower = text.lower()
    if any(token in lower for token in ("privacy", "leak", "safety", "unsupported", "invent", "private", "branch")):
        return "safety"
    if any(token in lower for token in ("cost", "token", "time", "efficient")):
        return "efficiency"
    if any(token in lower for token in ("general", "cross-domain", "novel", "new task")):
        return "generalization"
    if any(token in lower for token in ("preserve", "retain", "existing", "backward", "does not")):
        return "retention"
    return "adaptivity"


def migrate(path: Path) -> bool:
    payload = json.loads(path.read_text(encoding="utf-8"))
    changed = payload.get("schema_version") != 2
    payload["schema_version"] = 2
    skill = str(payload.get("skill_name", path.parent.parent.name))
    for case in payload.get("evals", []):
        if "partition" not in case:
            case["partition"] = "regression"
            changed = True
        if "tags" not in case:
            case["tags"] = [skill]
            changed = True
        if "repeats" not in case:
            case["repeats"] = 3
            changed = True
        assertions = []
        for assertion in case.get("assertions", []):
            if isinstance(assertion, str):
                assertion = {"text": assertion}
                changed = True
            item = dict(assertion)
            if "type" not in item:
                item["type"] = "llm_rubric"
                changed = True
            inferred = dimension(str(item.get("text", "")))
            if "dimension" not in item:
                item["dimension"] = inferred
                changed = True
            if "critical" not in item:
                item["critical"] = inferred == "safety"
                changed = True
            if "weight" not in item:
                item["weight"] = 1.0
                changed = True
            assertions.append(item)
        case["assertions"] = assertions
    if changed:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail when a migration would change a file")
    args = parser.parse_args()
    changed = []
    for path in sorted(ROOT.glob("skills*/**/evals/evals.json")):
        original = path.read_text(encoding="utf-8")
        if args.check:
            payload = json.loads(original)
            if payload.get("schema_version") != 2 or any(
                not {"partition", "tags", "repeats"}.issubset(case)
                or any(
                    not {"type", "dimension", "critical", "weight"}.issubset(assertion)
                    for assertion in case.get("assertions", [])
                )
                for case in payload.get("evals", [])
            ):
                changed.append(path)
        elif migrate(path):
            changed.append(path)
    if args.check and changed:
        paths = ", ".join(str(path.relative_to(ROOT)) for path in changed)
        raise SystemExit(f"Eval schema migration required: {paths}")
    print(f"Eval schema v2 ready; changed={len(changed)}")


if __name__ == "__main__":
    main()
