# NeuroFlow Skill Library Spec

This document defines the target NeuroFlow skill library and the evidence needed before a capability is promoted from a reference playbook into an independent skill.

## Gap Analysis

| Rank | Target skill | Current status | Decision |
|---|---|---|---|
| 1 | `neuro-orchestrator` | Exists as the routing controller. | Strengthen routing across the full library. |
| 2 | `neuro-idea-finder` | Missing. | Promote to independent skill because idea generation has distinct triggers, templates, and failure modes. |
| 3 | `paper-rag-plus` | Exists as literature grounding. | Keep and route to it for claim support, citation mapping, and related work. |
| 4 | `eeg-benchmark-hunter` | Missing. | Promote to independent skill because benchmark discovery needs license, leakage, access, and adaptation checks. |
| 5 | `repro-pack` | Missing. | Promote to independent skill because reproduction needs environment, data, weight, command, sanity-check, and failure-recovery contracts. |
| 6 | `continual-learning-designer` | Missing. | Promote to independent skill because continual BCI adaptation has specific forgetting, calibration, replay, and online/offline risks. |
| 7 | `experiment-copilot` | Exists as experiment matrix design. | Keep and use after ideas, benchmark audits, or paper claims require evidence. |
| 8 | `reviewer-simulator` | Exists as review risk audit. | Keep and use before paper, rebuttal, and oral-writing artifacts. |
| 9 | `oral-writer` | Missing. | Promote to independent skill because oral-level writing needs thesis compression, figure narrative, and objection preemption. |
| 10 | `neuro-memory` | Exists as long-term memory consolidation. | Keep and route persistent lessons to it. |

`ai-bci-research` remains the shared domain guardrail skill across all routes. It is not a replacement for the specialist skills.

## Promotion Rule

A capability becomes an independent skill only when it has all six properties:

1. independent trigger;
2. independent first-read files;
3. non-substitutable check order;
4. fixed output template;
5. recurring failure modes;
6. eval prompts that protect future behavior.

If any property is missing, keep the capability as a reference, playbook, or workflow inside an existing skill.

## Skill Contracts

| Skill | Trigger | First reads | Core workflow | Output | Failure modes | Eval focus |
|---|---|---|---|---|---|---|
| `neuro-orchestrator` | Multi-step task or unclear route. | `references/routing.md`, `references/session-plan.md` | classify type/depth, choose chain, hand off, consolidate | routed plan | doing specialist work directly, missing memory handoff | route correctness |
| `neuro-idea-finder` | User asks for new BCI/NeuroAI ideas. | `references/idea-template.md`, `references/modality-opportunity-map.md` | define axis, generate hypotheses, rank risks, propose fastest validation | idea cards | novelty hype, missing data/baseline, untestable ideas | every idea has test path |
| `paper-rag-plus` | Claim needs literature support. | claim grounding and maps | map claim to inspected support | claim audit or paper card | invented citations, weak verification | no hallucinated citations |
| `eeg-benchmark-hunter` | User needs datasets, benchmarks, leaderboards, or baseline choices. | `references/benchmark-card-template.md`, `references/benchmark-risk-checklist.md` | find candidate, verify access/license, map protocol, assess leakage/adaptation cost | benchmark cards | invented dataset facts, ignoring license/leakage | requires verification fields |
| `repro-pack` | User needs to reproduce a paper or repo. | `references/repro-contract.md`, `references/failure-recovery.md` | inventory repo, pin environment, define data/weights, run smoke path, define expected outputs | reproduction plan | broad refactor, no sanity check, missing expected output | minimal runnable path |
| `continual-learning-designer` | User needs subject/session/device adaptation or streaming BCI learning. | `references/continual-bci-design.md`, `references/evaluation-protocol.md` | define stream, memory, update rule, forgetting metric, calibration and safety | continual learning plan | offline-only claims, forgetting ignored, leakage through adaptation | forgetting and online protocol |
| `experiment-copilot` | Claim needs experiments. | experiment matrix references | build matrix, controls, statistics | experiment matrix | weak controls, no stop rule | must-run checks |
| `reviewer-simulator` | Claim/paper/rebuttal needs review. | rubric and rebuttal plan | audit evidence and objections | review or rebuttal risk map | praise without blocking issues | reviewer risks first |
| `oral-writer` | User asks for oral-level paper framing or writing. | `references/oral-paper-structure.md`, `references/figure-narrative.md` | compress thesis, align evidence, build figure story, preempt objections | oral-ready outline/text | hype, unsupported first claims, weak figure flow | thesis-evidence-figure alignment |
| `neuro-memory` | Session contains reusable lessons. | memory routing references | compress and route memory | memory candidate | saving raw transcript, leaking private data | durable memory routing |

## Phased Implementation

| Phase | Scope | Acceptance criteria |
|---|---|---|
| 1 | Spec and audit | This document exists; manifest explains current and target skill decisions. |
| 2 | `neuro-idea-finder`, `eeg-benchmark-hunter`, `repro-pack` | Each has `SKILL.md`, `references/`, `evals/evals.json`, `agents/openai.yaml`; docs and manifest route to them. |
| 3 | `continual-learning-designer`, `oral-writer` | Each has the required structure and collaborates with existing skills instead of duplicating them. |
| 4 | Orchestrator upgrade | `neuro-orchestrator` routes all 10 target skills by task chain and depth; evals cover route selection. |

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
