"""Runtime registry for NeuroFlow skills and workflow chains."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .manifest import SkillManifest, load_manifests


@dataclass(frozen=True)
class WorkflowStage:
    name: str
    module: str
    output: str
    evidence_gates: tuple[str, ...] = ()


@dataclass(frozen=True)
class WorkflowChain:
    name: str
    stages: tuple[WorkflowStage, ...]
    artifact: str
    evidence_gates: tuple[str, ...]
    stop_condition: str

    @property
    def stage_names(self) -> tuple[str, ...]:
        return tuple(stage.name for stage in self.stages)

    @property
    def modules(self) -> tuple[str, ...]:
        return tuple(stage.module for stage in self.stages)


def stage(name: str, module: str, output: str, *gates: str) -> WorkflowStage:
    return WorkflowStage(name=name, module=module, output=output, evidence_gates=tuple(gates))


DEFAULT_CHAINS: tuple[WorkflowChain, ...] = (
    WorkflowChain(
        name="idea-to-experiment",
        stages=(
            stage("idea", "neuro-idea-finder", "Falsifiable hypothesis and kill test", "novelty"),
            stage("literature", "paper-rag-plus", "Closest-work and evidence map", "novelty"),
            stage("experiments", "experiment-copilot", "Controlled experiment matrix", "experiment"),
            stage("reviewer risk", "reviewer-simulator", "Blocking risk assessment", "experiment"),
            stage("memory", "neuro-memory", "Privacy-screened memory decision", "memory"),
        ),
        artifact="EXPERIMENT_IDEA_PLAN.md",
        evidence_gates=("novelty", "experiment", "memory"),
        stop_condition="A falsifiable experiment plan with evidence gaps and next actions exists.",
    ),
    WorkflowChain(
        name="paper-to-repro",
        stages=(
            stage("paper facts", "paper-rag-plus", "Source-traced paper facts", "novelty"),
            stage(
                "reproduction contract",
                "repro-pack",
                "Environment, data, weight, and command contract",
                "reproduction",
            ),
            stage("access checks", "eeg-benchmark-hunter", "Access, license, split, and metric audit", "benchmark"),
            stage("smoke path", "repro-pack", "Minimal runnable smoke path", "reproduction"),
            stage("memory", "neuro-memory", "Privacy-screened reproduction memory", "memory"),
        ),
        artifact="REPRO_CONTRACT.md",
        evidence_gates=("reproduction", "benchmark", "memory"),
        stop_condition="A minimal runnable path or explicit blocker list exists.",
    ),
    WorkflowChain(
        name="benchmark-to-baseline",
        stages=(
            stage("benchmark card", "eeg-benchmark-hunter", "Verified benchmark card", "benchmark"),
            stage("access/license", "eeg-benchmark-hunter", "Access and license decision", "benchmark"),
            stage("split/leakage", "eeg-benchmark-hunter", "Split and leakage audit", "benchmark"),
            stage("baseline matrix", "experiment-copilot", "Protocol-matched baseline matrix", "experiment"),
            stage("reviewer risk", "reviewer-simulator", "Benchmark reviewer-risk map", "experiment"),
        ),
        artifact="BENCHMARK_AUDIT.md",
        evidence_gates=("benchmark", "experiment"),
        stop_condition="Benchmarks, split risks, metrics, and baseline parity are explicit.",
    ),
    WorkflowChain(
        name="continual-adaptation",
        stages=(
            stage("stream", "continual-learning-designer", "Stream and update-event definition", "experiment"),
            stage("adaptation", "continual-learning-designer", "Adaptation policy and controls", "experiment"),
            stage("forgetting", "continual-learning-designer", "Retention and forgetting evaluation", "experiment"),
            stage(
                "online/offline boundary",
                "ai-bci-research",
                "Deployment boundary and safety constraints",
                "closed loop",
            ),
            stage("reviewer risk", "reviewer-simulator", "Continual-learning reviewer risks", "closed loop"),
        ),
        artifact="CONTINUAL_ADAPTATION_PLAN.md",
        evidence_gates=("experiment", "closed loop"),
        stop_condition="Adaptation protocol, baselines, forgetting checks, and deployment boundary are explicit.",
    ),
    WorkflowChain(
        name="experiment-to-paper",
        stages=(
            stage("claim", "paper-rag-plus", "Scoped claim ledger", "novelty"),
            stage("evidence", "paper-rag-plus", "Claim-to-evidence map", "novelty"),
            stage("ablations/statistics", "experiment-copilot", "Ablation and statistical support", "experiment"),
            stage("reviewer risk", "reviewer-simulator", "Blocking paper risks", "experiment"),
            stage("figure story", "oral-writer", "Evidence-aligned figure narrative", "experiment"),
        ),
        artifact="PAPER_NARRATIVE.md",
        evidence_gates=("novelty", "experiment", "memory"),
        stop_condition="Paper-facing claims are scoped to inspected evidence and missing evidence is named.",
    ),
    WorkflowChain(
        name="paper-to-rebuttal",
        stages=(
            stage("reviewer issues", "reviewer-simulator", "Prioritized reviewer issue map", "experiment"),
            stage("evidence gaps", "paper-rag-plus", "Source and evidence gap ledger", "novelty"),
            stage("edits/experiments", "experiment-copilot", "Required edits and experiments", "experiment"),
            stage("rebuttal", "oral-writer", "Evidence-scoped rebuttal text", "experiment"),
        ),
        artifact="REBUTTAL_PLAN.md",
        evidence_gates=("novelty", "experiment"),
        stop_condition="Reviewer responses and required evidence/actions are separated.",
    ),
    WorkflowChain(
        name="session-to-memory",
        stages=(
            stage("lesson", "neuro-memory", "Reusable lesson", "memory"),
            stage("privacy check", "neuro-memory", "Privacy classification", "memory"),
            stage("target memory", "neuro-memory", "Durable memory target", "memory"),
            stage("eval/reference update", "neuro-memory", "Minimal patch and regression eval", "memory"),
        ),
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
