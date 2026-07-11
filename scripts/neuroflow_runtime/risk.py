"""Patch inspection and risk classification for semi-automatic evolution."""

from __future__ import annotations

import re
import shlex
from dataclasses import dataclass, field
from pathlib import PurePosixPath

from .models import RiskLevel
from .privacy import sensitive_labels

PROTECTED_PATHS = {
    "evals/protected.json",
    ".private/evolution/evals/hidden.json",
    "skills/_shared/core/cross-model-review.md",
    "skills/_shared/core/evidence-gates.md",
    "skills/_shared/core/git-publish-safety.md",
    "skills/_shared/core/research-integrity.md",
}
HIGH_RISK_PATTERNS = (
    re.compile(r"(^|/)SKILL\.md$"),
    re.compile(r"(^|/)manifest\.yaml$"),
    re.compile(r"(^|/)scripts/"),
    re.compile(r"(^|/)migrations/"),
    re.compile(r"(^|/)agents/"),
    re.compile(r"(^|/)(pipeline|routing)\.md$"),
    re.compile(r"^(AGENTS\.md|pyproject\.toml|Makefile)$"),
)
PUBLIC_REFERENCE = re.compile(r"^skills(?:-codex)?/[^/]+/references/.+\.md$")
EVAL_PATH = re.compile(r"^skills(?:-codex)?/[^/]+/evals/evals\.json$")
PRIVATE_MEMORY = re.compile(
    r"^(?:\.private/(?:memory|references)/.+|skills(?:-codex)?/[^/]+/references/private/.+)\.md$"
)
SOURCE_LOCATORS = ("http://", "https://", "doi:", "doi.org", "arxiv:", "arxiv.org")
UNRESOLVED_MARKERS = ("unresolved", "todo", "manual-review", "人工核验")
COMMAND_ASSERTION = re.compile(r'"type"\s*:\s*"command_exit"', re.IGNORECASE)


@dataclass(frozen=True)
class PatchInspection:
    paths: tuple[str, ...]
    new_files: tuple[str, ...]
    added_lines: tuple[str, ...]
    deleted_lines: tuple[str, ...]
    additions: int
    deletions: int
    risk_level: RiskLevel
    requires_human: bool
    public_reference: bool
    source_traced: bool
    reasons: tuple[str, ...] = field(default_factory=tuple)


class UnsafePatch(ValueError):
    pass


def inspect_patch(patch: str) -> PatchInspection:
    if "GIT binary patch" in patch or re.search(r"^Binary files .+ differ$", patch, re.MULTILINE):
        raise UnsafePatch("Binary candidate patches are not supported")
    if re.search(r"^(?:new file mode|new mode) 120000$", patch, re.MULTILINE):
        raise UnsafePatch("Candidate patches cannot create symbolic links")
    paths: list[str] = []
    new_files: list[str] = []
    added: list[str] = []
    deleted: list[str] = []
    current_destination = ""
    for line in patch.splitlines():
        if line.startswith("diff --git "):
            try:
                parts = shlex.split(line)
            except ValueError as exc:
                raise UnsafePatch("Malformed quoted diff header") from exc
            if len(parts) < 4:
                raise UnsafePatch("Malformed diff header")
            for raw in parts[2:4]:
                path = _clean_path(raw)
                if path not in paths:
                    paths.append(path)
            current_destination = _clean_path(parts[3])
        elif line.startswith("new file mode"):
            if current_destination and current_destination not in new_files:
                new_files.append(current_destination)
        elif line.startswith("--- "):
            raw = _header_path(line[4:])
            if raw != "/dev/null":
                path = _clean_path(raw)
                if path not in paths:
                    paths.append(path)
        elif line.startswith("+++ "):
            raw = _header_path(line[4:])
            if raw != "/dev/null":
                path = _clean_path(raw)
                if path not in paths:
                    paths.append(path)
        elif line.startswith("+") and not line.startswith("+++"):
            added.append(line[1:])
        elif line.startswith("-") and not line.startswith("---"):
            deleted.append(line[1:])
    if not paths:
        raise UnsafePatch("Candidate patch does not modify any paths")

    reasons: list[str] = []
    public_reference = all(PUBLIC_REFERENCE.match(path) and "/references/private/" not in f"/{path}" for path in paths)
    eval_only = all(EVAL_PATH.match(path) for path in paths)
    private_memory_only = all(PRIVATE_MEMORY.match(path) for path in paths)
    additive_private_memory = private_memory_only and all(path in new_files for path in paths)
    added_text = "\n".join(added).lower()
    raw_added_text = "\n".join(added)
    labels = sensitive_labels(raw_added_text)
    if labels:
        raise UnsafePatch(f"Candidate patch contains sensitive material: {', '.join(labels)}")
    source_traced = "source-traced" in added_text and any(locator in added_text for locator in SOURCE_LOCATORS)
    has_unresolved = any(marker in added_text for marker in UNRESOLVED_MARKERS)
    deletes_file = any(line.startswith("deleted file mode") for line in patch.splitlines())
    executes_eval_command = eval_only and COMMAND_ASSERTION.search(raw_added_text) is not None

    if any(path in PROTECTED_PATHS for path in paths):
        risk = RiskLevel.CRITICAL
        reasons.append("patch touches a protected gate or protected eval")
    elif any(_high_risk(path) for path in paths) or deletes_file or executes_eval_command:
        risk = RiskLevel.HIGH
        reasons.append("patch changes code, executable evals, skill policy, routing, tooling, or deletes a file")
    elif public_reference and not deleted and source_traced and not has_unresolved:
        risk = RiskLevel.LOW
        reasons.append("source-traced additive public reference")
    elif eval_only and not deleted:
        risk = RiskLevel.LOW
        reasons.append("additive regression eval")
    elif additive_private_memory:
        risk = RiskLevel.LOW
        reasons.append("additive private Markdown memory")
    else:
        risk = RiskLevel.MEDIUM
        reasons.append("content change is not eligible for unattended promotion")

    if public_reference and not source_traced:
        reasons.append("public reference lacks source-trace markers")
    if has_unresolved:
        reasons.append("added content contains unresolved markers")
    requires_human = risk != RiskLevel.LOW
    return PatchInspection(
        paths=tuple(paths),
        new_files=tuple(new_files),
        added_lines=tuple(added),
        deleted_lines=tuple(deleted),
        additions=len(added),
        deletions=len(deleted),
        risk_level=risk,
        requires_human=requires_human,
        public_reference=public_reference,
        source_traced=source_traced,
        reasons=tuple(reasons),
    )


def _clean_path(raw: str) -> str:
    value = raw.strip()
    if value.startswith(("a/", "b/")):
        value = value[2:]
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or not value or value.startswith(".git/"):
        raise UnsafePatch(f"Unsafe patch path: {raw}")
    return str(path)


def _header_path(raw: str) -> str:
    try:
        values = shlex.split(raw.split("\t", 1)[0])
    except ValueError as exc:
        raise UnsafePatch("Malformed quoted file header") from exc
    if len(values) != 1:
        raise UnsafePatch("File header path with spaces must be quoted")
    return values[0]


def _high_risk(path: str) -> bool:
    return any(pattern.search(path) for pattern in HIGH_RISK_PATTERNS)
