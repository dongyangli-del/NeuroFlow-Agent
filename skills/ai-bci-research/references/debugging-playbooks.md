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

## Experiment Output Directory Routing Bug

Use this when a shell wrapper, multi-GPU launcher, or benchmark script is intended to write to a new experiment directory but outputs appear in an old directory. This is especially dangerous when rerunning fixed experiments because it can silently contaminate old results.

### Failure Pattern

- The wrapper sets `OUTPUT_DIR=outputs/eeg_diffusion_fixed` or another fixed root.
- The variable is used for skip checks, status summaries, or log discovery.
- The variable is not passed to train, sample, or evaluate commands, so child scripts use their own default output path.
- New fixed runs write into stale output directories and make old-vs-new comparisons invalid.

### Required Checks

1. Stop the current parent script and any orphaned child training, sampling, evaluation, or DataLoader processes before more files are written.
2. Inspect the actual command lines for train, sample, and evaluate. Confirm `--output_dir`, `--output-root`, or equivalent is passed to every stage.
3. Check that skip logic, summary logic, logs, checkpoints, predictions, and metrics all refer to the same resolved run directory.
4. Print the resolved output path at the start of every stage and write it into the config or metadata file.
5. Compare file modification times in old and new output directories to detect contamination.

### Timestamped Run Directory Pattern

Prefer immutable run directories under a semantic experiment root:

```bash
RUN_ID="run_$(TZ=Asia/Shanghai date +%Y%m%d_%H%M%S)"
OUTPUT_DIR="outputs/eeg_diffusion_fixed/${RUN_ID}"
```

Use UTC only when the whole project standardizes on UTC. For this project, use East 8 / `Asia/Shanghai` timestamps when the user requests local experiment comparison by date.

### Minimal Fix Pattern

- Define one resolved `OUTPUT_DIR` once in the top-level launcher.
- Pass that same directory explicitly to train, sample, and evaluate.
- Use the same path for skip checks and summaries.
- Store the command, git commit, timestamp, timezone, dataset split, checkpoint path, and metric output path inside the run directory.
- Never reuse a fixed output directory for a corrected run unless it is intentionally overwritten after archiving or deleting stale artifacts.
