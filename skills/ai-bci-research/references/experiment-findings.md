# Experiment Findings

Use this public file for templates and rules about durable experiment findings. Do not publish raw logs, private run directories, unpublished numeric results, reviewer strategy, or lab-internal interpretations here. Project-specific findings can be kept in a local gitignored private overlay.

## Public Finding Template

```text
## Finding Title - YYYY-MM-DD

### Result Snapshot

- Dataset / split:
- Model family:
- Baselines:
- Metrics:
- Public result summary:

### Confirmed Facts

- Fact 1:
- Fact 2:
- Fact 3:

### Interpretation

State the narrow interpretation supported by the evidence. Avoid over-generalizing from one dataset, subject group, split, or implementation.

### Required Diagnostics

1. Evaluation sanity check:
2. Distribution / calibration check:
3. Train/validation/test localization:
4. Leakage and alignment checks:
5. Baseline parity check:
6. Ablation or negative-control check:

### Acceptance Criteria

- Criterion 1:
- Criterion 2:
- Criterion 3:
```

## Public-Safe Consolidation Rules

- Include only conclusions that are already public, anonymized, or explicitly approved for release.
- Prefer qualitative reusable lessons over unpublished exact metrics.
- Replace local output paths with generic labels such as `run directory` or `experiment workspace`.
- Keep participant-level data, raw EEG traces, IRB material, credentials, checkpoints, and private review strategy outside the repository.
- If a finding is useful but private, store it in the local private overlay and add only the reusable public playbook to `debugging-playbooks.md`.
