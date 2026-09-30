# Source Traceability

Use this whenever a workflow depends on paper facts, dataset facts, numerical parameters, benchmark protocols, preprocessing choices, model checkpoints, or reviewer-facing claims.

## Traceable Fact Contract

```markdown
Fact or parameter:
Value:
Source:
Source location:
Verification status:
Missing or ambiguous:
Decision impact:
```

## Verification Status

Use the narrowest truthful status:

| Status | Meaning |
|---|---|
| `unverified` | Mentioned by the user or retrieved from memory, but not checked. |
| `source-traced` | Linked to an inspected paper, repository file, dataset page, config, or log. |
| `reproduced` | Confirmed by running code, checking outputs, or reproducing a metric/path. |
| `user-validated` | Confirmed by the user from private data, logs, or unpublished context. |
| `expert-reviewed` | Checked by a domain expert or stable project owner judgment. |

Do not upgrade status by inference. If a paper says a dataset was used but does not specify the split, the dataset use may be source-traced while the split remains unverified.

## Missing Information

Always list missing information when it affects a decision:

- dataset access, license, or human-subject restriction;
- subject/session/stimulus split;
- preprocessing, filter, normalization, time window, or sampling rate;
- target representation, checkpoint, layer, prompt, or embedding source;
- metric definition, evaluator code, or baseline protocol;
- random seed, variance, confidence interval, or statistical test;
- expected output, model weights, data path, or command.

## Deviations From Convention

Flag choices that are valid only under a narrowed claim:

- stimulus-wise split used for a cross-subject or cross-session claim;
- reconstruction metrics reported without baseline/evaluator parity;
- qualitative figures used to imply quantitative superiority;
- online or closed-loop language used for offline replay experiments;
- benchmark comparison across incompatible preprocessing, targets, or splits.
