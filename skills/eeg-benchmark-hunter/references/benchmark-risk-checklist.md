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
