# Field Verification Report

Generated: 2026-06-18T16:05:45Z

This report verifies fields for entries that already passed strict title matching. Content fields are upgraded only when a short title/abstract/keyword evidence snippet supports the field.

## Summary

- Entries checked: 177
- Fully resolved entries dropped from manual review: 0
- Auto-verified year: 177
- Auto-verified venue: 170
- Auto-verified doi: 168
- Auto-verified signal modality: 14
- Auto-verified task: 75
- Auto-verified method: 49
- Auto-verified dataset: 0
- Auto-verified metric: 30
- Auto-verified limitations: 54
- Remaining unresolved fields before agent batch: dataset=177, signal modality=163, metric=147, method=128, limitations=123, task=102, doi=8, venue=3

## Agent Batch Verification Addendum

Generated: 2026-06-27

This addendum records an agent-assisted source-traced pass over the 177 priority entries. Accepted fields are marked `agent-source-traced`; they are not human-reviewed or expert-reviewed.

- Entries checked: 177
- Entries with accepted updates: 177
- Accepted field updates: 768
- Rejected field candidates: 8
- Remaining unresolved fields after agent batch: dataset=17, signal modality=1, metric=26, method=0, limitations=33, task=0, doi=6, venue=0
- Remaining unresolved total after agent batch: 83
- Public manual-review file updated: `manual-review-needed.md`

Rejected candidates were kept unresolved because they were low confidence or empty:

- `Accelerating scientific discovery with Co-Scientist`: metric low confidence.
- `An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion`: metric low confidence.
- `Does the brain represent words? An evaluation of brain decoding studies of language understanding`: signal modality low confidence.
- `IMPLICIT GAUSSIAN PROCESS REPRESENTATION OF VECTOR FIELDS OVER ARBITRARY LATENT MANI-`: DOI empty/null.
- `OminiControl: Minimal and Universal Control for Diffusion Transformer`: metric low confidence.
- `PIA: Your Personalized Image Animator via Plug-and-Play Modules in Text-to-Image Models`: metric low confidence.
- `EmotionKD: A Cross-Modal Knowledge Distillation Framework for Emotion Recognition Based on Physiological Signals`: metric low confidence.
- `Generalized radiograph representation learning via cross-supervision between images and free-text radiology reports`: metric low confidence.

## P0 Small-Batch Verification Addendum

Generated: 2026-06-27

This addendum records a targeted follow-up over the 6 remaining DOI fields and the 8 previously rejected low-confidence/empty candidates. The pass used separate metadata, paper-evidence, and grey-literature scout roles, then merged only official/source-traced evidence through `preview_agent_verifications.py`.

- Official candidates checked: 13 unique `(entry, field)` targets.
- Accepted field updates: 9.
- Rejected/kept unresolved official candidates: 4.
- Grey-literature leads checked: 13.
- Grey-literature leads written to public citation-critical fields: 0.
- Remaining unresolved fields after P0 small batch: dataset=17, signal modality=0, metric=20, method=0, limitations=33, task=0, doi=4, venue=0.
- Remaining unresolved total after P0 small batch: 74.

Accepted updates:

- `Accelerating scientific discovery with Co-Scientist`: metric from Nature supplementary paper text.
- `An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion`: metric from OpenReview paper text.
- `Does the brain represent words? An evaluation of brain decoding studies of language understanding`: signal modality from arXiv paper text.
- `IMPLICIT GAUSSIAN PROCESS REPRESENTATION OF VECTOR FIELDS OVER ARBITRARY LATENT MANI-`: DOI from arXiv/DataCite/OpenAlex/DBLP metadata.
- `OminiControl: Minimal and Universal Control for Diffusion Transformer`: metric from CVF paper text.
- `PIA: Your Personalized Image Animator via Plug-and-Play Modules in Text-to-Image Models`: metric from CVF paper text.
- `Testing the Limits of Fine-Tuning for Improving Visual Cognition in Vision Language Models`: DOI from arXiv/DataCite/OpenAlex metadata.
- `EmotionKD: A Cross-Modal Knowledge Distillation Framework for Emotion Recognition Based on Physiological Signals`: metric from ACM metadata plus author-uploaded paper text.
- `Generalized radiograph representation learning via cross-supervision between images and free-text radiology reports`: metric from Nature Machine Intelligence paper text.

Kept unresolved:

- `SecureLLM: New private and confidential interfaces with LLMs`: DOI not found in trusted metadata.
- `Towards Brain-to-Text Generation: Neural Decoding with Pre-trained Encoder-Decoder Models`: DOI not found in trusted metadata.
- `CONDITIONAL DIFFUSION WITH ORDINAL REGRES- SION: LONGITUDINAL DATA GENERATION FOR NEURODEGENERATIVE DISEASE STUDIES`: DOI not found in trusted metadata for either duplicate entry.

## Remaining-Field Verification Addendum

Generated: 2026-06-27

This addendum records the full follow-up pass over the remaining 74 unresolved fields. The pass used field-specific agents for DOI, dataset, metric, and limitations; a grey-literature scout for non-authoritative leads; and a reviewer audit over all medium-confidence candidates plus high-risk metric/limitations spot checks.

- Remaining targets checked: 74.
- Official/source-traced accepted field updates: 49.
- Medium-confidence candidates reviewed: 11 approved, 0 rejected.
- High-risk high-confidence spot checks: 23 approved, 0 rejected.
- Grey-literature leads checked: 29.
- Grey-literature leads written to public citation-critical fields: 0.
- Remaining unresolved fields after full remaining-field pass: dataset=1, metric=15, limitations=5, doi=4.
- Remaining unresolved total after full remaining-field pass: 25.

Residual unresolved entries are retained because trusted sources did not directly support the field, the item is a review/perspective with no paper-specific dataset or metric, the DOI was absent from Tier 0/Tier 1 metadata, or accessible sources did not contain an explicit author limitation / clear experimental boundary:

- `SecureLLM: New private and confidential interfaces with LLMs`: DOI not found in DBLP, CEUR, Semantic Scholar, or Crossref-like trusted metadata.
- `Towards Brain-to-Text Generation: Neural Decoding with Pre-trained Encoder-Decoder Models`: DOI not found in OpenReview, workshop PDF, or trusted metadata.
- `CONDITIONAL DIFFUSION WITH ORDINAL REGRES- SION: LONGITUDINAL DATA GENERATION FOR NEURODEGENERATIVE DISEASE STUDIES`: DOI not found in DBLP, OpenReview, or official ICLR metadata for either duplicate entry.
- `How to build a cognitive map`: metric retained unresolved because the article is a review with no paper-specific evaluation metric.
- `Mental state decoders: game-changers or wishful thinking?`: metric retained unresolved because trusted sources identify a commentary/review rather than a primary empirical evaluation.
- `Neuroscience-Inspired Artificial Intelligence`: limitations and metric retained unresolved for both duplicate entries because no explicit author limitation or paper-specific metric was verified from trusted sources.
- `Predictive processing of scenes and objects`: metric retained unresolved because the item is a review article without a paper-specific evaluation metric.
- `Shared Neural Mechanisms of Visual Perception and Imagery`: metric retained unresolved because trusted sources describe a review/meta-synthesis rather than a primary evaluation with a single metric.
- `The Future of Memory: Remembering, Imagining, and the Brain`: limitations and metric retained unresolved because no explicit author limitation or paper-specific metric was verified from trusted sources.
- `What Learning Systems do Intelligent Agents Need? Complementary Learning Systems Theory Updated`: metric retained unresolved because it is a review/theory update.
- `Brain and Cognitive Science Inspired Deep Learning: A Comprehensive Survey`: dataset and metric retained unresolved because accessible trusted metadata identifies it as a survey and did not directly support a paper-specific dataset/metric.
- `Brain-Machine Coupled Learning Method for Facial Emotion Recognition`: limitations retained unresolved because no explicit author limitation or clear experimental-boundary statement was verified from accessible trusted sources.
- `Category selectivity in human visual cortex: Beyond visual object recognition`: metric retained unresolved because trusted sources identify a conceptual review/argument, not a primary metric-bearing evaluation.
- `Convergent multi-modular architecturefor adaptive learning in Drosophila and artificial intelligence`: metric retained unresolved because it is a Perspective/review-style article.
- `Data-Driven Approaches to Understanding Visual Neuron Activity`: metric retained unresolved because the article is a review of modeling approaches and no article-specific evaluation metric was verified.
- `Decoding the brain: From neural representations to mechanistic models`: metric retained unresolved for both duplicate entries because the item is a Perspective and no paper-specific evaluation metric was verified.
- `Efficient processing of natural scenes in visual cortex`: metric retained unresolved because the Frontiers page identifies a review article rather than a primary metric-bearing evaluation.
- `Fast neural distance field-based three-dimensional reconstruction method for geometrical parameter extraction of walnut shell from multiview images`: limitations retained unresolved because no explicit author limitation or clear experimental-boundary statement was verified from accessible trusted sources.

## Per-Entry Results

### Hopfield Networks is All You Need

- year: 2020 [Semantic Scholar strict title match]
- venue: International Conference on Learning Representations [Semantic Scholar strict title match]
- Unresolved: dataset, doi, limitations, method, metric, signal modality, task

### Neural Encoding and Decoding at Scale

- year: 2025 [Semantic Scholar strict title match]
- venue: International Conference on Machine Learning [Semantic Scholar strict title match]
- doi: 10.48550/arXiv.2504.08201 [Semantic Scholar strict title match]
- task: Neural decoding, Encoding model [Zotero BIB title/abstract/keywords]
  Evidence: Neural decoding, Encoding model; evidence: Neural Encoding and Decoding at Scale.
- Unresolved: dataset, limitations, method, metric, signal modality

### Neural Encoding and Decoding at Scale

- year: 2025 [Semantic Scholar strict title match]
- venue: International Conference on Machine Learning [Semantic Scholar strict title match]
- doi: 10.48550/arXiv.2504.08201 [Semantic Scholar strict title match]
- task: Neural decoding, Encoding model [Zotero BIB title/abstract/keywords]
  Evidence: Neural decoding, Encoding model; evidence: Neural Encoding and Decoding at Scale.
- Unresolved: dataset, limitations, method, metric, signal modality

### SecureLLM: New private and confidential interfaces with LLMs

- year: 2025 [Semantic Scholar strict title match]
- venue: IUI Workshops [Semantic Scholar strict title match]
- method: Large language model [Zotero BIB title/abstract/keywords]
  Evidence: The first capability allows an LLM to provide targeted answers only about the resources which a user has access to.
- Unresolved: dataset, doi, limitations, metric, signal modality, task

### TOPONETS: HIGH PERFORMING VISION AND LAN- GUAGE MODELS WITH BRAIN-LIKE TOPOGRAPHY

- year: 2025 [Semantic Scholar strict title match]
- venue: International Conference on Learning Representations [Semantic Scholar strict title match]
- doi: 10.48550/arXiv.2501.16396 [Semantic Scholar strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Towards Brain-to-Text Generation: Neural Decoding with Pre-trained Encoder-Decoder Models

- year: 2021 [Semantic Scholar strict title match]
- task: Neural decoding, Encoding model, Speech/language decoding, Continual/adaptive learning [Zotero BIB title/abstract/keywords]
  Evidence: Neural decoding, Encoding model, Speech/language decoding, Continual/adaptive learning; evidence: Towards Brain-to-Text Generation: Neural Decoding with Pre-trained Encoder-Decoder Models.
- metric: accuracy [public abstract/title evidence]
  Evidence: Our model achieves 18.20% and 7.95% top-1 accuracy in a vocabulary of more than 2,000 words on average across all participants on the two tasks respectively, signiﬁcantly outperforming their strong baselines.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, most of the existing studies have focused on discriminating which one in two stimuli corresponds to the given brain image, which is far from directly generating text from neural activities.
- Unresolved: dataset, doi, method, signal modality, venue

### 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities

- year: 2025 [DBLP strict title match]
- venue: NeurIPS [DBLP strict title match]
- task: Foundation model/pretraining [Zotero BIB title/abstract/keywords]
  Evidence: Foundation model/pretraining; evidence: 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities.
- method: Contrastive learning, Masked autoencoder/pretraining, Reinforcement learning/bandit [Zotero BIB title/abstract/keywords]
  Evidence: Evaluated on simulated locomotion and manipulation tasks, our approach increases performance on the self-supervised contrastive RL algorithm by 2× – 50×, outperforming other goal-conditioned baselines.
- Unresolved: dataset, doi, limitations, metric, signal modality

### A Unified Latent Schrodinger Bridge Diffusion Model for Unsupervised Anomaly Detection and Localization

- year: 2025 [DBLP strict title match]
- venue: CVPR [DBLP strict title match]
- doi: 10.1109/CVPR52734.2025.02377 [DBLP strict title match]
- task: Representation alignment, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment, Dataset/benchmark; evidence: This work introduces the Latent Anomaly Schr¨odinger Bridge (LASB), a unified unsupervised anomaly detection model that operates entirely in the latent space without requiring additional networks or custom modifications.
- method: Diffusion/generative model, Linear/encoding baseline [Zotero BIB title/abstract/keywords]
  Evidence: A Unified Latent Schrodinger Bridge Diffusion Model for Unsupervised Anomaly Detection and Localization.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Anomaly detection and localization remain pivotal challenges in computer vision, with applications ranging from industrial inspection to medical diagnostics.
- Unresolved: dataset, metric, signal modality

### Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data

- year: 2025 [Crossref strict title match]
- venue: 2025 IEEE/CVF International Conference on Computer Vision (ICCV) [Crossref strict title match]
- doi: 10.1109/iccv51701.2025.01239 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### MG-MotionLLM: A Unified Framework for Motion Comprehension and Generation across Multiple Granularities

- year: 2025 [Crossref strict title match]
- venue: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) [Crossref strict title match]
- doi: 10.1109/cvpr52734.2025.02593 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### MG-MotionLLM: A Unified Framework for Motion Comprehension and Generation across Multiple Granularities

