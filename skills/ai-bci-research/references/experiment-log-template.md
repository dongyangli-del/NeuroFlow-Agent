# Experiment Log Template

Use this template when planning, recording, comparing, or debugging AI x BCI experiments. Prefer filling unknown fields with `TBD` or `needs verification` rather than omitting them.

## Experiment Header

- Experiment ID:
- Date:
- Owner:
- Project / paper:
- Venue target:
- Research question:
- Hypothesis:
- Claim this experiment supports:
- Status: planned / running / completed / failed / superseded

## Data and Splits

- Dataset name and version:
- Data location:
- Access restrictions:
- Participants / subjects:
- Sessions:
- Trials:
- Signal modality: EEG / MEG / fMRI / ECoG / spikes / LFP / fNIRS / multimodal
- Acquisition setup: channels, sampling rate, montage, scanner/device, timing synchronization
- Stimulus space:
- Labels or target representations:
- Split protocol: subject-wise / session-wise / trial-wise / stimulus-wise / class-wise
- Train / validation / test counts:
- Candidate set size for retrieval:
- Leakage checks:
- Known exclusions:

## Preprocessing

- Raw input format:
- Filtering:
- Resampling:
- Epoch window:
- Baseline correction:
- Artifact rejection:
- Bad channel handling:
- ICA / SSP / source reconstruction:
- Normalization statistics and fit split:
- Data augmentation:
- Preprocessing script / command:

## Model and Training

- Model name:
- Architecture summary:
- Target embedding or decoder: CLIP / BERT / Wav2Vec2 / diffusion latent / MLLM embedding / custom
- Initialization / pretrained checkpoint:
- Loss:
- Optimizer:
- Learning rate schedule:
- Batch size:
- Epochs / steps:
- Seed:
- Hardware:
- Environment:
- Config file:
- Training command:
- Checkpoint selection rule:

## Evaluation

- Primary metric:
- Secondary metrics:
- Metric definitions:
- Baselines:
- Baseline parity notes:
- Ablations:
- Statistical test:
- Confidence interval or variance:
- Evaluation command:
- Qualitative output protocol:
- Failure-case protocol:

## Results

- Main result:
- Per-subject result:
- Per-session result:
- Per-class or per-stimulus result:
- Retrieval result:
- Reconstruction result:
- Closed-loop / online result:
- Runtime / latency:
- Calibration time:
- Tables / figures generated:
- Logs and checkpoints:

## Interpretation

- What worked:
- What failed:
- Likely cause:
- Reviewer risk:
- Claim supported:
- Claim not supported:
- Follow-up experiment:
- Paper text or figure affected:

## Reproducibility Record

- Git repository:
- Commit hash:
- Dirty files:
- Dependency file:
- Random seeds:
- Dataset checksum or manifest:
- Config snapshot:
- Output directory:
- WandB / tracker link:
- Notes for rerun:

