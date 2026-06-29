# Acceptance Readiness

Use this reference for whole-paper or pre-submission audits where the user wants to know whether a paper is ready, rescueable, or should be delayed.

## Readiness Classes

| Class | Meaning | Action |
|---|---|---|
| `submit-ready` | No blocking issue remains; major risks are disclosed or directly supported. | Polish, verify citations, and run final reproducibility checks. |
| `submit-with-risk` | Main claim is mostly supported, but one or more major risks remain. | Narrow claims, add limitations, and prioritize one feasible experiment. |
| `needs-revision-before-submit` | The paper has fixable evidence, analysis, or presentation gaps that will likely affect score. | Repair before submission; do not rely on rebuttal. |
| `delay-or-scope-down` | Main claim needs major new evidence or has structural method/protocol risk. | Delay, redesign, or reframe around a weaker supported contribution. |

## Acceptance Gate

Check in this order:

1. **Main claim**: exact contribution and supported setting.
2. **Closest prior work**: verified closest comparison and novelty boundary.
3. **Evidence sufficiency**: baselines, splits, metrics, ablations, uncertainty, and error analysis.
4. **Neuro/BCI validity**: modality, preprocessing, leakage, subject/session split, online/offline boundary, human-subject constraints.
5. **Reproducibility**: code path, data access, environment, seeds, checkpoints, expected outputs.
6. **Narrative clarity**: figures/tables/captions map cleanly to claims.
7. **Ethics and privacy**: consent, data governance, and deployment boundary.

## Decision Output

```markdown
Acceptance readiness:
Main blocker:
Score risk:
Fatal issues:
Major issues:
Quick revisions:
Feasible extra experiments:
Claims to narrow:
Submit/delay recommendation:
```

Do not classify a paper as submit-ready if the main claim still depends on missing experiments, unverified citations, unfair baselines, leakage-prone splits, or online claims from offline evidence.
