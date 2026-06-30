# Research Integrity Forensics

Use this shared gate when a task could turn research artifacts into paper claims, reviewer judgments, result tables, or reproduction evidence.

## Core Principle

Treat integrity review as evidence forensics, not style detection. Do not judge a paper, draft, or result by whether it "sounds AI-generated." Judge only concrete mismatches between claims, evidence spans, numbers, code, data, citations, and reproduction observability.

## Finding Schema

For each integrity concern, record:

```markdown
Pattern:
Affected claim:
Evidence span:
Observed mismatch:
Observability level:
Severity: blocking | major | minor
False-positive caveat:
Best repair:
Verification needed:
```

## Observability Levels

| Level | Meaning | Safe conclusion |
|---|---|---|
| L0 text-only | Only the paper text, abstract, PDF, or draft is visible. | Flag inconsistencies and missing evidence; do not infer code or data behavior. |
| L1 source-traced | Paper text plus cited source, repository, dataset card, appendix, or author artifact is visible. | Verify whether a claim is supported by inspected external evidence. |
| L2 artifact-checked | Code, data, command, table, figure, or logs were inspected or run locally. | State what was actually checked and what remains unreproduced. |
| L3 reproduced | The relevant command or analysis was run under a documented environment and produced expected output. | Call only the reproduced target verified; do not generalize to the full paper. |

## High-Risk Patterns

- Claim-evidence mismatch: a claim is broader than the inspected evidence span.
- Citation mismatch: a citation supports a different task, modality, dataset, metric, or setting.
- Protocol mismatch: the text claims cross-subject, cross-session, online, or closed-loop capability from incompatible evidence.
- Numeric inconsistency: table, caption, result paragraph, abstract, and claim state different values, ranks, deltas, or metric directions.
- Baseline ambiguity: comparison omits split, tuning budget, data access, checkpoint, or metric parity needed for the claim.
- Reproduction opacity: the paper or repo lacks the command, data, weights, expected output, or sanity check required to verify a result.
- Overreliance on secondary summaries: a blog, social post, or paper list is treated as if it were inspected paper evidence.

## Adjudication Rules

- Anchor every concern to a concrete span, number, citation, table, figure, command, file, or repository path.
- Separate proven mismatch from unresolved missing information.
- Include a false-positive caveat whenever the evidence surface is incomplete.
- Prefer scoped repair: narrow the claim, add the missing source, expose the protocol boundary, or run the required check.
- Do not use writing style, fluency, generic wording, or "AI detector" signals as verdict evidence.
