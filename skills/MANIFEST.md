# Skill Manifest

## Phase 1 Skills

| Skill | Role | Use when |
|---|---|---|
| `neuro-orchestrator` | Research workflow controller | A task needs routing across literature, experiments, review, and memory |
| `paper-rag-plus` | Literature grounding | A claim needs paper support, citation mapping, or related-work structure |
| `experiment-copilot` | Experiment design | A claim needs experiments, ablations, controls, statistics, or stop rules |
| `reviewer-simulator` | Review risk audit | A paper, claim, or rebuttal needs strict conference-review simulation |
| `neuro-memory` | Long-term memory consolidation | A completed session may contain reusable workflow, playbook, finding, case, or eval memory |
| `ai-bci-research` | Shared AI x BCI guardrails | A task needs domain assumptions, BCI validity checks, or existing public workflow memory |

## Default Flow

```text
neuro-orchestrator
-> paper-rag-plus
-> experiment-copilot
-> reviewer-simulator
-> neuro-memory
```

`ai-bci-research` supplies shared domain constraints throughout the flow.

## Promotion Rule

Keep a behavior as a reference workflow until it has a distinct trigger, first-read set, check order, output template, failure mode, and eval. Promote it to an independent skill only after repeated use shows that separation reduces confusion.
