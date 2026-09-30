# NeuroFlow Agent Guide

This document explains the NeuroFlow workflow model. Repository-level agents should follow `AGENTS.md` first; this guide provides the longer rationale, routing details, and artifact conventions.

## Entry Rule

`neuro-orchestrator` is the only default entry point.

Do not begin a NeuroFlow session by choosing a specialist skill directly unless the user explicitly names that specialist. Start with `neuro-orchestrator`, classify the task, choose the pipeline stage, and then call or emulate specialist workflows as optional modules. Agents should do this for natural research requests even when the user does not mention workflow, plan, routing, or skills.

`ai-bci-research` is a shared domain-guardrail and memory skill. It is not the default workflow entry point.

## Main Pipeline

Use this control loop for AI x BCI, NeuroAI, EEG decoding, neural reconstruction, brain-language alignment, closed-loop BCI, paper, benchmark, reproduction, experiment, review, writing, or memory tasks:

```text
neuro-orchestrator
-> classify task type and depth
-> select one pipeline chain
-> load AI x BCI guardrails when needed
-> apply research supervision gates before committing claims
-> invoke optional specialist modules only for distinct subtasks
-> produce the requested artifact
-> decide whether the session should update durable memory
```

## Pipeline Chains

| Chain | Use when | Optional specialist modules |
|---|---|---|
| idea-to-experiment | A rough research direction should become a testable plan. | `neuro-idea-finder`, `paper-rag-plus`, `experiment-copilot`, `reviewer-simulator`, `neuro-memory` |
| paper-to-repro | A paper or repository should become runnable. | `paper-rag-plus`, `repro-pack`, `eeg-benchmark-hunter`, `experiment-copilot`, `neuro-memory` |
| benchmark-to-baseline | A claim needs datasets, baselines, metrics, split checks, or leakage audit. | `eeg-benchmark-hunter`, `paper-rag-plus`, `experiment-copilot`, `reviewer-simulator` |
| continual-adaptation | A method needs cross-subject, cross-session, cross-device, online, or streaming adaptation. | `continual-learning-designer`, `experiment-copilot`, `reviewer-simulator`, `ai-bci-research` |
| experiment-to-paper | Results should become submission-facing claims, figures, or narrative. | `experiment-copilot`, `reviewer-simulator`, `oral-writer`, `paper-rag-plus`, `neuro-memory` |
| paper-to-rebuttal | A draft, review, or rebuttal needs evidence-scoped response. | `paper-rag-plus`, `reviewer-simulator`, `oral-writer` |
| session-to-memory | A completed session contains reusable behavior. | `neuro-memory`, `ai-bci-research` |

## Preflight and Artifact Contract

Every routed session should internally name the artifact before doing detailed work:

```markdown
Task type:
Task depth:
Pipeline chain:
Primary artifact:
Optional specialist modules:
Required first reads:
Evidence gates:
Stop condition:
Memory candidate:
```

Expose the full contract when the user asks for a plan, the task is deep or persistent, or a multi-stage handoff would be ambiguous. For shallow and standard work, keep this as an internal preflight and proceed directly.

Use durable artifact names when a session spans multiple turns or tools:

- `NEUROFLOW_PLAN.md`
- `LITERATURE_GROUNDING.md`
- `BENCHMARK_AUDIT.md`
- `REPRO_CONTRACT.md`
- `EXPERIMENT_MATRIX.md`
- `REVIEWER_RISK.md`
- `PAPER_NARRATIVE.md`
- `MEMORY_CANDIDATE.md`

## Failure Modes

- Treating specialist skills as independent default entry points.
- Letting `ai-bci-research` swallow a multi-step workflow without routing through `neuro-orchestrator`.
- Calling every specialist for every task instead of selecting the smallest useful chain.
- Producing polished ideas, paper text, or benchmark recommendations before evidence gates.
- Using AI to outsource novelty, citations, experiment design, or result interpretation instead of using it as a supervised accelerator.
- Saving raw private logs, human-subject material, unpublished results, or credentials into public memory.

## External Methodology Inspirations

NeuroFlow may use license-safe abstractions inspired by public research-supervision resources. One example is HKUSTDial/Supervisor-Skills (https://github.com/HKUSTDial/Supervisor-Skills), which motivates advisor-style checks for idea commitment, paper logic, benchmark substance, figure narrative, and pre-submission review. Do not copy its CC BY-NC-SA 4.0 text into NeuroFlow; use NeuroFlow's own `research-supervision-gates.md` wording.
