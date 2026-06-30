# Cross-Model Review Gate

Use this gate for high-risk research tasks where the executor should not self-approve the final scientific judgment.

## Core Rule

Separate execution from adjudication:

- **Executor model**: performs retrieval, extraction, coding, experiment planning, reproduction setup, or drafting.
- **Reviewer model**: independently checks the executor output against evidence, protocol, numbers, citations, and missing information.
- **Final gate**: cannot be marked passed by the same model or same uninterrupted reasoning pass that produced the executor output.

If no independent reviewer model or second-pass reviewer is available, mark `cross_model_review_status: required_but_not_run` and downgrade the final confidence.

## Required For

Use cross-model review by default for:

- claim-to-citation mapping;
- novelty or related-work positioning;
- citation-critical paper facts;
- experiment plans that support paper-facing claims;
- benchmark, split, leakage, baseline, or metric audits;
- reproduction claims and observability upgrades;
- numeric result interpretation;
- reviewer-risk, integrity, or acceptance-readiness decisions;
- any artifact that could enter a paper, rebuttal, release note, or public knowledge base.

## Review Contract

```markdown
Executor:
Reviewer:
Artifacts reviewed:
Evidence checked:
Disagreements:
Required fixes:
Final gate: pass | pass_with_caveats | fail | required_but_not_run
Confidence after review:
```

## Reviewer Duties

- Check source spans, citation fit, and unresolved fields.
- Check dataset, split, metric, baseline, leakage, and protocol boundaries.
- Check numeric consistency across tables, captions, paragraphs, abstracts, and conclusions.
- Check reproduction observability: L0 text-only, L1 source-traced, L2 artifact-checked, or L3 reproduced.
- Look for claim inflation, citation laundering, protocol inflation, and missing negative controls.
- Record disagreements instead of silently rewriting the executor output.

## Fail Conditions

The final gate should fail when:

- the reviewer cannot find the cited source span;
- the claim scope exceeds the evidence;
- metric direction, dataset, split, or baseline parity is unresolved for the main claim;
- reproduction is claimed without an L3 run for the target artifact;
- executor and reviewer disagree on a blocking issue and no repair is made.

## Fallback

When only one model is available, simulate independence with a separate adversarial review pass after clearing local context as much as possible. Label it `same-model-second-pass`, not true cross-model review.
