# Integrity Forensics Review

Use this reference when reviewing a draft, claim, table, rebuttal, repository, or submission for research-integrity risk.

## Goal

Find concrete integrity risks that a strict reviewer could verify from the artifact. This is not an AI-text detector and not a tone critique. The target is claim-to-evidence consistency, citation fit, numeric self-consistency, protocol truthfulness, and reproduction observability.

## Review Order

1. Identify the exact claim, result, table, figure, citation, or repo instruction under review.
2. Assign the highest observability level available: L0 text-only, L1 source-traced, L2 artifact-checked, or L3 reproduced.
3. Check whether the evidence span supports the scope of the claim.
4. Check table, caption, result paragraph, abstract, and conclusion for numeric consistency.
5. Check whether modality, dataset, split, metric, baseline, or online/offline setting changed across the paper.
6. Separate proven mismatch from unresolved missing information.
7. Give the smallest repair that removes the reviewer attack surface.

## Integrity Finding Template

```markdown
Integrity finding:
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

## Severity Guide

| Severity | Use when | Typical repair |
|---|---|---|
| blocking | The main claim, novelty claim, primary result, citation, or protocol boundary is unsupported or contradicted. | Add direct evidence, correct the claim, or delay/scope down. |
| major | The claim may survive, but a reviewer can attack comparison fairness, missing evidence, unclear protocol, or unresolved reproducibility. | Add the missing source, table note, command, parity check, or limitation. |
| minor | The issue is local wording, caption ambiguity, citation formatting, or a small consistency problem that does not change the main conclusion. | Patch text and keep the evidence boundary explicit. |

## Pattern Checks

- Claim-evidence mismatch: the written claim is stronger than the available experiment, source, or artifact.
- Citation mismatch: the cited paper supports a different setting, modality, dataset, metric, task, or conclusion.
- Protocol mismatch: offline, within-subject, same-session, or qualitative evidence is used to imply online, cross-subject, cross-session, quantitative, or closed-loop capability.
- Numeric inconsistency: values, ranks, deltas, metric direction, statistical significance, or best-value marking conflict across text, table, caption, and abstract.
- Reproduction opacity: the paper or repo does not expose the environment, data, weights, command, expected output, or sanity check needed for the stated result.
- Secondary-source inflation: a blog, list, social post, or summary is used as if it were inspected primary evidence.

## Output Rule

Lead with the most severe integrity finding before writing polish. If no concrete mismatch is found, say that the inspected surface did not reveal an integrity issue and list the remaining unobserved surfaces.
