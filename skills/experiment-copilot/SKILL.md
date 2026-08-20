---
name: experiment-copilot
description: AI neuroscience experiment matrix and ablation design skill. Use for turning claims into must-run experiments, ablations, controls, robustness checks, statistical plans, stop rules, and reviewer-ready evidence chains.
---

# Experiment-Copilot

Use this skill when a research claim needs an executable experiment plan.

## First Reads

- `../_shared/core/proportional-execution.md`: Always read first to keep experiments and review gates tied to live uncertainties in the claim.
- `references/experiment-matrix.md`: Always read for matrix structure.
- `references/controls-and-ablations.md`: Read for baselines, controls, and ablation design.
- `references/statistics-and-stop-rules.md`: Read when results need confidence intervals, significance tests, or stop criteria.

## Operating Rules

- Define the claim before experiments.
- Separate must-run, should-run, and nice-to-have experiments.
- Match evaluation protocol across baseline and proposed method.
- Check leakage, normalization, checkpoint selection, metric definitions, and split protocol.
- Trace key parameters, metrics, baselines, and dataset choices to a paper, config, log, dataset page, or user-validated source.
- List missing information and deviations from convention before paper-facing interpretation.
- For a final paper-facing experiment plan, use one cross-model review at the consequential milestone: the reviewer checks baseline parity, leakage, split protocol, metrics, statistics, and claim scope.
- Use `statistical-analysis`, `ablation-planner`, and `experiment-results-notebook` when deeper analysis is needed.

## Required Output

```markdown
Claim:
Verification status:
Minimum viable experiment:
Main table:
Ablation matrix:
Negative controls:
Robustness checks:
Statistics:
Source evidence:
Cross-model review:
Missing information:
Deviations from convention:
Expected failure patterns:
Stop rule:
Reviewer-facing interpretation:
Memory candidate:
```
