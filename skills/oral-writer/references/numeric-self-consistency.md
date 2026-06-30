# Numeric Self-Consistency

Use this reference when writing or revising Results sections, abstracts, conclusions, tables, captions, figure titles, rebuttals, or claims that contain numbers.

## Goal

Prevent polished paper text from changing the evidence. The writer must preserve supplied numbers and check that values, ranks, deltas, metric direction, protocol boundaries, uncertainty, and statistical claims stay consistent across the artifact.

## Preflight

```markdown
Numbers present:
Metric direction:
Compared methods:
Dataset/split/protocol:
Ranks and best values:
Deltas stated in text:
Variance or confidence intervals:
Statistical test present:
Latency/efficiency values:
Protocol boundary:
```

Expose missing information when it changes interpretation.

## Consistency Checks

- Preserve every supplied number exactly unless the user asks for rounding.
- Do not convert percentages, decimals, deltas, or ranks without showing the conversion.
- Do not mark a best value unless metric direction and comparable rows are clear.
- Do not claim significance without variance, confidence interval, or a supplied statistical test.
- Do not turn within-subject, same-session, offline, or qualitative evidence into cross-subject, cross-session, online, closed-loop, or quantitative claims.
- Check that table values, caption takeaway, result paragraph, abstract, and conclusion state the same ordering and evidence boundary.
- For small gains without uncertainty, state the visible margin and mark uncertainty as missing.

## Numeric Audit Output

```markdown
Numeric self-consistency:
Preserved values:
Computed margins:
Metric direction:
Comparable rows:
Unsupported numeric claims:
Missing uncertainty:
Protocol boundary:
Safe wording:
```

When the user only asks for final prose, keep the audit internal unless a mismatch or missing uncertainty materially affects the wording.
