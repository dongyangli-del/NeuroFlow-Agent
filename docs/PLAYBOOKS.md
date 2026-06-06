# Playbook Catalog

Detailed playbooks live inside `skills/ai-bci-research/references/`. This catalog explains when to load each one.

## Experiment Debugging

Read `references/debugging-playbooks.md` when metrics collapse, generated EEG has the wrong scale, a generative model badly underperforms a deterministic baseline, or run outputs appear in the wrong directory.

Current playbooks include:

- EEG diffusion prediction underperforms regression.
- Experiment output directory routing bug.
- EEG diffusion versus linear baseline large gap.
- Conditional EEG diffusion objective mismatch.

## Experiment Findings

Read `references/experiment-findings.md` when interpreting completed experiment batches or choosing the next ablation after surprising results. Findings should be compact, dated, and reusable.

## Session Memory Consolidation

Read `references/workflows/skill-factory.md` and `references/playbooks/session-memory-consolidation.md` when a completed session should become durable skill memory. Use this for reusable check orders, first-read rules, non-skippable criteria, demo cases, and eval prompts.

## BCI Workflow Guardrails

Read `references/bci-workflows.md` when designing or auditing neural decoding, reconstruction, alignment, or closed-loop BCI experiments.

## Paper and Rebuttal

Read `references/writing-style.md`, `references/reviewer-objections.md`, and `references/venue-workflows.md` for submission-facing writing, reviews, rebuttals, and claim-risk audits.
