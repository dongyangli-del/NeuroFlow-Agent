# AI x BCI Validity Checks

Use these checks for EEG, iEEG, fMRI, MEG, LFP, spike, behavioral, cognitive, and closed-loop BCI tasks.

## Data and Split

- Identify subject, session, trial, stimulus, task condition, and repetition structure.
- Prefer subject-wise or session-wise splits when claiming cross-person or cross-session generalization.
- Check whether train and test share repeated stimuli, adjacent windows, augmentations, labels, or target embeddings.

## Signal and Target Alignment

- Confirm channel order, sampling rate, time window, baseline correction, filtering, normalization, and artifact handling.
- Confirm target identity, image/text token mapping, layer choice, timestamp alignment, and trial order.
- Audit output routing so generated files, metrics, and checkpoints are read from the intended run.

## Baseline Fairness

- Use the same data, preprocessing, split, metric, and evaluation code for baselines and proposed methods.
- Reproduce the strongest deterministic baseline before increasing model capacity.
- Report variance or confidence intervals when sample count or subject count is small.

## Interpretation Boundaries

- Separate decoding, reconstruction, representation alignment, causal interpretation, and closed-loop control claims.
- Do not infer neural mechanism from predictive performance alone.
- For online or human-subject claims, state calibration, latency, safety, fatigue, consent, and failure handling.
