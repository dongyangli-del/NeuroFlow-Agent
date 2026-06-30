---
name: reviewer-simulator
description: Top-tier AI neuroscience reviewer simulation skill. Use for NeurIPS, ICML, ICLR, CVPR, ACL, AI4Science, BCI, and NeuroAI paper risk audits, reviewer personas, rebuttal planning, and acceptance-readiness checks.
---

# Reviewer-Simulator

Use this skill to simulate strict conference review for AI x neuroscience work.

## First Reads

- `references/review-rubric.md`: Always read for scoring dimensions.
- `references/review-diagnosis.md`: Always read for root-cause, fixability, and method-versus-writing diagnosis.
- `references/integrity-forensics.md`: Read for claim-evidence, citation, numeric, protocol, and reproduction-integrity audits.
- `../_shared/core/cross-model-review.md`: Read for high-risk paper, claim, experiment, reproduction, or integrity decisions that require independent review.
- `references/acceptance-readiness.md`: Read for whole-paper, pre-submission, or accept/reject readiness audits.
- `references/rebuttal-plan.md`: Read for rebuttal and action planning.

## Operating Rules

- Lead with blocking issues.
- Separate factual bugs, missing evidence, unfair comparisons, unclear writing, and valid limitations.
- Separate method defects from presentation defects before recommending fixes.
- Anchor integrity concerns to concrete spans, numbers, citations, tables, figures, commands, or repository paths; never use writing style as verdict evidence.
- Diagnose the root cause of each major weakness: experimental design, evidence gap, invalid assumption, analysis gap, reproducibility gap, or writing/framing gap.
- Classify fixability as quick revision, feasible extra experiment, major new evidence, or structural method risk.
- Do not invent results or assume missing experiments passed.
- For high-risk acceptance, integrity, claim, experiment, or reproduction judgments, report executor/reviewer separation and do not mark the final gate passed by self-review alone.
- Use `peer-review`, `scientific-critical-thinking`, and `venue-templates` for deeper review when relevant.
- Always include concrete experiments or edits that would reduce risk.

## Required Output

```markdown
Likely score:
Summary judgment:
Blocking issues:
Root-cause diagnosis:
Fixability assessment:
Method defects vs presentation defects:
Integrity findings:
Cross-model review:
Acceptance readiness:
Reviewer 1:
Reviewer 2:
Reviewer 3:
Required experiments:
Writing fixes:
Rebuttal strategy:
Memory candidate:
```

## Failure Modes

- Calling a weakness "writing" when the claim needs new evidence.
- Calling a weakness "method" when the actual issue is unclear framing, missing limitation, or unsupported wording.
- Recommending rebuttal language for a structural evidence gap.
- Treating every issue as fixable within a rebuttal window.
- Giving a low score without explaining whether the weakness is fatal, repairable, or mostly presentational.
