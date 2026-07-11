from __future__ import annotations

from pathlib import Path

from neuroflow_runtime.registry import build_registry

ROOT = Path(__file__).resolve().parents[1]


def test_every_stage_has_explicit_owner_and_contract() -> None:
    registry = build_registry(ROOT)
    skills = registry.skills()
    for chain in registry.chains().values():
        assert chain.stages
        assert len(chain.stage_names) == len(chain.modules)
        for stage in chain.stages:
            assert stage.module in skills
            assert stage.output
            assert stage.evidence_gates


def test_runtime_manifest_loads_routing_boundaries() -> None:
    manifest = build_registry(ROOT).get_skill("neuro-memory")
    assert manifest.routing_boundary["do_not_use_when"]
    assert manifest.anchors["verbs"]
    assert manifest.outputs["primary"]
