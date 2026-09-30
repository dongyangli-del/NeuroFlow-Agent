# Contributing

This repository should stay compact, rigorous, and useful to future AI x BCI research agents. Treat it as a persistent workflow system, not a storage folder for notes.

## Design Principle

Agent behavior is shaped by three components: model, tools, and workflow. This repository customizes the workflow layer for AI x BCI research. Contributions should therefore improve how future agents inspect evidence, replay memory, avoid invalid claims, debug experiments, or consolidate new lessons.

## What Belongs Here

- Concise workflows that change agent behavior.
- Reusable experiment debugging playbooks.
- Dated findings distilled from real inspected experiments.
- Eval prompts that test important behaviors.
- Small scripts that validate or summarize the skill.
- Memory replay and consolidation rules that make future sessions more reliable.

## What Does Not Belong Here

- Raw logs, checkpoints, datasets, generated figures, or private human-subject data.
- Long transcripts that cannot be reused.
- Unverified citations, invented results, or speculative claims written as facts.
- Generic neuroscience notes that do not improve agent behavior.
- Personal paper maps, unpublished experiment findings, private repository notes, and lab-specific strategy. Keep them in `.private/` or a private branch.

## Change Checklist

1. Keep `SKILL.md` concise; put detailed material in `references/` or `docs/`.
2. If adding a new workflow, add a short routing note in `SKILL.md` only when needed.
3. If adding a reusable finding, include date, confirmed facts, interpretation, next action, and acceptance criteria.
4. Rebuild the knowledge index when references change.
5. Run `make validate`.
6. Review the diff for accidental mode changes, generated files, and private data.
7. For public-facing changes, check [docs/PUBLIC_READY.md](docs/PUBLIC_READY.md).

## Memory Consolidation Checklist

Before adding new content, ask whether it will change a future agent's behavior. If yes, place it in the smallest useful home:

- durable mission or scope change -> `research-profile.md`;
- repeated debugging pattern -> `debugging-playbooks.md`;
- inspected experiment result -> `experiment-findings.md`;
- claim or reviewer risk -> `reviewer-objections.md`;
- reproducibility or setup fact -> `repositories.md`;
- expected behavior regression test -> `evals/evals.json`.

If the content is only raw context, keep it outside this repository and summarize the reusable lesson.

## Demo Case Rules

Demo cases should be based on real inspected artifacts or user-approved summaries. If a demo is not ready, leave a template or planned slot rather than inventing one.
