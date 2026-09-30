# Venue Workflows

Use this file when the user is preparing a submission, revision, rebuttal, workshop paper, camera-ready, or research plan for a specific venue. Prefer venue-specific constraints over generic paper advice, and ask for missing deadline/page/format details only when they change the next action.

## Universal Conference Submission Loop

1. Identify venue, deadline, paper type, page limit, anonymity policy, artifact policy, and checklist requirements.
2. State the central claim in one sentence and list the evidence needed for that claim.
3. Map the paper to the closest prior work, including the user's own prior work, and make the novelty delta explicit.
4. Audit experiments before polishing prose: splits, baselines, metrics, ablations, statistics, and reproducibility.
5. Tighten the method section so a careful reviewer can reproduce training, inference, and evaluation.
6. Stress-test every broad claim against the evidence actually present.
7. Produce the requested artifact: outline, section rewrite, experiment plan, rebuttal, limitation, checklist, figure/table caption, or submission readiness review.

## Venue Priorities

### NeurIPS / ICML / ICLR

- Emphasize method novelty, learning problem formulation, empirical rigor, reproducibility, and clear comparison to strong baselines.
- For EEG/BCI submissions, translate neuroscience details into ML-valid assumptions: data distribution, split, target representation, objective, and evaluation protocol.
- Include ablations that isolate the proposed mechanism, not only component removal.
- Report variance across seeds and subjects when possible.
- Be conservative with foundation-model and AGI framing; reviewers will expect testable mechanisms.

### CVPR / ICCV / ECCV / ACM MM

- Emphasize visual reconstruction, retrieval, generation quality, multimodal alignment, and comparison to vision-language/generative baselines.
- Separate semantic reconstruction metrics from low-level image similarity metrics.
- State candidate set size for retrieval and whether images/classes are seen or unseen.
- Include qualitative figures only after quantitative protocols are clear.
- For diffusion-based methods, describe guidance signals, conditioning path, inference budget, and failure cases.

### ACL / EMNLP / NAACL

- Emphasize language grounding, semantic alignment, decoding of reading/listening signals, text/audio embeddings, and evaluation validity.
- Define language units, timing alignment, text/audio preprocessing, and whether the model predicts words, semantics, embeddings, or responses.
- Avoid implying direct thought decoding; use neural correlates of language processing and semantic representation language.
- Include controls for stimulus frequency, length, audio duration, and linguistic confounds.

### Nature / Science / Scientific Data Style

- Emphasize dataset value, protocol clarity, reproducibility, participant/session details, acquisition hardware, preprocessing, metadata, access, and reuse.
- Separate resource contribution from model performance claims.
- Make ethics, consent, privacy, and data governance explicit.
- Provide validation analyses that demonstrate data quality and utility across tasks.

### BCI / NeuroAI / AI4Science Workshops

- Emphasize scientific hypothesis, neural validity, human-subject constraints, online feasibility, and bridge value between AI and neuroscience.
- Make it clear whether the contribution is decoding, encoding, reconstruction, intervention, modulation, or closed-loop control.
- Include safety, calibration, latency, fatigue, and online/offline mismatch discussion for interactive systems.
- Workshop versions can be more exploratory, but label hypotheses and preliminary results clearly.

## Submission Readiness Checklist

- Main claim is stated once and supported by exact experiments.
- Closest prior work and user-prior-work relationship are explicit.
- Dataset, subject/session counts, channels, sampling rate, stimuli, and split protocol are stated.
- No train/test leakage through subjects, sessions, trials, stimuli, augmentations, normalization, or checkpoint selection.
- Baselines are strong, fair, and run under the same data/split/metric protocol.
- Metrics match the claim and include uncertainty where possible.
- Ablations test the proposed mechanism.
- Limitations separate non-invasive EEG constraints, online/offline claims, and generalization boundaries.
- Code/data/checkpoint availability is accurately described.
- The writing avoids unsupported "first", "robust", "general", "understands thoughts", and unqualified AGI claims.

## Rebuttal Workflow

1. Classify each concern as factual error, missing evidence, weak comparison, unclear writing, or valid limitation.
2. Answer the reviewer first, then describe new analysis or planned revision.
3. Use concrete evidence: table numbers, metric values, split definitions, or additional experiments.
4. Avoid defensive language and avoid promising impossible experiments.
5. Where evidence is missing, concede the boundary and propose a precise revision.

