# Skill Manifest

## Complete NeuroFlow Skills

Default entry point: `neuro-orchestrator`.

Specialist skills are optional modules selected by the orchestrator. `ai-bci-research` provides shared AI x BCI guardrails and public memory; it is not the default workflow router.

| Skill | Status | Role | Natural triggers |
|---|---|---|---|
| `neuro-orchestrator` | Stable | Single NeuroFlow workflow entry point | "what should I check next", "why is this result worse", "help me plan this experiment", "下一步查什么" |
| `neuro-idea-finder` | Stable | Research idea generator | "new EEG idea", "hypothesis", "fast validation", "研究 idea" |
| `paper-rag-plus` | Stable | Literature grounding | "support this claim", "closest prior work", "citation map", "相关工作" |
| `eeg-benchmark-hunter` | Stable | Benchmark discovery and audit | "find EEG dataset", "is this benchmark fair", "leakage risk", "找 EEG 数据集" |
| `repro-pack` | Stable | Reproduction contract builder | "make this reproducible", "smoke test", "baseline table", "复现" |
| `continual-learning-designer` | Beta | Continual BCI adaptation design | "online adaptation", "cross-session", "forgetting", "持续学习" |
| `experiment-copilot` | Stable | Experiment design | "design ablations", "baseline is stronger", "metric gap", "实验矩阵" |
| `reviewer-simulator` | Stable | Review risk audit | "review this claim", "what will reviewers attack", "rebuttal plan", "审稿风险" |
| `oral-writer` | Beta | Oral-level paper writing | "write abstract", "paper claim", "figure story", "写摘要" |
| `neuro-memory` | Stable | Long-term memory consolidation | "make this reusable", "save this lesson", "memory candidate", "沉淀经验" |
| `ai-bci-research` | Stable | Shared AI x BCI guardrails | "BCI validity", "signal leakage", "closed loop", "脑机接口检查" |

## Shared Resources

Shared workflow primitives live under `skills/_shared/core/`. They are resource files, not triggerable skills:

| Shared file | Use |
|---|---|
| `evidence-gates.md` | Novelty, benchmark, experiment, reproduction, closed-loop, and memory gates. |
| `claim-discipline.md` | Claim ladder, safer wording, and paper-facing checks. |
| `bci-validity.md` | Split, signal alignment, baseline fairness, and interpretation boundaries. |
| `reviewer-risk.md` | Blocking reviewer risks and rebuttal discipline. |
| `output-contracts.md` | Compact artifacts for next checks, benchmark cards, claim rewrites, and memory candidates. |

High-use skills may include `manifest.yaml` files that declare status, natural triggers, always-loaded references, task axes, and on-demand shared resources.

## Default Pipeline Flow

```text
neuro-orchestrator
-> choose one task chain
-> call optional specialist modules only when needed
-> enforce evidence gates
-> produce the artifact
-> decide whether to update neuro-memory
```

`ai-bci-research` supplies shared domain constraints throughout the flow.

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

## Promotion Rule

Keep a behavior as a reference workflow until it has a distinct trigger, first-read set, check order, output template, failure mode, and eval. Promote it to an independent skill only after repeated use shows that separation reduces confusion.
