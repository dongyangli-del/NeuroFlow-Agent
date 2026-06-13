# NeuroFlow Pipeline for Codex

`neuro-orchestrator` is the only default entry point.

Codex skill triggering is opportunistic, so this entry skill must be able to run the workflow even when no specialist skill is automatically loaded. Specialist skills are optional modules, not the workflow backbone.

## Control Loop

1. Classify task type and depth.
2. Choose one pipeline chain.
3. Name the primary artifact.
4. Load only the needed first reads.
5. Invoke or emulate optional specialist modules.
6. Apply evidence gates.
7. Produce the requested artifact.
8. Decide whether memory should be updated.

## Pipeline Chains

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
Stop condition:
Memory candidate:
```

## Evidence Gates

- Novelty: inspected literature or marked uncertainty.
- Benchmark: access, license, split, metric, baseline, leakage.
- Experiment: matched protocol, metrics, baselines, ablations, stop rules.
- Reproduction: environment, data, weights, command, expected output, sanity check.
- Closed loop: online/offline boundary, safety, calibration, latency, human-subject constraints.
- Memory: privacy filter and explicit target.
