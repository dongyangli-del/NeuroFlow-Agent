# Cross-Model Review Gate

Use this gate for final, consequential research decisions where the executor should not self-approve the scientific judgment. Do not turn intermediate drafting or routine debugging into a review loop.

## Core Rule

Separate execution from adjudication:

- **Executor model**: performs retrieval, extraction, coding, experiment planning, reproduction setup, or drafting.
- **Reviewer model**: independently checks the executor output against evidence, protocol, numbers, citations, and missing information.
- **Final gate**: cannot be marked passed by the same model or same uninterrupted reasoning pass that produced the executor output.

If an independent reviewer is required but unavailable, mark `cross_model_review_status: required_but_not_run` and downgrade the final confidence. Do not automatically substitute repeated self-review.

## Required For Final Decisions

Use cross-model review at the final claim-bearing or promotion milestone for:

- claim-to-citation, novelty, or related-work judgments entering a paper or rebuttal;
- experiment, benchmark, split, leakage, metric, or numeric interpretations supporting a public claim;
- L2/L3 reproduction claims or release-facing reproducibility statements;
- acceptance-readiness, research-integrity, public-memory, or workflow-promotion decisions;
- any case where the user or project explicitly requires independent review.

Do not require it for exploratory notes, intermediate drafts, routine code fixes, ordinary experiment debugging, or an unchanged artifact that already passed the same gate. Review once at the consequential milestone; repeat only after a material artifact change or unresolved blocking disagreement.

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
- Return `pass` when no evidence-backed blocker exists; do not manufacture findings to appear adversarial.

## Fail Conditions

The final gate should fail when:

- the reviewer cannot find the cited source span;
- the claim scope exceeds the evidence;
- metric direction, dataset, split, or baseline parity is unresolved for the main claim;
- reproduction is claimed without an L3 run for the target artifact;
- executor and reviewer disagree on a blocking issue and no repair is made.

## Fallback

When only one model is available, use a separate diagnostic pass only if the user requests it or the consequential decision cannot responsibly proceed without another check. Label it `same-model-second-pass`, not true cross-model review; otherwise record `required_but_not_run` and continue with appropriately scoped confidence.
