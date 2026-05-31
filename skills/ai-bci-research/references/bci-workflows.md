# AI x BCI Workflows

## Neural Decoding and Reconstruction Checklist

- Define signal modality: EEG, MEG, fMRI, ECoG, spikes, LFP, fNIRS, or multimodal.
- Define task: visual perception, reading, listening, motor behavior, cognitive workload, emotion, stimulation response, or closed-loop modulation.
- Define split protocol: subject-wise, session-wise, trial-wise, stimulus-wise, or class-wise. Flag leakage risk.
- Define preprocessing: filtering, resampling, artifact rejection, ICA/SSP if used, epoching, baseline correction, normalization, bad channel handling.
- Define representation target: CLIP, BERT, Wav2Vec2, image features, text embeddings, audio embeddings, diffusion latents, motor/action embeddings, or custom MLLM embeddings.
- Define model: EEG encoder, multimodal encoder, contrastive alignment, diffusion prior, adapter, readout model, adversarial/domain adaptation, retrieval head, or generation pipeline.
- Define metrics: top-k retrieval, classification accuracy, correlation, R2, FID/CLIP similarity, reconstruction metrics, behavioral score, modulation target score, online latency, and calibration time.
- Define baselines: chance, linear model, EEGNet, ShallowFBCSPNet, subject-specific model, joint-subject model, pretrained frozen encoder, random target embeddings, and ablated modalities.

## Leakage and Validity Checks

- Never mix augmented views of the same trial across train and test.
- Check whether stimulus classes or exact images overlap across splits.
- Do not select checkpoints on the test set.
- For cross-subject claims, avoid leaking subject-specific normalization statistics from test subjects.
- For retrieval, report candidate set size and whether retrieval is within-subject, cross-subject, seen-class, or zero-shot.
- For reconstruction, separate semantic similarity from pixel/low-level similarity.
- For closed-loop work, distinguish offline replay from live human feedback.

## Bidirectional BCI / Closed-Loop Design

Use this structure for closed-loop proposals:

1. Objective: what neural state, behavior, or subjective target is optimized.
2. Observation: EEG/other signal features and latency.
3. Action: visual stimulus, prompt, motor cue, neurofeedback, or embodied action.
4. Policy/optimizer: black-box search, Bayesian optimization, evolutionary search, reinforcement learning, diffusion guidance, or MLLM planner.
5. Safety: stimulus constraints, fatigue control, adverse response handling, stop criteria.
6. Calibration: subject-specific setup, baseline recording, model warm start, adaptation schedule.
7. Evaluation: online improvement, offline replay, sham control, random control, fixed-stimulus control, statistical test.

## MLLM and Generative Model Integration

Prefer mechanisms that create testable links:

- Use MLLM embedding spaces to align brain signals with language, image, audio, and action semantics.
- Use generative models to transform neural embeddings into candidate stimuli or reconstructions.
- Use diffusion guidance for controllable generation, but report constraints and failure modes.
- Use MLLMs as planners or interpreters only when inputs/outputs can be audited.
- For Physical AI, connect neural signals to perception-action loops rather than only text outputs.

## Fast Validation Template

For a new idea, produce:

- Hypothesis:
- Dataset:
- Signal modality:
- Model:
- Baseline:
- Metric:
- Ablation:
- Leakage risk:
- Smallest runnable experiment:
- Expected failure mode:
