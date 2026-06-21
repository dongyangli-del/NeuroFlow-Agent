"""Manifest loading for the lightweight NeuroFlow runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class SkillManifest:
    name: str
    path: Path
    version: str = ""
    status: str = ""
    verification_status: str = ""
    purpose: str = ""
    natural_triggers: tuple[str, ...] = ()
    always_load: tuple[str, ...] = ()
    optional_modules: tuple[str, ...] = ()
    axes: dict[str, dict[str, str]] = field(default_factory=dict)


def _strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _parse_manifest_subset(text: str) -> dict[str, object]:
    """Parse the limited YAML subset used by NeuroFlow manifests.

    Supported shapes:
    - top-level `key: scalar`
    - top-level `key:` followed by `  - list items`
    - `axes:` with one nested mapping level and scalar leaves
    """
    result: dict[str, object] = {}
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip() or line.lstrip().startswith("#") or line.startswith(" "):
            index += 1
            continue
        if ":" not in line:
            index += 1
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if raw_value:
            result[key] = _strip_quotes(raw_value)
            index += 1
            continue

        block: list[str] = []
        index += 1
        while index < len(lines) and (lines[index].startswith("  ") or not lines[index].strip()):
            if lines[index].strip():
                block.append(lines[index])
            index += 1

        if block and all(item.startswith("  - ") for item in block):
            result[key] = tuple(_strip_quotes(item[4:].strip()) for item in block)
        elif key == "axes":
            result[key] = _parse_axes(block)
        else:
            result[key] = tuple()
    return result


def _parse_axes(block: list[str]) -> dict[str, dict[str, str]]:
    axes: dict[str, dict[str, str]] = {}
    current_axis = ""
    for line in block:
        if line.startswith("  ") and not line.startswith("    ") and line.strip().endswith(":"):
            current_axis = line.strip()[:-1]
            axes[current_axis] = {}
            continue
        if current_axis and line.startswith("    ") and ":" in line:
            name, value = line.strip().split(":", 1)
            axes[current_axis][name.strip()] = _strip_quotes(value.strip())
    return axes


def load_manifest(path: Path) -> SkillManifest:
    data = _parse_manifest_subset(path.read_text(encoding="utf-8"))
    return SkillManifest(
        name=str(data.get("name", "")),
        path=path,
        version=str(data.get("version", "")),
        status=str(data.get("status", "")),
        verification_status=str(data.get("verification_status", "")),
        purpose=str(data.get("purpose", "")),
        natural_triggers=tuple(data.get("natural_triggers", ()) or ()),
        always_load=tuple(data.get("always_load", ()) or ()),
        optional_modules=tuple(data.get("optional_modules", ()) or ()),
        axes=dict(data.get("axes", {}) or {}),
    )


def load_manifests(root: Path) -> list[SkillManifest]:
    manifests = []
    for base in (root / "skills", root / "skills-codex"):
        if not base.exists():
            continue
        for path in sorted(base.glob("*/manifest.yaml")):
            manifest = load_manifest(path)
            if manifest.name:
                manifests.append(manifest)
    return manifests
