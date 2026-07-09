# Skill Physics Gate

Use this gate before adding, promoting, or broadening NeuroFlow skills.

This rule is inspired by Evolvent's skill-routing analysis, which argues that larger skill libraries can become less reliable when semantically similar skills compete in the same routing pool.

## Core Rule

Do not add a new top-level skill just because a new capability is useful. Prefer references, shared core gates, evals, docs, or runtime checks unless the behavior has a distinct trigger, first-read set, output contract, failure mode, and eval.

## Required Checks

Before adding or broadening a skill:

1. Identify the nearest competing skills.
2. Define `anchors.verbs`, `anchors.objects`, and `anchors.constraints`.
3. Add explicit `do_not_use_when` boundaries.
4. State which skill should win when two skills look plausible.
5. Keep broad intent disambiguation inside `neuro-orchestrator`, not in a competing specialist skill.
6. Re-inject the original user intent at each deep handoff so the middle of the pipeline does not drift.
7. Run `make skill-competition`.

For a proposed new skill, run:

```bash
make skill-simulate CANDIDATE=path/to/manifest.yaml
```

Do not promote the skill when the simulation shows high competition with an existing specialist unless the new skill has a sharper boundary and a distinct output contract.

## Anti-Patterns

- Adding another writing, review, paper, experiment, or memory skill that overlaps an existing specialist.
- Letting `oral-writer`, `reviewer-simulator`, `paper-rag-plus`, or `experiment-copilot` all compete for the same paper-facing request.
- Using a specialist as a general "research assistant" when `neuro-orchestrator` should route the task.
- Calling every optional module in a deep workflow instead of using sequential handoffs with concrete artifacts.

## Promotion Rule

Keep behavior as a reference workflow until it has:

- distinct natural triggers;
- explicit anchors;
- a unique check order;
- a clear primary artifact;
- explicit counterexamples;
- at least one eval that would fail if the behavior were routed incorrectly.
