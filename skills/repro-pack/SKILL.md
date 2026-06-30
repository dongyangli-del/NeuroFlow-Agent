---
name: repro-pack
description: Reproduction packaging skill for AI, neuroscience, BCI, and top-conference papers. Use for building minimal runnable reproduction plans with environment, data, weights, commands, expected outputs, sanity checks, and failure recovery.
---

# Repro-Pack

Use this skill when the user wants to reproduce a paper, repository, benchmark baseline, or experiment pipeline.

## First Reads

- `references/repro-contract.md`: Always read for the reproduction contract.
- `references/observability-levels.md`: Always read for L0/L1/L2/L3 reproduction observability and upgrade paths.
- `references/failure-recovery.md`: Read when setup, data, weights, or commands fail.
- Use `paper-rag-plus` for paper facts and claimed metrics.
- Use `eeg-benchmark-hunter` for dataset access and split verification.
- Use `experiment-copilot` after a smoke run when reproduction becomes an experiment matrix.

## Operating Rules

- Inspect local files before writing commands for a repository.
- Build a minimal runnable path before refactoring or broad automation.
- Record environment, data path, weights, command, expected output, sanity check, and known failure recovery.
- Do not assume unseen scripts, checkpoints, or dataset availability.
- Separate smoke reproduction from full-paper reproduction.
- Separate source-traced setup instructions from outputs actually reproduced locally.
- Assign an observability level before saying what is verified: L0 text-only, L1 source-traced, L2 artifact-checked, or L3 reproduced.
- List missing assets, ambiguous parameters, and deviations from the paper or repository convention.

## Workflow

1. Identify target artifact: paper result, figure, table, baseline, checkpoint, or demo.
2. Inventory repository entry points, configs, environment files, data requirements, and evaluation scripts.
3. Define the minimal smoke run with expected output and failure checks.
4. Define the full reproduction path only after smoke run assumptions are clear.
5. Record missing assets and blocking uncertainties explicitly.

## Required Output

```markdown
Target artifact:
Repository status:
Verification status:
Observability level:
Environment:
Data:
Weights:
Minimal command:
Expected output:
Source evidence:
Sanity checks:
Full reproduction path:
Failure recovery:
Missing evidence:
Missing information:
Deviations from convention:
Next skill:
Memory candidate:
```

## Failure Modes

- Producing a polished script before verifying the minimal path.
- Omitting expected output or sanity checks.
- Confusing demo execution with paper reproduction.
- Ignoring dataset, checkpoint, or license blockers.
- Changing unrelated repository code during reproduction.
