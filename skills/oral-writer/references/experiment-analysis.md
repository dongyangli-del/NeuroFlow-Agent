# Experiment Analysis

Use this reference when experiment results should become paper prose, result-section analysis, or a table/figure-centered takeaway.

## Analysis Preflight

Before writing, identify:

```markdown
Result role: main result | ablation | robustness | efficiency | error analysis | limitation
Compared methods:
Dataset/protocol:
Metric and direction:
Uncertainty: standard deviation | confidence interval | seed sweep | missing
Largest supported contrast:
Smallest meaningful contrast:
Claim boundary:
Missing evidence:
```

Do not infer uncertainty, significance, cross-subject generalization, or deployment readiness from a single table unless the input provides evidence.

## Result Roles

| Role | Safe analysis focus | Required caveat |
|---|---|---|
| `main-result` | The primary comparison under the paper's stated protocol. | Name dataset, split, metric direction, and strongest baseline. |
| `ablation` | Which component changes the metric and by how much. | Do not claim mechanism unless the ablation isolates it. |
| `robustness` | Stability across seeds, subjects, sessions, perturbations, or domains. | Require variance or repeated conditions. |
| `efficiency` | Runtime, parameters, memory, calibration time, or latency. | Do not claim deployability without the relevant resource metric. |
| `error-analysis` | Failure cases, subgroup behavior, or qualitative examples. | Do not let examples replace quantitative evidence. |
| `limitation` | What the current evidence cannot support. | State the boundary without hiding it. |

## BCI/NeuroAI Analysis Gates

- Separate within-subject, cross-subject, cross-session, and cross-dataset claims.
- Report exact margins when gains are small and uncertainty is missing.
- Do not treat reconstruction image quality as proof of neural alignment without a neural or semantic control.
- For decoding, name chance level or baseline parity when available.
- For closed-loop or online claims, require online protocol evidence; offline replay supports only offline claims.
- If subjects, sessions, seeds, or folds are missing, write that as an evidence boundary.

## Default Output

```markdown
Result role:
Supported takeaway:
Paper paragraph:
Evidence boundary:
Missing checks:
Safer claim:
```

The paragraph should be concise and use only supplied values, citations, and protocol details.
