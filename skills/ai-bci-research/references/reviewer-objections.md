# Reviewer Objections

Use this file to pre-review drafts, plan missing experiments, or respond to reviews. Lead with blocking issues and evidence gaps before polishing style.

## Common Blocking Concerns

### Leakage or Invalid Splits

Reviewer concern:
"The reported performance may result from leakage across train and test rather than true neural decoding or generalization."

Check:
- Exact stimulus/image overlap across splits.
- Class/category overlap if claiming zero-shot or stimulus-level generalization.
- Subject/session/trial leakage.
- Augmented views of the same trial crossing splits.
- Test-subject statistics used in normalization or model selection.
- Checkpoint or hyperparameter selection on the test set.

Better response:
- State the exact split unit and candidate set.
- Add a split audit table.
- Re-run with stricter stimulus-wise, session-wise, or subject-wise splits if the claim requires it.
- Downgrade the claim if only trial-wise generalization is demonstrated.

### Weak Baselines

Reviewer concern:
"The baselines do not establish that the proposed method is necessary."

Check:
- Chance and random target embedding baselines.
- Linear probe / ridge regression / CCA / simple MLP baselines.
- EEGNet, ShallowFBCSPNet, or other domain-standard neural baselines when applicable.
- Subject-specific versus cross-subject baselines.
- Frozen pretrained encoder versus fine-tuned encoder.
- Ablations with the same backbone and training budget.

Better response:
- Add baseline parity details: same split, same preprocessing, same candidate set, same metric.
- Report variance across subjects/seeds.
- Explain what each baseline tests.

### Unclear Claim Scope

Reviewer concern:
"The paper overclaims beyond the evidence."

Check:
- Does the claim say online when the evidence is offline?
- Does the claim say cross-subject when results are subject-specific?
- Does the claim say semantic understanding when the model predicts embeddings?
- Does the claim imply mind reading from EEG?
- Does the claim invoke AGI, Physical AI, or NeuroAI without a mechanism?

Better response:
- Replace broad claims with the exact demonstrated task.
- Use "neural decoding", "semantic alignment", "stimulus reconstruction", or "brain-signal-guided generation".
- Mark broader implications as future directions.

### Reconstruction Metrics Are Insufficient

Reviewer concern:
"Qualitative reconstructions are cherry-picked or metrics do not match the claim."

Check:
- Retrieval metrics and candidate set size.
- CLIP/ImageNet/semantic similarity versus low-level metrics such as SSIM/LPIPS.
- Human evaluation protocol if used.
- Per-subject and per-category breakdowns.
- Failure cases, not only best examples.

Better response:
- Add a standardized qualitative grid with random or fixed examples.
- Report quantitative metrics for all test samples.
- Separate semantic similarity from perceptual fidelity.

### Closed-Loop Validity

Reviewer concern:
"The closed-loop system is not demonstrated online or may only optimize a proxy."

Check:
- Offline replay versus live human feedback.
- Latency budget and update frequency.
- Calibration protocol and adaptation schedule.
- Random, sham, and fixed-stimulus controls.
- Fatigue, safety, stop criteria, and adverse response handling.
- Objective target: neural state, behavior, or subjective report.

Better response:
- State whether the experiment is live, simulated, replayed, or pilot-scale.
- Include controls and safety constraints.
- Avoid claiming brain modulation unless the outcome measure supports it.

### Missing Reproducibility Details

Reviewer concern:
"The method cannot be reproduced from the paper."

Check:
- Dataset version and access path.
- Subject/session/stimulus counts.
- Preprocessing parameters.
- Model architecture and target embedding source.
- Training hyperparameters, seed, checkpoint selection, and hardware.
- Metric definition and evaluation script.

Better response:
- Add a reproducibility paragraph or appendix table.
- Release config files, scripts, or checkpoints when allowed.
- State unavailable data/checkpoints and why.

## Reviewer Response Template

Use this structure for each concern:

1. Thank the reviewer and restate the concern precisely.
2. Give the direct answer in one sentence.
3. Provide evidence or new analysis.
4. State the manuscript change.
5. If evidence is unavailable, acknowledge the limitation and narrow the claim.

## Pre-Submission Red-Team Questions

- What is the single strongest reason a reviewer would reject this paper?
- Which claim would fail if the split were made stricter?
- Which baseline could make the method look unnecessary?
- Which figure is persuasive but not yet quantitatively supported?
- Which result depends on a hidden implementation detail?
- Which limitation should be stated proactively?

