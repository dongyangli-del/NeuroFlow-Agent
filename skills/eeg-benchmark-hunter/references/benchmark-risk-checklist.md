# Benchmark Risk Checklist

## Access and Governance

- Is the data public, gated, application-only, or unavailable?
- Does the license allow redistribution, commercial use, derivative datasets, or model release?
- Are there human-subject, IRB, consent, or privacy constraints?
- Are raw data, preprocessed data, labels, stimuli, and metadata all available?

## Protocol Validity

- Is the official split subject-wise, session-wise, trial-wise, or stimulus-wise?
- Can repeated stimuli leak between train and test?
- Are validation and test sets used for model selection?
- Are preprocessing and target extraction identical across baselines?

## Adaptation Difficulty

- File format and loader complexity.
- Missing stimuli, labels, channels, sampling rates, or event markers.
- Compute and storage requirements.
- Need for anatomical, language, image, audio, or behavioral alignment.

## Reviewer Risks

- Benchmark too small for broad claims.
- Split protocol too easy for generalization claims.
- Qualitative reconstruction without retrieval, classification, or semantic metrics.
- No deterministic baseline.
- Cross-paper numbers not comparable.

## Benchmark Substance Gate

A neural, behavioral, or BCI benchmark should define what capability boundary it measures. Check:

- Evaluation gap: which existing benchmark or protocol cannot diagnose the target failure?
- Construction path: how are stimuli, tasks, labels, neural signals, behavioral traces, or annotations produced?
- Quality control: how are ambiguity, artifacts, noisy labels, leakage, and preprocessing errors detected?
- Evaluation taxonomy: what dimensions, difficulty tiers, error types, cognitive conditions, or neural conditions are reported?
- Baseline suite: which deterministic, neural, behavioral, and model-family baselines make the benchmark interpretable?
- Empirical findings: what actionable capability boundary should future work learn from the benchmark?
- Governance: what access, license, privacy, human-subject, consent, and redistribution constraints apply?
