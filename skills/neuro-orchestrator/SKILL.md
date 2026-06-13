---
name: neuro-orchestrator
description: Primary and only default NeuroFlow entry point. Use first for AI x BCI, NeuroAI, EEG decoding, neural reconstruction, benchmarks, reproduction, experiments, reviewer simulation, paper writing, rebuttal, and memory tasks. It runs one explicit pipeline and treats specialist skills as optional modules.
---

# Neuro-Orchestrator

Use this skill as the single default entry point for NeuroFlow-Agent. It routes work through one explicit pipeline, keeps the output artifact explicit, and treats narrower specialist skills as optional modules.

## First Reads

- `references/pipeline.md`: Always read first for the single-entry pipeline and artifact contract.
- `references/routing.md`: Always read first for task routing.
- `references/session-plan.md`: Read for multi-step task plans, artifacts, and handoff format.

## Operating Rules

- Start here for any non-trivial NeuroFlow task unless the user explicitly names a specialist.
- Do not wait for automatic specialist skill triggering; execute the selected pipeline even if only this skill is loaded.
- Use `ai-bci-research` for shared AI x BCI guardrails and domain assumptions, not as the workflow router.
- Use `neuro-idea-finder` for EEG/iEEG/fMRI/MEG/LFP/spike/BCI idea generation.
- Use `paper-rag-plus` for literature grounding and claim-to-citation mapping.
- Use `eeg-benchmark-hunter` for benchmark, dataset, access, license, split, and leakage audits.
- Use `repro-pack` for reproduction contracts, smoke runs, expected outputs, and failure recovery.
- Use `continual-learning-designer` for subject/session/device adaptation, streaming calibration, and forgetting protocols.
- Use `experiment-copilot` for experiment matrices, ablations, controls, and statistics.
- Use `reviewer-simulator` for top-tier review risk and rebuttal planning.
- Use `oral-writer` for oral-level thesis compression, figure narrative, and evidence-to-claim writing.
- Use `neuro-memory` after meaningful sessions to consolidate reusable behavior.
- For code reproduction or implementation, also use existing general engineering skills such as `modern-python`, `python-testing`, or repo-aware tools when relevant.
- Use the smallest specialist set that adds distinct evidence or validation.

## Task Depths

| Depth | Use when | Routing behavior |
|---|---|---|
| Shallow | A narrow answer or next check is enough. | Use the orchestrator directly with minimal first reads. |
| Standard | The task needs a concrete artifact. | Use one optional module plus one evidence gate. |
| Deep | The task spans ideas, papers, experiments, review, and writing. | Use a pipeline chain with explicit handoffs and evidence gates. |
| Persistent | The session should change future agent behavior. | Route the final lesson to `neuro-memory` and relevant reference/eval targets. |

## Task Chains

| Chain | Route |
|---|---|
| idea-to-experiment | `neuro-idea-finder` -> `paper-rag-plus` -> `experiment-copilot` -> `reviewer-simulator` -> `neuro-memory` |
| paper-to-repro | `paper-rag-plus` -> `repro-pack` -> `experiment-copilot` -> `neuro-memory` |
| benchmark-to-baseline | `eeg-benchmark-hunter` -> `experiment-copilot` -> `reviewer-simulator` |
| continual-adaptation | `continual-learning-designer` -> `experiment-copilot` -> `reviewer-simulator` |
| experiment-to-paper | `experiment-copilot` -> `reviewer-simulator` -> `oral-writer` -> `neuro-memory` |
| paper-to-rebuttal | `paper-rag-plus` -> `reviewer-simulator` -> `oral-writer` |
| session-to-memory | `neuro-memory` with `ai-bci-research` guardrails |

## Required Output

For routed tasks, produce:

```markdown
Task type:
Task depth:
Pipeline chain:
Primary artifact:
Optional specialist modules:
Required first reads:
Evidence needed:
Expected artifact:
Stop condition:
Memory candidate:
```

## Handoff Contract

Each specialist handoff must include the claim, inspected evidence, missing evidence, expected output format, and whether the result should feed `neuro-memory`.
