# Contributing

This repository should stay compact, rigorous, and useful to future AI x BCI research agents.

## What Belongs Here

- Concise workflows that change agent behavior.
- Reusable experiment debugging playbooks.
- Dated findings distilled from real inspected experiments.
- Eval prompts that test important behaviors.
- Small scripts that validate or summarize the skill.

## What Does Not Belong Here

- Raw logs, checkpoints, datasets, generated figures, or private human-subject data.
- Long transcripts that cannot be reused.
- Unverified citations, invented results, or speculative claims written as facts.
- Generic neuroscience notes that do not improve agent behavior.

## Change Checklist

1. Keep `SKILL.md` concise; put detailed material in `references/` or `docs/`.
2. If adding a new workflow, add a short routing note in `SKILL.md` only when needed.
3. If adding a reusable finding, include date, confirmed facts, interpretation, next action, and acceptance criteria.
4. Rebuild the knowledge index when references change.
5. Run `make validate`.
6. Review the diff for accidental mode changes, generated files, and private data.

## Demo Case Rules

Demo cases should be based on real inspected artifacts or user-approved summaries. If a demo is not ready, leave a template or planned slot rather than inventing one.
