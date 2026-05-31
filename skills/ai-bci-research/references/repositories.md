# Repository Index

Use these repositories as entry points. Inspect local files before editing or giving exact run commands. Public GitHub pages may be newer than local clones.

## EEG_Image_decode

- URL: `https://github.com/ncclab-sustech/EEG_Image_decode`
- Paper: Visual Decoding and Reconstruction via EEG Embeddings with Guided Diffusion.
- Public description: uses vision-language models to decode natural image perception from non-invasive brain recordings.
- Important public structure: `EEG-preprocessing/`, `MEG-preprocessing/`, `Retrieval/`, `Generation/`, `models/`.
- Public workflow signals:
  - Retrieval training uses EEG encoders aligned with normalized CLIP embeddings.
  - Reconstruction includes high-level semantic and low-level structural pipelines.
  - Public README notes a `develop` branch with refactored validation split, early stopping, retrieval benchmark, and reconstruction benchmark updates.
- Common tasks: reproduce retrieval, reconstruct images, add evaluation metrics, compare EEGNet-style baselines, clean training scripts, document data paths.

## BHA Project Page

- URL: `https://github.com/ncclab-sustech/BHA-project-page`
- Use as a project page or publication website repository. Inspect before editing; likely web-focused rather than model-training-focused.
- Common tasks: update project pages, paper metadata, figures, links, and result summaries.

## ChineseEEG-2

- URL: `https://github.com/ncclab-sustech/ChineseEEG-2`
- Related work: An EEG Dataset for Multimodal Semantic Alignment and Neural Decoding during Reading and Listening.
- Public scope: high-density EEG dataset for cross-modal semantic alignment between reading aloud and passive listening within a unified Chinese corpus.
- Public structure: `novel_segmentation/`, `experiment/`, `data_preprocessing/`, `text_and_audio_embeddings/`, `analysis/`.
- Public workflow signals:
  - Supports aligned EEG, text, and audio timelines.
  - Includes BERT and Wav2Vec2 semantic embeddings.
  - Includes ISC, source reconstruction, and stimulus decoding tools.
  - EEG setup includes EGI Geodesic EEG 400 series and GSN-HydroCel-128 montage.
- Common tasks: dataset documentation, BIDS conversion, semantic embedding generation, reading/listening alignment analysis, EEG preprocessing, source analysis.

## MindPilot

- URL: `https://github.com/ncclab-sustech/MindPilot`
- Paper: MindPilot: Closed-loop Visual Stimulation Optimization for Brain Modulation with EEG-guided Diffusion.
- Public scope: closed-loop visual stimulation optimization with EEG-guided diffusion and black-box optimization.
- Public structure: `Heuristic_generation/`, `Interactive_search/`, `client/`, `experiments/`, `model/`, `server/`.
- Public workflow signals:
  - Trains EEG readout models.
  - Performs evolutionary or heuristic search in latent/stimulus space.
  - Includes offline generation benchmarks and real-time human experiment client/server components.
  - Provides pretrained weights and preprocessed datasets through Hugging Face.
- Common tasks: closed-loop experiment planning, server/client debugging, online latency checks, offline vs online benchmark comparison, EEG readout modeling, safety/IRB-oriented protocol review.

## BrainFLORA

- URL: `https://github.com/ncclab-sustech/BrainFLORA`
- Paper: BrainFLORA: Uncovering Brain Concept Representation via Multimodal Neural Embeddings.
- Public scope: multimodal neural embeddings for brain concept representation.
- Public structure: `Retrieval/`, `configs/`, `data_preparing/`, `eval/`, `layers/`, `model/`, `train/`, `utils/`.
- Public workflow signals:
  - Supports visual retrieval and reconstruction.
  - Uses multimodal neural embeddings aligned with CLIP-like representation spaces.
  - Public README references EEG, MEG, and fMRI modalities.
  - Provides preprocessed datasets and pretrained checkpoints through Hugging Face.
- Common tasks: multimodal encoder training, cross-modality comparison, concept alignment analysis, retrieval/reconstruction evaluation, config cleanup, benchmark extension.

## Local Repo Workflow

When the user provides a local path:

1. Run `rg --files` to inspect structure.
2. Read `README`, environment files, config files, and entry scripts before editing.
3. Identify data path assumptions and checkpoint dependencies.
4. Run lightweight checks first: import checks, config validation, dry runs, or unit tests if present.
5. Preserve existing experiment outputs and do not delete data/checkpoints unless explicitly asked.
