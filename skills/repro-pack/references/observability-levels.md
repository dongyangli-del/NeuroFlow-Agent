# Reproduction Observability Levels

Use this reference when building a reproduction plan, smoke test, repo audit, baseline reproduction, or paper artifact checklist.

## Levels

| Level | Name | Requirement | What can be claimed |
|---|---|---|---|
| L0 | Text-only | Paper, README, abstract, or draft was read. | A claimed path exists in text, but artifact behavior is unverified. |
| L1 | Source-traced | Linked repository, dataset card, appendix, release page, or official artifact was inspected. | The source exposes or omits required reproduction assets. |
| L2 | Artifact-checked | Environment files, configs, scripts, data paths, checkpoints, outputs, or logs were inspected locally. | The artifact contains a plausible runnable path or a concrete blocker. |
| L3 | Reproduced | A documented command was run and produced expected output under a recorded environment. | The target run, figure, table, or sanity check was reproduced. |

## Contract Additions

Every reproduction contract should include:

```markdown
Observability level:
Observed artifacts:
Unobserved surfaces:
Claim allowed at this level:
Upgrade path:
```

## Upgrade Rules

- L0 -> L1: inspect the official source, repository, dataset page, appendix, or author artifact.
- L1 -> L2: inspect local files, configs, commands, data requirements, checkpoint names, and expected outputs.
- L2 -> L3: run the minimal documented command and record environment, inputs, output, and sanity checks.

## Failure Labels

- `missing-command`: no runnable command for the target artifact.
- `missing-data`: required dataset is unavailable, ambiguous, or license-blocked.
- `missing-weights`: checkpoint is required but unavailable.
- `ambiguous-config`: hyperparameters, split, seed, or model variant cannot be identified.
- `missing-expected-output`: command exists but expected file, metric, or visual output is not defined.
- `protocol-mismatch`: runnable artifact does not match the paper claim, split, metric, or baseline setting.

Do not call a repository "reproduced" unless it reaches L3 for the target artifact.