- year: 2025 [Crossref strict title match]
- venue: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) [Crossref strict title match]
- doi: 10.1109/cvpr52734.2025.02593 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### MiSO: Optimizing brain stimulation to create neural population activity states

- year: 2024 [Crossref strict title match]
- venue: Advances in Neural Information Processing Systems 37 [Crossref strict title match]
- doi: 10.52202/079017-0760 [Crossref strict title match]
- task: Representation alignment, Closed-loop BCI [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment, Closed-loop BCI; evidence: MiSO: Optimizing brain stimulation to create neural population activity states.
- method: CNN/RNN deep model [Zotero BIB title/abstract/keywords]
  Evidence: In this study, we implemented MiSO with a factor analysis (FA) based alignment method, a convolutional neural network (CNN), and an epsilon greedy optimization algorithm.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, it is challenging to search the large space of stimulation parameters, for example, selecting which subset of electrodes to be used for stimulation.
- Unresolved: dataset, metric, signal modality

### ScaMo: Exploring the Scaling Law in Autoregressive Motion Generation Model

- year: 2025 [Crossref strict title match]
- venue: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) [Crossref strict title match]
- doi: 10.1109/cvpr52734.2025.02595 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### ScaMo: Exploring the Scaling Law in Autoregressive Motion Generation Model

- year: 2025 [Crossref strict title match]
- venue: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) [Crossref strict title match]
- doi: 10.1109/cvpr52734.2025.02595 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### World Action Models are Zero-shot Policies

