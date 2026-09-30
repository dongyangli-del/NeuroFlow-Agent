# Controls and Ablations

## Required Controls

- Random or shuffled target control.
- Subject/session/stimulus leakage audit.
- Baseline with identical train/test protocol.
- Metric replay using known baseline predictions when evaluator parity is uncertain.
- Zero-condition or shuffled-condition ablation for conditional models.

## Common Ablations

- Modality ablation.
- Feature layer or token ablation.
- Subject-specific versus cross-subject.
- Preprocessing and normalization ablation.
- Model size versus data scale.
- Deterministic versus stochastic decoding or generation.

## Acceptance Criteria

An ablation is useful only if it changes the interpretation of the claim, rules out a failure mode, or answers a likely reviewer objection.
