# Routing

## Entry Policy

`neuro-orchestrator` is the only default NeuroFlow entry point. Specialist skills are modules selected by the orchestrator, not competing default entry points.

If a specialist skill is unavailable or not automatically triggered, keep going through the selected pipeline and use the specialist's expected fields as an internal checklist.

## Task Router

| User intent | Pipeline module | Supporting modules |
|---|---|---|
| Broad research planning | `neuro-orchestrator` | `ai-bci-research`, `neuro-memory` |
| New research ideas or hypotheses | `neuro-idea-finder` | `paper-rag-plus`, `experiment-copilot`, `ai-bci-research` |
| Literature search or paper positioning | `paper-rag-plus` | `literature-review`, `paper-lookup`, `citation-management` |
| Benchmark, dataset, leaderboard, or baseline discovery | `eeg-benchmark-hunter` | `paper-rag-plus`, `experiment-copilot` |
| Paper or repository reproduction | `repro-pack` | `paper-rag-plus`, `eeg-benchmark-hunter`, `experiment-copilot` |
| Continual learning, personalization, or streaming adaptation | `continual-learning-designer` | `experiment-copilot`, `reviewer-simulator`, `ai-bci-research` |
| Experiment matrix or ablation design | `experiment-copilot` | `statistical-analysis`, `ablation-planner`, `experiment-results-notebook` |
| Reviewer simulation or rebuttal | `reviewer-simulator` | `peer-review`, `scientific-critical-thinking`, `venue-templates` |
| Oral-level writing, figure narrative, or thesis compression | `oral-writer` | `paper-rag-plus`, `experiment-copilot`, `reviewer-simulator` |
| Session memory or skill evolution | `neuro-memory` | `skill-creator`, `scientific-critical-thinking` |
| AI x BCI domain guardrails | `ai-bci-research` | `scientific-critical-thinking` |

## Task Depths

| Depth | Rule |
|---|---|
| Shallow | Use one primary skill and minimal first reads. |
| Standard | Use one primary skill plus one supporting skill that validates evidence or risk. |
| Deep | Use a chain when the task crosses idea, literature, benchmark, experiment, review, reproduction, writing, or memory boundaries. |
| Persistent | End with `neuro-memory` and a concrete memory candidate target. |

## Task Chains

| Chain | Use when | Route |
|---|---|---|
| idea-to-experiment | A rough idea should become a testable research plan. | `neuro-idea-finder` -> `paper-rag-plus` -> `experiment-copilot` -> `reviewer-simulator` -> `neuro-memory` |
| paper-to-repro | A paper or repo should become runnable. | `paper-rag-plus` -> `repro-pack` -> `experiment-copilot` -> `neuro-memory` |
| benchmark-to-baseline | A claim needs datasets, baselines, and protocol checks. | `eeg-benchmark-hunter` -> `experiment-copilot` -> `reviewer-simulator` |
| continual-adaptation | A method needs personalization or continual BCI learning. | `continual-learning-designer` -> `experiment-copilot` -> `reviewer-simulator` |
| experiment-to-paper | Results should become submission-facing writing. | `experiment-copilot` -> `reviewer-simulator` -> `oral-writer` -> `neuro-memory` |
| paper-to-rebuttal | A draft or review needs evidence-scoped rebuttal text. | `paper-rag-plus` -> `reviewer-simulator` -> `oral-writer` |
| session-to-memory | A completed session contains reusable behavior. | `neuro-memory` with `ai-bci-research` guardrails |

## Routing Checks

1. Identify the task type.
2. Choose the pipeline chain.
3. Name optional specialist modules only when they add a distinct method or validation layer.
4. State the artifact before doing the work.
5. Decide whether the session should end with a memory candidate.
6. Use `ai-bci-research` as shared guardrails for neural decoding, reconstruction, alignment, and closed-loop claims.

## Anti-Patterns

- Treating a specialist skill as the default workflow entry point.
- Calling every skill for every task.
- Treating `paper-rag-plus` output as evidence without paper inspection.
- Designing experiments before defining the claim and evaluation target.
- Recommending benchmarks without access, license, split, baseline, metric, and leakage checks.
- Treating a smoke run as full paper reproduction.
- Calling offline fine-tuning an online continual BCI result.
- Writing oral-level claims before mapping evidence to figures and reviewer risks.
- Writing rebuttals before separating factual gaps from framing issues.
- Saving transcript details as memory.
