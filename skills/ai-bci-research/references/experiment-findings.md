# Experiment Findings

Use this file for compact, reusable conclusions from completed experiment batches. Keep raw logs in the experiment workspace; store only the result snapshot, confirmed facts, interpretation, and next diagnostic actions here.

## EEG Diffusion ViT Feature Benchmark Snapshot - 2026-06-03

### Result Snapshot

Five ViT-conditioned EEG diffusion experiments have completed. `dino_vit_b_16` full is still training, and the `dino2_vit_b_14` queue has not started yet.

| Model | Mode | Layer | Mean Corr | Peak Corr | Peak Time | EV | Best Val | Best Epoch |
|---|---|---|---:|---:|---:|---:|---:|---:|
| vit_b_32 | full | full_layers | 0.041141 | 0.137229 | 100 ms | -6.964 | 0.256963 | 126 |
| dino_vit_b_16 | single | blocks.11 | 0.036239 | 0.137408 | 110 ms | -7.086 | 0.246317 | 276 |
| openclip_vit_b_32 | full | full_layers | 0.007615 | 0.047337 | 110 ms | -7.498 | 0.257021 | 126 |
| openclip_vit_b_32 | single | visual.transformer.resblocks.11 | 0.003743 | 0.047100 | 110 ms | -6.327 | 0.248315 | 209 |
| vit_b_32 | single | encoder.layer.11 | -0.005148 | 0.028670 | 350 ms | -6.418 | 0.248537 | 209 |

Unified noise ceiling:

- Lower: `0.374877`
- Upper: `0.825916`

### Current Interpretation

Current evidence supports a task/objective and calibration mismatch plus weak condition utilization, rather than a simple evaluation error or a broad conclusion that diffusion is inherently weaker than regression. The gap is too large to attribute to model capacity alone; treat it as an implementation and protocol diagnosis until the checks below are complete.

Confirmed facts:

- Diffusion evaluation is intended to match the linear encoding protocol: test repetition split-half, 60--500 ms window, synthetic prediction versus half-1 EEG, and lower/upper noise ceiling.
- The MindPilot linear baseline uses `time_mode=all`, so it also predicts the full `17 x 100` EEG target jointly. The gap is not explained by linear regression predicting one time point at a time.
- After the EEG scale fix, diffusion outputs no longer explode to std around `16`, but the test-window std remains high: biological averaged EEG std is about `0.288`, diffusion std is about `0.45--0.47`, and linear ViT prediction std is about `0.273--0.276`.
- Linear ViT mean correlation is about `0.27--0.29`; current diffusion best mean correlation is about `0.041`. This gap requires auditing implementation, objective, condition usage, and sampling protocol before scientific interpretation.

### Required Diagnostics

1. Evaluation sanity check: run the diffusion evaluator on MindPilot linear `synthetic_eeg_test.npy` and confirm it reproduces the linear CSV mean/peak correlations. If it fails, repair evaluation before changing models.
2. Distribution check: compare mean/std/min/max, per-channel std, and per-time std for biological averaged EEG, linear predictions, and diffusion predictions in the same test window.
3. Sampling variance check: fix condition and sample multiple noise seeds; estimate sample variance. If noise-seed variance dominates condition variance, stochastic DDPM sampling is not aligned with correlation-style evaluation.
4. Deterministic prediction check: evaluate `pred_x0`, DDIM deterministic sampling, posterior mean, or conditional mean over multiple samples.
5. Condition-use check: compare real condition, shuffled condition, and zero condition. If correlations are similar, image-feature cross attention is not being used effectively.
6. Condition-vs-noise check: under the same noise, compare outputs for different image conditions; under the same condition, compare outputs for different noise seeds.
7. Train/val/test localization: evaluate sampled predictions on train, val, and test splits. Low train correlation indicates underfit, objective mismatch, or broken conditioning; high train but low test indicates overfit or split generalization failure.
8. Feature alignment check: verify feature filenames, CLS/patch token layout, image IDs, condition indices, and EEG target ordering.

### Model and Training Fix Candidates

Prioritize small discriminative probes before full reruns:

