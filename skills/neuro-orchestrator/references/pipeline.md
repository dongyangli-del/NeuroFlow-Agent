# NeuroFlow Pipeline

## Single Entry Contract

`neuro-orchestrator` is the only default NeuroFlow entry point.

Specialist skills are optional modules. Use them when a subtask needs their check order or output template, but do not require Codex to auto-trigger them for the workflow to work. If a specialist skill is unavailable, the orchestrator should still execute the same stage using the artifact contract below.

`ai-bci-research` supplies AI x BCI guardrails, leakage checks, closed-loop cautions, and public workflow memory. It is not the primary router.

## Control Loop

1. Classify the user request by task type and depth.
2. Choose one pipeline chain.
3. Name the primary artifact before detailed work.
4. Apply the proportional-execution gate and remove stages that do not resolve a live uncertainty for this artifact.
5. Load only the first-read files needed for the chosen chain.
6. Use optional specialist modules for distinct subtasks.
7. For multi-stage work, carry the original user intent and operational anchors into each handoff.
8. Apply the relevant research supervision gates from `references/research-supervision-gates.md`.
9. Enforce evidence gates before claims, experiments, writing, or memory updates.
10. Stop after the requested artifact and smallest relevant validation pass; default to no memory update unless the lesson is reusable.

## Pipeline Chains

Pipeline chains are available routes, not mandatory stage lists. Shallow and standard tasks may stop after the stage that produces and validates the requested artifact.

| Chain | Use when | Possible stages |
|---|---|---|
| idea-to-experiment | A rough idea should become a testable plan. | idea card -> literature grounding -> experiment matrix -> reviewer risk -> memory decision |
| paper-to-repro | A paper or repository should become runnable. | paper facts -> reproduction contract -> data/weight access -> smoke run plan -> memory decision |
| benchmark-to-baseline | A claim needs datasets, baselines, metrics, or split checks. | benchmark card -> access/license check -> split/leakage audit -> baseline matrix -> reviewer risk |
| continual-adaptation | A method needs subject/session/device/online adaptation. | stream definition -> adaptation rule -> forgetting metrics -> online/offline boundary -> reviewer risk |
| experiment-to-paper | Results should become submission-facing writing. | claim -> evidence map -> ablations/statistics -> reviewer risk -> figure narrative |
| paper-to-rebuttal | A draft or review needs a response. | reviewer issue map -> evidence gaps -> experiments/edits -> scoped rebuttal text |
| session-to-memory | A session contains reusable behavior. | lesson -> target memory type -> privacy check -> eval or reference target |

## Artifact Contract

```markdown
Task type:
Task depth:
Pipeline chain:
Primary artifact:
Optional specialist modules:
Required first reads:
Evidence gates:
Original user intent:
Operational anchors:
Stop condition:
Memory candidate:
```

Use durable artifact files only when the user requests persistence or a later handoff needs them. Possible names:

- `NEUROFLOW_PLAN.md`
- `LITERATURE_GROUNDING.md`
- `BENCHMARK_AUDIT.md`
- `REPRO_CONTRACT.md`
- `EXPERIMENT_MATRIX.md`
- `REVIEWER_RISK.md`
- `PAPER_NARRATIVE.md`
- `MEMORY_CANDIDATE.md`

## Evidence Gates

- Novelty claims require inspected literature or explicit uncertainty.
- Benchmark recommendations require access, license, split, metric, baseline, and leakage fields.
- Experiment claims require matched protocols, metric definitions, baselines, ablations, and stop rules.
- Reproduction claims require environment, data, weights, commands, expected outputs, and sanity checks.
- Closed-loop claims require online/offline boundary, safety, calibration, latency, and human-subject constraints.
- Research-integrity checks require claim-evidence consistency, citation fit, numeric self-consistency, protocol truthfulness, and an explicit observability level.
- Cross-model review checks require one executor/reviewer split at a final consequential claim, reproduction, public-memory, or promotion milestone, or an explicit `required_but_not_run` caveat; intermediate and unchanged artifacts do not repeat the gate.
- Git publish safety checks require target-branch confirmation, fresh remote state, ancestry checks, user-named branch delivery, and cleanup of temporary branches only after the target branch contains the commits.
- Skill physics checks require avoiding overlapping specialists when a reference, shared gate, eval, or sequential handoff is enough; every deep handoff preserves original user intent and operational anchors.
- Memory updates require privacy filtering and a target file or eval.

## Completion Rule

Finish when the primary artifact exists and the smallest validation tied to its live uncertainty passes. Optional confidence work is non-blocking and must not start another review, artifact, or memory loop.

## Supervision Gates

Use `references/research-supervision-gates.md` when a task involves idea commitment, paper logic, benchmark substance, figure narrative, pre-submission review, or AI-assisted research integrity. These gates prevent the workflow from polishing weak science.
