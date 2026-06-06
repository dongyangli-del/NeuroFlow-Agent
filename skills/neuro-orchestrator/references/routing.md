# Routing

## Task Router

| User intent | Primary skill | Supporting skills |
|---|---|---|
| Broad research planning | `neuro-orchestrator` | `ai-bci-research`, `neuro-memory` |
| Literature search or paper positioning | `paper-rag-plus` | `literature-review`, `paper-lookup`, `citation-management` |
| Experiment matrix or ablation design | `experiment-copilot` | `statistical-analysis`, `ablation-planner`, `experiment-results-notebook` |
| Reviewer simulation or rebuttal | `reviewer-simulator` | `peer-review`, `scientific-critical-thinking`, `venue-templates` |
| Session memory or skill evolution | `neuro-memory` | `skill-creator`, `scientific-critical-thinking` |
| AI x BCI domain guardrails | `ai-bci-research` | `scientific-critical-thinking` |

## Routing Checks

1. Identify the task type.
2. Decide the primary skill.
3. Name supporting skills only when they add a distinct method or validation layer.
4. State the artifact before doing the work.
5. Decide whether the session should end with a memory candidate.

## Anti-Patterns

- Calling every skill for every task.
- Treating `paper-rag-plus` output as evidence without paper inspection.
- Designing experiments before defining the claim and evaluation target.
- Writing rebuttals before separating factual gaps from framing issues.
- Saving transcript details as memory.
