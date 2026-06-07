# Skill Manifest

## Complete NeuroFlow Skills

| Skill | Role | Use when |
|---|---|---|
| `neuro-orchestrator` | AI research workflow controller | A task needs routing across ideas, literature, benchmarks, reproduction, experiments, review, writing, and memory |
| `neuro-idea-finder` | Research idea generator | A task needs EEG/iEEG/fMRI/MEG/LFP/spike/BCI hypotheses, technical routes, baselines, risks, and fast validation |
| `paper-rag-plus` | Literature grounding | A claim needs paper support, citation mapping, or related-work structure |
| `eeg-benchmark-hunter` | Benchmark discovery and audit | A task needs open datasets, benchmark suitability, access, license, splits, baselines, metrics, or leakage checks |
| `repro-pack` | Reproduction contract builder | A paper or repository needs environment, data, weights, commands, expected outputs, sanity checks, or failure recovery |
| `continual-learning-designer` | Continual BCI adaptation design | A task needs cross-subject/session/device adaptation, streaming calibration, forgetting checks, or test-time adaptation |
| `experiment-copilot` | Experiment design | A claim needs experiments, ablations, controls, statistics, or stop rules |
| `reviewer-simulator` | Review risk audit | A paper, claim, or rebuttal needs strict conference-review simulation |
| `oral-writer` | Oral-level paper writing | A paper needs thesis compression, figure narrative, evidence-to-claim alignment, or reviewer-objection preemption |
| `neuro-memory` | Long-term memory consolidation | A completed session may contain reusable workflow, playbook, finding, case, or eval memory |
| `ai-bci-research` | Shared AI x BCI guardrails | A task needs domain assumptions, BCI validity checks, or existing public workflow memory |

## Default Deep Flow

```text
neuro-orchestrator
-> neuro-idea-finder when ideas are needed
-> paper-rag-plus
-> eeg-benchmark-hunter when benchmarks are needed
-> repro-pack when reproduction is needed
-> continual-learning-designer when adaptation is needed
-> experiment-copilot
-> reviewer-simulator
-> oral-writer when writing is needed
-> neuro-memory
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
