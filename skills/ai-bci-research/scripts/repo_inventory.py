#!/usr/bin/env python3
"""Create a lightweight inventory for a local research code repository."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "__pycache__",
    ".ipynb_checkpoints",
    "node_modules",
    "wandb",
    "outputs",
    "checkpoints",
    "data",
    "datasets",
}

IMPORTANT_NAMES = {
    "README.md",
    "requirements.txt",
    "environment.yml",
    "pyproject.toml",
    "setup.py",
    "setup.sh",
    "Dockerfile",
}


def iter_files(root: Path, max_files: int):
    count = 0
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if not path.is_file():
            continue
        yield path
        count += 1
        if count >= max_files:
            break


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", help="Local repository path")
    parser.add_argument("--output", help="Markdown output path")
    parser.add_argument("--max-files", type=int, default=1000)
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    if not repo.exists():
        raise SystemExit(f"Repo does not exist: {repo}")

    files = list(iter_files(repo, args.max_files))
    suffixes = Counter(path.suffix or "[no extension]" for path in files)
    important = [path for path in files if path.name in IMPORTANT_NAMES]
    top_dirs = sorted({path.relative_to(repo).parts[0] for path in files if path.relative_to(repo).parts})

    lines = [
        f"# Repository Inventory: {repo.name}",
        "",
        f"- Path: `{repo}`",
        f"- Files scanned: {len(files)}",
        "",
        "## Top-Level Entries",
        *[f"- `{name}`" for name in top_dirs[:80]],
        "",
        "## Important Files",
        *[f"- `{path.relative_to(repo)}`" for path in important],
        "",
        "## File Types",
        *[f"- `{suffix}`: {count}" for suffix, count in suffixes.most_common()],
    ]

    text = "\n".join(lines).rstrip() + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
