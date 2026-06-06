#!/usr/bin/env python3
"""Build a compact markdown index for this skill's reference files."""

from __future__ import annotations

import argparse
from pathlib import Path


def headings(path: Path) -> list[str]:
    result: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            result.append(line.strip())
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Skill root directory")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    references = root / "references"
    output = references / "knowledge-index.md"

    lines = ["# Knowledge Index", ""]
    for path in sorted(references.rglob("*.md")):
        if path.name == output.name:
            continue
        if "private" in path.relative_to(references).parts:
            continue
        rel = path.relative_to(root)
        lines.append(f"## {rel}")
        file_headings = headings(path)
        if file_headings:
            lines.extend(f"- {heading}" for heading in file_headings[:20])
        else:
            lines.append("- No markdown headings found.")
        lines.append("")

    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
