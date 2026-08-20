# NeuroFlow Pipeline for Codex

`neuro-orchestrator` is the only default entry point.

Codex skill triggering is opportunistic, so this entry skill must be able to run the workflow even when no specialist skill is automatically loaded. Specialist skills are optional modules, not the workflow backbone.

## Control Loop

1. Classify task type and depth.
2. Choose one pipeline chain.
3. Name the primary artifact.
4. Apply the proportional-execution gate and remove stages that do not resolve a live uncertainty for this artifact.
5. Load only the needed first reads.
6. Invoke or emulate optional specialist modules.
7. For multi-stage work, carry the original user intent and operational anchors into each handoff.
8. Apply research supervision gates from `references/research-supervision-gates.md`.
9. Apply evidence gates.
10. Produce the requested artifact and its smallest relevant validation.
11. Stop; default to no memory update unless the lesson is reusable.

## Pipeline Chains

Pipeline chains are available routes, not mandatory stage lists. Shallow and standard tasks may stop after the stage that produces and validates the requested artifact.

| Chain | Use when | Stages |
|---|---|---|
| idea-to-experiment | A rough idea should become a testable plan. | idea -> literature -> experiments -> reviewer risk -> memory |
| paper-to-repro | A paper or repo should become runnable. | paper facts -> reproduction contract -> access checks -> smoke path -> memory |
| benchmark-to-baseline | A claim needs datasets, baselines, metrics, or leakage audit. | benchmark card -> access/license -> split/leakage -> baseline matrix -> reviewer risk |
| continual-adaptation | A method needs personalization or streaming BCI learning. | stream -> adaptation -> forgetting -> online/offline boundary -> reviewer risk |
| experiment-to-paper | Results should become paper narrative. | claim -> evidence -> ablations/statistics -> reviewer risk -> figure story |
| paper-to-rebuttal | A draft or review needs response. | reviewer issues -> evidence gaps -> edits/experiments -> rebuttal |
| session-to-memory | A reusable lesson should persist. | lesson -> privacy check -> target memory -> eval/reference update |

## Artifact Contract

```markdown
Task type:
Task depth:
Pipeline chain:
Primary artifact:
Optional specialist modules:
Required first reads:
Evidence gates:
Work order:
Original user intent:
Operational anchors:
Stop condition:
Memory candidate:
```

## Evidence Gates

- Novelty: inspected literature or marked uncertainty.
- Benchmark: access, license, split, metric, baseline, leakage.
- Experiment: matched protocol, metrics, baselines, ablations, stop rules.
- Reproduction: environment, data, weights, command, expected output, sanity check.
- Closed loop: online/offline boundary, safety, calibration, latency, human-subject constraints.
- Research integrity: claim-evidence consistency, citation fit, numeric self-consistency, protocol truthfulness, observability level.
- Cross-model review: one executor/reviewer split is required at a final consequential claim, reproduction, public-memory, or promotion milestone, or record `required_but_not_run`; intermediate and unchanged artifacts do not repeat the gate.
- Git publish safety: commit, push, branch deletion, and remote synchronization requests require target-branch confirmation, fresh remote state, ancestry checks, and cleanup of temporary branches only after the target contains the commits.
- Skill physics: avoid adding or calling overlapping specialists when a reference, shared gate, eval, or sequential handoff is enough; every deep handoff must preserve original user intent and operational anchors.
- Memory: privacy filter and explicit target.

## Completion Rule

Finish when the primary artifact exists and the smallest validation tied to its live uncertainty passes. Optional confidence work is non-blocking and must not start another review, artifact, or memory loop.

## Supervision Gates

Read `references/research-supervision-gates.md` for advisor-style checks on idea commitment, paper logic, benchmark substance, figure narrative, pre-submission review, and AI-assisted research integrity.
