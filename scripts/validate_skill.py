#!/usr/bin/env python3
"""Validate the AI x BCI skill repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "ai-bci-research"
REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "README_CN.md",
    ROOT / "CONTRIBUTING.md",
    SKILL_DIR / "SKILL.md",
    SKILL_DIR / "agents" / "openai.yaml",
    SKILL_DIR / "evals" / "evals.json",
    SKILL_DIR / "references" / "knowledge-index.md",
    SKILL_DIR / "scripts" / "update_knowledge_index.py",
]

LINK_RE = re.compile(r"(?<!!)[\[]([^\]]+)[\]]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_required_files() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.exists()]
    if missing:
        fail("Missing required files: " + ", ".join(missing))


def validate_skill_frontmatter() -> None:
    text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    try:
        frontmatter = text.split("---\n", 2)[1]
    except IndexError:
        fail("SKILL.md frontmatter is not closed")
    for key in ("name:", "description:"):
        if key not in frontmatter:
            fail(f"SKILL.md frontmatter missing {key}")


def validate_json() -> None:
    with open(SKILL_DIR / "evals" / "evals.json", encoding="utf-8") as f:
        json.load(f)


def iter_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts and "__pycache__" not in path.parts
    )


def validate_local_links() -> None:
    for md in iter_markdown_files():
        text = md.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(2).strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if target.startswith("/"):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            resolved = (md.parent / path_part).resolve()
            if not resolved.exists():
                fail(f"Broken link in {md.relative_to(ROOT)}: {target}")


def validate_no_large_files() -> None:
    limit = 2 * 1024 * 1024
    offenders = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.stat().st_size > limit:
            offenders.append(f"{path.relative_to(ROOT)} ({path.stat().st_size} bytes)")
    if offenders:
        fail("Large files should not live in this skill repo: " + ", ".join(offenders))


def main() -> None:
    validate_required_files()
    validate_skill_frontmatter()
    validate_json()
    validate_local_links()
    validate_no_large_files()
    print("Skill repository validation passed.")


if __name__ == "__main__":
    main()
