# Public-Ready Checklist

Use this checklist before making NeuroFlow Agent public.

## Required Gate

- `make validate` passes.
- README links and badges point to public-safe destinations.
- No raw logs, checkpoints, datasets, generated experiment outputs, credentials, or human-subject material are committed.
- Personal paper maps, unpublished experiment findings, private repository notes, and lab-specific strategy live in `.private/` or another non-public branch.
- Public `references/` files contain reusable workflows, templates, guardrails, and approved examples only.

## Private Memory Policy

Local private memory can live under:

```text
.private/
skills/ai-bci-research/references/private/
```

Both paths are gitignored. Keep these files out of public commits:

- unpublished numeric results;
- private run directories or machine paths;
- paper/rebuttal strategy before public release;
- private repository structure or setup notes;
- participant-level details, IRB material, raw EEG traces, and consent-related records.

When a private lesson is broadly useful, distill only the public-safe procedure into a workflow, playbook, template, or eval prompt.

## Recommended Public Launch Gate

- 3 real public-safe case studies.
- 5 behavior eval prompts.
- One validated install path.
- One privacy/leakage scan through `make validate`.
- A clear contribution rule: every contribution must change future agent behavior.
