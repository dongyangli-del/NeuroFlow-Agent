#!/usr/bin/env python3
"""Validate the AI x BCI skill repository."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
SKILL_DIR = SKILLS_DIR / "ai-bci-research"
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
SENSITIVE_PATTERNS = [
    (re.compile("/" + r"vePFS-[^\s)>\"]+"), "local vePFS path"),
    (re.compile("/" + r"home/ldy(?:/|\\b)"), "local home path"),
    (re.compile("/" + r"Users/[^/\s)>\"]+"), "local macOS user path"),
    (re.compile(r"AKIA[0-9A-Z]{16}"), "AWS access key pattern"),
    (re.compile(r"AIza[0-9A-Za-z_-]{35}"), "Google API key pattern"),
    (re.compile(r"gh[pousr]_[0-9A-Za-z_]{20,}"), "GitHub token pattern"),
    (re.compile(r"sk-[A-Za-z0-9]{20,}"), "OpenAI-style API key pattern"),
    (re.compile(r"BEGIN (RSA|OPENSSH|EC|DSA) PRIVATE KEY"), "private key block"),
]
SKIP_DIRS = {".git", "__pycache__", ".private"}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_required_files() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.exists()]
    if missing:
        fail("Missing required files: " + ", ".join(missing))


def validate_skill_frontmatter() -> None:
    for skill_md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        text = skill_md.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            fail(f"{skill_md.relative_to(ROOT)} must start with YAML frontmatter")
        try:
            frontmatter = text.split("---\n", 2)[1]
        except IndexError:
            fail(f"{skill_md.relative_to(ROOT)} frontmatter is not closed")
        for key in ("name:", "description:"):
            if key not in frontmatter:
                fail(f"{skill_md.relative_to(ROOT)} frontmatter missing {key}")


def validate_json() -> None:
    for evals_json in sorted(SKILLS_DIR.glob("*/evals/evals.json")):
        with open(evals_json, encoding="utf-8") as f:
            json.load(f)


def validate_skill_structure() -> None:
    missing = []
    for skill_dir in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
        for rel in ("SKILL.md", "agents/openai.yaml", "evals/evals.json"):
            if not (skill_dir / rel).exists():
                missing.append(str((skill_dir / rel).relative_to(ROOT)))
    if missing:
        fail("Missing skill structure files: " + ", ".join(missing))


def iter_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not (SKIP_DIRS & set(path.parts))
    )


def iter_public_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and not (SKIP_DIRS & set(path.parts))
        and path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".pyc"}
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
        if not path.is_file() or (SKIP_DIRS & set(path.parts)):
            continue
        if path.stat().st_size > limit:
            offenders.append(f"{path.relative_to(ROOT)} ({path.stat().st_size} bytes)")
    if offenders:
        fail("Large files should not live in this skill repo: " + ", ".join(offenders))


def validate_public_leakage() -> None:
    offenders = []
    for path in iter_public_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern, label in SENSITIVE_PATTERNS:
            if pattern.search(text):
                offenders.append(f"{path.relative_to(ROOT)} ({label})")
                break
    if offenders:
        fail("Potential private or secret material in public files: " + ", ".join(offenders))


def validate_high_precision_maps() -> None:
    script = ROOT / "skills" / "paper-rag-plus" / "scripts" / "validate_high_precision_maps.py"
    if script.exists():
        subprocess.run([sys.executable, str(script)], cwd=ROOT, check=True)


def main() -> None:
    validate_required_files()
    validate_skill_structure()
    validate_skill_frontmatter()
    validate_json()
    validate_local_links()
    validate_no_large_files()
    validate_public_leakage()
    validate_high_precision_maps()
    print("Skill repository validation passed.")


if __name__ == "__main__":
    main()