- year: 2026 [Semantic Scholar strict title match]
- venue: arXiv.org [Semantic Scholar strict title match]
- doi: 10.48550/arXiv.2602.15922 [Semantic Scholar strict title match]
- task: Representation alignment, Foundation model/pretraining [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment, Foundation model/pretraining; evidence: We introduce DreamZero, a World Action Model (WAM) built upon a pretrained video diffusion backbone.
- method: Diffusion/generative model, Masked autoencoder/pretraining [Zotero BIB title/abstract/keywords]
  Evidence: We introduce DreamZero, a World Action Model (WAM) built upon a pretrained video diffusion backbone.
- Unresolved: dataset, limitations, metric, signal modality

### 🦩 Flamingo: a Visual Language Model for Few-Shot Learning

- year: 2022 [Crossref strict title match]
- venue: Advances in Neural Information Processing Systems 35 [Crossref strict title match]
- doi: 10.52202/068431-1723 [Crossref strict title match]
- signal modality: Multimodal neural data, Non-neural AI baseline [Zotero BIB title/abstract/keywords]
  Evidence: Building models that can be rapidly adapted to novel tasks using only a handful of annotated examples is an open challenge for multimodal machine learning research.
- task: Foundation model/pretraining, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Foundation model/pretraining, Dataset/benchmark; evidence: We propose key architectural innovations to: (i) bridge powerful pretrained vision-only and language-only models, (ii) handle sequences of arbitrarily interleaved visual and textual data, and (iii) seamlessly ingest images or videos as inputs.
- method: Large language model, Masked autoencoder/pretraining, Linear/encoding baseline [Zotero BIB title/abstract/keywords]
  Evidence: Flamingo: a Visual Language Model for Few-Shot Learning.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Building models that can be rapidly adapted to novel tasks using only a handful of annotated examples is an open challenge for multimodal machine learning research.
- Unresolved: dataset, metric

### A Brain-Media Deep Framework Towards Seeing Imaginations Inside Brains

- year: 2021 [Crossref strict title match]
- venue: IEEE Transactions on Multimedia [Crossref strict title match]
- doi: 10.1109/tmm.2020.2999183 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### A Perovskite Memristor with Large Dynamic Space for Analog-Encoded Image Recognition

- year: 2022 [Crossref strict title match]
- venue: ACS Nano [Crossref strict title match]
- doi: 10.1021/acsnano.2c09569 [Crossref strict title match]
- metric: accuracy [public abstract/title evidence]
  Evidence: The computing capability of the image classification task of a Fashion-MNIST data set with a high recognition accuracy of up to 90.1% shows that the excellent analog and short-term properties of our perovskite memristor allow the hardware implementation of neuromorphic computing with a reduced training cost..
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, the previously reported memristor-based RC mostly utilized binarized data sets to reduce the difficulty of signal processing of the memristor, which inevitably induces data distortion to a certain extent, leading to poor network computing performance.
- Unresolved: dataset, method, signal modality, task

### A multi-agent system for automating scientific discovery

- year: 2026 [Crossref strict title match]
- venue: Nature [Crossref strict title match]
- doi: 10.1038/s41586-026-10652-y [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### A spatiotemporal style transfer algorithm for dynamic visual stimulus generation

- year: 2024 [Crossref strict title match]
- venue: Nature Computational Science [Crossref strict title match]
- doi: 10.1038/s43588-024-00746-w [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### A unified acoustic-to-speech-to-language embedding space captures the neural basis of natural language processing in everyday conversations

- year: 2025 [Crossref strict title match]
- venue: Nature Human Behaviour [Crossref strict title match]
- doi: 10.1038/s41562-025-02105-9 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Accelerating scientific discovery with Co-Scientist

- year: 2026 [Crossref strict title match]
- venue: Nature [Crossref strict title match]
- doi: 10.1038/s41586-026-10644-y [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Adversarial Decoding: Generating Readable Documents for Adversarial Objectives

- year: 2026 [Crossref strict title match]
- venue: Findings of the Association for Computational Linguistics: EACL 2026 [Crossref strict title match]
- doi: 10.18653/v1/2026.findings-eacl.108 [Crossref strict title match]
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Prior methods either produce easily detectable gibberish, or cannot handle objectives that include embedding similarity.
- Unresolved: dataset, method, metric, signal modality, task

### AgiBot World Colosseo: Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems

- year: 2025 [Crossref strict title match]
- venue: 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) [Crossref strict title match]
- doi: 10.1109/iros60139.2025.11247088 [Crossref strict title match]
- task: Representation alignment, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment, Dataset/benchmark; evidence: AgiBot World Colosseo: Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: We explore how scalable robot data can address real-world challenges for generalized robotic manipulation.
- Unresolved: dataset, method, metric, signal modality

### AgiBot World Colosseo: Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems

- year: 2025 [Crossref strict title match]
- venue: 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) [Crossref strict title match]
- doi: 10.1109/iros60139.2025.11247088 [Crossref strict title match]
- task: Representation alignment, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment, Dataset/benchmark; evidence: AgiBot World Colosseo: Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: We explore how scalable robot data can address real-world challenges for generalized robotic manipulation.
- Unresolved: dataset, method, metric, signal modality

### An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion

- year: 2023 [DBLP strict title match]
- venue: ICLR [DBLP strict title match]
- doi: 10.48550/arxiv.2208.01618 [OpenAlex]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### AnyGrasp: Robust and Efficient Grasp Perception in Spatial and Temporal Domains

- year: 2022 [DBLP strict title match]
- venue: CoRR [DBLP strict title match]
- doi: 10.48550/ARXIV.2212.08333 [DBLP strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### AnySkill: Learning Open-Vocabulary Physical Skill for Interactive Agents

- year: 2024 [DBLP strict title match]
- venue: CVPR [DBLP strict title match]
- doi: 10.1109/CVPR52733.2024.00087 [DBLP strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Attention is All you Need

- year: 2025 [Crossref strict title match]
- doi: 10.65215/nxvz2v36 [Crossref strict title match]
- method: Transformer, CNN/RNN deep model [Zotero BIB title/abstract/keywords]
  Evidence: Attention is All you Need.
- metric: generation quality [public abstract/title evidence]
  Evidence: Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU.
- Unresolved: dataset, limitations, signal modality, task, venue

### Attention is All you Need

- year: 2025 [Crossref strict title match]
- doi: 10.65215/nxvz2v36 [Crossref strict title match]
- method: Transformer, CNN/RNN deep model [Zotero BIB title/abstract/keywords]
  Evidence: Attention is All you Need.
- metric: generation quality [public abstract/title evidence]
  Evidence: Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU.
- Unresolved: dataset, limitations, signal modality, task, venue

### Brain–computer interface control with artificial intelligence copilots

- year: 2025 [Crossref strict title match]
- venue: Nature Machine Intelligence [Crossref strict title match]
- doi: 10.1038/s42256-025-01090-y [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Brant: Foundation Model for Intracranial Neural Signal

- year: 2023 [Crossref strict title match]
- venue: Advances in Neural Information Processing Systems 36 [Crossref strict title match]
- doi: 10.52202/075280-1144 [Crossref strict title match]
- task: Visual reconstruction, Representation alignment, Foundation model/pretraining, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Visual reconstruction, Representation alignment, Foundation model/pretraining, Dataset/benchmark; evidence: Brant: Foundation Model for Intracranial Neural Signal.
- metric: correlation [public abstract/title evidence]
  Evidence: The design of Brant is to capture long-term temporal dependency and spatial correlation from neural signals, combining the information in both time and frequency domains.
- Unresolved: dataset, limitations, method, signal modality

### CONDITIONAL DIFFUSION WITH ORDINAL REGRES- SION: LONGITUDINAL DATA GENERATION FOR NEURODEGENERATIVE DISEASE STUDIES

- year: 2025 [Semantic Scholar strict title match]
- venue: International Conference on Learning Representations [Semantic Scholar strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: Our method sequentially generates continuous data by bridging gaps between sparse data points with a diffusion model, ensuring a realistic representation of disease progression.
- method: Diffusion/generative model, Linear/encoding baseline [Zotero BIB title/abstract/keywords]
  Evidence: CONDITIONAL DIFFUSION WITH ORDINAL REGRES- SION: LONGITUDINAL DATA GENERATION FOR NEURODEGENERATIVE DISEASE STUDIES.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, scarcity of longitudinal data and complex disease dynamics make the analysis highly challenging.
- Unresolved: dataset, doi, metric, signal modality

### CONDITIONAL DIFFUSION WITH ORDINAL REGRES- SION: LONGITUDINAL DATA GENERATION FOR NEURODEGENERATIVE DISEASE STUDIES

- year: 2025 [Semantic Scholar strict title match]
- venue: International Conference on Learning Representations [Semantic Scholar strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: Our method sequentially generates continuous data by bridging gaps between sparse data points with a diffusion model, ensuring a realistic representation of disease progression.
- method: Diffusion/generative model, Linear/encoding baseline [Zotero BIB title/abstract/keywords]
  Evidence: CONDITIONAL DIFFUSION WITH ORDINAL REGRES- SION: LONGITUDINAL DATA GENERATION FOR NEURODEGENERATIVE DISEASE STUDIES.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, scarcity of longitudinal data and complex disease dynamics make the analysis highly challenging.
- Unresolved: dataset, doi, metric, signal modality

### Can Language Understand Depth?

- year: 2022 [Crossref strict title match]
- venue: Proceedings of the 30th ACM International Conference on Multimedia [Crossref strict title match]
- doi: 10.1145/3503161.3549201 [Crossref strict title match]
- method: Contrastive learning [Zotero BIB title/abstract/keywords]
  Evidence: Besides image classification, Contrastive Language-Image Pre-training (CLIP) has accomplished extraordinary success for a wide range of vision tasks, including object-level and 3D space understanding.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, it's still challenging to transfer semantic knowledge learned from CLIP into more intricate tasks of quantified targets, such as depth estimation with geometric information.
- Unresolved: dataset, metric, signal modality, task

### Computational framework to predict and shape human–machine interactions in closed-loop, co-adaptive neural interfaces

- year: 2026 [Crossref strict title match]
- venue: Nature Machine Intelligence [Crossref strict title match]
- doi: 10.1038/s42256-026-01194-z [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Computational models reveal that intuitive physics underlies visual processing of soft objects

- year: 2025 [Crossref strict title match]
- venue: Nature Communications [Crossref strict title match]
- doi: 10.1038/s41467-025-61458-x [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Does the brain represent words? An evaluation of brain decoding studies of language understanding

- year: 2018 [Crossref strict title match]
- venue: 2018 Conference on Cognitive Computational Neuroscience [Crossref strict title match]
- doi: 10.32470/ccn.2018.1237-0 [Crossref strict title match]
- task: Neural decoding, Speech/language decoding, Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Neural decoding, Speech/language decoding, Representation alignment; evidence: An evaluation of brain decoding studies of language understanding.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: (2018), showing how standard evaluations fail to distinguish between language processing models which deploy different mechanisms and which are optimized to solve very different tasks.
- Unresolved: dataset, method, metric, signal modality

### Dynamic memristor-based reservoir computing for high-efficiency temporal signal processing

- year: 2021 [Crossref strict title match]
- venue: Nature Communications [Crossref strict title match]
- doi: 10.1038/s41467-020-20692-1 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### ECG Electrode Localization: 3D DS Camera System for Use in Diverse Clinical Environments

- year: 2023 [Crossref strict title match]
- venue: Sensors [Crossref strict title match]
- doi: 10.3390/s23125552 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Electrophysiological Correlates of Semantic Dissimilarity Reflect the Comprehension of Natural, Narrative Speech

- year: 2017 [Semantic Scholar strict title match]
- venue: bioRxiv [Semantic Scholar strict title match]
- doi: 10.1101/193201 [Semantic Scholar strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### End-to-end privacy preserving deep learning on multi-institutional medical imaging

- year: 2021 [Crossref strict title match]
- venue: Nature Machine Intelligence [Crossref strict title match]
- doi: 10.1038/s42256-021-00337-8 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### ExBody2: Advanced Expressive Humanoid Whole-Body Control

- year: 2024 [Semantic Scholar strict title match]
- venue: arXiv.org [Semantic Scholar strict title match]
- doi: 10.48550/arXiv.2412.13196 [Semantic Scholar strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### FREDF: LEARNING TO FORECAST IN THE FREQUENCY DOMAIN

- year: 2026 [Crossref strict title match]
- venue: AI for Time Series [Crossref strict title match]
- doi: 10.1201/9781003612742-3 [Crossref strict title match]
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Time series modeling presents unique challenges due to autocorrelation in both historical data and future sequences.
- Unresolved: dataset, method, metric, signal modality, task

### How to build a cognitive map

- year: 2022 [Crossref strict title match]
- venue: Nature Neuroscience [Crossref strict title match]
- doi: 10.1038/s41593-022-01153-y [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Human-in-the-Loop Optimization for Deep Stimulus Encoding in Visual Prostheses

- year: 2023 [Crossref strict title match]
- venue: Advances in Neural Information Processing Systems 36 [Crossref strict title match]
- doi: 10.52202/075280-3474 [Crossref strict title match]
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Exact placement of implants and differences in individual perception lead to significant variations in stimulus response, making personalized stimulus optimization a key challenge.
- Unresolved: dataset, method, metric, signal modality, task

### Hybrid computing using a neural network with dynamic external memory

- year: 2016 [Crossref strict title match]
- venue: Nature [Crossref strict title match]
- doi: 10.1038/nature20101 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### IMPLICIT GAUSSIAN PROCESS REPRESENTATION OF VECTOR FIELDS OVER ARBITRARY LATENT MANI-

- year: 2024 [DBLP strict title match]
- venue: ICLR [DBLP strict title match]
- signal modality: EEG [Zotero BIB title/abstract/keywords]
  Evidence: Furthermore, we use RVGP to reconstruct high-density neural dynamics derived from low-density EEG recordings in healthy individuals and Alzheimer’s patients.
- task: Encoding model, Visual reconstruction, Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Encoding model, Visual reconstruction, Representation alignment; evidence: IMPLICIT GAUSSIAN PROCESS REPRESENTATION OF VECTOR FIELDS OVER ARBITRARY LATENT MANI-.
- metric: accuracy [public abstract/title evidence]
  Evidence: We show that vector field singularities are important disease markers and that their reconstruction leads to a classification accuracy of disease states comparable to high-density recordings.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, these approaches assume that the manifold underlying the data is known, limiting their practical utility.
- Unresolved: dataset, doi, method

### Improved protein structure prediction using potentials from deep learning

- year: 2020 [DBLP strict title match]
- venue: Nat. [DBLP strict title match]
- doi: 10.1038/S41586-019-1923-7 [DBLP strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Inception loops discover what excites neurons most using deep predictive models

- year: 2019 [Crossref strict title match]
- venue: Nature Neuroscience [Crossref strict title match]
- doi: 10.1038/s41593-019-0517-x [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Interactive Search for Image Categories by Mental Matching

- year: 2007 [Crossref strict title match]
- venue: 2007 IEEE 11th International Conference on Computer Vision [Crossref strict title match]
- doi: 10.1109/iccv.2007.4409072 [Crossref strict title match]
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, when the image database is unstructured, and when the category is semantic and resides only in the mind of the user, there is no obvious way to begin (the “page zero” problem).
- Unresolved: dataset, method, metric, signal modality, task

### MapGuide: A Simple yet Effective Method to Reconstruct Continuous Language from Brain Activities

- year: 2024 [Crossref strict title match]
- venue: Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers) [Crossref strict title match]
- doi: 10.18653/v1/2024.naacl-long.211 [Crossref strict title match]
- task: Neural decoding, Encoding model, Visual reconstruction, Speech/language decoding, Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Neural decoding, Encoding model, Visual reconstruction, Speech/language decoding, Representation alignment; evidence: MapGuide: A Simple yet Effective Method to Reconstruct Continuous Language from Brain Activities.
- metric: correlation, generation quality [public abstract/title evidence]
  Evidence: We further validate the proposed modules through detailed ablation studies and case analyses and highlight a critical correlation: the more precisely we map brain activities to text embeddings, the better the text reconstruction results.
- Unresolved: dataset, limitations, method, signal modality

### Mastering Atari, Go, chess and shogi by planning with a learned model

- year: 2020 [Crossref strict title match]
- venue: Nature [Crossref strict title match]
- doi: 10.1038/s41586-020-03051-4 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Mastering the game of Go with deep neural networks and tree search

- year: 2016 [Crossref strict title match]
- venue: Nature [Crossref strict title match]
- doi: 10.1038/nature16961 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Mental state decoders: game-changers or wishful thinking?

- year: 2024 [Crossref strict title match]
- venue: Trends in Cognitive Sciences [Crossref strict title match]
- doi: 10.1016/j.tics.2024.06.004 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### ModaVerse: Efficiently Transforming Modalities with LLMs

- year: 2024 [Crossref strict title match]
- venue: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) [Crossref strict title match]
- doi: 10.1109/cvpr52733.2024.02512 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### MotionFix: Text-Driven 3D Human Motion Editing

- year: 2024 [Crossref strict title match]
- venue: SIGGRAPH Asia 2024 Conference Papers [Crossref strict title match]
- doi: 10.1145/3680528.3687559 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### NeuroGen: Activation optimized image synthesis for discovery neuroscience

- year: 2022 [Crossref strict title match]
- venue: NeuroImage [Crossref strict title match]
- doi: 10.1016/j.neuroimage.2021.118812 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Neuroscience-Inspired Artificial Intelligence

- year: 2017 [Crossref strict title match]
- venue: Neuron [Crossref strict title match]
- doi: 10.1016/j.neuron.2017.06.011 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Neuroscience-Inspired Artificial Intelligence

- year: 2017 [Crossref strict title match]
- venue: Neuron [Crossref strict title match]
- doi: 10.1016/j.neuron.2017.06.011 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### OminiControl: Minimal and Universal Control for Diffusion Transformer

- year: 2025 [Crossref strict title match]
- venue: 2025 IEEE/CVF International Conference on Computer Vision (ICCV) [Crossref strict title match]
- doi: 10.1109/iccv51701.2025.01386 [Crossref strict title match]
- method: Transformer, Diffusion/generative model [Zotero BIB title/abstract/keywords]
  Evidence: OminiControl: Minimal and Universal Control for Diffusion Transformer.
- Unresolved: dataset, limitations, metric, signal modality, task

### Online dynamical learning and sequence memory with neuromorphic nanowire networks

- year: 2023 [Crossref strict title match]
- venue: Nature Communications [Crossref strict title match]
- doi: 10.1038/s41467-023-42470-5 [Crossref strict title match]
- metric: accuracy, correlation [public abstract/title evidence]
  Evidence: Applied to the MNIST handwritten digit classification task, online dynamical learning with the NWN device achieves an overall accuracy of 93.4%.
- Unresolved: dataset, limitations, method, signal modality, task

### PIA: Your Personalized Image Animator via Plug-and-Play Modules in Text-to-Image Models

- year: 2024 [Crossref strict title match]
- venue: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) [Crossref strict title match]
- doi: 10.1109/cvpr52733.2024.00740 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Photogrammetry-based stereoscopic optode registration method for functional near-infrared spectroscopy

- year: 2020 [Crossref strict title match]
- venue: Journal of Biomedical Optics [Crossref strict title match]
- doi: 10.1117/1.jbo.25.9.095001 [Crossref strict title match]
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Unfortunately, because this technique does not provide neuroanatomical information to accompany the functional data, its data interpretation remains a persistent challenge in fNIRS brain imaging applications.
- Unresolved: dataset, method, metric, signal modality, task

### PhysHSI: Towards a Real-World Generalizable and Natural Humanoid-Scene Interaction System

- year: 2025 [Semantic Scholar strict title match]
- venue: arXiv.org [Semantic Scholar strict title match]
- doi: 10.48550/arXiv.2510.11072 [Semantic Scholar strict title match]
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Although prior approaches have advanced each capability individually, combining them in a unified system is still an ongoing challenge.
- Unresolved: dataset, method, metric, signal modality, task

### Predictability of real temporal networks

- year: 2020 [Crossref strict title match]
- venue: National Science Review [Crossref strict title match]
- doi: 10.1093/nsr/nwaa015 [Crossref strict title match]
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Interestingly, we find that, for most real temporal networks, despite the greater complexity of predictability brought by the increase in dimension, the combined topological–temporal predictability is higher than the temporal predictability.
- Unresolved: dataset, method, metric, signal modality, task

### Predictive processing of scenes and objects

- year: 2023 [Crossref strict title match]
- venue: Nature Reviews Psychology [Crossref strict title match]
- doi: 10.1038/s44159-023-00254-0 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Proposal for an accurate TMS-MRI co-registration process via 3D laser scanning

- year: 2019 [Crossref strict title match]
- venue: Neuroscience Research [Crossref strict title match]
- doi: 10.1016/j.neures.2018.08.012 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Real-to-Sim for Highly Cluttered Environments via Physics-Consistent Inter-Object Reasoning

- year: 2026 [Crossref strict title match]
- venue: IEEE Robotics and Automation Letters [Crossref strict title match]
- doi: 10.1109/lra.2026.3699238 [Crossref strict title match]
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, in scenarios requiring precise contact reasoning, such as robotic manipulation in highly cluttered environments, geometric fidelity alone is insufficient.
- Unresolved: dataset, method, metric, signal modality, task

### Reverse predictivity for bidirectional comparison of neural networks and biological brains

- year: 2026 [Crossref strict title match]
- venue: Nature Machine Intelligence [Crossref strict title match]
- doi: 10.1038/s42256-026-01204-0 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### STORM-Net: Simple and Timely Optode Registration Method for Functional Near-Infrared Spectroscopy (fNIRS)

- year: 2020 [Crossref strict title match]
- venue: bioRxiv (Cold Spring Harbor Laboratory) [OpenAlex]
- doi: 10.1101/2020.12.29.424683 [Crossref strict title match]
- metric: accuracy [public abstract/title evidence]
  Evidence: We show our method achieves comparable accuracy to current appearance-based methods, while being orders of magnitude faster.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Existing methods pose motion constraints, require expert annotation, or are only applicable in laboratory conditions.
- Unresolved: dataset, method, signal modality, task

### Self-Calibrating BCIs: Ranking and Recovery of Mental Targets Without Labels

- year: 2025 [Semantic Scholar strict title match]
- venue: arXiv.org [Semantic Scholar strict title match]
- doi: 10.48550/arXiv.2506.11151 [Semantic Scholar strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Shared Neural Mechanisms of Visual Perception and Imagery

- year: 2019 [Crossref strict title match]
- doi: 10.31234/osf.io/d8fru [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Spatio-temporal correlations and visual signalling in a complete neuronal population

- year: 2008 [Crossref strict title match]
- venue: Nature [Crossref strict title match]
- doi: 10.1038/nature07140 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### State-dependent pupil dilation rapidly shifts visual feature selectivity

- year: 2022 [Crossref strict title match]
- venue: Nature [Crossref strict title match]
- doi: 10.1038/s41586-022-05270-3 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Subspace communication in the hippocampal–retrosplenial axis

- year: 2026 [Crossref strict title match]
- venue: bioRxiv (Cold Spring Harbor Laboratory) [OpenAlex]
- doi: 10.64898/2025.12.31.697203 [Crossref strict title match]
- metric: correlation [public abstract/title evidence]
  Evidence: Based on a linear dimensionality reduction technique known as partial canonical correlation analysis, we identify low-dimensional communication subspaces 1 between two regions while accounting for measured third-area influences.
- Unresolved: dataset, limitations, method, signal modality, task

### Testing the Limits of Fine-Tuning for Improving Visual Cognition in Vision Language Models

- year: 2025 [DBLP strict title match]
- venue: ICML [DBLP strict title match]
- signal modality: Non-neural AI baseline [Zotero BIB title/abstract/keywords]
  Evidence: Testing the Limits of Fine-Tuning for Improving Visual Cognition in Vision Language Models.
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: In an effort to improve visual cognition and align models with human behavior, we introduce visual stimuli and human judgments on visual cognition tasks, allowing us to systematically evaluate performance across cognitive domains under a consistent environment.
- method: Large language model [Zotero BIB title/abstract/keywords]
  Evidence: Testing the Limits of Fine-Tuning for Improving Visual Cognition in Vision Language Models.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, we find that task-specific finetuning does not contribute to robust human-like generalization to data with other visual characteristics or to tasks in other cognitive domains..
- Unresolved: dataset, doi, metric

### The Bayesian image retrieval system, PicHunter: theory, implementation, and psychophysical experiments

- year: 2000 [Crossref strict title match]
- venue: IEEE Transactions on Image Processing [Crossref strict title match]
- doi: 10.1109/83.817596 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### The Future of Memory: Remembering, Imagining, and the Brain

- year: 2012 [Crossref strict title match]
- venue: Neuron [Crossref strict title match]
- doi: 10.1016/j.neuron.2012.11.001 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### The features underlying the memorability of objects

- year: 2022 [Crossref strict title match]
- venue: bioRxiv (Cold Spring Harbor Laboratory) [OpenAlex]
- doi: 10.1101/2022.04.29.490104 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### The neural network RTNet exhibits the signatures of human perceptual decision-making

- year: 2024 [Crossref strict title match]
- venue: Nature Human Behaviour [Crossref strict title match]
- doi: 10.1038/s41562-024-01914-8 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Towards Variable and Coordinated Holistic Co-Speech Motion Generation

- year: 2024 [Crossref strict title match]
- venue: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) [Crossref strict title match]
- doi: 10.1109/cvpr52733.2024.00155 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### Towards a “universal translator” for neural dynamics at single-cell, single-spike resolution

- year: 2024 [Crossref strict title match]
- venue: Advances in Neural Information Processing Systems 37 [Crossref strict title match]
- doi: 10.52202/079017-2559 [Crossref strict title match]
- signal modality: Spike [Zotero BIB title/abstract/keywords]
  Evidence: Towards a “universal translator” for neural dynamics at single-cell, single-spike resolution.
- Unresolved: dataset, limitations, method, metric, task

### Tracking the Emergence of Conceptual Knowledge during Human Decision Making

- year: 2009 [Crossref strict title match]
- venue: Neuron [Crossref strict title match]
- doi: 10.1016/j.neuron.2009.07.030 [Crossref strict title match]
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Surprisingly little, however, is understood about how we acquire and deploy concepts.
- Unresolved: dataset, method, metric, signal modality, task

### Unsupervised Embedding Learning via Invariant and Spreading Instance Feature

- year: 2019 [Crossref strict title match]
- venue: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) [Crossref strict title match]
- doi: 10.1109/cvpr.2019.00637 [Crossref strict title match]
- metric: accuracy [public abstract/title evidence]
  Evidence: It achieves significantly faster learning speed and higher accuracy than all existing methods.
- Unresolved: dataset, limitations, method, signal modality, task

### VISION-XL: High Definition Video Inverse Problem Solver using Latent Image Diffusion Models

- year: 2025 [Crossref strict title match]
- venue: 2025 IEEE/CVF International Conference on Computer Vision (ICCV) [Crossref strict title match]
- doi: 10.1109/iccv51701.2025.00974 [Crossref strict title match]
- method: Diffusion/generative model [Zotero BIB title/abstract/keywords]
  Evidence: VISION-XL: High Definition Video Inverse Problem Solver using Latent Image Diffusion Models.
- Unresolved: dataset, limitations, metric, signal modality, task

### What Learning Systems do Intelligent Agents Need? Complementary Learning Systems Theory Updated

- year: 2016 [Crossref strict title match]
- venue: Trends in Cognitive Sciences [Crossref strict title match]
- doi: 10.1016/j.tics.2016.05.004 [Crossref strict title match]
- Unresolved: dataset, limitations, method, metric, signal modality, task

### A 7T fMRI dataset of synthetic images for out-of-distribution modeling of vision

- year: 2026 [Crossref strict title match]
- venue: Nature Communications [Crossref strict title match]
- doi: 10.1038/s41467-026-69345-9 [Crossref strict title match]
- signal modality: fMRI [Zotero BIB title/abstract/keywords]
  Evidence: A 7T fMRI dataset of synthetic images for out-of-distribution modeling of vision.
- task: Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Dataset/benchmark; evidence: A 7T fMRI dataset of synthetic images for out-of-distribution modeling of vision.
- Unresolved: dataset, limitations, method, metric

### A Brain-Inspired Way of Reducing the Network Complexity via Concept-Regularized Coding for Emotion Recognition

- year: 2024 [Crossref strict title match]
- venue: Proceedings of the AAAI Conference on Artificial Intelligence [Crossref strict title match]
- doi: 10.1609/aaai.v38i1.27811 [Crossref strict title match]
- task: Visual reconstruction, Representation alignment, Emotion/cognitive state recognition, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Visual reconstruction, Representation alignment, Emotion/cognitive state recognition, Dataset/benchmark; evidence: A Brain-Inspired Way of Reducing the Network Complexity via Concept-Regularized Coding for Emotion Recognition.
- Unresolved: dataset, limitations, method, metric, signal modality

### A Level Set Theory for Neural Implicit Evolution Under Explicit Flows

- year: 2022 [Crossref strict title match]
- venue: Lecture Notes in Computer Science [Crossref strict title match]
- doi: 10.1007/978-3-031-20086-1_41 [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: Coordinate-based neural networks parameterizing implicit surfaces have emerged as efficient representations of geometry.
- Unresolved: dataset, limitations, method, metric, signal modality

### A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning

- year: 2010 [Semantic Scholar strict title match]
- venue: International Conference on Artificial Intelligence and Statistics [Semantic Scholar strict title match]
- doi: 10.1184/r1/6550949 [OpenAlex]
- task: Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Dataset/benchmark; evidence: We demonstrate that this new approach outperforms previous approaches on two challenging imitation learning problems and a benchmark sequence labeling problem..
- Unresolved: dataset, limitations, method, metric, signal modality

### A Vector Quantized Approach for Text to Speech Synthesis on Real-World Spontaneous Speech

- year: 2023 [Crossref strict title match]
- venue: Proceedings of the AAAI Conference on Artificial Intelligence [Crossref strict title match]
- doi: 10.1609/aaai.v37i11.26488 [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: We observe the mismatch between training and inference alignments in mel-spectrogram based autoregressive models, leading to unintelligible synthesis, and demonstrate that learned discrete codes within multiple code groups effectively resolves this issue.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: The diversity of human speech, however, often goes beyond the coverage of these corpora.
- Unresolved: dataset, method, metric, signal modality

### A brain machine interface control algorithm designed from a feedback control perspective

- year: 2012 [Crossref strict title match]
- venue: 2012 Annual International Conference of the IEEE Engineering in Medicine and Biology Society [Crossref strict title match]
- doi: 10.1109/embc.2012.6346180 [Crossref strict title match]
- task: Closed-loop BCI [Zotero BIB title/abstract/keywords]
  Evidence: Closed-loop BCI; evidence: A brain machine interface control algorithm designed from a feedback control perspective.
- Unresolved: dataset, limitations, method, metric, signal modality

### A brain-to-text framework of decoding natural tonal sentences

- year: 2024 [Crossref strict title match]
- venue: Cell Reports [Crossref strict title match]
- doi: 10.1016/j.celrep.2024.114924 [Crossref strict title match]
- task: Neural decoding, Speech/language decoding [Zotero BIB title/abstract/keywords]
  Evidence: Neural decoding, Speech/language decoding; evidence: A brain-to-text framework of decoding natural tonal sentences.
- metric: accuracy [public abstract/title evidence]
  Evidence: The results demonstrate accurate tone and syllable decoding under variances in continuous naturalistic speech production, surpassing previous intracranial Mandarin tonal syllable decoders in decoding accuracy.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Abstract Speech brain-computer interfaces (BCIs) directly translate brain activity into speech sound and text, yet decoding tonal languages like Mandarin Chinese poses a significant, unexplored challenge.
- Unresolved: dataset, method, signal modality

### A distributional code for value in dopamine-based reinforcement learning

- year: 2020 [Crossref strict title match]
- venue: Nature [Crossref strict title match]
- doi: 10.1038/s41586-019-1924-6 [Crossref strict title match]
- method: Reinforcement learning/bandit [Zotero BIB title/abstract/keywords]
  Evidence: A distributional code for value in dopamine-based reinforcement learning.
- Unresolved: dataset, limitations, metric, signal modality, task

### A generalist vision–language foundation model for diverse biomedical tasks

- year: 2024 [Crossref strict title match]
- venue: Nature Medicine [Crossref strict title match]
- doi: 10.1038/s41591-024-03185-2 [Crossref strict title match]
- task: Foundation model/pretraining [Zotero BIB title/abstract/keywords]
  Evidence: Foundation model/pretraining; evidence: A generalist vision–language foundation model for diverse biomedical tasks.
- Unresolved: dataset, limitations, method, metric, signal modality

### A streaming brain-to-voice neuroprosthesis to restore naturalistic communication

- year: 2025 [Crossref strict title match]
- venue: Nature Neuroscience [Crossref strict title match]
- doi: 10.1038/s41593-025-01905-6 [Crossref strict title match]
- task: Neural decoding [Zotero BIB title/abstract/keywords]
  Evidence: Neural decoding; evidence: A streaming brain-to-voice neuroprosthesis to restore naturalistic communication.
- Unresolved: dataset, limitations, method, metric, signal modality

### Accurate digitization of EEG electrode locations by electromagnetic tracking system: The proposed head rotation method and comparison against optical system

- year: 2024 [Crossref strict title match]
- venue: MethodsX [Crossref strict title match]
- doi: 10.1016/j.mex.2024.102766 [Crossref strict title match]
- signal modality: EEG [Zotero BIB title/abstract/keywords]
  Evidence: Accurate digitization of EEG electrode locations by electromagnetic tracking system: The proposed head rotation method and comparison against optical system.
- metric: accuracy [public abstract/title evidence]
  Evidence: The present study aimed to evaluate the digitizing accuracy of electromagnetic and optical systems.
- Unresolved: dataset, limitations, method, task

### Accurate structure prediction of biomolecular interactions with AlphaFold 3

- year: 2026 [Crossref strict title match]
- doi: 10.55277/researchhub.zto7x62j [Crossref strict title match]
- method: Diffusion/generative model [Zotero BIB title/abstract/keywords]
  Evidence: Here we describe our AlphaFold 3 model with a substantially updated diffusion-based architecture that is capable of predicting the joint structure of complexes including proteins, nucleic acids, small molecules, ions and modified residues.
- metric: accuracy [public abstract/title evidence]
  Evidence: The new AlphaFold model demonstrates substantially improved accuracy over many previous specialized tools: far greater accuracy for protein–ligand interactions compared with state-of-the-art docking tools, much higher accuracy for protein–nucleic acid interactions compared with nucleic-acid-specific predictors and substantially higher antibody–antigen predic
- Unresolved: dataset, limitations, signal modality, task

### Accurate transition state generation with an object-aware equivariant elementary reaction diffusion model

- year: 2023 [Crossref strict title match]
- venue: Nature Computational Science [Crossref strict title match]
- doi: 10.1038/s43588-023-00563-7 [Crossref strict title match]
- method: Diffusion/generative model [Zotero BIB title/abstract/keywords]
  Evidence: Accurate transition state generation with an object-aware equivariant elementary reaction diffusion model.
- Unresolved: dataset, limitations, metric, signal modality, task

### Addressing Spatial-Temporal Heterogeneity: General Mixed Time Series Analysis via Latent Continuity Recovery and Alignment

- year: 2024 [Crossref strict title match]
- venue: Advances in Neural Information Processing Systems 37 [Crossref strict title match]
- doi: 10.52202/079017-0569 [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: Addressing Spatial-Temporal Heterogeneity: General Mixed Time Series Analysis via Latent Continuity Recovery and Alignment.
- method: Transformer, Linear/encoding baseline [Zotero BIB title/abstract/keywords]
  Evidence: Subsequently, MiTSformer captures complete spatial-temporal dependencies within and across LCVs and CVs via cascaded self- and cross-attention blocks.
- Unresolved: dataset, limitations, metric, signal modality

### Adopting a human developmental visual diet yields robust and shape-based AI vision

- year: 2026 [Crossref strict title match]
- venue: Nature Machine Intelligence [Crossref strict title match]
- doi: 10.1038/s42256-026-01228-6 [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: Abstract Despite years of research and the dramatic scaling of artificial intelligence (AI) systems, a striking misalignment between artificial and human vision persists.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Abstract Despite years of research and the dramatic scaling of artificial intelligence (AI) systems, a striking misalignment between artificial and human vision persists.
- Unresolved: dataset, method, metric, signal modality

### Algorithmic localization of high-density EEG electrode positions using motion capture

- year: 2020 [Crossref strict title match]
- venue: Journal of Neuroscience Methods [Crossref strict title match]
- doi: 10.1016/j.jneumeth.2020.108919 [Crossref strict title match]
- signal modality: EEG [Zotero BIB title/abstract/keywords]
  Evidence: Algorithmic localization of high-density EEG electrode positions using motion capture.
- metric: accuracy [public abstract/title evidence]
  Evidence: Algorithm accuracy was evaluated across 5 differentsized head models.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: The algorithm is particularly useful for research involving young children and others who cannot remain still for extended time periods.
- Unresolved: dataset, method, task

### Aligning Model and Macaque Inferior Temporal Cortex Representations Improves Model-to-Human Behavioral Alignment and Adversarial Robustness

- year: 2022 [Crossref strict title match]
- venue: bioRxiv (Cold Spring Harbor Laboratory) [OpenAlex]
- doi: 10.1101/2022.07.01.498495 [Crossref strict title match]
- task: Visual reconstruction, Representation alignment, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Visual reconstruction, Representation alignment, Dataset/benchmark; evidence: Aligning Model and Macaque Inferior Temporal Cortex Representations Improves Model-to-Human Behavioral Alignment and Adversarial Robustness.
- metric: accuracy, correlation [public abstract/title evidence]
  Evidence: We then use these data to fine-tune (end-to-end) the model "IT" representations such that they are more aligned with the biological IT representations, while preserving accuracy on object recognition tasks.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: We further assessed the limitations of this approach and find that the improvements in behavioral alignment and adversarial robustness generalize across different image statistics, but not to object categories outside of those covered in our IT training set.
- Unresolved: dataset, method, signal modality

### Aligning individual brains with Fused Unbalanced Gromov-Wasserstein

- year: 2022 [Crossref strict title match]
- venue: Advances in Neural Information Processing Systems 35 [Crossref strict title match]
- doi: 10.52202/068431-1584 [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: Aligning individual brains with Fused Unbalanced Gromov-Wasserstein.
- Unresolved: dataset, limitations, method, metric, signal modality

### AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models

- year: 2021 [Crossref strict title match]
- venue: Nucleic Acids Research [Crossref strict title match]
- doi: 10.1093/nar/gkab1061 [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: AlphaFold DB provides programmatic access to and interactive visualization of predicted atomic coordinates, per-residue and pairwise model-conﬁdence estimates and predicted aligned errors.
- metric: accuracy [public abstract/title evidence]
  Evidence: AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models.
- Unresolved: dataset, limitations, method, signal modality

### Are Transformers Effective for Time Series Forecasting?

- year: 2023 [Crossref strict title match]
- venue: Proceedings of the AAAI Conference on Artificial Intelligence [Crossref strict title match]
- doi: 10.1609/aaai.v37i9.26317 [Crossref strict title match]
- method: Transformer [Zotero BIB title/abstract/keywords]
  Evidence: Are Transformers Effective for Time Series Forecasting?.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Despite the growing performance over the past few years, we question the validity of this line of research in this work.
- Unresolved: dataset, metric, signal modality, task

### Attention Is All You Need

- year: 2025 [Crossref strict title match]
- doi: 10.65215/nxvz2v36 [Crossref strict title match]
- method: Transformer, CNN/RNN deep model [Zotero BIB title/abstract/keywords]
  Evidence: Attention is All you Need.
- metric: generation quality [public abstract/title evidence]
  Evidence: Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU.
- Unresolved: dataset, limitations, signal modality, task

### BAD: Bidirectional Auto-regressive Diffusion for Text-to-Motion Generation

- year: 2025 [Crossref strict title match]
- venue: ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) [Crossref strict title match]
- doi: 10.1109/icassp49660.2025.10889942 [Crossref strict title match]
- method: Diffusion/generative model [Zotero BIB title/abstract/keywords]
  Evidence: BAD: Bidirectional Auto-regressive Diffusion for Text-to-Motion Generation.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Autoregressive models excel in modeling sequential dependencies by enforcing causal constraints, yet they struggle to capture complex bidirectional patterns due to their unidirectional nature.
- Unresolved: dataset, metric, signal modality, task

### Better models of human high-level visual cortex emerge from natural language supervision with a large and diverse dataset

- year: 2023 [DBLP strict title match]
- venue: Nat. Mac. Intell. [DBLP strict title match]
- doi: 10.1038/S42256-023-00753-Y [DBLP strict title match]
- task: Visual reconstruction, Speech/language decoding, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Visual reconstruction, Speech/language decoding, Dataset/benchmark; evidence: Better models of human high-level visual cortex emerge from natural language supervision with a large and diverse dataset.
- Unresolved: dataset, limitations, method, metric, signal modality

### Better models of human high-level visual cortex emerge from natural language supervision with a large and diverse dataset

- year: 2023 [DBLP strict title match]
- venue: Nat. Mac. Intell. [DBLP strict title match]
- doi: 10.1038/S42256-023-00753-Y [DBLP strict title match]
- task: Visual reconstruction, Speech/language decoding, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Visual reconstruction, Speech/language decoding, Dataset/benchmark; evidence: Better models of human high-level visual cortex emerge from natural language supervision with a large and diverse dataset.
- Unresolved: dataset, limitations, method, metric, signal modality

### BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion

- year: 2025 [DBLP strict title match]
- venue: CoRR [DBLP strict title match]
- doi: 10.48550/ARXIV.2508.08241 [DBLP strict title match]
- method: Diffusion/generative model [Zotero BIB title/abstract/keywords]
  Evidence: BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, prior works either produce unnatural motions or rely on motion-specific tuning to achieve satisfactory naturalness.
- Unresolved: dataset, metric, signal modality, task

### Bidirectional Diffusion Bridge Models

- year: 2025 [DBLP strict title match]
- venue: KDD [DBLP strict title match]
- doi: 10.1145/3711896.3736858 [DBLP strict title match]
- method: Diffusion/generative model, Variational autoencoder, Linear/encoding baseline [Zotero BIB title/abstract/keywords]
  Evidence: Bidirectional Diffusion Bridge Models.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, existing methods are limited by their unidirectional nature, requiring separate models for forward and reverse translations.
- Unresolved: dataset, metric, signal modality, task

### Brain Treebank: Large-scale intracranial recordings from naturalistic language stimuli

- year: 2024 [Crossref strict title match]
- venue: Advances in Neural Information Processing Systems 37 [Crossref strict title match]
- doi: 10.52202/079017-3060 [Crossref strict title match]
- task: Speech/language decoding, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Speech/language decoding, Dataset/benchmark; evidence: Brain Treebank: Large-scale intracranial recordings from naturalistic language stimuli.
- Unresolved: dataset, limitations, method, metric, signal modality

### Brain Treebank: Large-scale intracranial recordings from naturalistic language stimuli

- year: 2024 [Crossref strict title match]
- venue: Advances in Neural Information Processing Systems 37 [Crossref strict title match]
- doi: 10.52202/079017-3060 [Crossref strict title match]
- task: Speech/language decoding, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Speech/language decoding, Dataset/benchmark; evidence: Brain Treebank: Large-scale intracranial recordings from naturalistic language stimuli.
- Unresolved: dataset, limitations, method, metric, signal modality

### Brain and Cognitive Science Inspired Deep Learning: A Comprehensive Survey

- year: 2025 [Crossref strict title match]
- venue: IEEE Transactions on Knowledge and Data Engineering [Crossref strict title match]
- doi: 10.1109/tkde.2025.3527551 [Crossref strict title match]
- task: Emotion/cognitive state recognition [Zotero BIB title/abstract/keywords]
  Evidence: Emotion/cognitive state recognition; evidence: Brain and Cognitive Science Inspired Deep Learning: A Comprehensive Survey.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, its interpretability remains limited, and it often underperforms in certain fields due to its lack of human-like characteristics.
- Unresolved: dataset, method, metric, signal modality

### Brain-Machine Coupled Learning Method for Facial Emotion Recognition

- year: 2023 [Crossref strict title match]
- venue: IEEE Transactions on Pattern Analysis and Machine Intelligence [Crossref strict title match]
- doi: 10.1109/tpami.2023.3257846 [Crossref strict title match]
- task: Emotion/cognitive state recognition [Zotero BIB title/abstract/keywords]
  Evidence: Emotion/cognitive state recognition; evidence: Brain-Machine Coupled Learning Method for Facial Emotion Recognition.
- Unresolved: dataset, limitations, method, metric, signal modality

### BridgeVoC: Neural Vocoder with Schrödinger Bridge

- year: 2025 [Crossref strict title match]
- venue: Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence [Crossref strict title match]
- doi: 10.24963/ijcai.2025/903 [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: Specifically, the mel-spectrogram can be projected into the target linear-scale domain and regarded as a degraded spectral representation with a deficient rank distribution.
- method: Diffusion/generative model, Linear/encoding baseline [Zotero BIB title/abstract/keywords]
  Evidence: While previous diffusion-based neural vocoders typically follow a noise-to-data generation pipeline, the linear-degradation prior of the melspectrogram is often neglected, resulting in limited generation quality.
- Unresolved: dataset, limitations, metric, signal modality

### Bridging Supervised Learning and Reinforcement Learning in Math Reasoning

- year: 2025 [Semantic Scholar strict title match]
- venue: arXiv.org [Semantic Scholar strict title match]
- doi: 10.48550/arXiv.2505.18116 [Semantic Scholar strict title match]
- method: Large language model, Linear/encoding baseline, Reinforcement learning/bandit [Zotero BIB title/abstract/keywords]
  Evidence: This implicit policy is parameterized with the same positive LLM we target to optimize on positive data, enabling direct policy optimization on all LLMs’ generations.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: In this work, we challenge the prevailing notion that selfimprovement is exclusive to RL and propose Negative-aware Fine-Tuning (NFT) —a supervised approach that enables LLMs to reflect on their failures and improve autonomously with no external teachers.
- Unresolved: dataset, metric, signal modality, task

### Bridging the Gap between Brain and Machine in Interpreting Visual Semantics: Towards Self-adaptive Brain-to-Text Decoding

- year: 2025 [Crossref strict title match]
- venue: 2025 IEEE/CVF International Conference on Computer Vision (ICCV) [Crossref strict title match]
- doi: 10.1109/iccv51701.2025.02037 [Crossref strict title match]
- task: Neural decoding, Visual reconstruction, Speech/language decoding, Representation alignment, Foundation model/pretraining [Zotero BIB title/abstract/keywords]
  Evidence: Neural decoding, Visual reconstruction, Speech/language decoding, Representation alignment, Foundation model/pretraining; evidence: Bridging the Gap between Brain and Machine in Interpreting Visual Semantics: Towards Self-adaptive Brain-to-Text Decoding.
- method: Transformer, Contrastive learning, Masked autoencoder/pretraining [Zotero BIB title/abstract/keywords]
  Evidence: In contrast, due to selective attention, only part of the visual semantics in the stimulus may be preferentially represented in the neural patterns when subjects view images.
- Unresolved: dataset, limitations, metric, signal modality

### CAP-Net: A Unified Network for 6D Pose and Size Estimation of Categorical Articulated Parts from a Single RGB-D Image

- year: 2025 [Crossref strict title match]
- venue: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) [Crossref strict title match]
- doi: 10.1109/cvpr52734.2025.01088 [Crossref strict title match]
- task: Representation alignment, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment, Dataset/benchmark; evidence: This paper tackles category-level pose estimation of articulated objects in robotic manipulation tasks and introduces a new benchmark dataset.
- method: Linear/encoding baseline [Zotero BIB title/abstract/keywords]
  Evidence: To bridge the sim-to-real domain gap, we introduce the RGBD-Art dataset, the largest RGB-D articulated dataset to date, featuring photorealistic RGB images and depth noise simulated from real sensors.
- metric: accuracy [public abstract/title evidence]
  Evidence: These approaches overlook dense semantic cues from RGB images, leading to suboptimal accuracy, particularly for objects with small parts.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: To address these limitations, we propose a single-stage Network, CAP-Net, for estimating the 6D poses and sizes of Categorical Articulated Parts.
- Unresolved: dataset, signal modality

### Category selectivity in human visual cortex: Beyond visual object recognition

- year: 2017 [Crossref strict title match]
- venue: Neuropsychologia [Crossref strict title match]
- doi: 10.1016/j.neuropsychologia.2017.03.033 [Crossref strict title match]
- task: Encoding model, Visual reconstruction, Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Encoding model, Visual reconstruction, Representation alignment; evidence: Category selectivity in human visual cortex: Beyond visual object recognition.
- Unresolved: dataset, limitations, method, metric, signal modality

### CheckManual: A New Challenge and Benchmark for Manual-based Appliance Manipulation

- year: 2025 [Crossref strict title match]
- venue: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) [Crossref strict title match]
- doi: 10.1109/cvpr52734.2025.02104 [Crossref strict title match]
- task: Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Dataset/benchmark; evidence: CheckManual: A New Challenge and Benchmark for Manual-based Appliance Manipulation.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: CheckManual: A New Challenge and Benchmark for Manual-based Appliance Manipulation.
- Unresolved: dataset, method, metric, signal modality

### CoCoG-2: Controllable generation of visual stimuli for understanding human concept representation

- year: 2025 [Crossref strict title match]
- venue: Communications in Computer and Information Science [Crossref strict title match]
- doi: 10.1007/978-981-96-4001-0_2 [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: CoCoG-2: Controllable generation of visual stimuli for understanding human concept representation.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, methods for controllable image generation in concept space are underdeveloped.
- Unresolved: dataset, method, metric, signal modality

### Compact deep neural network models of visual cortex

- year: 2023 [Crossref strict title match]
- venue: bioRxiv (Cold Spring Harbor Laboratory) [OpenAlex]
- doi: 10.1101/2023.11.22.568315 [Crossref strict title match]
- task: Visual reconstruction, Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Visual reconstruction, Representation alignment; evidence: Compact deep neural network models of visual cortex.
- metric: accuracy [public abstract/title evidence]
  Evidence: We then compress this deep ensemble to identify compact models that have 5,000x fewer parameters yet equivalent accuracy as the deep ensemble.
- Unresolved: dataset, limitations, method, signal modality

### Comparing EEG/ERP-Like and fMRI-Like Techniques for Reading Machine Thoughts

- year: 2010 [Crossref strict title match]
- venue: Lecture Notes in Computer Science [Crossref strict title match]
- doi: 10.1007/978-3-642-15314-3_13 [Crossref strict title match]
- signal modality: EEG, fMRI [Zotero BIB title/abstract/keywords]
  Evidence: Comparing EEG/ERP-Like and fMRI-Like Techniques for Reading Machine Thoughts.
- Unresolved: dataset, limitations, method, metric, task

### Convergent multi-modular architecturefor adaptive learning in Drosophila and artificial intelligence

- year: 2025 [Crossref strict title match]
- venue: iScience [Crossref strict title match]
- doi: 10.1016/j.isci.2025.113799 [Crossref strict title match]
- task: Continual/adaptive learning [Zotero BIB title/abstract/keywords]
  Evidence: Continual/adaptive learning; evidence: This biological hierarchy incorporates the respective strengths of EL and MoE to improve adaptability and employ effective strategies to address their technical challenges, promoting generalization and alleviating interference on a continual basis.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Faced with dynamic, uncertain environments, a common goal of biological intelligence (BI) and artificial intelligence (AI) is to develop robust adaptive learning capabilities, despite different origins.
- Unresolved: dataset, method, metric, signal modality

### Data-Driven Approaches to Understanding Visual Neuron Activity

- year: 2019 [Crossref strict title match]
- venue: Annual Review of Vision Science [Crossref strict title match]
- doi: 10.1146/annurev-vision-091718-014731 [Crossref strict title match]
- task: Visual reconstruction, Closed-loop BCI [Zotero BIB title/abstract/keywords]
  Evidence: Visual reconstruction, Closed-loop BCI; evidence: Data-Driven Approaches to Understanding Visual Neuron Activity.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, models that are able to more accurately reproduce observed neural activity often defy simple interpretations.
- Unresolved: dataset, method, metric, signal modality

### Decoding Neuronal Ensembles in the Human Hippocampus

- year: 2009 [Crossref strict title match]
- venue: Current Biology [Crossref strict title match]
- doi: 10.1016/j.cub.2009.02.033 [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: Conclusions: These results show that highly abstracted representations of space are expressed in the human hippocampus.
- Unresolved: dataset, limitations, method, metric, signal modality

### Decoding and synthesizing tonal language speech from brain activity

- year: 2023 [Crossref strict title match]
- venue: Science Advances [Crossref strict title match]
- doi: 10.1126/sciadv.adh0478 [Crossref strict title match]
- task: Neural decoding, Speech/language decoding [Zotero BIB title/abstract/keywords]
  Evidence: Neural decoding, Speech/language decoding; evidence: Decoding and synthesizing tonal language speech from brain activity.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, tonal language speech BCI is challenging because additional precise control of laryngeal movements to produce lexical tones is required.
- Unresolved: dataset, method, metric, signal modality

### Decoding the brain: From neural representations to mechanistic models

- year: 2024 [Crossref strict title match]
- venue: Cell [Crossref strict title match]
- doi: 10.1016/j.cell.2024.08.051 [Crossref strict title match]
- task: Neural decoding, Encoding model, Visual reconstruction, Speech/language decoding, Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Neural decoding, Encoding model, Visual reconstruction, Speech/language decoding, Representation alignment; evidence: Decoding the brain: From neural representations to mechanistic models.
- Unresolved: dataset, limitations, method, metric, signal modality

### Decoding the brain: From neural representations to mechanistic models

- year: 2024 [Crossref strict title match]
- venue: Cell [Crossref strict title match]
- doi: 10.1016/j.cell.2024.08.051 [Crossref strict title match]
- task: Neural decoding, Encoding model, Visual reconstruction, Speech/language decoding, Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Neural decoding, Encoding model, Visual reconstruction, Speech/language decoding, Representation alignment; evidence: Decoding the brain: From neural representations to mechanistic models.
- Unresolved: dataset, limitations, method, metric, signal modality

### Deep Neural Networks Reveal a Gradient in the Complexity of Neural Representations across the Ventral Stream

- year: 2015 [Crossref strict title match]
- venue: Journal of Neuroscience [Crossref strict title match]
- doi: 10.1523/jneurosci.5023-14.2015 [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: Deep Neural Networks Reveal a Gradient in the Complexity of Neural Representations across the Ventral Stream.
- metric: accuracy [public abstract/title evidence]
  Evidence: Furthermore, it allowed decoding of representations from human brain activity at an unsurpassed degree of accuracy, confirming the quality of the developed approach.
- Unresolved: dataset, limitations, method, signal modality

### Deep Residual Network Predicts Cortical Representation and Organization of Visual Features for Rapid Categorization

- year: 2018 [Crossref strict title match]
- venue: Scientific Reports [Crossref strict title match]
- doi: 10.1038/s41598-018-22160-9 [Crossref strict title match]
- task: Encoding model, Visual reconstruction, Speech/language decoding, Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Encoding model, Visual reconstruction, Speech/language decoding, Representation alignment; evidence: Deep Residual Network Predicts Cortical Representation and Organization of Visual Features for Rapid Categorization.
- metric: accuracy [public abstract/title evidence]
  Evidence: Using this predictive model, we mapped human cortical representations to 64,000 visual objects from 80 categories with high throughput and accuracy.
- Unresolved: dataset, limitations, method, signal modality

### Deep Unsupervised Learning using Nonequilibrium Thermodynamics

- year: 2015 [Semantic Scholar strict title match]
- venue: International Conference on Machine Learning [Semantic Scholar strict title match]
- doi: 10.48550/arxiv.1503.03585 [OpenAlex]
- method: Diffusion/generative model [Zotero BIB title/abstract/keywords]
  Evidence: The essential idea, inspired by non-equilibrium statistical physics, is to systematically and slowly destroy structure in a data distribution through an iterative forward diffusion process.
- Unresolved: dataset, limitations, metric, signal modality, task

### Deep Unsupervised Learning using Nonequilibrium Thermodynamics

- year: 2015 [Semantic Scholar strict title match]
- venue: International Conference on Machine Learning [Semantic Scholar strict title match]
- doi: 10.48550/arxiv.1503.03585 [OpenAlex]
- method: Diffusion/generative model [Zotero BIB title/abstract/keywords]
  Evidence: The essential idea, inspired by non-equilibrium statistical physics, is to systematically and slowly destroy structure in a data distribution through an iterative forward diffusion process.
- Unresolved: dataset, limitations, metric, signal modality, task

### DiffEditor: Boosting Accuracy and Flexibility on Diffusion-Based Image Editing

- year: 2024 [Crossref strict title match]
- venue: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) [Crossref strict title match]
- doi: 10.1109/cvpr52733.2024.00811 [Crossref strict title match]
- method: Diffusion/generative model [Zotero BIB title/abstract/keywords]
  Evidence: DiffEditor: Boosting Accuracy and Flexibility on Diffusion-Based Image Editing.
- metric: accuracy [public abstract/title evidence]
  Evidence: DiffEditor: Boosting Accuracy and Flexibility on Diffusion-Based Image Editing.
- Unresolved: dataset, limitations, signal modality, task

### Diffusion Schrödinger Bridge Matching

- year: 2023 [Crossref strict title match]
- venue: Advances in Neural Information Processing Systems 36 [Crossref strict title match]
- doi: 10.52202/075280-2717 [Crossref strict title match]
- method: Diffusion/generative model, Linear/encoding baseline [Zotero BIB title/abstract/keywords]
  Evidence: Diffusion Schrödinger Bridge Matching.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, while it is desirable in many applications to approximate the deterministic dynamic Optimal Transport (OT) map which admits attractive properties, DDMs and FMMs are not guaranteed to provide transports close to the OT map.
- Unresolved: dataset, metric, signal modality, task

### Dimensions That Matter – Interpretable Object Dimensions in Humans and Deep Neural Networks

- year: 2023 [Crossref strict title match]
- venue: 2023 Conference on Cognitive Computational Neuroscience [Crossref strict title match]
- doi: 10.32470/ccn.2023.1291-0 [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: Here we address this question by introducing a novel approach that allows us to compare human and deep neural network (DNN) representations through an interpretable embedding.
- Unresolved: dataset, limitations, method, metric, signal modality

### Dimensions That Matter – Interpretable Object Dimensions in Humans and Deep Neural Networks

- year: 2023 [Crossref strict title match]
- venue: 2023 Conference on Cognitive Computational Neuroscience [Crossref strict title match]
- doi: 10.32470/ccn.2023.1291-0 [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: Here we address this question by introducing a novel approach that allows us to compare human and deep neural network (DNN) representations through an interpretable embedding.
- Unresolved: dataset, limitations, method, metric, signal modality

### Direct Diffusion Bridge using Data Consistency for Inverse Problems

- year: 2023 [Crossref strict title match]
- venue: Advances in Neural Information Processing Systems 36 [Crossref strict title match]
- doi: 10.52202/075280-0313 [Crossref strict title match]
- method: Diffusion/generative model, Linear/encoding baseline [Zotero BIB title/abstract/keywords]
  Evidence: Direct Diffusion Bridge using Data Consistency for Inverse Problems.
- Unresolved: dataset, limitations, metric, signal modality, task

### Discovering faster matrix multiplication algorithms with reinforcement learning

- year: 2022 [Crossref strict title match]
- venue: Nature [Crossref strict title match]
- doi: 10.1038/s41586-022-05172-4 [Crossref strict title match]
- method: Reinforcement learning/bandit [Zotero BIB title/abstract/keywords]
  Evidence: Discovering faster matrix multiplication algorithms with reinforcement learning.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, automating the algorithm discovery procedure is intricate, as the space of possible algorithms is enormous.
- Unresolved: dataset, metric, signal modality, task

### Distributed representations of behaviour-derived object dimensions in the human visual system

- year: 2024 [Crossref strict title match]
- venue: Nature Human Behaviour [Crossref strict title match]
- doi: 10.1038/s41562-024-01980-y [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: Distributed representations of behaviour-derived object dimensions in the human visual system.
- Unresolved: dataset, limitations, method, metric, signal modality

### Distributed representations of behaviour-derived object dimensions in the human visual system

- year: 2024 [Crossref strict title match]
- venue: Nature Human Behaviour [Crossref strict title match]
- doi: 10.1038/s41562-024-01980-y [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: Distributed representations of behaviour-derived object dimensions in the human visual system.
- Unresolved: dataset, limitations, method, metric, signal modality

### Dynamical flexible inference of nonlinear latent factors and structures in neural population activity

- year: 2023 [Crossref strict title match]
- venue: Nature Biomedical Engineering [Crossref strict title match]
- doi: 10.1038/s41551-023-01106-1 [Crossref strict title match]
- method: Linear/encoding baseline [Zotero BIB title/abstract/keywords]
  Evidence: Dynamical flexible inference of nonlinear latent factors and structures in neural population activity.
- Unresolved: dataset, limitations, metric, signal modality, task

### EEG Electrodes and Where to Find Them: Automated Localization From 3D Scans

- year: 2024 [Crossref strict title match]
- venue: Journal of Neural Engineering [Crossref strict title match]
- doi: 10.1088/1741-2552/ad7c7e [Crossref strict title match]
- signal modality: EEG [Zotero BIB title/abstract/keywords]
  Evidence: EEG Electrodes and Where to Find Them: Automated Localization From 3D Scans.
- metric: accuracy [public abstract/title evidence]
  Evidence: In this paper, we present a novel, versatile approach that utilizes 3D scans to localize EEG electrode positions with high accuracy.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: This limitation restricts the use of these advanced methods..
- Unresolved: dataset, method, task

### EEG electrode digitization with commercial virtual reality hardware

- year: 2018 [Crossref strict title match]
- venue: PLOS ONE [Crossref strict title match]
- doi: 10.1371/journal.pone.0207516 [Crossref strict title match]
- signal modality: EEG [Zotero BIB title/abstract/keywords]
  Evidence: EEG electrode digitization with commercial virtual reality hardware.
- Unresolved: dataset, limitations, method, metric, task

### EEG electrode localization with 3D iPhone scanning using point-cloud electrode selection (PC-ES)

- year: 2023 [Crossref strict title match]
- venue: Journal of Neural Engineering [Crossref strict title match]
- doi: 10.1088/1741-2552/ad12db [Crossref strict title match]
- signal modality: EEG [Zotero BIB title/abstract/keywords]
  Evidence: EEG electrode localization with 3D iPhone scanning using point-cloud electrode selection (PC-ES).
- metric: accuracy [public abstract/title evidence]
  Evidence: These metrics demonstrate comparable performance of iPhone/PC-ES scanning to currently available technology and sufficient accuracy for ESI.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: As a result, electrode localization challenges further impede access to ESI, particularly in inpatient and intensive care settings.
- Unresolved: dataset, method, task

### Efficient Estimation of Word Representations in Vector Space

- year: 2020 [Crossref strict title match]
- venue: Journal of Innovations in Engineering Education [Crossref strict title match]
- doi: 10.3126/jiee.v3i1.34327 [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: Efficient Estimation of Word Representations in Vector Space.
- metric: accuracy [public abstract/title evidence]
  Evidence: We observe large improvements in accuracy at much lower computational cost, i.e.
- Unresolved: dataset, limitations, method, signal modality

### Efficient processing of natural scenes in visual cortex

- year: 2022 [Crossref strict title match]
- venue: Frontiers in Cellular Neuroscience [Crossref strict title match]
- doi: 10.3389/fncel.2022.1006703 [Crossref strict title match]
- task: Visual reconstruction [Zotero BIB title/abstract/keywords]
  Evidence: Visual reconstruction; evidence: Efficient processing of natural scenes in visual cortex.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: We conclude by discussing how adaptation to natural temporal statistics may aid in learning and representing visual objects, and propose two challenges for the future: (1) explaining the distribution of shape sensitivity in the ventral visual stream from the statistics of object shape in natural images, and (2) explaining cell types of the vertebrate retina
- Unresolved: dataset, method, metric, signal modality

### EgoLM: Multi-Modal Language Model of Egocentric Motions

- year: 2025 [Crossref strict title match]
- venue: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) [Crossref strict title match]
- doi: 10.1109/cvpr52734.2025.00503 [Crossref strict title match]
- signal modality: Multimodal neural data, Non-neural AI baseline [Zotero BIB title/abstract/keywords]
  Evidence: EgoLM: Multi-Modal Language Model of Egocentric Motions.
- method: Large language model [Zotero BIB title/abstract/keywords]
  Evidence: EgoLM: Multi-Modal Language Model of Egocentric Motions.
- Unresolved: dataset, limitations, metric, task

### EmotionKD: A Cross-Modal Knowledge Distillation Framework for Emotion Recognition Based on Physiological Signals

- year: 2023 [Crossref strict title match]
- venue: Proceedings of the 31st ACM International Conference on Multimedia [Crossref strict title match]
- doi: 10.1145/3581783.3612277 [Crossref strict title match]
- signal modality: Multimodal neural data [Zotero BIB title/abstract/keywords]
  Evidence: EmotionKD: A Cross-Modal Knowledge Distillation Framework for Emotion Recognition Based on Physiological Signals.
- Unresolved: dataset, limitations, method, metric, task

### EnerVerse-AC: Envisioning Embodied Environments with Action Condition

- year: 2025 [Crossref strict title match]
- venue: Preprints.org [OpenAlex]
- doi: 10.20944/preprints202505.1193.v1 [Crossref strict title match]
- task: Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Dataset/benchmark; evidence: As both a data engine and evaluator, EVAC augments human-collected trajectories into diverse datasets and generates realistic, action-conditioned video observations for policy testing, eliminating the need for physical robots or complex simulations.
- Unresolved: dataset, limitations, method, metric, signal modality

### Explorations of using a convolutional neural network to understand brain activations during movie watching

- year: 2024 [Crossref strict title match]
- venue: Psychoradiology [Crossref strict title match]
- doi: 10.1093/psyrad/kkae021 [Crossref strict title match]
- method: CNN/RNN deep model [Zotero BIB title/abstract/keywords]
  Evidence: Explorations of using a convolutional neural network to understand brain activations during movie watching.
- Unresolved: dataset, limitations, metric, signal modality, task

### Fast neural distance field-based three-dimensional reconstruction method for geometrical parameter extraction of walnut shell from multiview images

- year: 2024 [Crossref strict title match]
- venue: Computers and Electronics in Agriculture [Crossref strict title match]
- doi: 10.1016/j.compag.2024.109189 [Crossref strict title match]
- task: Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Dataset/benchmark; evidence: A low-cost image acquisition platform with two cameras was designed to create a multiview image dataset.
- metric: accuracy [public abstract/title evidence]
  Evidence: While maintaining high reconstruction accuracy, the proposed method completed the reconstruction in 7 minutes, surpassing the speed of popular pure vision-based methods.
- Unresolved: dataset, limitations, method, signal modality

### Fg-T2M: Fine-Grained Text-Driven Human Motion Generation via Diffusion Model

- year: 2023 [Crossref strict title match]
- venue: 2023 IEEE/CVF International Conference on Computer Vision (ICCV) [Crossref strict title match]
- doi: 10.1109/iccv51070.2023.02014 [Crossref strict title match]
- method: Diffusion/generative model, Graph neural network [Zotero BIB title/abstract/keywords]
  Evidence: Fg-T2M: Fine-Grained Text-Driven Human Motion Generation via Diffusion Model.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, current methods are limited to producing either deterministic or imprecise motion sequences, failing to effectively control the temporal and spatial relationships required to conform to a given text description.
- Unresolved: dataset, metric, signal modality, task

### Flexible Motion In-betweening with Diffusion Models

- year: 2024 [Crossref strict title match]
- venue: Special Interest Group on Computer Graphics and Interactive Techniques Conference Conference Papers [Crossref strict title match]
- doi: 10.1145/3641519.3657414 [Crossref strict title match]
- method: Diffusion/generative model [Zotero BIB title/abstract/keywords]
  Evidence: Flexible Motion In-betweening with Diffusion Models.
- Unresolved: dataset, limitations, metric, signal modality, task

### Flow Matching Posterior Sampling: A Training-free Conditional Generation for Flow Matching

- year: 2026 [Crossref strict title match]
- venue: IEEE Transactions on Image Processing [Crossref strict title match]
- doi: 10.1109/tip.2026.3698367 [Crossref strict title match]
- method: Diffusion/generative model, Linear/encoding baseline [Zotero BIB title/abstract/keywords]
  Evidence: Recently, a successful training-free conditional generation approach incorporates conditions via posterior sampling, which relies on the availability of a score function in the unconditional diffusion model.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, flow matching models do not possess an explicit score function, rendering such a strategy inapplicable.
- Unresolved: dataset, metric, signal modality, task

### Functional Connectivity of Imagined Speech and Visual Imagery based on Spectral Dynamics

- year: 2021 [Crossref strict title match]
- venue: 2021 9th International Winter Conference on Brain-Computer Interface (BCI) [Crossref strict title match]
- doi: 10.1109/bci51272.2021.9385302 [Crossref strict title match]
- task: Neural decoding, Visual reconstruction, Speech/language decoding, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Neural decoding, Visual reconstruction, Speech/language decoding, Dataset/benchmark; evidence: Functional Connectivity of Imagined Speech and Visual Imagery based on Spectral Dynamics.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, the internal dynamics of the two paradigms along with their intrinsic features haven't been revealed.
- Unresolved: dataset, method, metric, signal modality

### Generalized radiograph representation learning via cross-supervision between images and free-text radiology reports

- year: 2022 [Crossref strict title match]
- venue: Nature Machine Intelligence [Crossref strict title match]
- doi: 10.1038/s42256-021-00425-9 [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: Generalized radiograph representation learning via cross-supervision between images and free-text radiology reports.
- Unresolved: dataset, limitations, method, metric, signal modality

### Generating Long Videos of Dynamic Scenes

- year: 2022 [Crossref strict title match]
- venue: Advances in Neural Information Processing Systems 35 [Crossref strict title match]
- doi: 10.52202/068431-2303 [Crossref strict title match]
- task: Representation alignment, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment, Dataset/benchmark; evidence: To address these limitations, we prioritize the time axis by redesigning the temporal latent representation and learning long-term consistency from data by training on longer videos.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Existing video generation methods often fail to produce new content as a function of time while maintaining consistencies expected in real environments, such as plausible dynamics and object persistence.
- Unresolved: dataset, method, metric, signal modality

### Glove: Global Vectors for Word Representation

- year: 2014 [Crossref strict title match]
- venue: Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP) [Crossref strict title match]
- doi: 10.3115/v1/d14-1162 [Crossref strict title match]
- task: Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment; evidence: Glove: Global Vectors for Word Representation.
- method: Linear/encoding baseline [Zotero BIB title/abstract/keywords]
  Evidence: The result is a new global logbilinear regression model that combines the advantages of the two major model families in the literature: global matrix factorization and local context window methods.
- Unresolved: dataset, limitations, metric, signal modality

### Grandmaster level in StarCraft II using multi-agent reinforcement learning

- year: 2019 [Crossref strict title match]
- venue: Nature [Crossref strict title match]
- doi: 10.1038/s41586-019-1724-z [Crossref strict title match]
- method: Reinforcement learning/bandit [Zotero BIB title/abstract/keywords]
  Evidence: Grandmaster level in StarCraft II using multi-agent reinforcement learning.
- Unresolved: dataset, limitations, metric, signal modality, task

### Grounded Language-Image Pre-training

- year: 2022 [Crossref strict title match]
- venue: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) [Crossref strict title match]
- doi: 10.1109/cvpr52688.2022.01069 [Crossref strict title match]
- task: Representation alignment, Foundation model/pretraining [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment, Foundation model/pretraining; evidence: This paper presents a grounded language-image pretraining (GLIP) model for learning object-level, languageaware, and semantic-rich visual representations.
- method: Masked autoencoder/pretraining [Zotero BIB title/abstract/keywords]
  Evidence: This paper presents a grounded language-image pretraining (GLIP) model for learning object-level, languageaware, and semantic-rich visual representations.
- Unresolved: dataset, limitations, metric, signal modality

### Growing a Neural Network in Breadth, Depth, and Time

- year: 2026 [Semantic Scholar strict title match]
- method: CNN/RNN deep model [Zotero BIB title/abstract/keywords]
  Evidence: Here we define differentiable cost terms for breadth, depth, and time within a recurrent convolutional neural network conceived as a finite subset of an infinite lattice.
- metric: accuracy [public abstract/title evidence]
  Evidence: We find that all three resources can be traded off against each other to achieve a given level of accuracy.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Spatial and temporal resource constraints are critical for both biological and artificial intelligent systems.
- Unresolved: dataset, signal modality, task

### HSI-GPT: A General-Purpose Large Scene-Motion-Language Model for Human Scene Interaction

- year: 2025 [Crossref strict title match]
- venue: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) [Crossref strict title match]
- doi: 10.1109/cvpr52734.2025.00670 [Crossref strict title match]
- signal modality: Non-neural AI baseline [Zotero BIB title/abstract/keywords]
  Evidence: HSI-GPT: A General-Purpose Large Scene-Motion-Language Model for Human Scene Interaction.
- method: Large language model [Zotero BIB title/abstract/keywords]
  Evidence: HSI-GPT: A General-Purpose Large Scene-Motion-Language Model for Human Scene Interaction.
- Unresolved: dataset, limitations, metric, task

### HiDe-PET: Continual Learning via Hierarchical Decomposition of Parameter-Efficient Tuning

- year: 2025 [Crossref strict title match]
- venue: IEEE Transactions on Pattern Analysis and Machine Intelligence [Crossref strict title match]
- doi: 10.1109/tpami.2025.3562534 [Crossref strict title match]
- task: Representation alignment, Continual/adaptive learning [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment, Continual/adaptive learning; evidence: HiDe-PET: Continual Learning via Hierarchical Decomposition of Parameter-Efficient Tuning.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Despite the popularity of Prompt-based PET for CL, its empirical design often leads to sub-optimal performance in our evaluation of different PTMs and target tasks.
- Unresolved: dataset, method, metric, signal modality

### High-Resolution Image Reconstruction With Latent Diffusion Models From Human Brain Activity

- year: 2022 [Crossref strict title match]
- venue: bioRxiv (Cold Spring Harbor Laboratory) [OpenAlex]
- doi: 10.1101/2022.11.18.517004 [Crossref strict title match]
- task: Visual reconstruction [Zotero BIB title/abstract/keywords]
  Evidence: Visual reconstruction; evidence: High-Resolution Image Reconstruction With Latent Diffusion Models From Human Brain Activity.
- method: Diffusion/generative model [Zotero BIB title/abstract/keywords]
  Evidence: High-Resolution Image Reconstruction With Latent Diffusion Models From Human Brain Activity.
- Unresolved: dataset, limitations, metric, signal modality

### High-performance brain-to-text communication via handwriting

- year: 2021 [Crossref strict title match]
- venue: Nature [Crossref strict title match]
- doi: 10.1038/s41586-021-03506-2 [Crossref strict title match]
- task: Neural decoding [Zotero BIB title/abstract/keywords]
  Evidence: Neural decoding; evidence: High-performance brain-to-text communication via handwriting.
- Unresolved: dataset, limitations, method, metric, signal modality

### Highly accurate protein structure prediction for the human proteome

- year: 2021 [Crossref strict title match]
- venue: Nature [Crossref strict title match]
- doi: 10.1038/s41586-021-03828-1 [Crossref strict title match]
- task: Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Dataset/benchmark; evidence: The resulting dataset covers 58% of residues with a confident prediction, of which a subset (36% of all residues) have very high confidence.
- metric: accuracy [public abstract/title evidence]
  Evidence: We are making our predictions freely available to the community and anticipate that routine large-scale and high-accuracy structure prediction will become an important tool that will allow new questions to be addressed from a structural perspective..
- Unresolved: dataset, limitations, method, signal modality

### Highly accurate protein structure prediction with AlphaFold

- year: 2021 [Crossref strict title match]
- venue: Nature [Crossref strict title match]
- doi: 10.1038/s41586-021-03819-2 [Crossref strict title match]
- task: Representation alignment, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment, Dataset/benchmark; evidence: Accurate computational approaches are needed to address this gap and to enable large-scale structural bioinformatics.
- metric: accuracy [public abstract/title evidence]
  Evidence: Despite recent progress 10–14 , existing methods fall far short of atomic accuracy, especially when no homologous structure is available.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Despite recent progress 10–14 , existing methods fall far short of atomic accuracy, especially when no homologous structure is available.
- Unresolved: dataset, method, signal modality

### Hippocampal place cells construct reward related sequences through unexplored space

- year: 2015 [Crossref strict title match]
- venue: eLife [Crossref strict title match]
- doi: 10.7554/elife.06063 [Crossref strict title match]
- task: Visual reconstruction, Representation alignment [Zotero BIB title/abstract/keywords]
  Evidence: Visual reconstruction, Representation alignment; evidence: Dominant theories of hippocampal function propose that place cell representations are formed during an animal's first encounter with a novel environment and are subsequently replayed during off-line states to support consolidation and future behaviour.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: However, the place cell pattern that would become the mental map of the other inaccessible arm was not activated before the rat explored that area.
- Unresolved: dataset, method, metric, signal modality

### How to sample the world for understanding the visual system

- year: 2025 [Crossref strict title match]
- venue: Proceedings of Cognitive Computational Neuroscience 2025 [Crossref strict title match]
- doi: 10.32470/rfgh6r8 [Crossref strict title match]
- task: Visual reconstruction, Speech/language decoding, Representation alignment, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Visual reconstruction, Speech/language decoding, Representation alignment, Dataset/benchmark; evidence: How to sample the world for understanding the visual system.
- method: Contrastive learning [Zotero BIB title/abstract/keywords]
  Evidence: Our analysis of CLIP embeddings of these images suggests significant representational gaps in existing datasets, demonstrating that they cover only a restricted subset of the space spanned by LAION-natural.
- Unresolved: dataset, limitations, metric, signal modality

### How to sample the world for understanding the visual system

- year: 2025 [Crossref strict title match]
- venue: Proceedings of Cognitive Computational Neuroscience 2025 [Crossref strict title match]
- doi: 10.32470/rfgh6r8 [Crossref strict title match]
- task: Visual reconstruction, Speech/language decoding, Representation alignment, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Visual reconstruction, Speech/language decoding, Representation alignment, Dataset/benchmark; evidence: How to sample the world for understanding the visual system.
- method: Contrastive learning [Zotero BIB title/abstract/keywords]
  Evidence: Our analysis of CLIP embeddings of these images suggests significant representational gaps in existing datasets, demonstrating that they cover only a restricted subset of the space spanned by LAION-natural.
- Unresolved: dataset, limitations, metric, signal modality

### How to sample the world for understanding the visual system

- year: 2025 [Crossref strict title match]
- venue: Proceedings of Cognitive Computational Neuroscience 2025 [Crossref strict title match]
- doi: 10.32470/rfgh6r8 [Crossref strict title match]
- task: Visual reconstruction, Speech/language decoding, Representation alignment, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Visual reconstruction, Speech/language decoding, Representation alignment, Dataset/benchmark; evidence: How to sample the world for understanding the visual system.
- method: Contrastive learning [Zotero BIB title/abstract/keywords]
  Evidence: Our analysis of CLIP embeddings of these images suggests significant representational gaps in existing datasets, demonstrating that they cover only a restricted subset of the space spanned by LAION-natural.
- Unresolved: dataset, limitations, metric, signal modality

### Human-level control through deep reinforcement learning

- year: 2015 [Crossref strict title match]
- venue: Nature [Crossref strict title match]
- doi: 10.1038/nature14236 [Crossref strict title match]
- method: Reinforcement learning/bandit [Zotero BIB title/abstract/keywords]
  Evidence: Human-level control through deep reinforcement learning.
- Unresolved: dataset, limitations, metric, signal modality, task

### Human2Robot: Learning Robot Actions from Paired Human-Robot Videos

- year: 2026 [Crossref strict title match]
- venue: Proceedings of the AAAI Conference on Artificial Intelligence [Crossref strict title match]
- doi: 10.1609/aaai.v40i13.38086 [Crossref strict title match]
- task: Representation alignment, Dataset/benchmark [Zotero BIB title/abstract/keywords]
  Evidence: Representation alignment, Dataset/benchmark; evidence: Existing methods, which often rely on coarsely-aligned video pairs, are typically constrained to learning global or task-level features.
- limitations: source-traced limitation/caveat sentence [Zotero BIB title/abstract/keywords]
  Evidence: Existing methods, which often rely on coarsely-aligned video pairs, are typically constrained to learning global or task-level features.
- Unresolved: dataset, method, metric, signal modality

## Structured Manual-Review Schema Addendum

The manual-review artifact has been migrated from flat `Missing or unresolved` lines into a structured schema with four blocks:

- Bibliographic: `year`, `venue`, `doi`.
- Paper type: `primary_research`, `review`, `perspective`, `theory`, `benchmark`, `dataset`, or `system`.
- Evidence fields: `signal_modality`, `input_modality`, `task_taxonomy`, `paper_objective`, `method_family`, `method_summary`, `dataset`, `dataset_role`, `metric`, `metric_status`, `limitations`, and `limitation_source`.
- Verification: `final_unresolved_fields`, `verification_status`, `evidence_sources`, `evidence_tier`, and `confidence`.

Multi-agent review plus public-source checks found that most remaining `metric` and one `dataset` residue were applicability issues, not missing facts. Review, perspective, theory, and survey entries without paper-specific quantitative evaluation now use `metric_status: not_applicable` and `dataset_role: none_review` where appropriate.

After restructuring, the active manual-review queue contains only applicable unresolved targets:

- DOI: 4 workshop/OpenReview-style records where no trusted canonical DOI has been accepted.
- Limitations: 2 empirical primary-research records that still require original-paper limitation evidence.

The export and preview scripts now parse `final_unresolved_fields`, preserve structured status metadata, and avoid re-exporting `metric_status: not_applicable` as a missing `metric`.
