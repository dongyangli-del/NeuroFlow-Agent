"""Manifest loading for the NeuroFlow runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


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
    anchors: dict[str, tuple[str, ...]] = field(default_factory=dict)
    outputs: dict[str, str] = field(default_factory=dict)
    routing_boundary: dict[str, Any] = field(default_factory=dict)
    pipeline_edges: tuple[dict[str, Any], ...] = ()


def load_manifest(path: Path) -> SkillManifest:
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(raw, dict):
        raise ValueError(f"Manifest must be a YAML object: {path}")
    anchors = raw.get("anchors") or {}
    normalized_anchors = {
        str(key): tuple(str(item) for item in value or [])
        for key, value in anchors.items()
        if isinstance(value, list)
    }
    axes = raw.get("axes") or {}
    normalized_axes = {
        str(axis): {str(key): str(value) for key, value in values.items()}
        for axis, values in axes.items()
        if isinstance(values, dict)
    }
    outputs = raw.get("outputs") or {}
    return SkillManifest(
        name=str(raw.get("name", "")),
        path=path,
        version=str(raw.get("version", "")),
        status=str(raw.get("status", "")),
        verification_status=str(raw.get("verification_status", "")),
        purpose=str(raw.get("purpose", "")),
        natural_triggers=tuple(str(item) for item in raw.get("natural_triggers") or []),
        always_load=tuple(str(item) for item in raw.get("always_load") or []),
        optional_modules=tuple(str(item) for item in raw.get("optional_modules") or []),
        axes=normalized_axes,
        anchors=normalized_anchors,
        outputs={str(key): str(value) for key, value in outputs.items()} if isinstance(outputs, dict) else {},
        routing_boundary=dict(raw.get("routing_boundary") or {}),
        pipeline_edges=tuple(
            dict(item) for item in raw.get("pipeline_edges") or [] if isinstance(item, dict)
        ),
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
