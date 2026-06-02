# Debugging Playbooks

Use these playbooks when an AI x BCI experiment behaves suspiciously. Treat surprising results as possible code or protocol bugs until scale, alignment, sampling, checkpointing, and metrics have been checked.

## EEG Diffusion Prediction Underperforms Regression

Use this when a diffusion or generative model conditioned on image, text, CLIP, ViT, or multimodal features predicts EEG much worse than a deterministic regression baseline.

### Failure Pattern

- Regression predicts EEG directly in the original EEG scale and gives reasonable metrics.
- Diffusion is trained/evaluated against original-scale EEG, but generated EEG has implausible mean, standard deviation, or range.
- Example: true repetition-averaged test EEG has std around `0.27`, while generated EEG has std around `16`.
- DDPM epsilon loss may look low even though reverse sampling produces meaningless EEG.

### Primary Root Cause to Check

DDPM epsilon prediction assumes a normalized data space compatible with the standard Gaussian forward noising process. If EEG targets are small-scale, unstandardized, or inconsistently normalized, the model can learn an apparently easy denoising target while the reverse chain fails in the original EEG scale. This is a training/sampling protocol bug, not evidence that generative modeling is inherently worse than regression.

### Required Checks

1. Stop GPU jobs before launching more runs.
2. Print true train EEG, true validation/test EEG, regression output, and diffusion output statistics: mean, std, min, max, and per-channel std.
3. Verify whether EEG is standardized before diffusion training. Estimate mean/std on train indices only.
4. Save EEG normalization statistics in the checkpoint or config.
5. During sampling, generate in normalized EEG space and inverse-transform back to original EEG units before evaluation.
6. Clip or constrain predicted normalized `x0` during DDPM reverse sampling to prevent chain divergence.
7. Confirm feature-to-EEG alignment: image feature filenames, image IDs, condition indices, trial order, and test split order must match exactly.
8. Compare deterministic regression evaluation with stochastic DDPM evaluation fairly. If the metric expects a conditional mean, test multiple diffusion samples per condition and average.
9. Check beta schedule, number of sampling steps, EMA/non-EMA checkpoint choice, objective type, and train/sample config consistency.
10. Interpret metrics carefully: correlation may partly survive scale mismatch, but explained variance and MSE can collapse or become extremely negative under generated-scale explosion.

### Minimal Fix Pattern

- Compute `eeg_mean` and `eeg_std` on training EEG only.
- Train diffusion on `(eeg - eeg_mean) / eeg_std`.
- Validate loss in normalized space, but evaluate final predictions after inverse transform.
- Store `eeg_mean`, `eeg_std`, and normalization metadata in every checkpoint.
- In DDPM sampling, clip predicted normalized `x0` before computing the posterior mean.

### Reviewer-Facing Interpretation

Do not frame this failure as a model-class limitation until the protocol is fixed. Report it as a scale/normalization and sampling-consistency bug if confirmed. After the fix, rerun the exact same split, image features, metrics, and regression baseline before drawing conclusions about diffusion versus regression.
