# Table Writing

Use this reference when turning experiment results into LaTeX tables, table captions, or table-centered paper prose.

## Table Preflight

Before writing a table, identify:

```markdown
Table purpose:
Compared methods:
Datasets/protocols:
Metrics:
Metric direction:
Variance or confidence intervals:
Comparable rows:
Best-value rule:
Caption claim:
Missing caveats:
```

Expose missing information when it affects interpretation. Do not fill missing variance, seeds, splits, or metric direction by guessing.

## LaTeX Table Rules

- Prefer `booktabs` style with `\toprule`, `\midrule`, and `\bottomrule`.
- Keep method, dataset, metric, and split names exactly as supplied.
- Include metric direction markers such as `Acc. (\uparrow)` or `MAE (\downarrow)` when direction is known.
- Use consistent numeric precision within a metric column.
- Right-align numeric columns when the surrounding paper style supports it; otherwise keep simple `c` columns.
- Bold the best comparable value only when all rows share the same dataset, split, metric, and evaluation protocol.
- Mark second-best values only if the paper already uses that convention or the user asks.
- Never compare rows across different protocols without a visible separator or note.
- Put missing values as `--` only when the user supplied them as missing.
- Do not invent standard deviations, confidence intervals, p-values, or significance markers.

## Caption Rule

A table caption should contain:

```markdown
What is compared:
Dataset/protocol:
Metric and direction:
Main takeaway:
Critical caveat:
```

The main takeaway must be no stronger than the supplied numbers. If no variance is available, avoid "significant" and prefer "higher in this table" or "shows a higher reported value".

## Evidence Boundary

| Situation | Safe wording |
|---|---|
| Single split or no variance | "reports higher accuracy" rather than "significantly outperforms". |
| Within-subject only | Do not claim cross-subject generalization. |
| Different datasets | Compare within each dataset block, not globally. |
| Missing baseline implementation details | Mark baseline parity as unresolved. |
| Small gain without uncertainty | State the exact margin and note that variance is needed. |
| Efficiency metric absent | Do not claim speed, parameter efficiency, or deployability. |

## Default Output

When asked to write or revise a result table, produce:

```markdown
Table intent:
LaTeX table:
Caption:
Table notes:
Evidence boundary:
```

Keep notes short. If the user requested only the LaTeX table, include the notes as LaTeX comments or a compact postscript, depending on the target surface.
