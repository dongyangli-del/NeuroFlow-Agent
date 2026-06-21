"""Runtime registry for NeuroFlow skills and workflow chains."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .manifest import SkillManifest, load_manifests


@dataclass(frozen=True)
class WorkflowChain:
    name: str
    stages: tuple[str, ...]
    modules: tuple[str, ...]
    artifact: str
    evidence_gates: tuple[str, ...]
    stop_condition: str


DEFAULT_CHAINS: tuple[WorkflowChain, ...] = (
    WorkflowChain(
        name="idea-to-experiment",
        stages=("idea", "literature", "experiments", "reviewer risk", "memory"),
        modules=("neuro-idea-finder", "paper-rag-plus", "experiment-copilot", "reviewer-simulator", "neuro-memory"),
        artifact="EXPERIMENT_IDEA_PLAN.md",
        evidence_gates=("novelty", "experiment", "memory"),
        stop_condition="A falsifiable experiment plan with evidence gaps and next actions exists.",
    ),
    WorkflowChain(
        name="paper-to-repro",
        stages=("paper facts", "reproduction contract", "access checks", "smoke path", "memory"),
        modules=("paper-rag-plus", "repro-pack", "eeg-benchmark-hunter", "experiment-copilot", "neuro-memory"),
        artifact="REPRO_CONTRACT.md",
        evidence_gates=("reproduction", "benchmark", "memory"),
        stop_condition="A minimal runnable path or explicit blocker list exists.",
    ),
    WorkflowChain(
        name="benchmark-to-baseline",
        stages=("benchmark card", "access/license", "split/leakage", "baseline matrix", "reviewer risk"),
        modules=("eeg-benchmark-hunter", "experiment-copilot", "reviewer-simulator"),
        artifact="BENCHMARK_AUDIT.md",
        evidence_gates=("benchmark", "experiment"),
        stop_condition="Benchmarks, split risks, metrics, and baseline parity are explicit.",
    ),
    WorkflowChain(
        name="continual-adaptation",
        stages=("stream", "adaptation", "forgetting", "online/offline boundary", "reviewer risk"),
        modules=("continual-learning-designer", "experiment-copilot", "reviewer-simulator", "ai-bci-research"),
        artifact="CONTINUAL_ADAPTATION_PLAN.md",
        evidence_gates=("experiment", "closed loop"),
        stop_condition="Adaptation protocol, baselines, forgetting checks, and deployment boundary are explicit.",
    ),
    WorkflowChain(
        name="experiment-to-paper",
        stages=("claim", "evidence", "ablations/statistics", "reviewer risk", "figure story"),
        modules=("experiment-copilot", "reviewer-simulator", "oral-writer", "paper-rag-plus", "neuro-memory"),
        artifact="PAPER_NARRATIVE.md",
        evidence_gates=("novelty", "experiment", "memory"),
        stop_condition="Paper-facing claims are scoped to inspected evidence and missing evidence is named.",
    ),
    WorkflowChain(
        name="paper-to-rebuttal",
        stages=("reviewer issues", "evidence gaps", "edits/experiments", "rebuttal"),
        modules=("paper-rag-plus", "reviewer-simulator", "oral-writer"),
        artifact="REBUTTAL_PLAN.md",
        evidence_gates=("novelty", "experiment"),
        stop_condition="Reviewer responses and required evidence/actions are separated.",
    ),
    WorkflowChain(
        name="session-to-memory",
        stages=("lesson", "privacy check", "target memory", "eval/reference update"),
        modules=("neuro-memory", "ai-bci-research"),
        artifact="MEMORY_CANDIDATE.md",
        evidence_gates=("memory",),
        stop_condition="A privacy-screened memory decision and target artifact exist.",
    ),
)


class RuntimeRegistry:
    def __init__(self) -> None:
        self._skills: dict[str, SkillManifest] = {}
        self._chains: dict[str, WorkflowChain] = {}

    def register_skill(self, manifest: SkillManifest) -> None:
        existing = self._skills.get(manifest.name)
        if existing and existing.path != manifest.path:
            # Prefer the Codex-specific orchestrator manifest for identical names.
            if "skills-codex" in manifest.path.parts:
                self._skills[manifest.name] = manifest
            return
        self._skills[manifest.name] = manifest

    def register_chain(self, chain: WorkflowChain) -> None:
        if chain.name in self._chains:
            raise ValueError(f"Workflow chain already registered: {chain.name}")
        self._chains[chain.name] = chain

    def get_skill(self, name: str) -> SkillManifest:
        try:
            return self._skills[name]
        except KeyError as exc:
            raise KeyError(f"Unknown skill {name!r}; available: {sorted(self._skills)}") from exc

    def get_chain(self, name: str) -> WorkflowChain:
        try:
            return self._chains[name]
        except KeyError as exc:
            raise KeyError(f"Unknown chain {name!r}; available: {sorted(self._chains)}") from exc

    def skills(self) -> dict[str, SkillManifest]:
        return dict(self._skills)

    def chains(self) -> dict[str, WorkflowChain]:
        return dict(self._chains)


def build_registry(root: Path) -> RuntimeRegistry:
    registry = RuntimeRegistry()
    for manifest in load_manifests(root):
        registry.register_skill(manifest)
    for chain in DEFAULT_CHAINS:
        registry.register_chain(chain)
    return registry
