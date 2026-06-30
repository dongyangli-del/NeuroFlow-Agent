# Claim Ledger

Use this reference when a task needs claim-to-citation mapping, novelty support, related-work grounding, reviewer-facing evidence, or integrity-sensitive paper memory.

## Purpose

A claim ledger is a compact evidence table that prevents paper memory from becoming a bag of unverified summaries. It records the exact claim, the source span, the evidence tier, and the weakest unresolved link.

## Claim Ledger Row

```markdown
Claim ID:
Claim text:
Claim type: novelty | method | dataset | metric | result | limitation | reproduction | safety | interpretation
Scope:
Required evidence:
Supporting source:
Evidence span:
Evidence tier: L0 text-only | L1 source-traced | L2 artifact-checked | L3 reproduced
Support status: supported | partially_supported | contradicted | unresolved
Weakest link:
Citation fit:
Reviewer risk:
Safer wording:
Verification needed:
```

## Evidence Tier Rules

- Use L0 text-only only for claims extracted from the target paper or draft without external verification.
- Use L1 source-traced when the cited paper, appendix, dataset page, repository, or official artifact was inspected.
- Use L2 artifact-checked when code, data, tables, figures, configs, logs, or command paths were inspected locally.
- Use L3 reproduced only when the relevant command or analysis was run under a documented environment and produced expected output.

## Ledger Checks

- Every novelty claim needs closest-prior-work comparison or must be marked unresolved.
- Every empirical gain needs dataset, split, metric, baseline, and metric direction.
- Every cross-subject, cross-session, online, closed-loop, robustness, or generalization claim needs protocol-matched evidence.
- Every citation must fit the task, modality, dataset, metric, and conclusion being claimed.
- Secondary summaries may suggest leads, but they do not upgrade evidence tier without primary-source inspection.

## Default Output

```markdown
Claim ledger:
Unresolved claims:
Citation mismatches:
Protocol mismatches:
Numeric consistency risks:
Safer claim set:
Next verification step:
```
