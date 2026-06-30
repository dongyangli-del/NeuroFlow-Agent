---
name: neuro-orchestrator
description: Use first for non-trivial research work in NeuroFlow-Agent, including planning experiments, debugging ML results, checking baselines, designing ablations, reading papers, writing paper sections, reviewing claims, reproducing repositories, deciding next steps, and consolidating research memory. Do not wait for the user to say workflow, plan, routing, or skill.
---

# Neuro-Orchestrator

Use this skill as the single default entry point for NeuroFlow-Agent. It routes work through one explicit pipeline, keeps the output artifact explicit, and treats narrower specialist skills as optional modules. Do not rely on the user explicitly asking for a workflow.

## First Reads

- `references/pipeline.md`: Always read first for the single-entry pipeline and artifact contract.
- `references/routing.md`: Always read first for task routing.
- `references/session-plan.md`: Read for multi-step task plans, artifacts, and handoff format.
- `references/research-supervision-gates.md`: Read when committing to an idea, structuring a paper, designing a benchmark, planning figures, reviewing before submission, or using AI-assisted research workflows.

## Operating Rules

- Start here for any non-trivial NeuroFlow task unless the user explicitly names a specialist.
- Treat natural requests such as "what should I check next", "why is this result worse", "help write this claim", "review this experiment", or "make this reproducible" as NeuroFlow tasks even if the user never says workflow or plan.
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
- Apply research supervision gates before polishing ideas, paper text, figures, benchmarks, or claims.
- For paper-facing claims, reviews, result tables, citations, or reproduction statements, apply the research-integrity gate: claim-evidence consistency, citation fit, numeric self-consistency, protocol truthfulness, and observability level.
- For high-risk claim, citation, experiment, benchmark, reproduction, or public-memory artifacts, apply cross-model review by default: executor performs the work, reviewer independently checks it, and the final gate cannot be self-approved by the same model/pass.

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

## Internal Preflight and Output

Run this preflight internally before acting:

```markdown
Task type:
Task depth:
Pipeline chain:
Primary artifact:
Optional specialist modules:
Required first reads:
Evidence needed:
Cross-model review:
Expected artifact:
Stop condition:
Memory candidate:
```

Expose the full preflight only when the user asks for a plan, the task is deep or persistent, the work spans multiple stages, or the handoff would otherwise be ambiguous. For shallow or standard tasks, keep the preflight internal and proceed directly; mention the selected route only when it clarifies the answer.

## Handoff Contract

Each specialist handoff must include the claim, inspected evidence, missing evidence, expected output format, and whether the result should feed `neuro-memory`.
