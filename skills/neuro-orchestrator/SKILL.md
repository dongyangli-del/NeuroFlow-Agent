---
name: neuro-orchestrator
description: AI neuroscience research workflow router and controller. Use for multi-step AI x neuroscience tasks that need routing across literature grounding, experiment design, reviewer simulation, writing, reproduction, and long-term memory consolidation.
---

# Neuro-Orchestrator

Use this skill as the first entry point for complex AI x neuroscience research tasks. It should route work to narrower skills and keep the output artifact explicit.

## First Reads

- `references/routing.md`: Always read first for task routing.
- `references/session-plan.md`: Read for multi-step task plans, artifacts, and handoff format.

## Operating Rules

- Do not perform every subtask directly when a specialist skill fits.
- Use `ai-bci-research` for shared AI x BCI guardrails and domain assumptions.
- Use `paper-rag-plus` for literature grounding and claim-to-citation mapping.
- Use `experiment-copilot` for experiment matrices, ablations, controls, and statistics.
- Use `reviewer-simulator` for top-tier review risk and rebuttal planning.
- Use `neuro-memory` after meaningful sessions to consolidate reusable behavior.
- For code reproduction or implementation, also use existing general engineering skills such as `modern-python`, `python-testing`, or repo-aware tools when relevant.

## Required Output

For routed tasks, produce:

```markdown
Task type:
Primary skill:
Supporting skills:
Required first reads:
Evidence needed:
Expected artifact:
Stop condition:
Memory candidate:
```

## Handoff Contract

Each specialist handoff must include the claim, inspected evidence, missing evidence, expected output format, and whether the result should feed `neuro-memory`.
