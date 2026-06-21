#!/usr/bin/env python3
"""Validate the AI x BCI skill repository."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
CODEX_SKILLS_DIR = ROOT / "skills-codex"
SKILL_DIR = SKILLS_DIR / "ai-bci-research"
REQUIRED_FILES = [
    ROOT / "AGENTS.md",
    ROOT / "AGENT_GUIDE.md",
    ROOT / "README.md",
    ROOT / "README_CN.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "LICENSE",
    ROOT / "SECURITY.md",
    ROOT / "docs" / "DEMO_GALLERY.md",
    ROOT / "docs" / "TROUBLESHOOTING.md",
    ROOT / ".github" / "workflows" / "validate.yml",
    ROOT / "skills-codex" / "neuro-orchestrator" / "SKILL.md",
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
    skill_files = list(SKILLS_DIR.glob("*/SKILL.md")) + list(CODEX_SKILLS_DIR.glob("*/SKILL.md"))
    for skill_md in sorted(skill_files):
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
    eval_files = list(SKILLS_DIR.glob("*/evals/evals.json")) + list(CODEX_SKILLS_DIR.glob("*/evals/evals.json"))
    for evals_json in sorted(eval_files):
        with open(evals_json, encoding="utf-8") as f:
            json.load(f)


def validate_manifests() -> None:
    manifest_files = list(SKILLS_DIR.glob("*/manifest.yaml")) + list(CODEX_SKILLS_DIR.glob("*/manifest.yaml"))
    required_fields = ("name:", "version:", "status:", "verification_status:", "purpose:", "natural_triggers:")
    allowed_verification_statuses = {
        "unverified",
        "source-traced",
        "reproduced",
        "user-validated",
        "expert-reviewed",
    }
    for manifest in sorted(manifest_files):
        text = manifest.read_text(encoding="utf-8")
        for field in required_fields:
            if field not in text:
                fail(f"{manifest.relative_to(ROOT)} missing {field}")
        match = re.search(r"^verification_status:\s*([A-Za-z0-9_-]+)\s*$", text, re.MULTILINE)
        if not match:
            fail(f"{manifest.relative_to(ROOT)} has malformed verification_status")
        if match.group(1) not in allowed_verification_statuses:
            fail(
                f"{manifest.relative_to(ROOT)} has invalid verification_status "
                f"{match.group(1)!r}; expected one of {sorted(allowed_verification_statuses)}"
            )


def validate_skill_structure() -> None:
    missing = []
    skill_dirs = [path for path in SKILLS_DIR.iterdir() if path.is_dir() and not path.name.startswith("_")]
    if CODEX_SKILLS_DIR.exists():
        skill_dirs.extend(path for path in CODEX_SKILLS_DIR.iterdir() if path.is_dir() and not path.name.startswith("_"))
    for skill_dir in sorted(skill_dirs):
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


def validate_runtime_registry() -> None:
    cli = ROOT / "scripts" / "neuroflow_runtime" / "cli.py"
    if not cli.exists():
        fail("Missing runtime registry CLI: scripts/neuroflow_runtime/cli.py")
    subprocess.run([sys.executable, str(cli), "list", "--kind", "chains"], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
    with tempfile.TemporaryDirectory() as tmpdir:
        subprocess.run(
            [
                sys.executable,
                str(cli),
                "run",
                "--chain",
                "paper-to-repro",
                "--task",
                "validate runtime registry",
                "--output-root",
                tmpdir,
                "--dry-run",
            ],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )


def main() -> None:
    validate_required_files()
    validate_skill_structure()
    validate_skill_frontmatter()
    validate_json()
    validate_manifests()
    validate_local_links()
    validate_no_large_files()
    validate_public_leakage()
    validate_high_precision_maps()
    validate_runtime_registry()
    print("Skill repository validation passed.")


if __name__ == "__main__":
    main()