- Train an `x0` or direct EEG target variant using the same condition encoder. If this improves sharply, the architecture can learn image-to-EEG and the epsilon DDPM objective is the main mismatch.
- Add a deterministic mean predictor `f(image) -> EEG`; use diffusion only for residual modeling. Evaluate the mean prediction or residual expectation by default.
- Add optional feature standardization and a PCA-1000 condition version to match the linear baseline while preserving the no-PCA token version as the main idea.
- Ablate condition injection: cls-only, patch-only, cls+patch, full-layer tokens. Keep EEG tokens as queries and image tokens as keys/values unless a focused ablation shows the design is broken.
- Verify that full-layer first tokens are true CLS tokens for each saved ViT format. If a feature format lacks CLS, derive token roles from metadata or explicit shape rules.

### Acceptance Criteria

- The diffusion evaluator reproduces linear prediction metrics within `1e-6` or explains any split-half stochastic difference precisely.
- Real condition beats shuffled and zero condition clearly. Otherwise mark condition injection as failed.
- Train, val, and test correlations are all reported so underfit, overfit, sampling noise, and test generalization can be separated.
- At least one corrected variant has generated std close to biological averaged EEG or linear prediction, mean explained variance no longer strongly negative, and ViT mean correlation clearly above the current `0.04` scale.
- Final report includes linear baseline, current DDPM, x0/direct variant, and shuffled/zero ablations.


## EEG Diffusion Objective Diagnosis Update - 2026-06-03

### Added Diagnostics

New probes were added to `exps/diagnose_eeg_diffusion.py` for train/validation split evaluation, denoiser condition sensitivity, and timestep-specific condition loss profiles. These probes separate evaluator bugs, split generalization, sampling variance, and objective-level condition neglect.

### Key Results

For `vit_b_32` single-layer diffusion, deterministic sampling improves over stochastic DDPM but remains far below the linear baseline:

| Split | Sampling | Mean Corr | Peak Corr | EV | Pred Std | Target Std |
|---|---|---:|---:|---:|---:|---:|
| train | DDPM | 0.0052 | 0.0611 | -0.7701 | 0.4531 | 0.4802 |
| train | deterministic | 0.1690 | 0.2444 | 0.0188 | 0.2667 | 0.4802 |
| val | DDPM | 0.0162 | 0.0873 | -0.7468 | 0.4610 | 0.4970 |
| val | deterministic | 0.0674 | 0.1793 | 0.0057 | 0.2664 | 0.4970 |

Denoiser sensitivity shows weak image-specific conditioning: real versus shuffled condition changes output by only about `0.9%--2.3%` of output magnitude across timesteps, while real versus zero condition changes output more (`6%--26%`). This suggests the model reacts to the condition-token distribution but weakly distinguishes the specific image.

Timestep loss profiles show near-identical MSE for real and shuffled conditions. Shuffle relative deltas stay below about `0.3%`, while zero-condition deltas are much larger at many timesteps. This supports the hypothesis that epsilon DDPM training can solve much of the denoising objective from `x_t` and timestep, with little pressure to learn `image -> EEG`.

### Updated Interpretation

The performance gap is now more likely an objective/sampler mismatch than an evaluation-protocol error. Single stochastic DDPM samples are poorly aligned with EEG encoding metrics that reward the conditional mean. Deterministic posterior-mean sampling helps, but low train correlation means the learned denoiser still does not strongly learn the image-conditioned EEG mapping.

### Next Required Runs

1. Train/evaluate `prediction_type=x0` with the same split, feature tokens, architecture scale, and evaluator.
2. Train/evaluate the direct deterministic mean predictor already present in `exps/train_direct_eeg_predictor.py` and `exps/sample_direct_eeg_predictor.py`.
3. Report epsilon DDPM, deterministic epsilon posterior mean, `x0`, direct mean predictor, linear baseline, and real/shuffle/zero ablations in one table.
4. If direct mean succeeds but `x0` remains weak, inspect denoiser architecture and condition injection. If direct mean also fails, inspect feature standardization, token layout, split alignment, and optimizer/training scale.
5. Treat diffusion as residual or uncertainty modeling only after the deterministic conditional mean path is competitive.

### Assumptions and Bookkeeping

- Do not use the old `outputs/eeg_diffusion` directory for conclusions because it was contaminated by output-routing bugs.
- Main diagnostic runs should use `outputs/eeg_diffusion_fixed/run_20260603_021316` and later East 8 timestamped runs.
- Keep validation split separate; do not merge val into training until diagnosis is complete.
- Prefer non-destructive diagnostics and small ablations before rerunning every ViT feature family.
