---
name: neuro-orchestrator
description: Use first for non-trivial research work in NeuroFlow-Agent, including planning experiments, debugging ML results, checking baselines, designing ablations, reading papers, writing paper sections, reviewing claims, reproducing repositories, deciding next steps, and consolidating research memory. Do not wait for the user to say workflow, plan, routing, or skill.
---

# Neuro-Orchestrator for Codex

Use this skill as the single default entry point for NeuroFlow-Agent in Codex. Do not rely on Codex automatically triggering multiple specialist skills or on the user explicitly asking for a workflow. Route the session explicitly and use specialist modules only when they add a distinct check order or output template.

## First Reads

- `references/pipeline.md`: Always read first for the single-entry pipeline and artifact contract.
- `references/routing.md`: Read when choosing task type, depth, and specialist modules.
- `references/session-plan.md`: Read when producing a multi-step plan or handoff.
- `references/research-supervision-gates.md`: Read when committing to an idea, structuring a paper, designing a benchmark, planning figures, reviewing before submission, or using AI-assisted research workflows.

## Entry Rules

- Start every non-trivial NeuroFlow task here unless the user explicitly names another skill.
- Treat natural requests such as "what should I check next", "why is this result worse", "help write this claim", "review this experiment", or "make this reproducible" as NeuroFlow tasks even if the user never says workflow or plan.
- Treat `ai-bci-research` as shared AI x BCI guardrails and public memory, not the default router.
- If a specialist skill is not triggered or not installed, still execute the corresponding pipeline stage from this skill.
- Name the expected artifact before doing detailed work.
- Use the smallest pipeline chain that can satisfy the user request.
- Apply research supervision gates before polishing ideas, paper text, figures, benchmarks, or claims.
- For paper-facing claims, reviews, result tables, citations, or reproduction statements, apply the research-integrity gate: claim-evidence consistency, citation fit, numeric self-consistency, protocol truthfulness, and observability level.

## Optional Specialist Modules

- `neuro-idea-finder`: idea cards and fast falsification paths.
- `paper-rag-plus`: literature grounding and claim-to-citation mapping.
- `eeg-benchmark-hunter`: dataset, access, license, split, metric, baseline, and leakage audit.
- `repro-pack`: environment, data, weights, command, expected output, and smoke-run contract.
- `continual-learning-designer`: subject/session/device adaptation and online/offline boundary.
- `experiment-copilot`: experiment matrix, ablations, controls, statistics, and stop rules.
- `reviewer-simulator`: blocking reviewer risks and rebuttal strategy.
- `oral-writer`: thesis compression, figure narrative, and evidence-scoped paper text.
- `neuro-memory`: durable workflow, playbook, finding, case, eval, or private-memory routing.
- `ai-bci-research`: BCI validity, leakage, signal-processing, closed-loop, and safety guardrails.

## Internal Preflight and Output

Run this preflight internally before acting:

```markdown
Task type:
Task depth:
Pipeline chain:
Primary artifact:
Optional specialist modules:
Required first reads:
Evidence gates:
Work order:
Stop condition:
Memory candidate:
```

Expose the full preflight only when the user asks for a plan, the task is deep or persistent, the work spans multiple stages, or the handoff would otherwise be ambiguous. For shallow or standard tasks, keep the preflight internal and proceed directly; mention the selected route only when it clarifies the answer.

## Failure Modes

- Starting from `ai-bci-research` for a multi-step workflow instead of routing here.
- Waiting for automatic specialist skill triggering before making progress.
- Waiting for the user to explicitly say workflow, plan, routing, or skill before applying NeuroFlow.
- Calling every specialist for every task.
- Writing claims before evidence gates.
- Saving private data, unpublished results, or raw logs into public memory.
