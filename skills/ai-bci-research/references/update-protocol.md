# Update Protocol

Use this protocol whenever the user adds a new paper, repository, dataset, or experiment note.

## Guiding Principle

This repository is a persistent workflow system. Do not add material merely because it exists. Add material when it should change how a future AI x BCI research agent reads context, audits evidence, debugs experiments, writes claims, or responds to reviewers.

## Add a Paper

1. Add an entry to `papers-index.md`.
2. Include title, authors, venue/status, year, core contribution, related repo, datasets, metrics, and caveats.
3. Mark uncertain metadata as "from user" or "needs verification".
4. If the paper changes the user's research trajectory, update `research-profile.md`.

## Add a Repository

1. Add an entry to `repositories.md`.
2. Include URL or local path, paper link, purpose, top-level structure, environment setup, data/checkpoint dependencies, and common tasks.
3. If local, run `scripts/repo_inventory.py <repo_path> --output <summary.md>` and review the result.

## Add Experiment Notes

1. Add stable protocols to `bci-workflows.md`.
2. Keep raw lab notes out of the skill unless the user explicitly wants them embedded.
3. Avoid private participant data, credentials, IRB documents, or unreleased sensitive data in skill files.

## Consolidate Agent Memory

1. Run the five-question compression in `workflows/skill-factory.md`.
2. Turn reusable task sequences into `workflows/*.md`.
3. Turn repeated failure modes into `playbooks/*.md` or `debugging-playbooks.md` entries with symptom, checks, minimal probe, and acceptance criteria.
4. Turn stable inspected results into `experiment-findings.md` entries with date, confirmed facts, interpretation, next action, and caveats.
5. Turn real public demonstrations into `cases/*.md` using the fixed case template.
6. Turn recurring reviewer concerns into `reviewer-objections.md` entries with risk, evidence needed, and response pattern.
7. Turn must-preserve behavior into `evals/evals.json` prompts.
8. Update `docs/WORKFLOWS.md` only when the operating procedure itself changes.

## Memory Candidate Template

Use this block at the end of qualifying sessions:

```markdown
Memory candidate:
- Should enter repo? yes/no
- Target file:
- Minimal patch:
- Risk of leaking private info:
- Suggested eval:
```

Do not add transcript-shaped notes. Public memory must be compact, reusable, and free of sensitive project details.

## Rebuild Compact Index

Run:

```bash
python scripts/update_knowledge_index.py --root .
```

This writes `references/knowledge-index.md`, a compact overview of current reference files.
