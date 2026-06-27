# Manual Review Needed

Schema version: structured-manual-review-v1

This report uses the structured Paper-RAG++ review schema. It separates bibliographic facts, paper type, evidence fields, and final verification state so review/perspective papers can be closed with explicit `not_applicable` statuses instead of ambiguous unresolved fields.

## Summary

- entries: 177
- entries with final unresolved fields: 6
- unresolved doi: 4
- unresolved limitations: 2
- paper types: benchmark=31, dataset=1, perspective=3, primary_research=92, review=12, system=34, theory=4

## Schema

Bibliographic: year, venue, doi.
Paper type: primary_research | review | perspective | theory | benchmark | dataset | system.
Evidence fields: signal_modality, input_modality, task_taxonomy, paper_objective, method_family, method_summary, dataset, dataset_role, metric, metric_status, limitations, limitation_source.
Verification: final_unresolved_fields, verification_status, evidence_sources, evidence_tier, confidence.

## Priority Entries

### Hopfield Networks is All You Need

Bibliographic:
- year: 2020
- venue: International Conference on Learning Representations
- doi: 10.48550/arXiv.2008.02217

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: General ML method evaluation across transformer analysis, multiple instance learning, immune repertoire classification, small-data classification, and drug-design prediction.
- paper_objective: General ML method evaluation across transformer analysis, multiple instance learning, immune repertoire classification, small-data classification, and drug-design prediction.
- method_family: Modern continuous-state Hopfield networks / Hopfield layers whose update rule is equivalent to transformer attention; used as pooling, memory, association, and attention layers.
- method_summary: Modern continuous-state Hopfield networks / Hopfield layers whose update rule is equivalent to transformer attention; used as pooling, memory, association, and attention layers.
- dataset: Immune repertoire classification datasets; MIL benchmarks Tiger, Fox, Elephant, UCSB Breast Cancer; UCI small classification benchmark collection; drug-design datasets HIV, BACE, BBBP, and SIDER.
- dataset_role: used
- metric: AUC for MIL and immune repertoire classification; average rank with Wilcoxon signed-rank testing for UCI benchmarks; benchmark AUC-style scores for drug-design datasets including SIDER and BACE.
- metric_status: applicable
- limitations: Experimental boundary: the BERT attention-head analysis used the BERT-small setting, with 12 layers, 4 heads, reduced hidden size and sequence length shortened to 128 to keep training time manageable; broader transformer-scale conclusions should be read within that setup.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://www.semanticscholar.org/paper/804a6d7c23335bbca6eec3b7d3c8366dcbe395a5; https://openreview.net/forum?id=tL89RnzIiCd; https://arxiv.org/abs/2008.02217; https://arxiv.org/pdf/2008.02217
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=Paper text lists immune repertoire classification, MIL datasets, UCI benchmarks, and drug-design datasets. | confidence=high
- doi: evidence=arXiv page cites DOI link https://doi.org/10.48550/arXiv.2008.02217. | confidence=high
- limitations: evidence=The arXiv/OpenReview paper states that transformer architectures have high computational demands and that the authors adopted BERT-small and shortened sequence length to keep training manageable. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=Abstract states the new Hopfield update rule is equivalent to transformer attention. | confidence=high
- metric: evidence=Tables/text report MIL results in AUC, UCI average-rank comparisons, and drug-design benchmark values. | confidence=high
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=The evaluated tasks are ML/NLP/classification/drug-design benchmarks, not neural recordings. | confidence=high
- task_taxonomy: evidence=OpenReview abstract says broad applicability is demonstrated across MIL, immune repertoire classification, UCI small classification tasks, and drug-design datasets. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: Hopfield Networks is All You Need
- auto_source_url: https://www.semanticscholar.org/paper/804a6d7c23335bbca6eec3b7d3c8366dcbe395a5

### Neural Encoding and Decoding at Scale

Bibliographic:
- year: 2025
- venue: International Conference on Machine Learning
- doi: 10.48550/arXiv.2504.08201

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Neuropixels spike-sorted neural activity; appendix includes Utah-array monkey reaching data.
- input_modality: spiking/electrophysiology
- task_taxonomy: Neural decoding, Encoding model
- paper_objective: Neural decoding, Encoding model
- method_family: NEDS, a multimodal transformer with modality-specific tokenization and multi-task masking.
- method_summary: NEDS, a multimodal transformer with modality-specific tokenization and multi-task masking.
- dataset: International Brain Laboratory repeated site dataset: Neuropixels recordings from 83 mice; appendix also evaluates MC-RTT monkey reaching dataset.
- dataset_role: used
- metric: Encoding measured by bits per spike; decoding measured by accuracy and single-trial R-squared.
- metric_status: applicable
- limitations: Relies on trial-aligned data, limiting pretraining data scale; computational constraints limited hyperparameter tuning; human-data extensions require privacy and consent care.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://www.semanticscholar.org/paper/997d6559029b8cf93b59055848c02ef5171398be; https://proceedings.mlr.press/v267/zhang25bw.html; https://arxiv.org/abs/2504.08201
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=PMLR abstract says the method is pretrained on IBL repeated site recordings from 83 animals. | confidence=high
- limitations: evidence=Discussion states reliance on trial-aligned data, limited hyperparameter tuning, and human-data privacy concerns. | confidence=high
- method_summary: evidence=PMLR abstract and PDF methods describe a multimodal, multi-task NEDS model. | confidence=high
- metric: evidence=PDF tables and metric text report bits per spike, accuracy, and R-squared. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Dataset section states trial-aligned, spike-sorted Neuropixels recordings. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: Neural Encoding and Decoding at Scale
- auto_source_url: https://www.semanticscholar.org/paper/997d6559029b8cf93b59055848c02ef5171398be

### Neural Encoding and Decoding at Scale

Bibliographic:
- year: 2025
- venue: International Conference on Machine Learning
- doi: 10.48550/arXiv.2504.08201

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Neuropixels spike-sorted neural activity; appendix includes Utah-array monkey reaching data.
- input_modality: spiking/electrophysiology
- task_taxonomy: Neural decoding, Encoding model
- paper_objective: Neural decoding, Encoding model
- method_family: NEDS multimodal transformer using multi-task masking.
- method_summary: NEDS multimodal transformer using multi-task masking.
- dataset: International Brain Laboratory repeated site dataset: Neuropixels recordings from 83 mice; appendix also evaluates MC-RTT monkey reaching dataset.
- dataset_role: used
- metric: Bits per spike, choice/block accuracy, wheel/whisker R-squared, and brain-region classification accuracy.
- metric_status: applicable
- limitations: Trial-aligned data limits pretraining scale; computational constraints limited hyperparameter tuning; human-data extensions require privacy and consent care.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://www.semanticscholar.org/paper/997d6559029b8cf93b59055848c02ef5171398be; https://proceedings.mlr.press/v267/zhang25bw.html; https://arxiv.org/abs/2504.08201
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Duplicate entry verified from the same PMLR/arXiv sources as idx 2. | confidence=high
- limitations: evidence=Duplicate entry verified from the same PDF discussion as idx 2. | confidence=high
- method_summary: evidence=Duplicate entry verified from the same PMLR abstract/PDF methods as idx 2. | confidence=high
- metric: evidence=Duplicate entry verified from the same PDF tables/metric sections as idx 2. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Duplicate entry verified from the same dataset and appendix text as idx 2. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: Neural Encoding and Decoding at Scale
- auto_source_url: https://www.semanticscholar.org/paper/997d6559029b8cf93b59055848c02ef5171398be

### SecureLLM: New private and confidential interfaces with LLMs

Bibliographic:
- year: 2025
- venue: IUI Workshops
- doi: unresolved

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: text/speech
- task_taxonomy: Private/confidential LLM interfaces for access-controlled silo composition, data-loss/anomaly detection, and leak identification.
- paper_objective: Private/confidential LLM interfaces for access-controlled silo composition, data-loss/anomaly detection, and leak identification.
- method_family: Large language model
- method_summary: Large language model
- dataset: Secure-NL2SQL / SecureSQL generated disjoint SQL-silo dataset; CrossoverFanFic dataset compiled from ArchiveOfOurOwn fandom text.
- dataset_role: created
- metric: Normalized SQL tree edit distance with accuracy; ROC AUC; F1-score and weighted average accuracy.
- metric_status: applicable
- limitations: Practical applications would need a stronger underlying LLM to achieve high execution accuracy.
- limitation_source: discussion

Verification:
- final_unresolved_fields: doi
- verification_status: needs_human_review
- evidence_sources: https://www.semanticscholar.org/paper/bdaf27e85aab4397b33acc26533abdeeb5856f1a; https://ceur-ws.org/Vol-3957/; https://ceur-ws.org/Vol-3957/MIND-paper04.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=PDF data-generation section defines Secure-NL2SQL and CrossoverFanFic. | confidence=high
- limitations: evidence=Conclusion states practical applications would need a stronger underlying LLM. | confidence=high
- metric: evidence=Tables report normalized tree edit distance, AUC, F1 and weighted accuracy. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The paper evaluates LLM security and text/SQL datasets, not neural recordings. | confidence=high
- task_taxonomy: evidence=Abstract lists user, group, and organization-level LLM security capabilities. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: SecureLLM: New private and confidential interfaces with LLMs
- auto_source_url: https://www.semanticscholar.org/paper/bdaf27e85aab4397b33acc26533abdeeb5856f1a

### TOPONETS: HIGH PERFORMING VISION AND LAN- GUAGE MODELS WITH BRAIN-LIKE TOPOGRAPHY

Bibliographic:
- year: 2025
- venue: International Conference on Learning Representations
- doi: 10.48550/arXiv.2501.16396

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Artificial neural network activations with brain-response comparisons using fMRI/visual cortex benchmarks and language-cortex evidence.
- input_modality: fMRI
- task_taxonomy: Induce brain-like topographic organization in vision and language models while preserving task performance.
- paper_objective: Induce brain-like topographic organization in vision and language models while preserving task performance.
- method_family: TopoLoss, a topographic loss added to training, applied to ResNet, ViT, GPT-Neo, and NanoGPT.
- method_summary: TopoLoss, a topographic loss added to training, applied to ResNet, ViT, GPT-Neo, and NanoGPT.
- dataset: ImageNet; Wikipedia; FineWeb-Edu; OpenWebText; Natural Scenes Dataset and BrainScore for brain-response evaluation.
- dataset_role: used
- metric: ImageNet validation accuracy, BLiMP accuracy, smoothness/topography, effective dimensionality, perplexity, unit-to-voxel correlation R, and BrainScore regional scores.
- metric_status: applicable
- limitations: Further work is required to explore scalability and larger architectures.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://www.semanticscholar.org/paper/73dd4c6a593f5efe7ae67cdf1bdd491295e37906; https://openreview.net/forum?id=THqWPzL00e; https://arxiv.org/abs/2501.16396
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Methods state language models trained on Wikipedia and FineWeb-Edu, vision models on ImageNet, and brain-response analyses use Natural Scenes Dataset and BrainScore. | confidence=high
- limitations: evidence=Discussion states limitations around scalability and larger architectures. | confidence=high
- method_summary: evidence=Abstract and methods describe TopoLoss for spatially organized topographic representations. | confidence=high
- metric: evidence=Results report ImageNet accuracy, BLiMP, smoothness, effective dimensionality, perplexity, unit-to-voxel correlations, and BrainScore. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Paper evaluates ANN topography against brain responses and published brain-response benchmarks. | confidence=medium
- task_taxonomy: evidence=OpenReview abstract states the goal is inducing topography in AI models. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: TopoNets: High Performing Vision and Language Models with Brain-Like Topography
- auto_source_url: https://www.semanticscholar.org/paper/73dd4c6a593f5efe7ae67cdf1bdd491295e37906

### Towards Brain-to-Text Generation: Neural Decoding with Pre-trained Encoder-Decoder Models

Bibliographic:
- year: 2021
- venue: NeurIPS 2021 AI for Science Workshop: Mind the Gaps / NeurIPS-AI4Science Poster
- doi: unresolved

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: fMRI
- input_modality: fMRI
- task_taxonomy: Neural decoding, Encoding model, Speech/language decoding, Continual/adaptive learning
- paper_objective: Neural decoding, Encoding model, Speech/language decoding, Continual/adaptive learning
- method_family: Pre-trained BART encoder-decoder neural decoder with ridge regression, CSLS retrieval, and fMRI feature fusion into BART hidden states.
- method_summary: Pre-trained BART encoder-decoder neural decoder with ridge regression, CSLS retrieval, and fMRI feature fusion into BART hidden states.
- dataset: Brain imaging data from prior fMRI dataset: 180 fMRI images for 180 content words from 15 participants; 5,000 selected voxels.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: doi
- verification_status: needs_human_review
- evidence_sources: https://www.semanticscholar.org/paper/9aa14630c939ae75509ce90d88654e58400228ef; https://openreview.net/forum?id=13IJlk221xG; https://openreview.net/pdf?id=13IJlk221xG
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=PDF states brain imaging data contains 180 fMRI images for 180 content words from 15 participants. | confidence=high
- method_summary: evidence=PDF describes extracting semantic features from fMRI, ridge regression, CSLS retrieval, and BART fusion. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=PDF experiments specify fMRI images. | confidence=high
- venue: evidence=OpenReview lists NeurIPS-AI4Science Poster. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: Towards Brain-to-Text Generation: Neural Decoding with Pre-trained Encoder-Decoder Models
- auto_source_url: https://www.semanticscholar.org/paper/9aa14630c939ae75509ce90d88654e58400228ef

### 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities

Bibliographic:
- year: 2025
- venue: NeurIPS
- doi: 10.48550/arXiv.2503.14858

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Foundation model/pretraining
- paper_objective: Foundation model/pretraining
- method_family: Contrastive learning, Masked autoencoder/pretraining, Reinforcement learning/bandit
- method_summary: Contrastive learning, Masked autoencoder/pretraining, Reinforcement learning/bandit
- dataset: JaxGCRL benchmark experiments based on Brax and MJX environments.
- dataset_role: used
- metric: Number of time steps out of 1000 near the goal; average score over the last five training epochs.
- metric_status: applicable
- limitations: Compute cost/latency of scaling depth; scaling beyond 1024 layers was not possible due to computational constraints.
- limitation_source: explicit

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: http://papers.nips.cc/paper_files/paper/2025/hash/e74ee34cc0f2d0780f34ee77d8fba25b-Abstract-Conference.html; https://papers.nips.cc/paper_files/paper/2025/hash/e74ee34cc0f2d0780f34ee77d8fba25b-Abstract-Conference.html; https://arxiv.org/abs/2503.14858
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Paper states all RL experiments use JaxGCRL based on Brax and MJX. | confidence=high
- doi: evidence=arXiv page lists DOI 10.48550/arXiv.2503.14858. | confidence=high
- limitations: evidence=Limitations section says scaling network depth has compute cost and beyond 1024 layers was computationally constrained. | confidence=high
- metric: evidence=Experimental setup says evaluation measures time steps out of 1000 near the goal. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Self-supervised reinforcement learning on simulated tasks, not neural signals. | confidence=high

Identity trace:
- auto_verification_status: source-traced via DBLP strict title match
- auto_matched_title: 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities.
- auto_source_url: http://papers.nips.cc/paper_files/paper/2025/hash/e74ee34cc0f2d0780f34ee77d8fba25b-Abstract-Conference.html

### A Unified Latent Schrodinger Bridge Diffusion Model for Unsupervised Anomaly Detection and Localization

Bibliographic:
- year: 2025
- venue: CVPR
- doi: 10.1109/CVPR52734.2025.02377

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Representation alignment, Dataset/benchmark
- paper_objective: Representation alignment, Dataset/benchmark
- method_family: Diffusion/generative model, Linear/encoding baseline
- method_summary: Diffusion/generative model, Linear/encoding baseline
- dataset: MVTec-AD and VisA industrial anomaly detection datasets.
- dataset_role: used
- metric: AUROC, AP, and F1max for image-level anomaly detection and pixel-level anomaly localization.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://openaccess.thecvf.com/content/CVPR2025/html/Akshay_A_Unified_Latent_Schrodinger_Bridge_Diffusion_Model_for_Unsupervised_Anomaly_CVPR_2025_paper.html
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=PDF experiments section says the method is validated on MVTec-AD and VisA. | confidence=high
- metric: evidence=PDF evaluation section names AUROC, AP, and F1max. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Computer vision anomaly detection/localization using images, not neural recordings. | confidence=high

Identity trace:
- auto_verification_status: source-traced via DBLP strict title match
- auto_matched_title: A Unified Latent Schrodinger Bridge Diffusion Model for Unsupervised Anomaly Detection and Localization.
- auto_source_url: https://openaccess.thecvf.com/content/CVPR2025/html/Akshay_A_Unified_Latent_Schrodinger_Bridge_Diffusion_Model_for_Unsupervised_Anomaly_CVPR_2025_paper.html

### Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data

Bibliographic:
- year: 2025
- venue: 2025 IEEE/CVF International Conference on Computer Vision (ICCV)
- doi: 10.1109/iccv51701.2025.01239

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: motion
- task_taxonomy: Zero-shot text-to-motion / human motion generation from textual descriptions.
- paper_objective: Zero-shot text-to-motion / human motion generation from textual descriptions.
- method_family: Web-scale human motion annotation pipeline plus FSQ motion tokenization and scalable text-conditioned autoregressive transformer.
- method_summary: Web-scale human motion annotation pipeline plus FSQ motion tokenization and scalable text-conditioned autoregressive transformer.
- dataset: MotionMillion and MotionMillion-Eval; comparisons also reference HumanML3D, MotionX, and MotionUnion.
- dataset_role: used
- metric: MPJPE, acceleration, FID, R-precision, and human evaluation dimensions.
- metric_status: applicable
- limitations: Metrics may not fully reflect model capabilities; vanilla FSQ causes jitter; larger models show limited gains on physical feasibility and smoothness.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/iccv51701.2025.01239; https://openaccess.thecvf.com/content/ICCV2025/papers/Fan_Go_to_Zero_Towards_Zero-shot_Motion_Generation_with_Million-scale_Data_ICCV_2025_paper.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Abstract and benchmark section state MotionMillion and MotionMillion-Eval. | confidence=high
- limitations: evidence=Paper says metrics cannot fully reflect capabilities and FSQ causes jitter. | confidence=medium
- method_summary: evidence=Architecture section describes FSQ tokenization and transformer scaling. | confidence=high
- metric: evidence=Tables/sections report MPJPE, acceleration, FID, R@1/R@2/R@3, and human evaluation. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Text-conditioned human motion generation, not neural signals. | confidence=high
- task_taxonomy: evidence=Abstract states zero-shot text-to-motion generation. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Go to Zero: Towards Zero-Shot Motion Generation with Million-Scale Data
- auto_source_url: https://doi.org/10.1109/iccv51701.2025.01239

### MG-MotionLLM: A Unified Framework for Motion Comprehension and Generation across Multiple Granularities

Bibliographic:
- year: 2025
- venue: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
- doi: 10.1109/cvpr52734.2025.02593

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: motion
- task_taxonomy: Unified multi-granular motion comprehension and generation.
- paper_objective: Unified multi-granular motion comprehension and generation.
- method_family: Motion VQ-VAE plus T5-based motion-aware language model with two-stage training.
- method_summary: Motion VQ-VAE plus T5-based motion-aware language model with two-stage training.
- dataset: HumanML3D and FineMotion.
- dataset_role: used
- metric: FID, MM-Dist, R-Precision, Diversity, BLEU, ROUGE, BERTScore.
- metric_status: applicable
- limitations: Focuses mainly on body movements, leaving facial expressions and hand gestures unexplored.
- limitation_source: explicit

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/cvpr52734.2025.02593; https://openaccess.thecvf.com/content/CVPR2025/html/Wu_MG-MotionLLM_A_Unified_Framework_for_Motion_Comprehension_and_Generation_across_CVPR_2025_paper.html
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Experimental setup says evaluations use HumanML3D and FineMotion. | confidence=high
- limitations: evidence=Appendix H lists limitations around body movements, facial/hand details, and interactions. | confidence=high
- method_summary: evidence=Method section states MG-MotionLLM consists of motion VQ-VAE and T5-based language model. | confidence=high
- metric: evidence=Evaluation metrics section lists FID, MM-Dist, R-Precision, Diversity, BLEU, ROUGE, and BERTScore. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Human motion-language modeling using motion sequences and text, not neural recordings. | confidence=high
- task_taxonomy: evidence=Abstract and task table list multi-granular motion tasks. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: MG-MotionLLM: A Unified Framework for Motion Comprehension and Generation across Multiple Granularities
- auto_source_url: https://doi.org/10.1109/cvpr52734.2025.02593

### MG-MotionLLM: A Unified Framework for Motion Comprehension and Generation across Multiple Granularities

Bibliographic:
- year: 2025
- venue: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
- doi: 10.1109/cvpr52734.2025.02593

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: motion
- task_taxonomy: Multi-granular human motion-language tasks.
- paper_objective: Multi-granular human motion-language tasks.
- method_family: Motion VQ-VAE plus T5-based motion-aware language model.
- method_summary: Motion VQ-VAE plus T5-based motion-aware language model.
- dataset: HumanML3D and FineMotion
- dataset_role: used
- metric: FID, MM-Dist, R-Precision, Diversity, BLEU, ROUGE, BERTScore.
- metric_status: applicable
- limitations: Excludes generation tasks when only detailed descriptions are available; larger T5 size does not consistently improve all tasks because HumanML3D is limited in scale.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/cvpr52734.2025.02593; https://openaccess.thecvf.com/content/CVPR2025/html/Wu_MG-MotionLLM_A_Unified_Framework_for_Motion_Comprehension_and_Generation_across_CVPR_2025_paper.html
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Paper states evaluations use HumanML3D and FineMotion. | confidence=high
- limitations: evidence=It states tasks requiring generation from detailed descriptions are excluded and larger models can degrade because HumanML3D is small. | confidence=medium
- method_summary: evidence=The model consists of Motion VQ-VAE and T5-based motion-aware language model. | confidence=high
- metric: evidence=Evaluation metrics include FID, MM-Dist, R-Precision, Diversity, BLEU, ROUGE, and BERTScore. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Human motion-text data, not neural recordings. | confidence=high
- task_taxonomy: evidence=Abstract and experiments name text-to-motion, motion-to-text, localization, and editing tasks. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: MG-MotionLLM: A Unified Framework for Motion Comprehension and Generation across Multiple Granularities
- auto_source_url: https://doi.org/10.1109/cvpr52734.2025.02593

### MiSO: Optimizing brain stimulation to create neural population activity states

Bibliographic:
- year: 2024
- venue: Advances in Neural Information Processing Systems 37
- doi: 10.52202/079017-0760

Paper type:
- type: system

Evidence fields:
- signal_modality: Multi-electrode spiking activity in macaque prefrontal cortex with electrical microstimulation
- input_modality: spiking/electrophysiology
- task_taxonomy: Representation alignment, Closed-loop BCI
- paper_objective: Representation alignment, Closed-loop BCI
- method_family: CNN/RNN deep model
- method_summary: CNN/RNN deep model
- dataset: Closed-loop non-human primate experiment with a macaque monkey and 96-electrode Utah array in prefrontal cortex area 8Ar.
- dataset_role: used
- metric: L1 error/distance between induced latent activity and target state; prediction MSE; statistical tests; spatial-response correlation.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.52202/079017-0760; https://proceedings.neurips.cc/paper_files/paper/2024/hash/2af641762dc02035c31a9314b2d090b6-Abstract-Conference.html
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Experiment details describe electrical microstimulation in a macaque with a 96-electrode Utah array. | confidence=high
- metric: evidence=Closed-loop optimization minimizes L1 distance and figures report MSE, p-values, and spatial correlations. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Paper states spiking activity was recorded from a multi-electrode array implanted in PFC. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: MiSO: Optimizing brain stimulation to create neural activity states
- auto_source_url: https://doi.org/10.52202/079017-0760

### ScaMo: Exploring the Scaling Law in Autoregressive Motion Generation Model

Bibliographic:
- year: 2025
- venue: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
- doi: 10.1109/cvpr52734.2025.02595

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: motion
- task_taxonomy: Text-driven human motion generation and scaling-law analysis.
- paper_objective: Text-driven human motion generation and scaling-law analysis.
- method_family: Motion FSQ-VAE plus text-prefix autoregressive transformer with frozen T5-XL text encoder.
- method_summary: Motion FSQ-VAE plus text-prefix autoregressive transformer with frozen T5-XL text encoder.
- dataset: MotionUnion plus HumanML3D.
- dataset_role: used
- metric: Reconstruction loss, MPJPE, codebook utilization, entropy, FID, R-Precision, matching score, and normalized loss.
- metric_status: applicable
- limitations: FID is biased toward the motion domain and pretrained motion features make model differences hard to distinguish.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/cvpr52734.2025.02595; https://arxiv.org/abs/2412.14559
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Paper introduces MotionUnion and evaluates tokenizers using HumanML3D and MotionUnion. | confidence=high
- limitations: evidence=It states FID is biased and pretrained motion features make model differences hard to distinguish. | confidence=medium
- method_summary: evidence=Abstract and method describe Motion FSQ-VAE, T5-XL embeddings, and autoregressive generator. | confidence=high
- metric: evidence=Experiment settings list reconstruction loss, MPJPE, codebook utilization, entropy, FID, R-precision, matching score, and normalized loss. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Text-motion datasets and generated human motion, not neural recordings. | confidence=high
- task_taxonomy: evidence=Paper frames the work as text-driven motion generation and scaling-law verification. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: ScaMo: Exploring the Scaling Law in Autoregressive Motion Generation Model
- auto_source_url: https://doi.org/10.1109/cvpr52734.2025.02595

### ScaMo: Exploring the Scaling Law in Autoregressive Motion Generation Model

Bibliographic:
- year: 2025
- venue: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
- doi: 10.1109/cvpr52734.2025.02595

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: motion
- task_taxonomy: Text-driven human motion generation and scaling-law analysis.
- paper_objective: Text-driven human motion generation and scaling-law analysis.
- method_family: Motion FSQ-VAE plus text-prefix autoregressive transformer with frozen T5-XL text encoder.
- method_summary: Motion FSQ-VAE plus text-prefix autoregressive transformer with frozen T5-XL text encoder.
- dataset: MotionUnion plus HumanML3D.
- dataset_role: used
- metric: Reconstruction loss, MPJPE, codebook utilization, entropy, FID, R-Precision, matching score, and normalized loss.
- metric_status: applicable
- limitations: FID is biased toward the motion domain and pretrained motion features make model differences hard to distinguish.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/cvpr52734.2025.02595; https://arxiv.org/abs/2412.14559
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Duplicate entry verified from the same ScaMo sources as idx 13. | confidence=high
- limitations: evidence=Duplicate entry verified from same ScaMo discussion as idx 13. | confidence=medium
- method_summary: evidence=Duplicate entry verified from same ScaMo method as idx 13. | confidence=high
- metric: evidence=Duplicate entry verified from same ScaMo experiment settings as idx 13. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Duplicate entry verified from same ScaMo source as idx 13. | confidence=high
- task_taxonomy: evidence=Duplicate entry verified from same ScaMo source as idx 13. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: ScaMo: Exploring the Scaling Law in Autoregressive Motion Generation Model
- auto_source_url: https://doi.org/10.1109/cvpr52734.2025.02595

### World Action Models are Zero-shot Policies

Bibliographic:
- year: 2026
- venue: arXiv.org
- doi: 10.48550/arXiv.2602.15922

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Representation alignment, Foundation model/pretraining
- paper_objective: Representation alignment, Foundation model/pretraining
- method_family: Diffusion/generative model, Masked autoencoder/pretraining
- method_summary: Diffusion/generative model, Masked autoencoder/pretraining
- dataset: AgiBot G1 teleoperation corpus; DROID; YAM robot and egocentric human transfer demonstrations.
- dataset_role: used
- metric: Average task progress, success rate, standard error, inference speed/latency/Hz, and speedup.
- metric_status: applicable
- limitations: WAM scaling laws lack evidence; human-data transfer is small-scale; computationally expensive; short-horizon context.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://www.semanticscholar.org/paper/badf8adcf2b6a6780a308881de75f148a4cacea0; https://arxiv.org/abs/2602.15922
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Paper reports AgiBot G1 data, DROID, and YAM/human demonstrations. | confidence=high
- limitations: evidence=Discussion notes missing scaling-law evidence, small human transfer data, high computational cost, and short-horizon memory. | confidence=high
- metric: evidence=Evaluation uses task progress, success rate, and speed metrics. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Robot video, actions, proprioception, and language instructions; no neural signals. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: World Action Models are Zero-shot Policies
- auto_source_url: https://www.semanticscholar.org/paper/badf8adcf2b6a6780a308881de75f148a4cacea0

### 🦩 Flamingo: a Visual Language Model for Few-Shot Learning

Bibliographic:
- year: 2022
- venue: Advances in Neural Information Processing Systems 35
- doi: 10.52202/068431-1723

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Multimodal neural data, Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Foundation model/pretraining, Dataset/benchmark
- paper_objective: Foundation model/pretraining, Dataset/benchmark
- method_family: Large language model, Masked autoencoder/pretraining, Linear/encoding baseline
- method_summary: Large language model, Masked autoencoder/pretraining, Linear/encoding baseline
- dataset: Training uses M3W, ALIGN, LTIP, and VTP; evaluation spans 16 multimodal image/video-language benchmarks.
- dataset_role: used
- metric: CIDEr for captioning, top-1/accuracy for VQA/classification-style tasks, and aggregate normalized score in ablations.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.52202/068431-1723; https://arxiv.org/abs/2204.14198
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=PDF describes training on M3W, ALIGN/LTIP image-text pairs, and VTP video-text pairs; evaluation uses 16 multimodal benchmarks. | confidence=high
- metric: evidence=PDF tables label COCO/VATEX with CIDEr and OKVQA/VQAv2 with top1. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Flamingo: A Visual Language Model for Few-Shot Learning
- auto_source_url: https://doi.org/10.52202/068431-1723

### A Brain-Media Deep Framework Towards Seeing Imaginations Inside Brains

Bibliographic:
- year: 2021
- venue: IEEE Transactions on Multimedia
- doi: 10.1109/tmm.2020.2999183

Paper type:
- type: system

Evidence fields:
- signal_modality: EEG
- input_modality: EEG
- task_taxonomy: EEG-based visualization/reconstruction of image-evoked brain activity into image-like brain-media.
- paper_objective: EEG-based visualization/reconstruction of image-evoked brain activity into image-like brain-media.
- method_family: Dual-conditioned, lateralization-supported GAN combining EEG-derived brain features and visual features.
- method_summary: Dual-conditioned, lateralization-supported GAN combining EEG-derived brain features and visual features.
- dataset: ImageNet-EEG and ObjectCategory-EEG.
- dataset_role: used
- metric: Classification precision/accuracy for EEG encoding and Inception Score for generated image quality.
- metric_status: applicable
- limitations: Limited to externally stimulated brain activity and not the same as reading minds or thoughts.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/tmm.2020.2999183
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Experimental section states two standard EEG datasets were adopted: ImageNet-EEG and ObjectCategory-EEG. | confidence=high
- limitations: evidence=Conclusion says the concept is not mind reading and is limited to external stimulation. | confidence=high
- method_summary: evidence=Abstract and method describe a dual-conditioned GAN with EEG and visual features. | confidence=high
- metric: evidence=Tables report classification precision and Inception Score. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Abstract says corresponding EEG sequences are collected. | confidence=high
- task_taxonomy: evidence=Paper frames the goal as visualizing brain activities evoked by natural images. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: A Brain-Media Deep Framework Towards Seeing Imaginations Inside Brains
- auto_source_url: https://doi.org/10.1109/tmm.2020.2999183

### A Perovskite Memristor with Large Dynamic Space for Analog-Encoded Image Recognition

Bibliographic:
- year: 2022
- venue: ACS Nano
- doi: 10.1021/acsnano.2c09569

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: ECoG
- task_taxonomy: Analog-encoded image recognition / Fashion-MNIST image classification.
- paper_objective: Analog-encoded image recognition / Fashion-MNIST image classification.
- method_family: Fully memristive reservoir computing system using solution-processed perovskite memristors with analog conductance states.
- method_summary: Fully memristive reservoir computing system using solution-processed perovskite memristors with analog conductance states.
- dataset: Fashion-MNIST.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1021/acsnano.2c09569; https://pubmed.ncbi.nlm.nih.gov/36519795/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=PubMed abstract states the image classification task used Fashion-MNIST. | confidence=high
- method_summary: evidence=Abstract reports a fully memristive reservoir computing architecture based on perovskite memristors. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Memristor reservoir computing and image classification, not biological neural recordings. | confidence=high
- task_taxonomy: evidence=Title and abstract identify analog-encoded image recognition and Fashion-MNIST classification. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: A Perovskite Memristor with Large Dynamic Space for Analog-Encoded Image Recognition
- auto_source_url: https://doi.org/10.1021/acsnano.2c09569

### A multi-agent system for automating scientific discovery

Bibliographic:
- year: 2026
- venue: Nature
- doi: 10.1038/s41586-026-10652-y

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Automated scientific discovery for experimental biology and dry AMD therapeutic hypothesis generation.
- paper_objective: Automated scientific discovery for experimental biology and dry AMD therapeutic hypothesis generation.
- method_family: Robin multi-agent workflow integrating literature-search agents with a Jupyter-native data-analysis agent.
- method_summary: Robin multi-agent workflow integrating literature-search agents with a Jupyter-native data-analysis agent.
- dataset: Dry AMD therapeutic discovery case using literature, ARPE-19/RPE phagocytosis flow-cytometry data, bulk RNA-seq data, plus Finch/BixBench-related evaluation material.
- dataset_role: used
- metric: Flow-cytometry MFI/phagocytosis fold-change, differential-expression adjusted p-values, GO enrichment, LLM-judge/expert concordance, and consistency measures.
- metric_status: applicable
- limitations: Robin does not yet produce precise executable protocols; Finch relies on domain-expert prompt engineering; LLM-judged hypothesis evaluation needs better alignment with human judgment.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41586-026-10652-y; https://www.nature.com/articles/s41586-026-10652-y; https://arxiv.org/abs/2505.13400
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Nature page lists flow-cytometry results and Finch/BixBench material; arXiv describes ARPE-19 assays and RNA-seq. | confidence=high
- limitations: evidence=Discussion states limitations around executable protocols, expert prompts, and LLM-judge alignment. | confidence=high
- method_summary: evidence=Abstract and methods describe integrating literature search agents with data analysis agents. | confidence=high
- metric: evidence=Paper reports phagocytosis, DGE adjusted p-values, GO enrichment, and LLM judge/expert agreement. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Inputs are literature, flow cytometry, RNA-seq, and agent outputs; no neural signal is used. | confidence=high
- task_taxonomy: evidence=Abstract states Robin identifies therapeutic candidates and supports hypothesis generation/data analysis. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: A multi-agent system for automating scientific discovery
- auto_source_url: https://doi.org/10.1038/s41586-026-10652-y

### A spatiotemporal style transfer algorithm for dynamic visual stimulus generation

Bibliographic:
- year: 2024
- venue: Nature Computational Science
- doi: 10.1038/s43588-024-00746-w

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Dynamic visual stimulus generation for vision science and model metamer testing.
- paper_objective: Dynamic visual stimulus generation for vision science and model metamer testing.
- method_family: Spatiotemporal Style Transfer, a two-stream neural style transfer framework matching layer activations and Gram-matrix texture statistics across videos.
- method_summary: Spatiotemporal Style Transfer, a two-stream neural style transfer framework matching layer activations and Gram-matrix texture statistics across videos.
- dataset: Natural videos including YouTube-8M clips; ImageNet1K-trained image models, Kinetics400-trained video models, KITTI-trained PredNet; validation dataset with n=100 videos.
- dataset_role: used
- metric: Low-level feature preservation, CKA activation similarity, SSIM/cSSIM, human caption embedding classification/cosine distance, and 2AFC perceptual similarity.
- metric_status: applicable
- limitations: Available video-generation methods are scarce; examples mainly manipulate texture/style; base optimization can have perceptual instability.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s43588-024-00746-w; https://www.nature.com/articles/s43588-024-00746-w; https://arxiv.org/abs/2403.04940
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Methods/arXiv text says YouTube-8M clips were used; Nature reports n=100 videos and model settings. | confidence=high
- limitations: evidence=Nature discussion says dynamic visual stimulus methods are scarce and examples manipulate texture/style; arXiv notes perceptual instabilities. | confidence=medium
- method_summary: evidence=Nature abstract and main text define STST as a two-stream dynamic stimulus generation framework. | confidence=high
- metric: evidence=Nature reports SSIM/cSSIM, CKA-like similarity, and human captioning/2AFC tasks. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Uses generated/natural videos, DNN activations, PredNet, and behavioral judgments, not neural recordings. | confidence=high
- task_taxonomy: evidence=Abstract says STST manipulates and synthesizes video stimuli for vision research. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: A spatiotemporal style transfer algorithm for dynamic visual stimulus generation
- auto_source_url: https://doi.org/10.1038/s43588-024-00746-w

### A unified acoustic-to-speech-to-language embedding space captures the neural basis of natural language processing in everyday conversations

Bibliographic:
- year: 2025
- venue: Nature Human Behaviour
- doi: 10.1038/s41562-025-02105-9

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Intracranial ECoG aligned with natural speech audio and transcripts.
- input_modality: spiking/electrophysiology
- task_taxonomy: Predict and characterize neural activity during speech comprehension and production in everyday conversations.
- paper_objective: Predict and characterize neural activity during speech comprehension and production in everyday conversations.
- method_family: Whisper acoustic, speech, and language embeddings were reduced with PCA and mapped to ECoG activity using electrode-wise linear encoding models with 10-fold held-out conversation testing and variance partitioning.
- method_summary: Whisper acoustic, speech, and language embeddings were reduced with PCA and mapped to ECoG activity using electrode-wise linear encoding models with 10-fold held-out conversation testing and variance partitioning.
- dataset: Dense natural-conversation ECoG/speech recordings from 4 epilepsy patients: about 50 h comprehension, 50 h production, 520,209 total words, with 644 usable left-hemisphere electrodes.
- dataset_role: used
- metric: Encoding performance was measured as correlation between predicted and actual neural signals, with multiple-comparison correction; reported correlations reached up to about 0.50.
- metric_status: applicable
- limitations: Experimental boundary: recordings came from 4 ECoG patients in an epilepsy unit, with analysis focused on left-hemisphere electrodes after excluding corrupted channels.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41562-025-02105-9; https://www.nature.com/articles/s41562-025-02105-9
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Nature abstract/results report ECoG across 100 h of speech production and comprehension from 4 participants, with about 50 h/289,971 words comprehension and 50 h/230,238 words production. | confidence=high
- limitations: evidence=Results section states only 1 participant had right-hemisphere coverage, so analyses focused on left-hemisphere electrodes; 10 electrodes were excluded as corrupted. | confidence=high
- method_summary: evidence=Figure 1 caption and Results describe Whisper embeddings, PCA to 50 dimensions, linear regression encoding models, and 10-fold cross-validation. | confidence=high
- metric: evidence=Methods/results describe calculating correlations between predicted and actual neural signals on held-out conversations. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Abstract states electrocorticography was used to record neural signals during conversations. | confidence=high
- task_taxonomy: evidence=Abstract states the goal was linking acoustic, speech, and linguistic structures to neural language processing in everyday conversations. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: A unified acoustic-to-speech-to-language embedding space captures the neural basis of natural language processing in everyday conversations
- auto_source_url: https://doi.org/10.1038/s41562-025-02105-9

### Accelerating scientific discovery with Co-Scientist

Bibliographic:
- year: 2026
- venue: Nature
- doi: 10.1038/s41586-026-10644-y

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline.
- input_modality: not specified
- task_taxonomy: Automating and accelerating scientific hypothesis generation and discovery.
- paper_objective: Automating and accelerating scientific hypothesis generation and discovery.
- method_family: AI co-scientist system for scientific discovery using multi-agent hypothesis generation, critique, ranking, and refinement with scientist-in-the-loop review.
- method_summary: AI co-scientist system for scientific discovery using multi-agent hypothesis generation, critique, ranking, and refinement with scientist-in-the-loop review.
- dataset: Empirical scientific-discovery case studies rather than a named dataset.
- dataset_role: used
- metric: Elo auto-evaluation rating; GPQA accuracy/top-1 accuracy; LLM-as-a-judge preference ranking; classifier AUC in ablations
- metric_status: applicable
- limitations: The evaluation includes preliminary human-seeded refinement findings, resource-intensive human expert evaluation supplemented by LLM-as-a-judge, single-institution oncologist review, drug-repurposing proposals not yet supported by randomized phase III trials, and a pilot proposal-evaluation rubric that omits full grant-review axes and still needs validation.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41586-026-10644-y; https://www.nature.com/articles/s41586-026-10644-y; https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-026-10644-y/MediaObjects/41586_2026_10644_MOESM1_ESM.pdf
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=Nature article page identifies the work as a 2026 Nature article on accelerating scientific discovery with Co-Scientist; accessible metadata does not expose a named dataset. | confidence=medium
- limitations: evidence=Nature supplementary text calls the human-seeded refinement result preliminary, describes human expert review as the gold standard but resource-intensive, notes the single-institution expert panel, states that proposed drug candidates lack randomized phase III trials, and says the rubric is a pilot framework that omits detailed grant-review elements and requires further validation. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=Article title and abstract context describe Co-Scientist as a system for scientific discovery; public descriptions identify it as a multi-agent scientist-in-the-loop system. | confidence=medium
- metric: evidence=Nature supplementary information states that the Elo auto-evaluation rating is a key metric, analyzes concordance with GPQA accuracy, reports top-1 accuracy, describes LLM-as-a-judge preference ranking, and reports classifier AUC for correctness in ablations. | confidence=high | tier=tier1_paper_text
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=The paper is an AI scientific-discovery system, not a neural-signal study. | confidence=high
- task_taxonomy: evidence=The title and article context directly frame the task as accelerating scientific discovery. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Accelerating scientific discovery with Co-Scientist
- auto_source_url: https://doi.org/10.1038/s41586-026-10644-y

### Adversarial Decoding: Generating Readable Documents for Adversarial Objectives

Bibliographic:
- year: 2026
- venue: Findings of the Association for Computational Linguistics: EACL 2026
- doi: 10.18653/v1/2026.findings-eacl.108

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline.
- input_modality: not specified
- task_taxonomy: Generate readable adversarial documents for RAG poisoning, LLM guard evasion, and jailbreaking.
- paper_objective: Generate readable adversarial documents for RAG poisoning, LLM guard evasion, and jailbreaking.
- method_family: Adversarial decoding augments beam search with objective-specific scoring functions, including readability, embedding-similarity/RAG, jailbreak, and evasion scorers.
- method_summary: Adversarial decoding augments beam search with objective-specific scoring functions, including readability, embedding-similarity/RAG, jailbreak, and evasion scorers.
- dataset: MS MARCO for retrieval/RAG poisoning and HarmBench for jailbreak and guard-evasion experiments.
- dataset_role: used
- metric: Retrieval rate, attack success rate, evasion ASR, jailbreak ASR, and overall ASR.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.18653/v1/2026.findings-eacl.108; https://aclanthology.org/2026.findings-eacl.108.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Paper references MS MARCO for retrieval experiments and HarmBench for harmful-instruction jailbreak/evasion evaluation. | confidence=high
- method_summary: evidence=Paper states AdvDec equips beam search with scoring functions for different adversarial objectives and readability. | confidence=high
- metric: evidence=Tables report retrieval rates and attack success rates; evasion section defines pure evasion, jailbreak ASR, and overall ASR. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=This is an NLP/security attack generation method, not a neural-signal paper. | confidence=high
- task_taxonomy: evidence=Abstract and contributions state the goal is readable documents for RAG poisoning and LLM guard evasion/jailbreak objectives. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Adversarial Decoding: Generating Readable Documents for Adversarial Objectives
- auto_source_url: https://doi.org/10.18653/v1/2026.findings-eacl.108

### AgiBot World Colosseo: Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems

Bibliographic:
- year: 2025
- venue: 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
- doi: 10.1109/iros60139.2025.11247088

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Embodied robot manipulation data, including vision, actions, and bimanual/visuo-tactile manipulation contexts.
- input_modality: image/video
- task_taxonomy: Representation alignment, Dataset/benchmark
- paper_objective: Representation alignment, Dataset/benchmark
- method_family: Full-stack embodied manipulation platform with AgiBot World data, benchmarks, and GO-1 generalist policy using a latent planner.
- method_summary: Full-stack embodied manipulation platform with AgiBot World data, benchmarks, and GO-1 generalist policy using a latent planner.
- dataset: AgiBot World robot manipulation dataset, including beta-scale data up to about 1M trajectories across large-scale real-world manipulation tasks.
- dataset_role: used
- metric: Normalized task-completion score averaged across rollouts; paper also reports success-rate improvements and over-60% success on complex tasks.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/iros60139.2025.11247088; https://arxiv.org/html/2503.06669v3; https://ieeexplore.ieee.org/document/11247088/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=arXiv page describes AgiBot World Colosseo as a large-scale robot-learning platform; search/source snippets report 1M trajectories and 217 tasks. | confidence=high
- method_summary: evidence=Paper describes the Colosseo platform and GO-1 policy with latent planner. | confidence=high
- metric: evidence=Evaluation section states normalized score is averaged across 10 rollouts per task/scenario/method and scores full or partial success. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Paper describes robot manipulation tasks across domestic, retail, industrial, restaurant, and office settings with bimanual and visuo-tactile examples. | confidence=medium

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems
- auto_source_url: https://doi.org/10.1109/iros60139.2025.11247088

### AgiBot World Colosseo: Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems

Bibliographic:
- year: 2025
- venue: 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
- doi: 10.1109/iros60139.2025.11247088

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Embodied robot manipulation data, including vision, actions, and bimanual/visuo-tactile manipulation contexts.
- input_modality: image/video
- task_taxonomy: Representation alignment, Dataset/benchmark
- paper_objective: Representation alignment, Dataset/benchmark
- method_family: Full-stack embodied manipulation platform with AgiBot World data, benchmarks, and GO-1 generalist policy using a latent planner.
- method_summary: Full-stack embodied manipulation platform with AgiBot World data, benchmarks, and GO-1 generalist policy using a latent planner.
- dataset: AgiBot World robot manipulation dataset, including beta-scale data up to about 1M trajectories across large-scale real-world manipulation tasks.
- dataset_role: used
- metric: Normalized task-completion score averaged across rollouts; paper also reports success-rate improvements and over-60% success on complex tasks.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/iros60139.2025.11247088; https://arxiv.org/html/2503.06669v3; https://ieeexplore.ieee.org/document/11247088/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=arXiv page describes AgiBot World Colosseo as a large-scale robot-learning platform; search/source snippets report 1M trajectories and 217 tasks. | confidence=high
- method_summary: evidence=Paper describes the Colosseo platform and GO-1 policy with latent planner. | confidence=high
- metric: evidence=Evaluation section states normalized score is averaged across 10 rollouts per task/scenario/method and scores full or partial success. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Paper describes robot manipulation tasks across domestic, retail, industrial, restaurant, and office settings with bimanual and visuo-tactile examples. | confidence=medium

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems
- auto_source_url: https://doi.org/10.1109/iros60139.2025.11247088

### An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion

Bibliographic:
- year: 2023
- venue: ICLR
- doi: 10.48550/arxiv.2208.01618

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Images plus natural-language text prompts.
- input_modality: image/video
- task_taxonomy: Personalized text-to-image generation for user-provided visual concepts.
- paper_objective: Personalized text-to-image generation for user-provided visual concepts.
- method_family: Optimize a new word/token embedding in the text-embedding space of a frozen text-to-image model, then compose that token in natural-language prompts.
- method_summary: Optimize a new word/token embedding in the text-embedding space of a frozen text-to-image model, then compose that token in natural-language prompts.
- dataset: User-provided concept examples: only 3-5 images per object or style concept.
- dataset_role: used
- metric: CLIP-space cosine similarity for reconstruction/image similarity and prompt/text similarity; user-study rankings/preference
- metric_status: applicable
- limitations: Experimental/method boundary: personalization is learned from a small set of concept images and represented as a new token embedding in a frozen text-to-image model.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://openreview.net/forum?id=NAQvF08TcyG; https://openreview.net/pdf?id=NAQvF08TcyG
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=OpenReview abstract states the method uses only 3-5 images of a user-provided concept. | confidence=high
- limitations: evidence=OpenReview abstract states the learned representation is a new word in the embedding space of a frozen text-to-image model. | confidence=medium
- method_summary: evidence=OpenReview abstract describes learning new words in embedding space and composing them in sentences. | confidence=high
- metric: evidence=The ICLR paper's Evaluation Metrics section evaluates reconstruction with average pairwise CLIP-space cosine similarity between generated images and concept images, evaluates prompt adherence with CLIP text-image cosine similarity, and adds a user study ranking visual similarity and context/text similarity. | confidence=high | tier=tier1_paper_text
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=The paper concerns image concepts and text-to-image generation. | confidence=high
- task_taxonomy: evidence=OpenReview TL;DR states the task is personalized text-to-image generation. | confidence=high

Identity trace:
- auto_verification_status: source-traced via DBLP strict title match
- auto_matched_title: An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion.
- auto_source_url: https://openreview.net/forum?id=NAQvF08TcyG

### AnyGrasp: Robust and Efficient Grasp Perception in Spatial and Temporal Domains

Bibliographic:
- year: 2022
- venue: CoRR
- doi: 10.48550/ARXIV.2212.08333

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Robot depth/RGB-D perception for 7-DoF grasp pose generation.
- input_modality: not specified
- task_taxonomy: Robotic grasp perception, dynamic grasp tracking, and grasp execution.
- paper_objective: Robotic grasp perception, dynamic grasp tracking, and grasp execution.
- method_family: Dense spatial-temporal supervision with real perception and analytic labels, center-of-mass awareness, and grasp correspondence for dynamic tracking.
- method_summary: Dense spatial-temporal supervision with real perception and analytic labels, center-of-mass awareness, and grasp correspondence for dynamic tracking.
- dataset: Cornell grasping dataset, multi-object evaluation data, household-object grasping tests, and bin-clearing with over 300 unseen objects.
- dataset_role: used
- metric: Cornell image-wise/object-wise accuracy, grasp localization and grasping success rate, bin-clearing success rate, and mean picks per hour.
- metric_status: applicable
- limitations: Method boundary: AnyGrasp is designed for parallel-gripper grasp perception.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.48550/arXiv.2212.08333; https://arxiv.org/abs/2212.08333; https://www.semanticscholar.org/paper/6e1c0a5f083db4ad691f54878aed36f284bde019
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Search and Semantic Scholar abstracts mention Cornell, multi-object/household tests, and over 300 unseen objects. | confidence=high
- limitations: evidence=Semantic Scholar abstract states AnyGrasp enables robots to grasp using a parallel gripper. | confidence=medium
- method_summary: evidence=Semantic Scholar abstract lists dense supervision, real perception/analytic labels, center-of-mass awareness, and grasp correspondence. | confidence=high
- metric: evidence=Sources report Cornell accuracies, 93.3% bin-clearing success, and over 900 mean-picks-per-hour. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The method generates 7-DoF dense grasp poses and is robust to depth-sensing noise. | confidence=high
- task_taxonomy: evidence=Abstract frames the work as grasp perception for robot prehensile manipulation. | confidence=high

Identity trace:
- auto_verification_status: source-traced via DBLP strict title match
- auto_matched_title: AnyGrasp: Robust and Efficient Grasp Perception in Spatial and Temporal Domains.
- auto_source_url: https://doi.org/10.48550/arXiv.2212.08333

### AnySkill: Learning Open-Vocabulary Physical Skill for Interactive Agents

Bibliographic:
- year: 2024
- venue: CVPR
- doi: 10.1109/CVPR52733.2024.00087

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline.
- input_modality: text/speech
- task_taxonomy: Open-vocabulary physical skill learning and interactive humanoid motion generation from text instructions.
- paper_objective: Open-vocabulary physical skill learning and interactive humanoid motion generation from text instructions.
- method_family: Hierarchical controller: low-level atomic actions learned via GAIL, and a high-level policy selects latent actions to maximize CLIP similarity between rendered images and text.
- method_summary: Hierarchical controller: low-level atomic actions learned via GAIL, and a high-level policy selects latent actions to maximize CLIP similarity between rendered images and text.
- dataset: Unlabeled reference motion clips and open-vocabulary text instructions in a physics-based humanoid simulation environment.
- dataset_role: used
- metric: CLIP similarity is used as reward; experiments report qualitative and quantitative measures against open-vocabulary motion-generation baselines.
- metric_status: applicable
- limitations: Authors state natural and interactive actions for open-vocabulary models remain an ongoing challenge.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/CVPR52733.2024.00087; https://openaccess.thecvf.com/content/CVPR2024/papers/Cui_AnySkill_Learning_Open-Vocabulary_Physical_Skill_for_Interactive_Agents_CVPR_2024_paper.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Paper describes a reference motion dataset M, unlabeled motions, open-vocabulary descriptions, simulation environment, and rendered images. | confidence=medium
- limitations: evidence=Introduction states creating natural and interactive actions for open-vocabulary models remains an ongoing challenge. | confidence=high
- method_summary: evidence=Abstract and method describe a GAIL-trained low-level controller and high-level CLIP-reward policy. | confidence=high
- metric: evidence=Abstract/method state the high-level policy maximizes CLIP similarity between rendered images and text. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=This is simulated embodied AI/control, not neural-signal data. | confidence=high
- task_taxonomy: evidence=Abstract states the method learns physically plausible interactions following open-vocabulary instructions. | confidence=high

Identity trace:
- auto_verification_status: source-traced via DBLP strict title match
- auto_matched_title: AnySkill: Learning Open-Vocabulary Physical Skill for Interactive Agents.
- auto_source_url: https://doi.org/10.1109/CVPR52733.2024.00087

### Attention is All you Need

Bibliographic:
- year: 2025
- venue: Advances in Neural Information Processing Systems 30, 2017.
- doi: 10.65215/nxvz2v36

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline.
- input_modality: not specified
- task_taxonomy: Sequence transduction and machine translation using the Transformer architecture.
- paper_objective: Sequence transduction and machine translation using the Transformer architecture.
- method_family: Transformer, CNN/RNN deep model
- method_summary: Transformer, CNN/RNN deep model
- dataset: WMT 2014 English-German and English-French machine-translation datasets, plus English constituency parsing experiments.
- dataset_role: used
- metric: generation quality
- metric_status: applicable
- limitations: Experimental boundary: empirical evaluation focused on sequence-transduction NLP tasks, especially machine translation and parsing.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.65215/nxvz2v36; https://papers.nips.cc/paper/7181-attention-is-all-you-need; https://arxiv.org/abs/1706.03762
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=NeurIPS paper page identifies the original 2017 paper; the paper reports WMT 2014 En-De/En-Fr translation and parsing evaluations. | confidence=high
- limitations: evidence=The verified scope of the paper is NLP sequence transduction, not neural or biosignal modeling. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The Transformer is a non-neural-signal NLP architecture. | confidence=high
- task_taxonomy: evidence=Title and paper describe replacing recurrence/convolution with attention for sequence transduction. | confidence=high
- venue: evidence=NeurIPS proceedings page lists the 2017 paper in NeurIPS/NIPS. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Attention Is All You Need
- auto_source_url: https://doi.org/10.65215/nxvz2v36

### Attention is All you Need

Bibliographic:
- year: 2025
- venue: Advances in Neural Information Processing Systems 30, 2017.
- doi: 10.65215/nxvz2v36

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline.
- input_modality: not specified
- task_taxonomy: Sequence transduction and machine translation using the Transformer architecture.
- paper_objective: Sequence transduction and machine translation using the Transformer architecture.
- method_family: Transformer, CNN/RNN deep model
- method_summary: Transformer, CNN/RNN deep model
- dataset: WMT 2014 English-German and English-French machine-translation datasets, plus English constituency parsing experiments.
- dataset_role: used
- metric: generation quality
- metric_status: applicable
- limitations: Experimental boundary: empirical evaluation focused on sequence-transduction NLP tasks, especially machine translation and parsing.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.65215/nxvz2v36; https://papers.nips.cc/paper/7181-attention-is-all-you-need; https://arxiv.org/abs/1706.03762
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=NeurIPS paper page identifies the original 2017 paper; the paper reports WMT 2014 En-De/En-Fr translation and parsing evaluations. | confidence=high
- limitations: evidence=The verified scope of the paper is NLP sequence transduction, not neural or biosignal modeling. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The Transformer is a non-neural-signal NLP architecture. | confidence=high
- task_taxonomy: evidence=Title and paper describe replacing recurrence/convolution with attention for sequence transduction. | confidence=high
- venue: evidence=NeurIPS proceedings page lists the 2017 paper in NeurIPS/NIPS. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Attention Is All You Need
- auto_source_url: https://doi.org/10.65215/nxvz2v36

### Brain–computer interface control with artificial intelligence copilots

Bibliographic:
- year: 2025
- venue: Nature Machine Intelligence
- doi: 10.1038/s42256-025-01090-y

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-invasive EEG.
- input_modality: EEG
- task_taxonomy: BCI cursor control and robotic-arm sequential pick-and-place with AI copilots.
- paper_objective: BCI cursor control and robotic-arm sequential pick-and-place with AI copilots.
- method_family: Hybrid adaptive decoding using a convolutional neural network and ReFIT-like Kalman filter, plus AI copilots for cursor and robotic-arm tasks.
- method_summary: Hybrid adaptive decoding using a convolutional neural network and ReFIT-like Kalman filter, plus AI copilots for cursor and robotic-arm tasks.
- dataset: Experimental EEG BCI data from healthy users and a participant with paralysis; data are available via Zenodo.
- dataset_role: used
- metric: Target hit rate for cursor control and robotic-arm pick-and-place task performance; abstract reports 3.9-times higher target-hit-rate performance with copilot.
- metric_status: applicable
- limitations: Author framing notes clinical viability requires BCI performance to outweigh costs and risks; demonstrated system is non-invasive EEG with AI shared autonomy.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s42256-025-01090-y; https://www.nature.com/articles/s42256-025-01090-y; https://doi.org/10.5281/zenodo.15165133
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Nature page states data are available via Zenodo; abstract mentions healthy users and a participant with paralysis. | confidence=high
- limitations: evidence=Abstract states BCIs face clinical viability obstacles because performance should outweigh costs and risks. | confidence=medium
- method_summary: evidence=Abstract names CNN plus ReFIT-like Kalman filter and two AI copilots. | confidence=high
- metric: evidence=Abstract reports 3.9-times higher target-hit-rate performance and robotic arm task completion enabled by copilot. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Abstract states the non-invasive BCI decodes electroencephalography signals. | confidence=high
- task_taxonomy: evidence=Abstract describes cursor control and robotic arm pick-and-place tasks. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Brain–computer interface control with artificial intelligence copilots
- auto_source_url: https://doi.org/10.1038/s42256-025-01090-y

### Brant: Foundation Model for Intracranial Neural Signal

Bibliographic:
- year: 2023
- venue: Advances in Neural Information Processing Systems 36
- doi: 10.52202/075280-1144

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Intracranial neural signals, specifically iEEG/SEEG.
- input_modality: EEG
- task_taxonomy: Visual reconstruction, Representation alignment, Foundation model/pretraining, Dataset/benchmark
- paper_objective: Visual reconstruction, Representation alignment, Foundation model/pretraining, Dataset/benchmark
- method_family: Brain Neural Transformer with temporal and spatial Transformer encoders, frequency encoding, patching, and masked autoencoder-style self-supervised reconstruction.
- method_summary: Brain Neural Transformer with temporal and spatial Transformer encoders, frequency encoding, patching, and masked autoencoder-style self-supervised reconstruction.
- dataset: Pretrained on 1.01 TB of SEEG intracranial neural recordings: 2528 h at 1000 Hz; downstream seizure-labeled dataset contains 29.39 GB and 43 h.
- dataset_role: used
- metric: correlation
- metric_status: applicable
- limitations: Authors note Brant has over 500M parameters, but brain-signal foundation models remain smaller than billion-parameter CV/NLP models and have further scaling potential.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.52202/075280-1144; https://papers.neurips.cc/paper_files/paper/2023/file/535915d26859036410b0533804cee788-Paper-Conference.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=NeurIPS paper states Brant is pretrained on 1.01 TB, 2528 h, and uses a 43 h downstream seizure-labeled intracranial dataset. | confidence=high
- limitations: evidence=Limitations/future-work text discusses model scale and future potential compared with CV/NLP foundation models. | confidence=medium
- method_summary: evidence=Method section describes temporal/spatial encoders, frequency encoding, patching, and masked reconstruction. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Abstract and introduction describe intracranial neural recordings/iEEG/SEEG. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Brant: Foundation Model for Intracranial Neural Signal
- auto_source_url: https://doi.org/10.52202/075280-1144

### CONDITIONAL DIFFUSION WITH ORDINAL REGRES- SION: LONGITUDINAL DATA GENERATION FOR NEURODEGENERATIVE DISEASE STUDIES

Bibliographic:
- year: 2025
- venue: International Conference on Learning Representations
- doi: unresolved

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Longitudinal Alzheimer's disease biomarker trajectories.
- input_modality: not specified
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: Diffusion/generative model, Linear/encoding baseline
- method_summary: Diffusion/generative model, Linear/encoding baseline
- dataset: Longitudinal neurodegenerative-disease data with experiments on four Alzheimer's disease biomarkers.
- dataset_role: used
- metric: Wasserstein distance (WD), root mean squared error (RMSE), and Jensen-Shannon divergence (JSD); the multi-domain table also reports test-set generation time and per-sequence generation time.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: doi
- verification_status: needs_human_review
- evidence_sources: https://www.semanticscholar.org/paper/5226db152c2623596f552c31e956085000b54b21; https://openreview.net/forum?id=9UGfOJBuL8; https://proceedings.iclr.cc/paper_files/paper/2025/hash/524ef58c2bd075775861234266e5e020-Abstract-Conference.html; https://proceedings.iclr.cc/paper_files/paper/2025/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=OpenReview abstract states extensive experiments were run on four AD biomarkers. | confidence=high
- metric: evidence=The official ICLR PDF states that three metrics were used to evaluate generated samples versus test data: WD, RMSE, and JSD. Tables 1-2 report WD/RMSE/JSD, with Table 2 additionally reporting generation time columns. | confidence=high | tier=tier1_paper_text
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=OpenReview abstract describes longitudinal sequences conditioned on age and disease severity for neurodegenerative disease progression. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: Conditional Diffusion with Ordinal Regression: Longitudinal Data Generation for Neurodegenerative Disease Studies
- auto_source_url: https://www.semanticscholar.org/paper/5226db152c2623596f552c31e956085000b54b21

### CONDITIONAL DIFFUSION WITH ORDINAL REGRES- SION: LONGITUDINAL DATA GENERATION FOR NEURODEGENERATIVE DISEASE STUDIES

Bibliographic:
- year: 2025
- venue: International Conference on Learning Representations
- doi: unresolved

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Longitudinal Alzheimer's disease biomarker trajectories.
- input_modality: not specified
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: Diffusion/generative model, Linear/encoding baseline
- method_summary: Diffusion/generative model, Linear/encoding baseline
- dataset: Longitudinal neurodegenerative-disease data with experiments on four Alzheimer's disease biomarkers.
- dataset_role: used
- metric: Wasserstein distance (WD), root mean squared error (RMSE), and Jensen-Shannon divergence (JSD); the multi-domain table also reports test-set generation time and per-sequence generation time.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: doi
- verification_status: needs_human_review
- evidence_sources: https://www.semanticscholar.org/paper/5226db152c2623596f552c31e956085000b54b21; https://openreview.net/forum?id=9UGfOJBuL8; https://proceedings.iclr.cc/paper_files/paper/2025/hash/524ef58c2bd075775861234266e5e020-Abstract-Conference.html; https://proceedings.iclr.cc/paper_files/paper/2025/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=OpenReview abstract states extensive experiments were run on four AD biomarkers. | confidence=high
- metric: evidence=The official ICLR PDF states that three metrics were used to evaluate generated samples versus test data: WD, RMSE, and JSD. Tables 1-2 report WD/RMSE/JSD, with Table 2 additionally reporting generation time columns. | confidence=high | tier=tier1_paper_text
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=OpenReview abstract describes longitudinal sequences conditioned on age and disease severity for neurodegenerative disease progression. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: Conditional Diffusion with Ordinal Regression: Longitudinal Data Generation for Neurodegenerative Disease Studies
- auto_source_url: https://www.semanticscholar.org/paper/5226db152c2623596f552c31e956085000b54b21

### Can Language Understand Depth?

Bibliographic:
- year: 2022
- venue: Proceedings of the 30th ACM International Conference on Multimedia
- doi: 10.1145/3503161.3549201

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: RGB image inputs paired with language/CLIP semantic representations.
- input_modality: image/video
- task_taxonomy: Zero-shot monocular depth estimation using CLIP/DepthCLIP.
- paper_objective: Zero-shot monocular depth estimation using CLIP/DepthCLIP.
- method_family: Contrastive learning
- method_summary: Contrastive learning
- dataset: NYU Depth v2 for zero-shot monocular depth estimation evaluation: 120K RGB-depth pairs captured with Microsoft Kinect across 464 indoor scenes; training split 36,253 images from 249 scenes and test split 654 images from 215 scenes.
- dataset_role: used
- metric: Mean absolute relative error (rel), root mean square error (rmse), absolute log10 error, and threshold accuracy delta_i for thresholds 1.25, 1.25^2, and 1.25^3.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1145/3503161.3549201; https://arxiv.org/abs/2207.01077; https://www.semanticscholar.org/paper/9d0afe58801fe9e5537902e853d6e9e385340a92; https://arxiv.org/html/2207.01077; https://dl.acm.org/doi/10.1145/3503161.3549201; https://arxiv.org/pdf/2207.01077
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=The paper's Experiments/Datasets section states that DepthCLIP is evaluated on NYU Depth v2, describes 120K RGB-depth image pairs from 464 indoor scenes, and gives the training/testing split sizes. | confidence=high | tier=tier1_paper_text
- metric: evidence=The paper's Evaluation Metrics section says the quantitative metrics are rel, rmse, log10, and threshold accuracy delta_i; Table 1 reports delta < 1.25, delta < 1.25^2, delta < 1.25^3, rel, log10, and rmse. | confidence=high | tier=tier1_paper_text
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=Semantic Scholar abstract describes adapting CLIP image-language knowledge to depth estimation from input image patches. | confidence=high
- task_taxonomy: evidence=Semantic Scholar abstract states the paper proposes DepthCLIP for zero-shot monocular depth estimation. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Can Language Understand Depth?
- auto_source_url: https://doi.org/10.1145/3503161.3549201

### Computational framework to predict and shape human–machine interactions in closed-loop, co-adaptive neural interfaces

Bibliographic:
- year: 2026
- venue: Nature Machine Intelligence
- doi: 10.1038/s42256-026-01194-z

Paper type:
- type: system

Evidence fields:
- signal_modality: Myoelectric/EMG interface signals rather than direct brain recordings.
- input_modality: not specified
- task_taxonomy: Predict and shape closed-loop co-adaptive human-machine interface behavior.
- paper_objective: Predict and shape closed-loop co-adaptive human-machine interface behavior.
- method_family: Game-theoretic computational framework for co-adaptive human-machine interfaces, tested by manipulating decoder learning rates and effort penalties in myoelectric experiments.
- method_summary: Game-theoretic computational framework for co-adaptive human-machine interfaces, tested by manipulating decoder learning rates and effort penalties in myoelectric experiments.
- dataset: Human closed-loop myoelectric interface experiments with co-adaptive encoder-decoder control.
- dataset_role: used
- metric: Trajectory-tracking performance, closed-loop stability, decoder effort, encoder/user effort, cursor speed, and Wilcoxon signed-rank tests.
- metric_status: applicable
- limitations: Authors state precise validation of some game-theoretic predictions will require improved methods to estimate user learning rates; observed user effort/speed trade-offs deviated from strict model predictions.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s42256-026-01194-z; https://www.nature.com/articles/s42256-026-01194-z
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Nature article describes myoelectric interface experiments with adaptive decoders. | confidence=medium
- limitations: evidence=Results text says precise validation requires improved methods to estimate user learning rates and notes deviations from model predictions. | confidence=high
- method_summary: evidence=Article describes a game-theoretic framework with decoder learning-rate and effort-penalty manipulations. | confidence=high
- metric: evidence=Results report performance, stability, decoder effort, encoder effort, cursor speed, and Wilcoxon tests. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Article explicitly refers to myoelectric interface experiments. | confidence=high
- task_taxonomy: evidence=Title and abstract frame the work as predicting and shaping co-adaptive neural-interface interactions. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Computational framework to predict and shape human–machine interactions in closed-loop, co-adaptive neural interfaces
- auto_source_url: https://doi.org/10.1038/s42256-026-01194-z

### Computational models reveal that intuitive physics underlies visual processing of soft objects

Bibliographic:
- year: 2025
- venue: Nature Communications
- doi: 10.1038/s41467-025-61458-x

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Visual video stimuli of simulated soft objects.
- input_modality: image/video
- task_taxonomy: Model human visual processing of soft-object physical properties and intuitive physics judgments.
- paper_objective: Model human visual processing of soft-object physical properties and intuitive physics judgments.
- method_family: Computational physics model and DNN comparisons for inferring task-relevant physical properties such as stiffness and mass from videos.
- method_summary: Computational physics model and DNN comparisons for inferring task-relevant physical properties such as stiffness and mass from videos.
- dataset: Simulated cloth-video dataset across wind, ramp, drape, and rotate scenarios, plus 80 psychophysics videos transformed into 720 testing samples.
- dataset_role: used
- metric: Human/model matching accuracy, correlation with human judgments, L1 distance between inferred physical properties, and validation loss/correlation to ground truth.
- metric_status: applicable
- limitations: Experimental boundary: stimuli and models were evaluated on soft-object cloth videos in four scene configurations.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41467-025-61458-x; https://www.nature.com/articles/s41467-025-61458-x
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Methods list 1742 wind, 1677 ramp, 1588 drape, and 1315 rotate videos, final 56,898 images, and 80 psychophysics videos/720 samples. | confidence=high
- limitations: evidence=Dataset section states all simulations used the same four scene configurations. | confidence=medium
- method_summary: evidence=Methods describe comparing DNN and Woven-style physical-property estimates to human judgments. | confidence=high
- metric: evidence=Methods define L1-distance choices, matching accuracy, correlation with human judgments, and validation loss. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The dataset consists of visual cloth videos/images. | confidence=high
- task_taxonomy: evidence=Title and methods concern visual processing of soft-object physical properties. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Computational models reveal that intuitive physics underlies visual processing of soft objects
- auto_source_url: https://doi.org/10.1038/s41467-025-61458-x

### Does the brain represent words? An evaluation of brain decoding studies of language understanding

Bibliographic:
- year: 2018
- venue: 2018 Conference on Cognitive Computational Neuroscience
- doi: 10.32470/ccn.2018.1237-0

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: fMRI brain activity/brain imaging responses
- input_modality: fMRI
- task_taxonomy: Neural decoding, Speech/language decoding, Representation alignment
- paper_objective: Neural decoding, Speech/language decoding, Representation alignment
- method_family: Evaluation of brain decoding studies of language understanding.
- method_summary: Evaluation of brain decoding studies of language understanding.
- dataset: Pereira et al. sentence-decoding fMRI dataset: 384 sentences and associated subject brain images used to train/evaluate decoders.
- dataset_role: used
- metric: Mean average rank (MAR) for learned decoders, plus r2 for pairwise regression evaluation of model representations; figures report bootstrap 95% confidence intervals for MAR.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.32470/ccn.2018.1237-0; https://api.crossref.org/works/10.32470/ccn.2018.1237-0; https://arxiv.org/abs/1806.00591; https://arxiv.org/pdf/1806.00591; https://ar5iv.org/pdf/1806.00591; https://www.foldl.me/uploads/papers/ccn2018.pdf
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=The arXiv paper states that decoders are trained on the 384 sentences used by Pereira et al. and the associated brain images, and evaluates predictions against representations of those 384 sentences. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=Crossref/DOI metadata title explicitly says it is an evaluation of brain decoding studies. | confidence=medium
- metric: evidence=The paper's Evaluation method says learned decoders are evaluated using mean average rank. It also states that Figure 3 reports the r2 metric for each pairwise regression evaluation, while Figure 2 reports MAR with bootstrap 95% confidence intervals. | confidence=high | tier=tier1_paper_text
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=The paper describes Pereira et al.-style studies using fMRI data from subjects reading sentences, training decoders from subjects' fMRI responses/brain images to model representations, and explicitly refers to decoding fMRI activity. | confidence=high | tier=tier1_paper_text

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Does the brain represent words? An evaluation of brain decoding studies of language understanding
- auto_source_url: https://doi.org/10.32470/ccn.2018.1237-0

### Dynamic memristor-based reservoir computing for high-efficiency temporal signal processing

Bibliographic:
- year: 2021
- venue: Nature Communications
- doi: 10.1038/s41467-020-20692-1

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline.
- input_modality: ECoG
- task_taxonomy: High-efficiency temporal signal processing, including spoken-digit recognition and time-series prediction.
- paper_objective: High-efficiency temporal signal processing, including spoken-digit recognition and time-series prediction.
- method_family: Parallel dynamic memristor-based reservoir computing with controllable masking to tune state richness, feedback strength, and input scaling.
- method_summary: Parallel dynamic memristor-based reservoir computing with controllable masking to tune state richness, feedback strength, and input scaling.
- dataset: Temporal-signal tasks including spoken-digit recognition and Henon-map time-series prediction.
- dataset_role: used
- metric: Word error rate, classification accuracy, and normalized root mean square error.
- metric_status: applicable
- limitations: Author future-work boundary: demonstrated system is positioned as a step toward handling more complex temporal tasks in the future.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41467-020-20692-1; https://www.nature.com/articles/s41467-020-20692-1; https://www.semanticscholar.org/paper/cfb8bc22e6dd6e409b849d3fdd8906378af25796
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Semantic Scholar abstract names spoken-digit recognition and Henon-map prediction. | confidence=high
- limitations: evidence=Abstract says the work could pave the road toward more complex temporal tasks in the future. | confidence=medium
- method_summary: evidence=Abstract describes a parallel dynamic memristor reservoir computing system with controllable mask process. | confidence=high
- metric: evidence=Abstract reports word error rate 0.4%, classification accuracy 99.6%, and NRMSE 0.046. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=This is neuromorphic/memristor AI hardware for temporal signals, not neural recordings. | confidence=high
- task_taxonomy: evidence=Abstract frames the system as processing temporal signals. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Dynamic memristor-based reservoir computing for high-efficiency temporal signal processing
- auto_source_url: https://doi.org/10.1038/s41467-020-20692-1

### ECG Electrode Localization: 3D DS Camera System for Use in Diverse Clinical Environments

Bibliographic:
- year: 2023
- venue: Sensors
- doi: 10.3390/s23125552

Paper type:
- type: system

Evidence fields:
- signal_modality: ECG electrode positions captured with 3D depth-sensing camera imagery.
- input_modality: spiking/electrophysiology
- task_taxonomy: Localize ECG electrodes for patient-specific cardiac/body models.
- paper_objective: Localize ECG electrodes for patient-specific cardiac/body models.
- method_family: 3D depth-sensing camera system for localizing ECG electrode positions as an alternative to CT or manual magnetic digitizer probing.
- method_summary: 3D depth-sensing camera system for localizing ECG electrode positions as an alternative to CT or manual magnetic digitizer probing.
- dataset: 3D depth-sensing camera recordings of 67 ECG electrodes attached to a patient's chest.
- dataset_role: used
- metric: Average positional deviation from manually placed markers: 2.0 mm ± 1.5 mm.
- metric_status: applicable
- limitations: Experimental boundary: system was evaluated for ECG electrode localization under clinical constraints such as adverse lighting and limited space; Crossref abstract describes one patient's chest.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.3390/s23125552; https://api.crossref.org/works/10.3390/s23125552
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Crossref abstract states the camera recorded positions of 67 electrodes attached to a patient's chest. | confidence=high
- limitations: evidence=Crossref abstract states the system was developed for adverse lighting and limited space encountered in clinical settings. | confidence=medium
- method_summary: evidence=Crossref abstract describes a 3D depth-sensing camera system for electrode localization. | confidence=high
- metric: evidence=Crossref abstract reports average deviation of 2.0 mm ± 1.5 mm from manual markers. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The measured objects are ECG electrode positions captured by 3D depth sensing. | confidence=high
- task_taxonomy: evidence=Abstract states precise ECG electrode positions are needed for diagnostic digital-twin/body models. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: ECG Electrode Localization: 3D DS Camera System for Use in Diverse Clinical Environments
- auto_source_url: https://doi.org/10.3390/s23125552

### Electrophysiological Correlates of Semantic Dissimilarity Reflect the Comprehension of Natural, Narrative Speech

Bibliographic:
- year: 2017
- venue: bioRxiv
- doi: 10.1101/193201

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: EEG
- input_modality: EEG
- task_taxonomy: Measure whether EEG responses during natural narrative speech reflect word-level semantic dissimilarity and comprehension.
- paper_objective: Measure whether EEG responses during natural narrative speech reflect word-level semantic dissimilarity and comprehension.
- method_family: Temporal response function analysis regressing low-frequency EEG against word-onset semantic-dissimilarity vectors.
- method_summary: Temporal response function analysis regressing low-frequency EEG against word-onset semantic-dissimilarity vectors.
- dataset: Dryad/OpenNeuro naturalistic speech EEG data; healthy adults listened to audiobook segments from The Old Man and the Sea.
- dataset_role: used
- metric: TRF response estimates and EEG prediction/correlation analyses, including Pearson correlation in related dataset documentation.
- metric_status: applicable
- limitations: Experimental boundary: the study derives EEG temporal response functions for semantic dissimilarity during natural narrative speech, and the authors note that subjects have marked limitations in reporting unattended-speech content when interpreting unattended-speech semantic processing.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://www.semanticscholar.org/paper/288136ff52b0db694f735a3ab2931c5f16d41869; https://www.biorxiv.org/content/10.1101/193201v1; https://datadryad.org/dataset/doi:10.5061/dryad.070jc; https://openneuro.org/datasets/ds004408/versions/1.0.8; https://www.cell.com/current-biology/fulltext/S0960-9822(18)30146-5; https://www.biorxiv.org/content/10.1101/193201v1.full; https://doi.org/10.1101/193201
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=Dryad lists the data from the Current Biology article; OpenNeuro describes EEG responses while adults listened to audiobook segments. | confidence=high
- limitations: evidence=The bioRxiv full text describes the natural-speech EEG/TRF paradigm and, in the unattended-speech discussion, notes marked limitations in subjects' ability to report unattended-speech content. | confidence=medium | tier=tier1_paper_text
- method_summary: evidence=bioRxiv text describes time-aligned semantic-dissimilarity impulses regressed against 1-8 Hz EEG to derive TRFs. | confidence=high
- metric: evidence=Sources describe TRF weights and prediction accuracy/correlation between predicted and actual EEG. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=The paper and dataset sources explicitly describe electroencephalographic/electrophysiological responses. | confidence=high
- task_taxonomy: evidence=The title and abstract state semantic dissimilarity responses during natural narrative speech comprehension. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: Electrophysiological correlates of semantic dissimilarity reflect the comprehension of natural, narrative speech
- auto_source_url: https://www.semanticscholar.org/paper/288136ff52b0db694f735a3ab2931c5f16d41869

### End-to-end privacy preserving deep learning on multi-institutional medical imaging

Bibliographic:
- year: 2021
- venue: Nature Machine Intelligence
- doi: 10.1038/s42256-021-00337-8

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Privacy-preserving training and encrypted inference for paediatric chest X-ray classification.
- paper_objective: Privacy-preserving training and encrypted inference for paediatric chest X-ray classification.
- method_family: PriMIA framework combining differentially private, securely aggregated federated learning with encrypted remote inference using secure multi-party computation.
- method_summary: PriMIA framework combining differentially private, securely aggregated federated learning with encrypted remote inference using secure multi-party computation.
- dataset: Multi-institutional paediatric chest X-ray case study.
- dataset_role: used
- metric: Classification performance compared with local non-secure training, plus empirical/theoretical privacy evaluation and gradient-inversion attack resistance.
- metric_status: applicable
- limitations: Experimental boundary: PriMIA is demonstrated on a paediatric chest-X-ray classification case study, with encrypted remote inference using secure multi-party computation; the Nature page also notes confidential test sets that cannot be publicly shared.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s42256-021-00337-8; https://portal.fis.tum.de/en/publications/end-to-end-privacy-preserving-deep-learning-on-multi-institutiona/; https://cris.fau.de/publications/290551499/; https://www.nature.com/articles/s42256-021-00337-8
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=Institutional metadata and abstract identify paediatric chest X-rays as the real-life case study. | confidence=high
- limitations: evidence=The Nature abstract says the framework is tested using a real-life paediatric chest-X-ray case study and encrypted remote inference, and the data availability statement says test sets 1 and 2 contain confidential patient information and cannot be shared publicly. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=Abstract describes Privacy-preserving Medical Image Analysis with differentially private federated learning, secure aggregation, and encrypted inference. | confidence=high
- metric: evidence=Abstract reports classification performance on par with locally trained models and evaluates privacy guarantees against model inversion. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=The empirical data are medical chest X-ray images, not neural signals. | confidence=high
- task_taxonomy: evidence=Abstract states the case study classifies paediatric chest X-rays while preserving privacy. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: End-to-end privacy preserving deep learning on multi-institutional medical imaging
- auto_source_url: https://doi.org/10.1038/s42256-021-00337-8

### ExBody2: Advanced Expressive Humanoid Whole-Body Control

Bibliographic:
- year: 2024
- venue: arXiv.org
- doi: 10.48550/arXiv.2412.13196

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: motion
- task_taxonomy: Sim-to-real humanoid whole-body tracking/control for expressive reference motions.
- paper_objective: Sim-to-real humanoid whole-body tracking/control for expressive reference motions.
- method_family: Advanced Expressive Whole-Body Control with motion retargeting, automated feasibility-diversity dataset filtering, generalist-specialist RL policies, teacher-student training, and decoupled motion-velocity control.
- method_summary: Advanced Expressive Whole-Body Control with motion retargeting, automated feasibility-diversity dataset filtering, generalist-specialist RL policies, teacher-student training, and decoupled motion-velocity control.
- dataset: Human motion capture data including CMU-derived motion sets, filtered subsets such as D50/D250/DCMU, and DACCAD out-of-distribution evaluation motions.
- dataset_role: used
- metric: Linear velocity error, keybody/keypoint tracking error, upper/lower body MPJPE, and joint tracking errors.
- metric_status: applicable
- limitations: Specialist policies cannot be seamlessly recombined or switched within a single tracking session, limiting flexible transitions across motion groups.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://www.semanticscholar.org/paper/ec61efac491056b4f43186e31ac592f415e73925; https://arxiv.org/abs/2412.13196; https://arxiv.org/pdf/2412.13196; https://exbody2.github.io/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=arXiv/PDF describes raw human motion data, CMU dataset filtering, D250/D50/DCMU, and DACCAD OOD tests. | confidence=high
- limitations: evidence=Conclusion states the inability to seamlessly recombine fine-tuned specialist policies reduces switching flexibility. | confidence=high
- method_summary: evidence=Abstract and framework describe ExBody2 as RL-trained whole-body tracking with filtering, finetuning, and decoupled velocity/keypoint control. | confidence=high
- metric: evidence=Evaluation section lists velocity error, keypoint position tracking, MPJPE, and joint tracking metrics. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The study is robotics control from motion data, not neural measurement. | confidence=high
- task_taxonomy: evidence=The paper frames the goal as controlling humanoids to mimic expressive whole-body motions while stable. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: ExBody2: Advanced Expressive Humanoid Whole-Body Control
- auto_source_url: https://www.semanticscholar.org/paper/ec61efac491056b4f43186e31ac592f415e73925

### FREDF: LEARNING TO FORECAST IN THE FREQUENCY DOMAIN

Bibliographic:
- year: 2026
- venue: AI for Time Series
- doi: 10.1201/9781003612742-3

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Time-series forecasting, with additional imputation and short-term forecasting experiments.
- paper_objective: Time-series forecasting, with additional imputation and short-term forecasting experiments.
- method_family: Frequency-enhanced Direct Forecast, which adds frequency-domain supervision via FFT-based comparison of forecasts and labels.
- method_summary: Frequency-enhanced Direct Forecast, which adds frequency-domain supervision via FFT-based comparison of forecasts and labels.
- dataset: Long-term forecasting/imputation datasets ETT, ECL, Traffic, Weather, PEMS, and short-term M4.
- dataset_role: used
- metric: MSE and MAE for forecasting benchmarks.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1201/9781003612742-3; https://arxiv.org/abs/2402.02399; https://arxiv.org/pdf/2402.02399; https://openreview.net/revisions?id=s3juB4ZWzI; https://www.taylorfrancis.com/chapters/edit/10.1201/9781003612742-3/fredf-learning-forecast-frequency-domain-hao-wang-licheng-pan-zhichao-chen-zhengnan-li
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=ICLR/arXiv paper lists ETT subsets, ECL, Traffic, Weather, PEMS, and M4 in setup and dataset descriptions. | confidence=high
- method_summary: evidence=Abstract and methods describe reducing direct-forecast bias by learning in the frequency domain. | confidence=high
- metric: evidence=Main performance tables report MSE and MAE across datasets. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The work is generic time-series ML, not neural data. | confidence=high
- task_taxonomy: evidence=Problem definition and experiments are multi-step time-series forecasting. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Fredf: Learning to Forecast in the Frequency Domain
- auto_source_url: https://doi.org/10.1201/9781003612742-3

### How to build a cognitive map

Bibliographic:
- year: 2022
- venue: Nature Neuroscience
- doi: 10.1038/s41593-022-01153-y

Paper type:
- type: review

Evidence fields:
- signal_modality: Neuroscience theory/review; no new recording modality.
- input_modality: not specified
- task_taxonomy: Explain principles by which cognitive maps are learned, represented, and used for flexible behavior.
- paper_objective: Explain principles by which cognitive maps are learned, represented, and used for flexible behavior.
- method_family: Perspective/review synthesizing computational models of hippocampal formation cognitive maps into a common language.
- method_summary: Perspective/review synthesizing computational models of hippocampal formation cognitive maps into a common language.
- dataset: No primary dataset; review article. The article explicitly states that no data were generated in the Review.
- dataset_role: none_review
- metric: unresolved
- metric_status: not_applicable
- limitations: Paper-type boundary: this is a Review that organizes existing cognitive-map models into an ontology rather than reporting new empirical data; the article states that no data were generated.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41593-022-01153-y; https://arxiv.org/abs/2202.01682; https://www.nature.com/articles/s41593-022-01153-y
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=Nature labels the article as a Review Article and the Data availability section states that no data were generated in the Review. | confidence=high | tier=tier1_paper_text
- limitations: evidence=The Nature Neuroscience page identifies the article as a Review and states in data availability that no data were generated in the review. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=arXiv/Nature abstract says the paper brings models into a common language and distills principles. | confidence=high
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=The abstract describes a Perspective on models and neural phenomena rather than a new empirical dataset. | confidence=high
- task_taxonomy: evidence=Abstract frames the aim as understanding learning and neural representation of cognitive maps. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: How to build a cognitive map
- auto_source_url: https://doi.org/10.1038/s41593-022-01153-y

### Human-in-the-Loop Optimization for Deep Stimulus Encoding in Visual Prostheses

Bibliographic:
- year: 2023
- venue: Advances in Neural Information Processing Systems 36
- doi: 10.52202/075280-3474

Paper type:
- type: system

Evidence fields:
- signal_modality: Visual prosthesis stimulation/perceptual feedback with simulated epiretinal phosphene responses.
- input_modality: image/video
- task_taxonomy: Personalized stimulus encoding optimization for visual prostheses.
- paper_objective: Personalized stimulus encoding optimization for visual prostheses.
- method_family: Deep stimulus encoder trained by inverting a prosthetic forward model, then personalized with preferential Bayesian optimization from pairwise user choices.
- method_summary: Deep stimulus encoder trained by inverting a prosthetic forward model, then personalized with preferential Bayesian optimization from pairwise user choices.
- dataset: MNIST target images for simulated prosthetic percepts; simulated patients; Argus II/epiretinal prosthesis patient data used for phosphene-model validation.
- dataset_role: used
- metric: Perceptual reconstruction loss/error, Brier score for preference-kernel validation, and robustness metrics under noisy or misspecified simulated patients.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.52202/075280-3474; https://proceedings.neurips.cc/paper_files/paper/2023/hash/fb06bc3abcece7b8725a8b83b8fa3632-Abstract-Conference.html; https://proceedings.neurips.cc/paper_files/paper/2023/file/fb06bc3abcece7b8725a8b83b8fa3632-Paper-Conference.pdf; https://arxiv.org/abs/2306.13104; https://github.com/bionicvisionlab/2023-NeurIPS-HILO
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=NeurIPS paper states MNIST targets, simulated patients, and prosthesis-user phosphene datasets for model validation. | confidence=high
- method_summary: evidence=Abstract and methods describe DSE plus preferential Bayesian optimization over patient-specific parameters. | confidence=high
- metric: evidence=Data and metrics section defines perceptual similarity/reconstruction loss; appendix uses Brier score for duel prediction. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The work concerns retinal/visual prosthesis electrical stimulation and evoked percepts. | confidence=high
- task_taxonomy: evidence=The paper goal is optimizing patient-specific stimulation parameters for restored vision. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Human-in-the-Loop Optimization for Deep Stimulus Encoding in Visual Prostheses
- auto_source_url: https://doi.org/10.52202/075280-3474

### Hybrid computing using a neural network with dynamic external memory

Bibliographic:
- year: 2016
- venue: Nature
- doi: 10.1038/nature20101

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Reasoning, graph traversal/shortest-path/inference, question answering, and reinforcement-learning planning tasks.
- paper_objective: Reasoning, graph traversal/shortest-path/inference, question answering, and reinforcement-learning planning tasks.
- method_family: Differentiable Neural Computer: a neural network controller with differentiable dynamic external memory.
- method_summary: Differentiable Neural Computer: a neural network controller with differentiable dynamic external memory.
- dataset: bAbI synthetic question-answering tasks, generated graph tasks, London Underground/family-tree generalization tests, and Mini-SHRDLU block-puzzle environment.
- dataset_role: used
- metric: Question error rate and task failures for bAbI; graph-task accuracy; classification/readout accuracy for memory analyses.
- metric_status: applicable
- limitations: Experiments focused on relatively small-scale synthetic tasks.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/nature20101; https://pubmed.ncbi.nlm.nih.gov/27732574/; https://gwern.net/doc/reinforcement-learning/model-free/2016-graves.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Nature/PubMed and PDF describe bAbI, graph tasks, London Underground/family tree, and block puzzle experiments. | confidence=high
- limitations: evidence=Discussion explicitly says the experiments focused on small-scale synthetic tasks. | confidence=high
- method_summary: evidence=Abstract introduces a differentiable neural computer with external memory. | confidence=high
- metric: evidence=Paper reports bAbI mean test error and graph accuracies, with detailed question error-rate methods. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The work evaluates synthetic AI tasks rather than neural signals. | confidence=high
- task_taxonomy: evidence=Abstract lists natural-language reasoning, graph path finding, link inference, and block puzzle solving. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Hybrid computing using a neural network with dynamic external memory
- auto_source_url: https://doi.org/10.1038/nature20101

### IMPLICIT GAUSSIAN PROCESS REPRESENTATION OF VECTOR FIELDS OVER ARBITRARY LATENT MANI-

Bibliographic:
- year: 2024
- venue: ICLR
- doi: 10.48550/arXiv.2309.16746

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: EEG
- input_modality: EEG
- task_taxonomy: Encoding model, Visual reconstruction, Representation alignment
- paper_objective: Encoding model, Visual reconstruction, Representation alignment
- method_family: RVGP, a Riemannian manifold vector-field Gaussian process using connection-Laplacian eigenfunctions as positional encodings.
- method_summary: RVGP, a Riemannian manifold vector-field Gaussian process using connection-Laplacian eigenfunctions as positional encodings.
- dataset: Synthetic/geometric vector-field experiments on meshes plus resting-state 256-channel EEG from Alzheimer's patients and healthy controls, downsampled to low-density EEG for reconstruction.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://openreview.net/forum?id=YEPlTU5mZC; https://arxiv.org/abs/2309.16746; https://arxiv.org/pdf/2309.16746; https://dblp.org/rec/journals/corr/abs-2309-16746.bib; https://api.datacite.org/dois/10.48550/arXiv.2309.16746; https://api.openalex.org/works/doi:10.48550/arXiv.2309.16746
- evidence_tier: tier0_metadata
- confidence: high

Field evidence:
- dataset: evidence=arXiv/OpenReview paper describes mesh superresolution/inpainting and EEG from Alzheimer's and control participants. | confidence=high
- doi: evidence=The OpenReview ICLR 2024 page and arXiv page identify the exact title and authors. arXiv displays the arXiv-issued DOI, DBLP records doi=10.48550/ARXIV.2309.16746 for the CoRR record, and DataCite/OpenAlex resolve the same DOI to the exact title. | confidence=high | tier=tier0_metadata
- method_summary: evidence=Abstract states RVGP learns vector signals on latent Riemannian manifolds using connection-Laplacian positional encoding. | confidence=high
- record: confidence=high | tier=tier0_metadata

Identity trace:
- auto_verification_status: source-traced via DBLP strict title match
- auto_matched_title: Implicit Gaussian process representation of vector fields over arbitrary latent manifolds.
- auto_source_url: https://openreview.net/forum?id=YEPlTU5mZC

### Improved protein structure prediction using potentials from deep learning

Bibliographic:
- year: 2020
- venue: Nat.
- doi: 10.1038/S41586-019-1923-7

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: protein sequence/structure
- task_taxonomy: Predict 3D protein structure from amino-acid sequence.
- paper_objective: Predict 3D protein structure from amino-acid sequence.
- method_family: AlphaFold CASP13 system using deep residual distance/torsion prediction to construct a protein-specific potential optimized by gradient descent and Rosetta relaxation.
- method_summary: AlphaFold CASP13 system using deep residual distance/torsion prediction to construct a protein-specific potential optimized by gradient descent and Rosetta relaxation.
- dataset: CASP13 targets plus training resources including PDB, CATH, Uniclust30, PSI-BLAST nr, and CASP11/CASP12 validation exclusions.
- dataset_role: used
- metric: TM-score, GDT_TS, RMSD, distogram lDDT, and CASP z-scores/contact precision.
- metric_status: applicable
- limitations: Free-modelling target accuracy still lagged template-based modelling targets in some cases.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41586-019-1923-7; https://dasher.wustl.edu/chem430/readings/nature-577-706-20.pdf; https://www.nature.com/articles/s41586-019-1923-7
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Methods list CASP13 assessment data and versions of PDB, CATH, Uniclust30, PSI-BLAST nr. | confidence=high
- limitations: evidence=Discussion notes FM accuracy still lags TBM accuracy for targets where homologous templates exist. | confidence=high
- method_summary: evidence=Abstract and methods describe neural distograms/torsions, learned potential, gradient descent, and Rosetta relaxation. | confidence=high
- metric: evidence=Paper reports TM-score, GDT_TS, RMSD, lDDT, and CASP scores. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Protein sequence/structure prediction is not neural data. | confidence=high
- task_taxonomy: evidence=Abstract states the goal is determining 3D protein shape from sequence. | confidence=high

Identity trace:
- auto_verification_status: source-traced via DBLP strict title match
- auto_matched_title: Improved protein structure prediction using potentials from deep learning.
- auto_source_url: https://doi.org/10.1038/s41586-019-1923-7

### Inception loops discover what excites neurons most using deep predictive models

Bibliographic:
- year: 2019
- venue: Nature Neuroscience
- doi: 10.1038/s41593-019-0517-x

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Two-photon calcium imaging
- input_modality: image/video
- task_taxonomy: Discover and validate visual stimuli that maximally excite individual neurons.
- paper_objective: Discover and validate visual stimuli that maximally excite individual neurons.
- method_family: Closed-loop inception-loop paradigm combining in vivo calcium recordings, CNN neural encoding models, and activation maximization to synthesize most-exciting images.
- method_summary: Closed-loop inception-loop paradigm combining in vivo calcium recordings, CNN neural encoding models, and activation maximization to synthesize most-exciting images.
- dataset: Two-photon calcium imaging responses from more than 2,000 excitatory neurons in mouse V1 layer 2/3 across five mice, using natural images and generated MEIs.
- dataset_role: used
- metric: Single-trial Pearson correlation between model predictions and responses; activation comparisons between MEIs and controls/natural images.
- metric_status: applicable
- limitations: The experiment was performed in V1 and the loop was executed once; authors note further passes could test generated stimuli more extensively.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41593-019-0517-x; https://pubmed.ncbi.nlm.nih.gov/31686023/; https://xaqlab.com/wp-content/uploads/2019/11/Inception_Walker_plusSupp.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Paper states responses from over 2,000 V1 L2/3 excitatory neurons in five mice. | confidence=high
- limitations: evidence=Discussion says V1 was used because it is well characterized and that only one inception-loop pass was executed. | confidence=high
- method_summary: evidence=Abstract describes closed-loop in vivo recordings with deep predictive models to synthesize MEIs. | confidence=high
- metric: evidence=Results report Pearson correlations and response activation comparisons. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Methods and figure captions specify two-photon calcium imaging. | confidence=high
- task_taxonomy: evidence=Abstract frames the task as identifying optimal sensory inputs for neurons. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Inception loops discover what excites neurons most using deep predictive models
- auto_source_url: https://doi.org/10.1038/s41593-019-0517-x

### Interactive Search for Image Categories by Mental Matching

Bibliographic:
- year: 2007
- venue: 2007 IEEE 11th International Conference on Computer Vision
- doi: 10.1109/iccv.2007.4409072

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Interactive image category search when the target category exists only in the user's mind.
- paper_objective: Interactive image category search when the target category exists only in the user's mind.
- method_family: Relevance-feedback framework based on mental matching, where the user compares displayed images against an internal target category.
- method_summary: Relevance-feedback framework based on mental matching, where the user compares displayed images against an internal target category.
- dataset: Unstructured image database/random image samples used in an interactive category-search setting.
- dataset_role: used
- metric: Number of iterations necessary to display an instance from the user's target category.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/iccv.2007.4409072; https://ieeexplore.ieee.org/document/4409072/; https://dblp.org/rec/conf/iccv/FerecatuG07; https://www.scilit.com/publications/79f56b0af2b9f96e6be818a6514014b9
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=IEEE/Scilit abstract says the search starts from random samples of images in an unstructured database. | confidence=medium
- method_summary: evidence=Abstract describes a mathematical framework for relevance feedback based on mental matching. | confidence=high
- metric: evidence=The official IEEE Xplore abstract states that at each iteration the user selects the displayed image closest to the category and that performance is measured by the number of iterations necessary to display an instance. | confidence=high | tier=tier1_paper_text
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=The paper is image retrieval with user feedback, not neural recording. | confidence=high
- task_taxonomy: evidence=Abstract identifies the page-zero problem for semantic image categories in the user's mind. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Interactive Search for Image Categories by Mental Matching
- auto_source_url: https://doi.org/10.1109/iccv.2007.4409072

### MapGuide: A Simple yet Effective Method to Reconstruct Continuous Language from Brain Activities

Bibliographic:
- year: 2024
- venue: Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)
- doi: 10.18653/v1/2024.naacl-long.211

Paper type:
- type: system

Evidence fields:
- signal_modality: fMRI
- input_modality: fMRI
- task_taxonomy: Neural decoding, Encoding model, Visual reconstruction, Speech/language decoding, Representation alignment
- paper_objective: Neural decoding, Encoding model, Visual reconstruction, Speech/language decoding, Representation alignment
- method_family: Two-stage MapGuide framework: Transformer-based mapper from fMRI to text embeddings with masking/contrastive learning, then guided text generation.
- method_summary: Two-stage MapGuide framework: Transformer-based mapper from fMRI to text embeddings with masking/contrastive learning, then guided text generation.
- dataset: LeBel et al. natural-language fMRI dataset: perceptual speech responses from three subjects, 27,449 training fMRI samples and 291 test samples.
- dataset_role: used
- metric: correlation, generation quality
- metric_status: applicable
- limitations: Testing was limited to English single-subject datasets.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.18653/v1/2024.naacl-long.211; https://aclanthology.org/2024.naacl-long.211/; https://aclanthology.org/2024.naacl-long.211.pdf; https://arxiv.org/abs/2403.17516; https://arxiv.org/html/2403.17516v2
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=arXiv paper states it uses LeBel et al. perceptual speech fMRI data with the listed train/test sample counts. | confidence=high
- limitations: evidence=The paper's limitation section states the testing has been limited to English single-subject datasets. | confidence=high
- method_summary: evidence=ACL/arXiv abstract and methods describe directly comparing generated text with predicted embeddings from brain activity. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The paper repeatedly identifies fMRI-recorded brain activity as the input. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: MapGuide: A Simple yet Effective Method to Reconstruct Continuous Language from Brain Activities
- auto_source_url: https://doi.org/10.18653/v1/2024.naacl-long.211

### Mastering Atari, Go, chess and shogi by planning with a learned model

Bibliographic:
- year: 2020
- venue: Nature
- doi: 10.1038/s41586-020-03051-4

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Model-based reinforcement learning and planning in Atari and board games without known environment dynamics.
- paper_objective: Model-based reinforcement learning and planning in Atari and board games without known environment dynamics.
- method_family: MuZero combines Monte Carlo tree search with a learned dynamics model that predicts reward, policy, and value for planning.
- method_summary: MuZero combines Monte Carlo tree search with a learned dynamics model that predicts reward, policy, and value for planning.
- dataset: 57 Atari Learning Environment games plus Go, chess, and shogi self-play/evaluation environments.
- dataset_role: used
- metric: Elo rating for board games; mean and median human-normalized score across Atari games.
- metric_status: applicable
- limitations: Atari planning improvements were less marked than Go, which the authors attribute to greater model inaccuracy.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41586-020-03051-4; https://arxiv.org/abs/1911.08265; https://arxiv.org/pdf/1911.08265
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Paper states evaluation on 57 Atari games and Go, chess, and shogi. | confidence=high
- limitations: evidence=Figure discussion notes planning helps less in Atari, presumably because of model inaccuracy. | confidence=high
- method_summary: evidence=Abstract describes tree-based search with a learned model predicting reward, action policy, and value. | confidence=high
- metric: evidence=Evaluation figure defines Elo for board games and human-normalized scores for Atari. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Game observations and states are non-neural AI benchmarks. | confidence=high
- task_taxonomy: evidence=Abstract frames MuZero as learning and planning in games without underlying dynamics. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Mastering Atari, Go, chess and shogi by planning with a learned model
- auto_source_url: https://doi.org/10.1038/s41586-020-03051-4

### Mastering the game of Go with deep neural networks and tree search

Bibliographic:
- year: 2016
- venue: Nature
- doi: 10.1038/nature16961

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Play full-size Go at professional/superhuman level.
- paper_objective: Play full-size Go at professional/superhuman level.
- method_family: AlphaGo combines supervised policy networks, reinforcement-learned policy/value networks, and Monte Carlo tree search.
- method_summary: AlphaGo combines supervised policy networks, reinforcement-learned policy/value networks, and Monte Carlo tree search.
- dataset: 30 million expert Go positions from the KGS Go Server plus self-play games for reinforcement learning/value training.
- dataset_role: used
- metric: Move-prediction accuracy, Elo rating, win rate against Go programs, and match outcome against the European Go champion.
- metric_status: applicable
- limitations: Experimental boundary: AlphaGo is evaluated in the full-sized game of Go, against other Go programs and the European Go champion; the paper does not establish performance outside the Go domain.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/nature16961; https://www.nature.com/articles/nature16961; https://staroceans.org.s3.amazonaws.com/documents/deepmind-mastering-go.pdf; https://www.researchgate.net/publication/292074166_Mastering_the_game_of_Go_with_deep_neural_networks_and_tree_search
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=Available paper copies and summaries report 30 million KGS positions and self-play training. | confidence=high
- limitations: evidence=The Nature abstract frames the contribution as computer Go, reports a 99.8% win rate against other Go programs, and reports a 5-0 match win against the European Go champion in full-sized Go. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=Nature abstract says policy/value networks are trained from human expert games and self-play and combined with tree search. | confidence=high
- metric: evidence=Nature abstract reports 99.8% win rate against other programs and 5-0 against the European champion; paper uses Elo. | confidence=high
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=The work is a Go-playing AI benchmark, not neural data. | confidence=high
- task_taxonomy: evidence=Title and abstract define the task as mastering Go. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Mastering the game of Go with deep neural networks and tree search
- auto_source_url: https://doi.org/10.1038/nature16961

### Mental state decoders: game-changers or wishful thinking?

Bibliographic:
- year: 2024
- venue: Trends in Cognitive Sciences
- doi: 10.1016/j.tics.2024.06.004

Paper type:
- type: perspective

Evidence fields:
- signal_modality: fMRI
- input_modality: fMRI
- task_taxonomy: Evaluate whether mental-state decoders provide neurophysiological insight or practical clinical value.
- paper_objective: Evaluate whether mental-state decoders provide neurophysiological insight or practical clinical value.
- method_family: Opinion/review critique of fMRI-based mental and perceptual state decoding literature.
- method_summary: Opinion/review critique of fMRI-based mental and perceptual state decoding literature.
- dataset: No primary dataset; review/opinion article about fMRI-based mental and perceptual state decoders.
- dataset_role: none_review
- metric: unresolved
- metric_status: not_applicable
- limitations: The article argues fMRI decoders are mainly predictive rather than explanatory, difficult to interpret physiologically, and may not generalize from evoked laboratory states to clinical or spontaneous states.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1016/j.tics.2024.06.004; https://pubmed.ncbi.nlm.nih.gov/38991876/; https://iannettilab.net/pdfs/mental_state_decoders.pdf
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=PubMed/E-utilities lists the publication type as Review and the abstract describes an opinion article arguing about fMRI-based decoders rather than reporting a new dataset. | confidence=high | tier=tier1_paper_text
- limitations: evidence=Accessible PDF excerpts discuss prediction versus explanation, interpretability problems, and poor expected generalization to clinical pain. | confidence=high
- method_summary: evidence=PubMed/Cell identify it as an opinion-style article about decoding mental and perceptual states using fMRI. | confidence=high
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=Abstract explicitly describes fMRI-based decoders. | confidence=high
- task_taxonomy: evidence=Title and abstract frame the paper as assessing claims about mental-state decoders. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Mental state decoders: game-changers or wishful thinking?
- auto_source_url: https://doi.org/10.1016/j.tics.2024.06.004

### ModaVerse: Efficiently Transforming Modalities with LLMs

Bibliographic:
- year: 2024
- venue: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
- doi: 10.1109/cvpr52733.2024.02512

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Any-to-any multimodal transformation among text, image, video, and audio.
- paper_objective: Any-to-any multimodal transformation among text, image, video, and audio.
- method_family: ModaVerse aligns ImageBind multimodal embeddings to an LLM with linear projections and uses the LLM as an agent to invoke text-to-image/video/audio generators.
- method_summary: ModaVerse aligns ImageBind multimodal embeddings to an LLM with linear projections and uses the LLM as an agent to invoke text-to-image/video/audio generators.
- dataset: COCO-caption, AudioCaps, MSR-VTT, and instruction data derived from multimodal instruction-tuning resources such as LLaVA, VideoChat, and InstructBLIP.
- dataset_role: used
- metric: FID, BLEU@4, METEOR, and CLIPSIM across image, audio, and video tasks.
- metric_status: applicable
- limitations: Failure cases include image editing that generates a new image instead of preserving the original background/layout; public datasets cover only common modality combinations.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/cvpr52733.2024.02512; https://arxiv.org/abs/2401.06395; https://arxiv.org/pdf/2401.06395; https://github.com/xinke-wang/ModaVerse
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=CVPR/arXiv paper evaluation sections list COCO-caption, AudioCaps, and MSR-VTT, plus instruction sources. | confidence=high
- limitations: evidence=Limitations/failure cases section states original background/layout preservation is poor and modality-combination data are limited. | confidence=high
- method_summary: evidence=Paper describes ImageBind input projection, LLM agent planning, and replaceable text-to-X output models. | confidence=high
- metric: evidence=Evaluation tables report FID, B@4, METEOR, and CLIPSIM. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The modalities are media inputs/outputs, not neural signals. | confidence=high
- task_taxonomy: evidence=Abstract states ModaVerse comprehends and transforms images, videos, audio, and text. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: ModaVerse: Efficiently Transforming Modalities with LLMs
- auto_source_url: https://doi.org/10.1109/cvpr52733.2024.02512

### MotionFix: Text-Driven 3D Human Motion Editing

Bibliographic:
- year: 2024
- venue: SIGGRAPH Asia 2024 Conference Papers
- doi: 10.1145/3680528.3687559

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: text/speech
- task_taxonomy: Generate an edited 3D human motion from an input motion and a natural-language edit instruction.
- paper_objective: Generate an edited 3D human motion from an input motion and a natural-language edit instruction.
- method_family: TMED, a text-driven motion editing diffusion model conditioned on source motion and edit instruction.
- method_summary: TMED, a text-driven motion editing diffusion model conditioned on source motion and edit instruction.
- dataset: MotionFix dataset with 4,771 source-target motion pairs and 1,280-word edit-text vocabulary, built from motion-capture data.
- dataset_role: used
- metric: Retrieval-based motion-editing metrics, including whether the target motion ranks highly and source-motion proximity.
- metric_status: applicable
- limitations: TMR-similar motions are not always true editing pairs; motions are capped at 5 seconds; TMED struggles with unseen or complex edit text and source-motion faithfulness.
- limitation_source: explicit

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1145/3680528.3687559; https://dl.acm.org/doi/10.1145/3680528.3687559; https://arxiv.org/abs/2408.00712; https://arxiv.org/pdf/2408.00712
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=arXiv/SIGGRAPH paper states MotionFix contains 4,771 x 2 motions and vocabulary size 1,280. | confidence=high
- limitations: evidence=Limitations section explicitly lists pair-assumption, duration, generalization, and faithfulness issues. | confidence=high
- method_summary: evidence=Abstract and methods describe TMED as a conditional diffusion model for source motion plus edit text. | confidence=high
- metric: evidence=Introduction/evaluation define retrieval-based metrics for target rank and source proximity. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The data are 3D motions and text, not neural signals. | confidence=high
- task_taxonomy: evidence=Abstract states the goal is text-driven 3D human motion editing. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: MotionFix: Text-Driven 3D Human Motion Editing
- auto_source_url: https://doi.org/10.1145/3680528.3687559

### NeuroGen: Activation optimized image synthesis for discovery neuroscience

Bibliographic:
- year: 2022
- venue: NeuroImage
- doi: 10.1016/j.neuroimage.2021.118812

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: fMRI
- input_modality: fMRI
- task_taxonomy: Activation-optimized image synthesis for probing and controlling human visual cortex responses.
- paper_objective: Activation-optimized image synthesis for probing and controlling human visual cortex responses.
- method_family: NeuroGen combines an fMRI-trained visual encoding model with a deep generative network to synthesize images predicted to target brain-activation patterns.
- method_summary: NeuroGen combines an fMRI-trained visual encoding model with a deep generative network to synthesize images predicted to target brain-activation patterns.
- dataset: fMRI visual-response data with several thousand observed image responses, associated with Natural Scenes Dataset-style human vision experiments.
- dataset_role: used
- metric: Encoding-model-predicted macro-scale brain activation and validation against observed fMRI image responses.
- metric_status: applicable
- limitations: The authors motivate NeuroGen by noting fMRI visual experiments are hypothesis-limited, restricted to presented image sets, noisy, and variable across individuals.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1016/j.neuroimage.2021.118812; https://pubmed.ncbi.nlm.nih.gov/34936922/; https://arxiv.org/abs/2105.07140; https://www.researchgate.net/publication/357181937_NeuroGen_Activation_optimized_image_synthesis_for_discovery_neuroscience
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Abstract describes verification using several thousand observed fMRI image responses; related sources tie the work to NSD human visual fMRI. | confidence=medium
- limitations: evidence=Abstract explicitly lists limitations of conventional fMRI visual experiments that NeuroGen addresses. | confidence=high
- method_summary: evidence=PubMed/arXiv abstract states NeuroGen combines an fMRI-trained encoding model and deep generative network. | confidence=high
- metric: evidence=Abstract describes predicted target activation patterns and verification in observed fMRI responses. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Title, abstract, and keywords identify functional MRI. | confidence=high
- task_taxonomy: evidence=Abstract frames the aim as synthesizing images for neuroscience discovery and target brain activation. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: NeuroGen: Activation optimized image synthesis for discovery neuroscience
- auto_source_url: https://doi.org/10.1016/j.neuroimage.2021.118812

### Neuroscience-Inspired Artificial Intelligence

Bibliographic:
- year: 2017
- venue: Neuron
- doi: 10.1016/j.neuron.2017.06.011

Paper type:
- type: review

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Argue how understanding biological brains can inform the design of intelligent machines.
- paper_objective: Argue how understanding biological brains can inform the design of intelligent machines.
- method_family: Perspective/review surveying historical and current interactions between neuroscience and AI.
- method_summary: Perspective/review surveying historical and current interactions between neuroscience and AI.
- dataset: No primary dataset; review article surveying interactions between neuroscience and AI and AI advances inspired by neural computation.
- dataset_role: none_review
- metric: unresolved
- metric_status: not_applicable
- limitations: Paper-type boundary: review/perspective/theory article without a primary empirical experiment-specific limitation.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1016/j.neuron.2017.06.011; https://pubmed.ncbi.nlm.nih.gov/28728020/; https://www.cell.com/neuron/abstract/S0896-6273(17)30509-3
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=PubMed/E-utilities lists the publication type as Review and the abstract says the article surveys historical interactions between AI and neuroscience and emphasizes AI advances inspired by neural computation. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=PubMed/Cell/Mendeley abstracts describe a review-style article surveying neuroscience-AI interactions. | confidence=high
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=The paper is a conceptual AI/neuroscience review and reports no new neural recordings. | confidence=high
- task_taxonomy: evidence=Abstract states the article argues better understanding biological brains could help build intelligent machines. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Neuroscience-Inspired Artificial Intelligence
- auto_source_url: https://doi.org/10.1016/j.neuron.2017.06.011

### Neuroscience-Inspired Artificial Intelligence

Bibliographic:
- year: 2017
- venue: Neuron
- doi: 10.1016/j.neuron.2017.06.011

Paper type:
- type: review

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Argue how understanding biological brains can inform the design of intelligent machines.
- paper_objective: Argue how understanding biological brains can inform the design of intelligent machines.
- method_family: Perspective/review surveying historical and current interactions between neuroscience and AI.
- method_summary: Perspective/review surveying historical and current interactions between neuroscience and AI.
- dataset: No primary dataset; review article surveying interactions between neuroscience and AI and AI advances inspired by neural computation.
- dataset_role: none_review
- metric: unresolved
- metric_status: not_applicable
- limitations: Paper-type boundary: review/perspective/theory article without a primary empirical experiment-specific limitation.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1016/j.neuron.2017.06.011; https://pubmed.ncbi.nlm.nih.gov/28728020/; https://www.cell.com/neuron/abstract/S0896-6273(17)30509-3
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=PubMed/E-utilities lists the publication type as Review and the abstract says the article surveys historical interactions between AI and neuroscience and emphasizes AI advances inspired by neural computation. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=PubMed/Cell/Mendeley abstracts describe a review-style article surveying neuroscience-AI interactions. | confidence=high
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=The paper is a conceptual AI/neuroscience review and reports no new neural recordings. | confidence=high
- task_taxonomy: evidence=Abstract states the article argues better understanding biological brains could help build intelligent machines. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Neuroscience-Inspired Artificial Intelligence
- auto_source_url: https://doi.org/10.1016/j.neuron.2017.06.011

### OminiControl: Minimal and Universal Control for Diffusion Transformer

Bibliographic:
- year: 2025
- venue: 2025 IEEE/CVF International Conference on Computer Vision (ICCV)
- doi: 10.1109/iccv51701.2025.01386

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Controllable text-to-image generation with image conditions for Diffusion Transformer models.
- paper_objective: Controllable text-to-image generation with image conditions for Diffusion Transformer models.
- method_family: Transformer, Diffusion/generative model
- method_summary: Transformer, Diffusion/generative model
- dataset: Subjects200K; evaluations cover subject-driven generation and spatially aligned controls such as edge, depth, colorization, deblurring, in-painting and out-painting.
- dataset_role: used
- metric: FID, SSIM, CLIP-IQA, MAN-IQA, MUSIQ, PSNR, CLIP Text, CLIP Image, F1 score for Canny control, MSE for other spatial controls, and five-criteria subject-driven generation evaluation/user studies
- metric_status: applicable
- limitations: The authors identify data scarcity/quality limits for subject-driven generation and address them with a synthetic DiT-generated dataset; broader limitations beyond the image-conditioned DiT setting were not clearly verified.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/iccv51701.2025.01386; https://openaccess.thecvf.com/content/ICCV2025/html/Tan_OminiControl_Minimal_and_Universal_Control_for_Diffusion_Transformer_ICCV_2025_paper.html; https://arxiv.org/abs/2411.15098; https://arxiv.org/html/2411.15098v6; https://openaccess.thecvf.com/content/ICCV2025/papers/Tan_OminiControl_Minimal_and_Universal_Control_for_Diffusion_Transformer_ICCV_2025_paper.pdf
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=CVF/arXiv abstract states OminiControl introduces Subjects200K, over 200,000 identity-consistent image pairs, and supports spatial conditions such as edges and depth. | confidence=high
- limitations: evidence=Author text says Subjects200K was introduced to overcome data limitations in subject-driven generation. | confidence=medium
- metric: evidence=The ICCV CVF paper states that spatially aligned tasks measure generation quality with FID, SSIM, CLIP-IQA, MAN-IQA, MUSIQ and PSNR, alignment with CLIP Text and CLIP Image, controllability with F1 for edge-conditioned generation and MSE for other controls; it also describes a five-criteria subject-driven generation framework and user studies. | confidence=high | tier=tier1_paper_text
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=The work is a diffusion-transformer image generation/control paper and does not use neural/brain signals. | confidence=high
- task_taxonomy: evidence=Abstract describes integrating image conditions into pre-trained DiT models for subject-driven and spatially aligned conditional generation. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: OminiControl: Minimal and Universal Control for Diffusion Transformer
- auto_source_url: https://doi.org/10.1109/iccv51701.2025.01386

### Online dynamical learning and sequence memory with neuromorphic nanowire networks

Bibliographic:
- year: 2023
- venue: Nature Communications
- doi: 10.1038/s41467-023-42470-5

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Electrical neuromorphic nanowire-network readout voltages driven by image-derived voltage pulse streams.
- input_modality: image/video
- task_taxonomy: Online MNIST digit classification and recall of target digits from temporal digit sequences.
- paper_objective: Online MNIST digit classification and recall of target digits from temporal digit sequences.
- method_family: Neuromorphic nanowire network reservoir computing with recursive least-squares online learning, plus sequence-memory recall from spatiotemporal readouts.
- method_summary: Neuromorphic nanowire network reservoir computing with recursive least-squares online learning, plus sequence-memory recall from spatiotemporal readouts.
- dataset: MNIST handwritten digit database; supporting data/code deposited on Zenodo.
- dataset_role: used
- metric: accuracy, correlation
- metric_status: applicable
- limitations: Online classification was implemented with an external digital layer; authors note a fully hardware implementation would require additional components such as a resistor cross-point array.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41467-023-42470-5; https://www.nature.com/articles/s41467-023-42470-5; https://zenodo.org/records/7662887
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Nature article states MNIST digit images are converted to temporal voltage pulse streams; Zenodo record says data and code support the paper. | confidence=high
- limitations: evidence=Discussion states the online classifier was external and suggests future end-to-end analogue hardware implementation. | confidence=high
- method_summary: evidence=Article describes NWN device readouts, a reservoir-computing framework, and an online RLS classifier updated sample by sample. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Input images are converted into voltage pulse streams and device responses are read as electrode-channel voltages. | confidence=high
- task_taxonomy: evidence=Abstract reports MNIST classification accuracy and a sequence-memory recall task. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Online dynamical learning and sequence memory with neuromorphic nanowire networks
- auto_source_url: https://doi.org/10.1038/s41467-023-42470-5

### PIA: Your Personalized Image Animator via Plug-and-Play Modules in Text-to-Image Models

Bibliographic:
- year: 2024
- venue: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
- doi: 10.1109/cvpr52733.2024.00740

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Personalized image animation / image-to-video generation controlled by text prompts.
- paper_objective: Personalized image animation / image-to-video generation controlled by text prompts.
- method_family: Plug-and-play condition module and temporal alignment layers added to personalized text-to-image models to animate a condition image using text motion prompts.
- method_summary: Plug-and-play condition module and temporal alignment layers added to personalized text-to-image models to animate a condition image using text motion prompts.
- dataset: WebVid10M for training; AnimateBench with 105 image-prompt pairs for evaluation.
- dataset_role: used
- metric: CLIP score for image alignment and text alignment; user-study preference rate
- metric_status: applicable
- limitations: Authors state future work should extend to stronger base T2I models such as SDXL and study color shift caused by low-quality training data.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/cvpr52733.2024.00740; https://arxiv.org/html/2312.13964v2; https://arxiv.org/html/2312.13964v1; https://openaccess.thecvf.com/content/CVPR2024/papers/Zhang_PIA_Your_Personalized_Image_Animator_via_Plug-and-Play_Modules_in_Text-to-Image_CVPR_2024_paper.pdf; https://openaccess.thecvf.com/CVPR2024?day=2024-06-19
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=ArXiv HTML states training is conducted on WebVid/WebVid10M and AnimateBench contains 105 personalized cases. | confidence=high
- limitations: evidence=ArXiv v1 snippet explicitly mentions studying color shift from low-quality training data and extending to SDXL. | confidence=high
- method_summary: evidence=Abstract and method sections describe a condition module taking the condition frame and inter-frame affinity with temporal alignment layers. | confidence=high
- metric: evidence=The CVPR CVF paper's Evaluation Metrics section says quantitative comparison evaluates image alignment and text alignment with CLIP score, and the user study asks users to choose videos matching the text or image best and reports preference rate. | confidence=high | tier=tier1_paper_text
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=The paper is a generative video/image model paper, not a neural-signal paper. | confidence=high
- task_taxonomy: evidence=Abstract says PIA animates personalized images with realistic motions while preserving style and detail. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: PIA: Your Personalized Image Animator via Plug-and-Play Modules in Text-to-Image Models
- auto_source_url: https://doi.org/10.1109/cvpr52733.2024.00740

### Photogrammetry-based stereoscopic optode registration method for functional near-infrared spectroscopy

Bibliographic:
- year: 2020
- venue: Journal of Biomedical Optics
- doi: 10.1117/1.jbo.25.9.095001

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: fNIRS optode positions with photogrammetry and MRI anatomical registration.
- input_modality: fNIRS
- task_taxonomy: Spatial registration of fNIRS optodes/channels to neuroanatomical coordinates.
- paper_objective: Spatial registration of fNIRS optodes/channels to neuroanatomical coordinates.
- method_family: Photogrammetry-based optode registration reconstructs cap/landmark geometry from stereoscopic photographs and aligns it to a brain anatomical template.
- method_summary: Photogrammetry-based optode registration reconstructs cap/landmark geometry from stereoscopic photographs and aligns it to a brain anatomical template.
- dataset: Empirical validation on 22 adult and 19 child participants with POR and MRI imaging.
- dataset_role: used
- metric: Overlap between POR-registered and MRI-registered channel measurements: 55% adults, 46% children overall; 65% adults and 60% children in frontal channels.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1117/1.jbo.25.9.095001; https://pmc.ncbi.nlm.nih.gov/articles/PMC7463164/; https://www.researchgate.net/publication/344096936_Photogrammetry-based_stereoscopic_optode_registration_method_for_functional_near-infrared_spectroscopy
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Search result from PMC/ResearchGate abstract reports 22 adult and 19 child participants. | confidence=high
- method_summary: evidence=Abstract says POR aligns reconstructed image with anatomical brain template. | confidence=high
- metric: evidence=Abstract reports adult/child overlap percentages overall and frontal-channel overlap percentages. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Title and abstract specify fNIRS optode registration. | confidence=high
- task_taxonomy: evidence=Paper aims to register fNIRS optodes for anatomical interpretation. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Photogrammetry-based stereoscopic optode registration method for functional near-infrared spectroscopy
- auto_source_url: https://doi.org/10.1117/1.jbo.25.9.095001

### PhysHSI: Towards a Real-World Generalizable and Natural Humanoid-Scene Interaction System

Bibliographic:
- year: 2025
- venue: arXiv.org
- doi: 10.48550/arXiv.2510.11072

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: motion
- task_taxonomy: Humanoid-scene interaction for box carrying, sitting, lying down and standing up in simulation and real-world deployment.
- paper_objective: Humanoid-scene interaction for box carrying, sitting, lying down and standing up in simulation and real-world deployment.
- method_family: AMP-based reinforcement-learning simulation pipeline plus coarse-to-fine real-world object localization using LiDAR odometry, camera/AprilTag localization and domain randomization.
- method_summary: AMP-based reinforcement-learning simulation pipeline plus coarse-to-fine real-world object localization using LiDAR odometry, camera/AprilTag localization and domain randomization.
- dataset: Retargeted AMASS and SAMP MoCap motions augmented with object annotations; roughly 2-5 complete trajectories per task in the reference data.
- dataset_role: used
- metric: Success rate and human-likeness score, averaged over five random seeds with 1000 evaluation episodes and three demo clips.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://www.semanticscholar.org/paper/a79f0a45851acff2f707b84bdb2373bc40a1ddc9; https://arxiv.org/abs/2510.11072; https://ar5iv.labs.arxiv.org/html/2510.11072v1; https://why618188.github.io/physhsi/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=ArXiv HTML states SMPL motions from AMASS and SAMP are retargeted, object trajectories annotated, and baselines use the same dataset with roughly 2-5 trajectories per task. | confidence=high
- method_summary: evidence=Abstract and method sections describe AMP policy learning and LiDAR/camera coarse-to-fine perception. | confidence=high
- metric: evidence=Experimental setup reports success rate and human-likeness score. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Robotics paper using MoCap, LiDAR, camera and proprioception, not neural signals. | confidence=high
- task_taxonomy: evidence=Abstract validates four tasks: box carrying, sitting, lying and standing up. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: PhysHSI: Towards a Real-World Generalizable and Natural Humanoid-Scene Interaction System
- auto_source_url: https://www.semanticscholar.org/paper/a79f0a45851acff2f707b84bdb2373bc40a1ddc9

### Predictability of real temporal networks

Bibliographic:
- year: 2020
- venue: National Science Review
- doi: 10.1093/nsr/nwaa015

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Quantify intrinsic predictability limits of temporal networks and compare them with existing temporal-network prediction algorithms.
- paper_objective: Quantify intrinsic predictability limits of temporal networks and compare them with existing temporal-network prediction algorithms.
- method_family: Entropy-based topological-temporal predictability framework for temporal networks.
- method_summary: Entropy-based topological-temporal predictability framework for temporal networks.
- dataset: 18 real temporal networks spanning animal contacts, human contacts, online communications, political events and transportation.
- dataset_role: used
- metric: Topological-temporal predictability (TTP), normalized TTP (NTTP), temporal predictability (TeP), normalized TeP (NTeP), normalized predictability of individual links (NPIL), and algorithmic prediction accuracy comparisons.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1093/nsr/nwaa015; https://academic.oup.com/nsr/article/7/5/929/5731923; https://academic.oup.com/nsr/issue/7/5
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Oxford article states framework was applied to 18 real temporal networks in five scenario categories. | confidence=high
- method_summary: evidence=Issue page describes an entropy-based framework; article discussion describes combined topology-temporal features. | confidence=high
- metric: evidence=Article snippet defines NTTP and NTeP and compares TTP with algorithmic accuracy. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Data are temporal networks, not neural recordings. | confidence=high
- task_taxonomy: evidence=Discussion states the method quantifies intrinsic predictability and uncovers predictability profiles. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Predictability of real temporal networks
- auto_source_url: https://doi.org/10.1093/nsr/nwaa015

### Predictive processing of scenes and objects

Bibliographic:
- year: 2023
- venue: Nature Reviews Psychology
- doi: 10.1038/s44159-023-00254-0

Paper type:
- type: review

Evidence fields:
- signal_modality: Visual cognition and neuroscience evidence, including scene/object perception studies rather than a single acquisition modality.
- input_modality: image/video
- task_taxonomy: Review how expectations from scene context and objects shape visual perception and recognition.
- paper_objective: Review how expectations from scene context and objects shape visual perception and recognition.
- method_family: Narrative review and synthesis of behavioral, cognitive-neuroscience and computational evidence on predictive scene-object processing.
- method_summary: Narrative review and synthesis of behavioral, cognitive-neuroscience and computational evidence on predictive scene-object processing.
- dataset: No primary dataset; Nature Reviews Psychology review synthesizing behavioural and neural findings on object and scene processing.
- dataset_role: none_review
- metric: unresolved
- metric_status: not_applicable
- limitations: The review identifies open questions rather than a closed empirical test: it is unknown which scene or object cues drive the reviewed perceptual effects, whether attention or conscious recognition is required, how automatic feedback signalling is, and modelling of contextual effects in neural networks needs improvement.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s44159-023-00254-0; https://repository.ubn.ru.nl/bitstream/handle/2066/298960/1/298960.pdf; https://www.researchgate.net/publication/375884443_Predictive_processing_of_scenes_and_objects; https://www.nature.com/articles/s44159-023-00254-0; https://drive.google.com/file/d/1irmQH_8EdxTD-bAilgQ9egmNTH3OYAjF/view?usp=drive_link
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=Nature labels the article as a Review Article, and the abstract says it synthesizes behavioural and neural findings on mechanisms of scene and object recognition rather than reporting a new experiment or dataset. | confidence=medium | tier=tier1_paper_text
- limitations: evidence=The publisher-version PDF's summary/future-directions section lists unknown cue contributions, attention/conscious-recognition and task-demand questions, and states that improving modelling of contextual effects in neural networks is an important avenue for future research. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=Nature Reviews Psychology article is a review; repository abstract describes synthesis of scene/object predictive processing. | confidence=high
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=Title, abstract and venue indicate visual perception/cognitive-neuroscience scope. | confidence=medium
- task_taxonomy: evidence=Search snippet says context-based expectations influence object and scene perception. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Predictive processing of scenes and objects
- auto_source_url: https://doi.org/10.1038/s44159-023-00254-0

### Proposal for an accurate TMS-MRI co-registration process via 3D laser scanning

Bibliographic:
- year: 2019
- venue: Neuroscience Research
- doi: 10.1016/j.neures.2018.08.012

Paper type:
- type: theory

Evidence fields:
- signal_modality: TMS coil geometry, MRI anatomy, 3D laser scans and motor evoked potentials.
- input_modality: image/video
- task_taxonomy: Co-register TMS stimulation coil position with MRI anatomy and estimate the TMS projection point onto the brain.
- paper_objective: Co-register TMS stimulation coil position with MRI anatomy and estimate the TMS projection point onto the brain.
- method_family: 3D laser-scanner-based TMS-MRI co-registration to capture positional relationships between the TMS coil and anatomical images.
- method_summary: 3D laser-scanner-based TMS-MRI co-registration to capture positional relationships between the TMS coil and anatomical images.
- dataset: Empirical 3D image-processing validation plus a motor evoked potential experiment targeting right finger motor areas.
- dataset_role: used
- metric: Registration error at each stage was kept within submillimeter level.
- metric_status: applicable
- limitations: Authors frame the system as a preliminary step for estimating the coil projection line/point; actual TMS-induced electric-field estimation remains difficult because fields are dispersed.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1016/j.neures.2018.08.012; https://pubmed.ncbi.nlm.nih.gov/30170008/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=PubMed abstract reports 3D image processing and a motor evoked potential experiment. | confidence=medium
- limitations: evidence=PubMed abstract states actual electric-field estimation is difficult and the projection line is a preliminary step. | confidence=high
- method_summary: evidence=PubMed abstract describes a new TMS-MRI co-registration procedure using a 3D laser-scanner system. | confidence=high
- metric: evidence=PubMed abstract reports submillimeter registration error. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Title and abstract include TMS, MRI, 3D laser scanning and MEP. | confidence=high
- task_taxonomy: evidence=Abstract states the goal is estimating the projection point beneath the coil into the brain. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Proposal for an accurate TMS-MRI co-registration process via 3D laser scanning
- auto_source_url: https://doi.org/10.1016/j.neures.2018.08.012

### Real-to-Sim for Highly Cluttered Environments via Physics-Consistent Inter-Object Reasoning

Bibliographic:
- year: 2026
- venue: IEEE Robotics and Automation Letters
- doi: 10.1109/lra.2026.3699238

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Reconstruct physically consistent digital twins of cluttered tabletop scenes for reliable simulation and contact-rich robot manipulation.
- paper_objective: Reconstruct physically consistent digital twins of cluttered tabletop scenes for reliable simulation and contact-rich robot manipulation.
- method_family: Physics-constrained Real-to-Sim pipeline from single-view RGB-D observations using contact graphs, two-stage differentiable rigid-body optimization and photometric refinement.
- method_summary: Physics-constrained Real-to-Sim pipeline from single-view RGB-D observations using contact graphs, two-stage differentiable rigid-body optimization and photometric refinement.
- dataset: Google Scanned Objects (GSO), YCB object set, and Toy4K for real-world experiments; 20 highly cluttered tabletop scenes per simulation dataset.
- dataset_role: used
- metric: Physical stability ratio, settling time, translational and rotational velocity, Chamfer Distance, F-Score, IoU, PSNR, SSIM, LPIPS, and real-world scene prediction error.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/lra.2026.3699238; https://arxiv.org/html/2602.12633v1
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=ArXiv HTML says experiments use GSO and YCB and construct 20 scenes per dataset; table includes Toy4K in real-world results. | confidence=high
- method_summary: evidence=Abstract and methods describe contact graph and differentiable rigid-body optimization from RGB-D. | confidence=high
- metric: evidence=Experiment section lists stability, geometry and rendering metrics. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Robotics/vision Real2Sim paper using RGB-D observations and object assets, not neural signals. | confidence=high
- task_taxonomy: evidence=Abstract states goal is reconstructing physically valid 3D scenes for robotic control. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Real-to-Sim for Highly Cluttered Environments via Physics-Consistent Inter-Object Reasoning
- auto_source_url: https://doi.org/10.1109/lra.2026.3699238

### Reverse predictivity for bidirectional comparison of neural networks and biological brains

Bibliographic:
- year: 2026
- venue: Nature Machine Intelligence
- doi: 10.1038/s42256-026-01204-0

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Macaque inferior temporal cortex neural responses with artificial neural network unit activations and behavioral data.
- input_modality: not specified
- task_taxonomy: Compare artificial visual models and primate brains bidirectionally to identify biologically shared and model-unique representational dimensions.
- paper_objective: Compare artificial visual models and primate brains bidirectionally to identify biologically shared and model-unique representational dimensions.
- method_family: Reverse predictivity metric measuring how well macaque IT neural responses predict ANN unit activations, paired with forward predictivity for bidirectional model-brain comparison.
- method_summary: Reverse predictivity metric measuring how well macaque IT neural responses predict ANN unit activations, paired with forward predictivity for bidirectional model-brain comparison.
- dataset: Behavioral datasets, example model features, macaque inferior temporal cortex neural responses and precomputed results released on OSF.
- dataset_role: used
- metric: Reverse predictivity, forward predictivity/variance explained, monkey-to-monkey mapping symmetry, unit common/unique analyses, Spearman correlations and behavior-prediction analyses.
- metric_status: applicable
- limitations: Reverse predictivity is presented as a conservative diagnostic; authors note it is influenced by feature dimensionality, training objectives and adversarial robustness.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s42256-026-01204-0; https://www.nature.com/articles/s42256-026-01204-0; https://osf.io/y3qmk/; https://github.com/vital-kolab/reverse_pred
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Nature data availability section lists behavioral datasets, example model features, macaque IT neural responses and precomputed results. | confidence=high
- limitations: evidence=Abstract describes reverse predictivity as conservative and affected by dimensionality, objectives and adversarial robustness. | confidence=medium
- method_summary: evidence=Abstract defines reverse predictivity as macaque IT responses predicting ANN unit activations. | confidence=high
- metric: evidence=Abstract reports forward predictivity around 50% variance explained and reverse-predictivity asymmetry; extended data references Spearman and behavior-prediction analyses. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Abstract specifies macaque inferior temporal cortex responses. | confidence=high
- task_taxonomy: evidence=Abstract frames the work as a diagnostic for ANN-brain representational comparison. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Reverse predictivity for bidirectional comparison of neural networks and biological brains
- auto_source_url: https://doi.org/10.1038/s42256-026-01204-0

### STORM-Net: Simple and Timely Optode Registration Method for Functional Near-Infrared Spectroscopy (fNIRS)

Bibliographic:
- year: 2020
- venue: bioRxiv (Cold Spring Harbor Laboratory)
- doi: 10.1101/2020.12.29.424683

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: fNIRS cap optode locations from video/photogrammetric registration, mapped to MNI or template coordinates.
- input_modality: fNIRS
- task_taxonomy: Automatic subject-specific fNIRS optode/cap co-registration.
- paper_objective: Automatic subject-specific fNIRS optode/cap co-registration.
- method_family: Neural-network-based optode registration from a short video of a subject wearing an fNIRS cap, using a premeasured template model and automatic/manual annotation.
- method_summary: Neural-network-based optode registration from a short video of a subject wearing an fNIRS cap, using a premeasured template model and automatic/manual annotation.
- dataset: Synthetic renderings from a Unity data generator for training; original experimental dataset required for reproduction is available upon request from the corresponding author.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1101/2020.12.29.424683; https://github.com/yoterel/STORM-Net
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=GitHub README states the repository contains a synthetic data generator and experimental mode requires the original dataset, available upon request. | confidence=high
- method_summary: evidence=README says the application estimates positions of points of interest on an fNIRS cap from a short video. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=README and title specify fNIRS optode registration and MNI coordinate output. | confidence=high
- task_taxonomy: evidence=README states STORM-Net is for automatic subject-specific co-registration of fNIRS probe placements. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: STORM-Net: Simple and Timely Optode Registration Method for Functional Near-Infrared Spectroscopy (fNIRS)
- auto_source_url: https://doi.org/10.1101/2020.12.29.424683

### Self-Calibrating BCIs: Ranking and Recovery of Mental Targets Without Labels

Bibliographic:
- year: 2025
- venue: arXiv.org
- doi: 10.48550/arXiv.2506.11151

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: EEG responses in an RSVP face-viewing paradigm, recorded with a 32-channel EasyCap system and reduced to 29 effective channels after preprocessing.
- input_modality: EEG
- task_taxonomy: Label-free self-calibration for ranking and recovering a user's mental target face from paired EEG and image data.
- paper_objective: Label-free self-calibration for ranking and recovering a user's mental target face from paired EEG and image data.
- method_family: CURSOR, a consistency-based unsupervised regression algorithm that scores hypothetical mental targets by comparing aligned versus shuffled EEG-to-distance estimation errors.
- method_summary: CURSOR, a consistency-based unsupervised regression algorithm that scores hypothetical mental targets by comparing aligned versus shuffled EEG-to-distance estimation errors.
- dataset: New EEG-face dataset: 9,234 stimuli-response pairs from 29 usable participants, generated from 17 target face images; additional human validation studies.
- dataset_role: used
- metric: Pearson score-distance correlation, target rank, similarity at top rank, RMSE, human identification error rate and Wilson confidence intervals.
- metric_status: applicable
- limitations: Authors state the findings should be replicated online; experiments use synthetic faces; no full DNN/transformer estimator was directly used; optimization used reduced dimensions chosen with external metrics; active sampling remains future work.
- limitation_source: explicit

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://www.semanticscholar.org/paper/e1457f8f00a8a49859d302764c9efa6e57029991; https://arxiv.org/html/2506.11151v2; https://openreview.net/forum?id=TtHvmhjNui&noteId=ZCEVgUymx1; https://github.com/jgrizou/neurips-self-calibrating-bci/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=ArXiv HTML reports 31 participants with 2 dropped, 9,234 pairs, 17 targets and 170 simulated dataset variants. | confidence=high
- limitations: evidence=Appendix F.1 explicitly lists online replication, real faces, complex estimators, reduced-dimensional optimization, active sampling and meta self-calibration. | confidence=high
- method_summary: evidence=Algorithm section defines CURSOR and the aligned/shuffled relative error-ratio scoring function. | confidence=high
- metric: evidence=Evaluation framework lists Pearson correlation, target rank and similarity at top rank; appendix reports RMSE and H-ID error rate. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Data acquisition section describes 32-channel EEG, artifact rejection and 29-channel processed EEG. | confidence=high
- task_taxonomy: evidence=Abstract describes recovering mental target faces without labels or pre-trained decoders. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: Self-Calibrating BCIs: Ranking and Recovery of Mental Targets Without Labels
- auto_source_url: https://www.semanticscholar.org/paper/e1457f8f00a8a49859d302764c9efa6e57029991

### Shared Neural Mechanisms of Visual Perception and Imagery

Bibliographic:
- year: 2019
- venue: Trends in Cognitive Sciences
- doi: 10.31234/osf.io/d8fru

Paper type:
- type: review

Evidence fields:
- signal_modality: Human visual perception/imagery neuroscience, including neuroimaging evidence rather than a single experimental signal modality.
- input_modality: image/video
- task_taxonomy: Review shared and distinct neural mechanisms underlying visual perception and imagery.
- paper_objective: Review shared and distinct neural mechanisms underlying visual perception and imagery.
- method_family: Review/synthesis of behavioral and neuroimaging evidence on overlap between visual perception and visual mental imagery.
- method_summary: Review/synthesis of behavioral and neuroimaging evidence on overlap between visual perception and visual mental imagery.
- dataset: No primary dataset; review of neuroimaging studies comparing visual perception and visual imagery.
- dataset_role: none_review
- metric: unresolved
- metric_status: not_applicable
- limitations: The review flags unresolved questions: temporal jitter in imagery onset can obscure fine-grained temporal dynamics, conclusions about temporal dynamics are hard to draw, imagery deficits without perceptual issues show the two simulations are not identical, and future work must test other modalities and how the brain separates real from imagined sensory content.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.31234/osf.io/d8fru; https://www.researchgate.net/publication/331691523_Shared_Neural_Mechanisms_of_Visual_Perception_and_Imagery; https://doi.org/10.1016/j.tics.2019.02.004; https://pubmed.ncbi.nlm.nih.gov/30876729/; https://www.sanderbosch.com/files/2019_dijkstra_tics.pdf
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=PubMed/E-utilities lists the publication type as Review and the abstract states that the article reviews recent neuroimaging studies comparing perception and imagery. | confidence=high | tier=tier1_paper_text
- limitations: evidence=The Trends in Cognitive Sciences PDF lists outstanding questions and future perspectives, including temporal uncertainty during imagery, unsolved questions, extension to other modalities, and mechanisms for distinguishing imagery from perception. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=Trends in Cognitive Sciences article is a review; ResearchGate metadata identifies the title, authors and venue. | confidence=high
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=Title and article metadata identify visual perception and imagery neural mechanisms. | confidence=medium
- task_taxonomy: evidence=The paper topic is the relation between perceived and imagined visual stimuli. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Shared neural mechanisms of visual perception and imagery
- auto_source_url: https://doi.org/10.31234/osf.io/d8fru

### Spatio-temporal correlations and visual signalling in a complete neuronal population

Bibliographic:
- year: 2008
- venue: Nature
- doi: 10.1038/nature07140

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Extracellular spiking activity from macaque retinal ganglion cells.
- input_modality: spiking/electrophysiology
- task_taxonomy: Analyze how correlated firing affects retinal population coding and visual-scene decoding.
- paper_objective: Analyze how correlated firing affects retinal population coding and visual-scene decoding.
- method_family: Multi-neuron probabilistic spike-response model fit directly to physiological data to capture stimulus dependence and spatiotemporal correlations.
- method_summary: Multi-neuron probabilistic spike-response model fit directly to physiological data to capture stimulus dependence and spatiotemporal correlations.
- dataset: Physiological spike-response data from a complete population of macaque parasol retinal ganglion cells.
- dataset_role: used
- metric: Spike-time prediction accuracy and decoded visual information; model-based decoding extracted 20% more information than independence decoding and preserved 40% more visual information than optimal linear decoding.
- metric_status: applicable
- limitations: Experimental boundary: the study analyzes correlated firing in a complete population of macaque parasol retinal ganglion cells using a fitted multi-neuron spike-response model for retinal coding of visual stimuli.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/nature07140; https://www.nature.com/articles/nature07140
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=Nature abstract states the analysis uses a complete population of macaque parasol retinal ganglion cells. | confidence=high
- limitations: evidence=The Nature abstract states that the analysis concerns a complete population of macaque parasol retinal ganglion cells, with model parameters fit to physiological data, and interprets correlated activity in retinal coding of visual stimuli. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=Abstract describes a model of multi-neuron spike responses with parameters fit to physiological data. | confidence=high
- metric: evidence=Abstract reports 20% more sensory information and 40% more visual information compared with baselines. | confidence=high
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=Abstract discusses spike responses and retinal ganglion cells. | confidence=high
- task_taxonomy: evidence=Abstract says the goal is understanding the role of correlated activity in retinal coding of visual stimuli. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Spatio-temporal correlations and visual signalling in a complete neuronal population
- auto_source_url: https://doi.org/10.1038/nature07140

### State-dependent pupil dilation rapidly shifts visual feature selectivity

Bibliographic:
- year: 2022
- venue: Nature
- doi: 10.1038/s41586-022-05270-3

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Mouse visual cortex population imaging with pupil/behavioral measurements.
- input_modality: image/video
- task_taxonomy: Test how pupil-linked behavioral state alters visual feature selectivity and decoding in mouse visual cortex.
- paper_objective: Test how pupil-linked behavioral state alters visual feature selectivity and decoding in mouse visual cortex.
- method_family: Population imaging in behaving mice combined with pharmacology and deep neural network modelling.
- method_summary: Population imaging in behaving mice combined with pharmacology and deep neural network modelling.
- dataset: Stimulus images and neuronal data stored at GIN/g-node for Franke_Willeke_2022.
- dataset_role: used
- metric: Stimulus selectivity/tuning shifts and decoding of ethologically relevant stimuli such as aerial predators against twilight sky.
- metric_status: applicable
- limitations: Experimental boundary: the reported mechanism is established in mouse visual cortex using population imaging in behaving mice, pharmacology and deep neural network modelling, in the context of coloured natural scenes and ethological stimuli.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41586-022-05270-3; https://www.nature.com/articles/s41586-022-05270-3; https://gin.g-node.org/cajal/Franke_Willeke_2022
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=Nature data availability section says stimulus images and neuronal data are stored at gin.g-node.org/cajal/Franke_Willeke_2022. | confidence=high
- limitations: evidence=The Nature abstract says the authors studied behavioural-state modulation in mouse visual cortex with coloured natural scenes, using population imaging in behaving mice, pharmacology and deep neural network modelling. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=Abstract states the study used population imaging, pharmacology and deep neural network modelling. | confidence=high
- metric: evidence=Abstract reports a shift in colour selectivity and facilitated decoding of ethological stimuli. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=Abstract identifies mouse visual cortex population imaging and pupil dilation. | confidence=high
- task_taxonomy: evidence=Abstract describes state-dependent modulation of stimulus selectivity in visual cortex. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: State-dependent pupil dilation rapidly shifts visual feature selectivity
- auto_source_url: https://doi.org/10.1038/s41586-022-05270-3

### Subspace communication in the hippocampal–retrosplenial axis

Bibliographic:
- year: 2026
- venue: bioRxiv (Cold Spring Harbor Laboratory)
- doi: 10.64898/2025.12.31.697203

Paper type:
- type: dataset

Evidence fields:
- signal_modality: Spiking activity across dentate gyrus, CA3, CA2, CA1 and retrosplenial cortex.
- input_modality: image/video
- task_taxonomy: Study hippocampal-retrosplenial communication subspaces during spatial/non-spatial tasks and post-experience sleep replay.
- paper_objective: Study hippocampal-retrosplenial communication subspaces during spatial/non-spatial tasks and post-experience sleep replay.
- method_family: Large-scale up-to-1024-channel recordings in behaving mice analyzed with partial canonical correlation analysis to identify low-dimensional communication subspaces.
- method_summary: Large-scale up-to-1024-channel recordings in behaving mice analyzed with partial canonical correlation analysis to identify low-dimensional communication subspaces.
- dataset: Datasets released in DANDI dandiset 001695 in NWB format; Allen Institute Visual Coding Dataset also used.
- dataset_role: used
- metric: correlation
- metric_status: applicable
- limitations: Experimental boundary: the study uses large-scale, up to 1,024-channel, recordings across hippocampal-retrosplenial cortex circuits in behaving mice, accessing DG, CA3, CA2, CA1 and RSC during spatial and non-spatial tasks and post-experience sleep.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.64898/2025.12.31.697203; https://www.nature.com/articles/s41586-026-10481-z; https://dandiarchive.org/dandiset/001695/0.260319.2023; https://allensdk.readthedocs.io/en/latest/visual_coding_neuropixels.html; https://www.biorxiv.org/content/10.64898/2025.12.31.697203v1.full-text
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=Nature data availability section lists DANDI dataset and Allen Visual Coding Dataset. | confidence=high
- limitations: evidence=The Nature article abstract states that the work uses up to 1,024-channel recordings across the hippocampal-retrosplenial circuit in behaving mice and maps subspaces during spatial and non-spatial tasks, with post-experience sleep reactivation analyses. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=Abstract states large-scale recordings and partial canonical correlation analysis. | confidence=high
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=Abstract specifies spiking activity in DG, CA3, CA2, CA1 and RSC. | confidence=high
- task_taxonomy: evidence=Abstract describes subspaces linking hippocampal inputs to RSC outputs and sleep reactivation. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Subspace communication in the hippocampal-retrosplenial axis
- auto_source_url: https://doi.org/10.64898/2025.12.31.697203

### Testing the Limits of Fine-Tuning for Improving Visual Cognition in Vision Language Models

Bibliographic:
- year: 2025
- venue: ICML
- doi: 10.48550/arXiv.2502.15678

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: Large language model
- method_summary: Large language model
- dataset: Cubeworld datasets for intuitive physics and causal reasoning, plus 100 naturalistic block-tower images from Lerer et al.; human judgments collected for alignment/evaluation.
- dataset_role: used
- metric: Model accuracy from normalized Yes/No token probabilities and alignment with human judgments across fine-tuning/generalization settings.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://proceedings.mlr.press/v267/schulze-buschoff25a.html; https://arxiv.org/html/2502.15678v2; https://openreview.net/forum?id=jSxU7ZGe3B; https://arxiv.org/abs/2502.15678; https://api.datacite.org/dois/10.48550/arXiv.2502.15678; https://api.openalex.org/works/doi:10.48550/arXiv.2502.15678
- evidence_tier: tier0_metadata
- confidence: high

Field evidence:
- dataset: evidence=ArXiv methods state four Cubeworld datasets were generated and 100 Lerer block-tower images were used; PMLR abstract mentions visual stimuli and human judgments. | confidence=high
- doi: evidence=PMLR/OpenReview identify the ICML 2025 paper title and authors. arXiv page for the same title and author list displays the arXiv-issued DOI, and DataCite/OpenAlex resolve the DOI to the exact title. | confidence=high | tier=tier0_metadata
- metric: evidence=ArXiv methods describe evaluating correctness by Yes/No token probabilities; abstract discusses model performance and human alignment. | confidence=high
- record: confidence=high | tier=tier0_metadata

Identity trace:
- auto_verification_status: source-traced via DBLP strict title match
- auto_matched_title: Testing the Limits of Fine-Tuning for Improving Visual Cognition in Vision Language Models.
- auto_source_url: https://proceedings.mlr.press/v267/schulze-buschoff25a.html

### The Bayesian image retrieval system, PicHunter: theory, implementation, and psychophysical experiments

Bibliographic:
- year: 2000
- venue: IEEE Transactions on Image Processing
- doi: 10.1109/83.817596

Paper type:
- type: theory

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Interactive content-based image retrieval to identify a user's target image from feedback.
- paper_objective: Interactive content-based image retrieval to identify a user's target image from feedback.
- method_family: Bayesian relevance-feedback content-based image retrieval: PicHunter maintains a probability distribution over possible target images and updates it from user actions.
- method_summary: Bayesian relevance-feedback content-based image retrieval: PicHunter maintains a probability distribution over possible target images and updates it from user actions.
- dataset: Image-retrieval experiments used image databases including the Corel stock photo library.
- dataset_role: used
- metric: Target-testing and psychophysical retrieval performance, including target-image rank / retrieval success measures.
- metric_status: applicable
- limitations: Experimental boundary: PicHunter is presented as a prototype content-based image retrieval system, and the paper reports psychophysical experiments conducted to address key issues arising during its development rather than a general-purpose evaluation of all image-search settings.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/83.817596; https://www.researchgate.net/publication/220501904_The_Bayesian_image_retrieval_system_PicHunter_Theory_implementation_and_psychophysical_experiments_vol_9_pg_20_2000; https://www0.cs.ucl.ac.uk/staff/I.Cox/Content/papers/2000/ip00.pdf; https://ieeexplore.ieee.org/document/817596; https://ieeexplore.ieee.org/iel5/83/17727/00817596.pdf
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=Search snippets from the paper/reference list cite Corel stock photo library as an image database source. | confidence=medium
- limitations: evidence=The IEEE Xplore PDF/metadata and abstract describe PicHunter as a prototype CBIR system and state that the paper presents the rationale, design and results of psychophysical experiments addressing issues from PicHunter's development. | confidence=medium | tier=tier1_paper_text
- method_summary: evidence=ResearchGate abstract states PicHunter uses Bayes' rule to predict a user's target image from actions via a probability distribution. | confidence=high
- metric: evidence=Abstract notes performance results and psychophysical experiments; related descriptions identify target testing and target image rank as evaluation paradigms. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=The work is CBIR/relevance feedback, not neural recording. | confidence=high
- task_taxonomy: evidence=Abstract describes a prototype content-based image retrieval system. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: The Bayesian image retrieval system, PicHunter: theory, implementation, and psychophysical experiments
- auto_source_url: https://doi.org/10.1109/83.817596

### The Future of Memory: Remembering, Imagining, and the Brain

Bibliographic:
- year: 2012
- venue: Neuron
- doi: 10.1016/j.neuron.2012.11.001

Paper type:
- type: review

Evidence fields:
- signal_modality: Human memory/imagination neuroscience, including default-network neuroimaging evidence rather than one primary signal modality.
- input_modality: not specified
- task_taxonomy: Review how memory supports imagination, simulation of future events and adaptive functioning.
- paper_objective: Review how memory supports imagination, simulation of future events and adaptive functioning.
- method_family: Review/synthesis of cognitive neuroscience research on memory, imagination and future thinking.
- method_summary: Review/synthesis of cognitive neuroscience research on memory, imagination and future thinking.
- dataset: No primary dataset; review of research on memory, imagination, and future thinking, focused on human-subject studies.
- dataset_role: none_review
- metric: unresolved
- metric_status: not_applicable
- limitations: Paper-type boundary: review/perspective/theory article without a primary empirical experiment-specific limitation.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1016/j.neuron.2012.11.001; https://pmc.ncbi.nlm.nih.gov/articles/PMC3815616/; https://www.researchgate.net/publication/233768009_The_Future_of_Memory_Remembering_Imagining_and_the_Brain
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=The PMC full text states that the article reviews progress since 2007 and focuses on studies with human subjects; no dataset or original data collection is reported as the target dataset. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=Neuron/PMC metadata and abstract identify the paper as a review discussing recent research. | confidence=high
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=Abstract discusses a common brain network underlying memory and imagination. | confidence=medium
- task_taxonomy: evidence=Abstract states the article examines remembering the past, imagining the future and default-network component processes. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: The Future of Memory: Remembering, Imagining, and the Brain
- auto_source_url: https://doi.org/10.1016/j.neuron.2012.11.001

### The features underlying the memorability of objects

Bibliographic:
- year: 2022
- venue: bioRxiv (Cold Spring Harbor Laboratory)
- doi: 10.1101/2022.04.29.490104

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Behavioral visual memory ratings for object images.
- input_modality: image/video
- task_taxonomy: Identify semantic and visual features that explain memorability of object images.
- paper_objective: Identify semantic and visual features that explain memorability of object images.
- method_family: Behavioral memorability-rating collection and feature/model analysis to predict image memorability and test whether typicality accounts for memorability.
- method_summary: Behavioral memorability-rating collection and feature/model analysis to predict image memorability and test whether typicality accounts for memorability.
- dataset: More than 1 million memory ratings for a naturalistic dataset of 26,107 object images.
- dataset_role: used
- metric: Memory ratings and model predictivity of image memorability.
- metric_status: applicable
- limitations: The authors frame prior work as limited by constrained stimulus sets; their own scope is a large but object-focused THINGS image set, and they identify future work on neuroimaging markers, other stimulus domains such as movies, scenes and non-visual stimuli, and biases in the typicality-memorability relationship.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1101/2022.04.29.490104; https://doi.org/10.1126/sciadv.add2981; https://www.researchgate.net/publication/370362744_The_features_underlying_the_memorability_of_objects; https://www.biorxiv.org/content/10.1101/2022.04.29.490104v1.full-text; https://www.science.org/doi/10.1126/sciadv.add2981; https://pure.mpg.de/rest/items/item_3508311_2/component/file_3597286/content
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=ResearchGate/Science Advances abstract states over 1 million memory ratings and 26,107 object images. | confidence=high
- limitations: evidence=The bioRxiv/Science Advances text says prior studies relied on constrained stimulus sets, notes that THINGS samples concrete object concepts, and the conclusion/future-work text calls for neuroimaging work and extension beyond objects to dynamic stimuli, scenes and non-visual stimuli. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=Abstract states the authors establish a model of object features predictive of image memorability and examine typicality. | confidence=high
- metric: evidence=Memory ratings are the empirical dependent measure; model predictivity is the reported analysis target. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=The data are human behavioral ratings of visual object images, not neural signals. | confidence=high
- task_taxonomy: evidence=Title and abstract define the goal as uncovering features underlying object memorability. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: The Features Underlying the Memorability of Objects
- auto_source_url: https://doi.org/10.1101/2022.04.29.490104

### The neural network RTNet exhibits the signatures of human perceptual decision-making

Bibliographic:
- year: 2024
- venue: Nature Human Behaviour
- doi: 10.1038/s41562-024-01914-8

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Perceptual decision-making and digit discrimination under difficulty and speed-accuracy manipulations.
- paper_objective: Perceptual decision-making and digit discrimination under difficulty and speed-accuracy manipulations.
- method_family: RTNet, a stochastic neural network with evidence accumulation designed to produce choices, response times and confidence.
- method_summary: RTNet, a stochastic neural network with evidence accumulation designed to produce choices, response times and confidence.
- dataset: MNIST handwritten digit images plus newly collected behavioral data from 60 human participants on a digit discrimination task.
- dataset_role: used
- metric: Accuracy, response time, confidence, RT distributions, and image-by-image correlations with human behavior.
- metric_status: applicable
- limitations: RTNet lacks recurrence and uses a non-optimal accumulation stopping rule; the paper notes future work is needed for state dependence.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41562-024-01914-8; https://pmc.ncbi.nlm.nih.gov/articles/PMC12261928/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=PMC text states the task used handwritten digits from MNIST and collected accuracy, RT and confidence from 60 human subjects. | confidence=high
- limitations: evidence=Author limitations mention non-optimal stopping and lack of recurrence/state dependence. | confidence=high
- method_summary: evidence=Abstract says RTNet generates stochastic decisions and human-like response time distributions. | confidence=high
- metric: evidence=Abstract and methods discuss accuracy, RT and confidence as core outputs compared to humans. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The verified study is an artificial neural network and behavioral decision model, not neural recordings. | confidence=high
- task_taxonomy: evidence=The paper tests an 8-choice digit discrimination perceptual decision task. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: The neural network RTNet exhibits the signatures of human perceptual decision-making
- auto_source_url: https://doi.org/10.1038/s41562-024-01914-8

### Towards Variable and Coordinated Holistic Co-Speech Motion Generation

Bibliographic:
- year: 2024
- venue: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
- doi: 10.1109/cvpr52733.2024.00155

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Audio-driven holistic co-speech motion generation for 3D avatars.
- paper_objective: Audio-driven holistic co-speech motion generation for 3D avatars.
- method_family: ProbTalk, a unified probabilistic PQ-VAE framework with MaskGIT-like non-autoregressive prediction, 2D positional encoding and a refinement stage.
- method_summary: ProbTalk, a unified probabilistic PQ-VAE framework with MaskGIT-like non-autoregressive prediction, 2D positional encoding and a refinement stage.
- dataset: SHOW dataset: 3D holistic body mesh annotations with synchronous audio from in-the-wild talkshow videos, 26.9 hours from 4 speakers.
- dataset_role: used
- metric: FGD for holistic/body/face realism, variance for diversity, FPS for inference efficiency, and L2 reconstruction errors.
- metric_status: applicable
- limitations: Ablations report trade-offs: product quantization improves FGD but reduces inference efficiency; MaskGIT speeds inference but can reduce generated-motion realism.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/cvpr52733.2024.00155; https://arxiv.org/html/2404.00368v1; https://openaccess.thecvf.com/content/CVPR2024/papers/Liu_Towards_Variable_and_Coordinated_Holistic_Co-Speech_Motion_Generation_CVPR_2024_paper.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Section 4.1 says SHOW contains synchronous audio and 3D holistic body mesh annotations from 26.9 hours of talkshow videos. | confidence=high
- limitations: evidence=Section 4.5 ablation text explicitly describes PQ and MaskGIT performance-efficiency trade-offs. | confidence=medium
- method_summary: evidence=Abstract and method describe ProbTalk with PQ-VAE, MaskGIT-like prediction, 2D positional encoding and refinement. | confidence=high
- metric: evidence=Evaluation Metrics section lists FGD, Variance, FPS and L2 errors. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The paper is a computer-vision/generation model using speech and motion data, not neural signals. | confidence=high
- task_taxonomy: evidence=Abstract states the problem is generating lifelike holistic co-speech motions for 3D avatars. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Towards Variable and Coordinated Holistic Co-Speech Motion Generation
- auto_source_url: https://doi.org/10.1109/cvpr52733.2024.00155

### Towards a “universal translator” for neural dynamics at single-cell, single-spike resolution

Bibliographic:
- year: 2024
- venue: Advances in Neural Information Processing Systems 37
- doi: 10.52202/079017-2559

Paper type:
- type: system

Evidence fields:
- signal_modality: Spike
- input_modality: spiking/electrophysiology
- task_taxonomy: Single-neuron and region-level activity prediction, forward prediction, and behavior decoding.
- paper_objective: Single-neuron and region-level activity prediction, forward prediction, and behavior decoding.
- method_family: Multi-task-masking (MtM), a self-supervised population activity model alternating masking/reconstruction across time steps, neurons and brain regions.
- method_summary: Multi-task-masking (MtM), a self-supervised population activity model alternating masking/reconstruction across time steps, neurons and brain regions.
- dataset: International Brain Laboratory repeated site dataset of multi-region Neuropixels recordings across animals/sessions.
- dataset_role: used
- metric: Bits per spike for activity prediction, R-squared for behavior prediction, and choice decoding accuracy.
- metric_status: applicable
- limitations: The authors state data diversity is still far below a full brain-wide map and that current NDT architectures may be less suited than more sophisticated models.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.52202/079017-2559; https://arxiv.org/abs/2407.14668; https://proceedings.neurips.cc/paper_files/paper/2024/file/934eb45b99eff8f16b5cb8e4d3cb5641-Paper-Conference.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Abstract identifies the IBL repeated site dataset with Neuropixels recordings targeting common brain locations. | confidence=high
- limitations: evidence=Conclusion says limitations remain in data diversity and current NDT architectures. | confidence=high
- method_summary: evidence=Abstract introduces a self-supervised modeling approach masking/reconstructing activity across time, neurons and regions. | confidence=high
- metric: evidence=Metrics section lists co-bps/bits per spike, R-squared and decoding accuracy. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- task_taxonomy: evidence=Abstract lists single-neuron, region-level, forward prediction and behavior decoding tasks. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Towards a "Universal Translator" for Neural Dynamics at Single-Cell, Single-Spike Resolution
- auto_source_url: https://doi.org/10.52202/079017-2559

### Tracking the Emergence of Conceptual Knowledge during Human Decision Making

Bibliographic:
- year: 2009
- venue: Neuron
- doi: 10.1016/j.neuron.2009.07.030

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: fMRI BOLD plus behavioral responses
- input_modality: fMRI
- task_taxonomy: Learning conceptual structure from related fractal patterns and using it for decision making and transfer to novel stimuli.
- paper_objective: Learning conceptual structure from related fractal patterns and using it for decision making and transfer to novel stimuli.
- method_family: Behavioral learning/probe trials with fractal stimuli combined with fMRI analyses of hippocampus and ventromedial prefrontal cortex.
- method_summary: Behavioral learning/probe trials with fractal stimuli combined with fMRI analyses of hippocampus and ventromedial prefrontal cortex.
- dataset: Human behavioral and fMRI data from a fractal-pattern weather-prediction/concept-learning task; group analyses report n=25.
- dataset_role: used
- metric: Percent correct responses, reaction times, confidence ratings, correlations with task-structure descriptions, and fMRI activation/regression analyses.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1016/j.neuron.2009.07.030; https://pmc.ncbi.nlm.nih.gov/articles/PMC2791172/; https://pubmed.ncbi.nlm.nih.gov/19778516/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=PMC figure text reports group-averaged n=25 performance and describes eight fractal patterns in Initial and New sessions. | confidence=high
- method_summary: evidence=PubMed abstract says hippocampus and vMPFC were studied as a coupled circuit underlying conceptual knowledge and choice behavior. | confidence=high
- metric: evidence=PMC text describes percent correct, reaction times, confidence ratings and fMRI data. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Article reports fMRI data and behavioral responses. | confidence=high
- task_taxonomy: evidence=Experimental design required participants to predict sun/rain outcomes from fractal patterns and transfer knowledge to new fractals. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Tracking the Emergence of Conceptual Knowledge during Human Decision Making
- auto_source_url: https://doi.org/10.1016/j.neuron.2009.07.030

### Unsupervised Embedding Learning via Invariant and Spreading Instance Feature

Bibliographic:
- year: 2019
- venue: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
- doi: 10.1109/cvpr.2019.00637

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Unsupervised visual embedding / metric representation learning.
- paper_objective: Unsupervised visual embedding / metric representation learning.
- method_family: Instance feature-based softmax embedding that learns augmentation-invariant and instance-spread-out features without labels.
- method_summary: Instance feature-based softmax embedding that learns augmentation-invariant and instance-spread-out features without labels.
- dataset: CIFAR-10, STL-10, CUB200-2011, Stanford Online Products and Cars196.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: The method assumes randomly sampled batch instances can be treated as negatives; the authors explicitly note this assumption may not always hold and batches may contain false negatives. Evaluation is bounded to seen-category and unseen-category image classification/embedding benchmarks with cosine similarity.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/cvpr.2019.00637; https://openaccess.thecvf.com/content_CVPR_2019/html/Ye_Unsupervised_Embedding_Learning_via_Invariant_and_Spreading_Instance_Feature_CVPR_2019_paper.html; https://arxiv.org/abs/1904.03436; https://openaccess.thecvf.com/content_CVPR_2019/papers/Ye_Unsupervised_Embedding_Learning_via_Invariant_and_Spreading_Instance_Feature_CVPR_2019_paper.pdf
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=CVF/arXiv paper experiments list CIFAR-10, STL-10 and fine-grained CUB200/Product/Cars datasets. | confidence=high
- limitations: evidence=The CVF paper states that treating randomly selected batch instances as negatives may not always hold and that batches may contain false negatives; its experiments are organized around seen and unseen testing-category protocols on CIFAR-10, STL-10, CUB200, Product and Car196. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=Abstract states the method directly optimizes real instance features on top of softmax to learn invariant and spread-out features. | confidence=high
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=Computer vision representation-learning paper; no neural data are used. | confidence=high
- task_taxonomy: evidence=Abstract says the paper studies unsupervised embedding learning. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Unsupervised Embedding Learning via Invariant and Spreading Instance Feature
- auto_source_url: https://doi.org/10.1109/cvpr.2019.00637

### VISION-XL: High Definition Video Inverse Problem Solver using Latent Image Diffusion Models

Bibliographic:
- year: 2025
- venue: 2025 IEEE/CVF International Conference on Computer Vision (ICCV)
- doi: 10.1109/iccv51701.2025.00974

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: High-definition video inverse problems including deblurring, super-resolution, inpainting, and spatio-temporal degradation restoration.
- paper_objective: High-definition video inverse problems including deblurring, super-resolution, inpainting, and spatio-temporal degradation restoration.
- method_family: Diffusion/generative model
- method_summary: Diffusion/generative model
- dataset: DAVIS and Pexels high-resolution video subsets; supplementary extension also uses GoPro for blind video deblurring.
- dataset_role: used
- metric: FVD, LPIPS, PSNR and SSIM.
- metric_status: applicable
- limitations: Experimental scope is bounded to an SDXL-based latent image diffusion solver for high-definition video inverse problems, evaluated on spatio-temporal degradations such as deblurring, super-resolution and inpainting, with runtime claims tied to a single NVIDIA 4090 GPU and landscape/vertical/square aspect ratios.
- limitation_source: explicit

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/iccv51701.2025.00974; https://arxiv.org/html/2412.00156; https://openaccess.thecvf.com/content/ICCV2025/papers/Kwon_VISION-XL_High_Definition_Video_Inverse_Problem_Solver_using_Latent_Image_ICCV_2025_paper.pdf
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=Dataset section says evaluation used four high-resolution video datasets from DAVIS and Pexels. | confidence=high
- limitations: evidence=CVF paper states the method addresses spatio-temporal inverse problems including deblurring, super-resolution and inpainting, supports landscape/vertical/square formats, and reports HD reconstruction under 6 seconds per frame on a single NVIDIA 4090 GPU; this supports an experimental-boundary limitation rather than a separate explicit limitations section. | confidence=medium | tier=tier1_paper_text
- metric: evidence=Evaluation section lists PSNR, SSIM, LPIPS and FVD. | confidence=high
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=Video restoration with latent image diffusion models; no neural signal. | confidence=high
- task_taxonomy: evidence=Abstract and experiments describe high-definition video inverse problem solving across spatial and spatio-temporal degradations. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: VISION-XL: High Definition Video Inverse Problem Solver using Latent Image Diffusion Models
- auto_source_url: https://doi.org/10.1109/iccv51701.2025.00974

### What Learning Systems do Intelligent Agents Need? Complementary Learning Systems Theory Updated

Bibliographic:
- year: 2016
- venue: Trends in Cognitive Sciences
- doi: 10.1016/j.tics.2016.05.004

Paper type:
- type: theory

Evidence fields:
- signal_modality: Neuroscience and cognitive theory review; no new signal modality.
- input_modality: not specified
- task_taxonomy: Update CLS theory and relate hippocampal/neocortical learning systems to artificial intelligent agents.
- paper_objective: Update CLS theory and relate hippocampal/neocortical learning systems to artificial intelligent agents.
- method_family: Review/theoretical update of complementary learning systems theory.
- method_summary: Review/theoretical update of complementary learning systems theory.
- dataset: No primary dataset; review/update of complementary learning systems theory connecting neuroscience and machine learning.
- dataset_role: none_review
- metric: unresolved
- metric_status: not_applicable
- limitations: The authors explicitly describe limitations of single-system learning: a structured neocortical parametric system alone cannot rapidly use individual experiences and suffers catastrophic interference, while a hippocampal system alone has capacity limitations and limited generalization.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1016/j.tics.2016.05.004; https://pubmed.ncbi.nlm.nih.gov/27315762/; https://web.stanford.edu/~jlmcc/papers/KumaranHassabisMcClelland16FinalMS.pdf
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=PubMed/E-utilities lists the publication type as Review and the abstract says the article updates complementary learning systems theory and highlights links between neuroscience and machine learning. | confidence=high | tier=tier1_paper_text
- limitations: evidence=Author manuscript states a parametric structured system alone has two drastic limitations, including individual-experience use and catastrophic interference; it also states a hippocampal system alone would be insufficient due to capacity limitations and limited generalization. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=PubMed marks the article as Review and its abstract says it updates CLS theory. | confidence=high
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=PubMed MeSH terms include hippocampus, neocortex and models, but the article is a review without new empirical recordings. | confidence=high
- task_taxonomy: evidence=Abstract says the paper broadens CLS theory and notes relevance to artificial intelligent agents. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: What Learning Systems do Intelligent Agents Need? Complementary Learning Systems Theory Updated
- auto_source_url: https://doi.org/10.1016/j.tics.2016.05.004

### A 7T fMRI dataset of synthetic images for out-of-distribution modeling of vision

Bibliographic:
- year: 2026
- venue: Nature Communications
- doi: 10.1038/s41467-026-69345-9

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: fMRI
- input_modality: fMRI
- task_taxonomy: Dataset/benchmark
- paper_objective: Dataset/benchmark
- method_family: Release and analysis of a 7T fMRI OOD visual dataset, with encoding-model and OOD generalization tests against NSD.
- method_summary: Release and analysis of a 7T fMRI OOD visual dataset, with encoding-model and OOD generalization tests against NSD.
- dataset: NSD-synthetic: 7T fMRI responses from the same eight Natural Scenes Dataset participants for 284 synthetic images.
- dataset_role: used
- metric: Noise-ceiling normalized encoding accuracy, OOD distributional distance in MDS embedding space, and zero-shot identification rank.
- metric_status: applicable
- limitations: Stimulus-related information is primarily encoded in early to intermediate visual areas because the synthetic stimuli mostly contain simple visual features and are less suited to higher visual cortex.
- limitation_source: explicit

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41467-026-69345-9; https://pmc.ncbi.nlm.nih.gov/articles/PMC12440068/; https://arxiv.org/abs/2503.06286
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Abstract states NSD-synthetic contains 7T fMRI responses from eight NSD participants for 284 synthetic images. | confidence=high
- limitations: evidence=Limitations section states responses are primarily in V1 to hV4 because stimuli are simple visual features. | confidence=high
- method_summary: evidence=Abstract describes release of NSD-synthetic and proof-of-principle OOD generalization tests. | confidence=high
- metric: evidence=PMC figure text describes encoding accuracy, OOD distance and zero-shot identification scores. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: A 7T fMRI dataset of synthetic images for out-of-distribution modeling of vision
- auto_source_url: https://doi.org/10.1038/s41467-026-69345-9

### A Brain-Inspired Way of Reducing the Network Complexity via Concept-Regularized Coding for Emotion Recognition

Bibliographic:
- year: 2024
- venue: Proceedings of the AAAI Conference on Artificial Intelligence
- doi: 10.1609/aaai.v38i1.27811

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: ECoG
- task_taxonomy: Visual reconstruction, Representation alignment, Emotion/cognitive state recognition, Dataset/benchmark
- paper_objective: Visual reconstruction, Representation alignment, Emotion/cognitive state recognition, Dataset/benchmark
- method_family: Dual-pathway concept-regularized perceptual network: a conceptual pathway disentangles emotion concepts from facial attributes and regularizes a perceptual CNN pathway.
- method_summary: Dual-pathway concept-regularized perceptual network: a conceptual pathway disentangles emotion concepts from facial attributes and regularizes a perceptual CNN pathway.
- dataset: RAF-DB, AffectNet and FED-RO facial emotion recognition datasets.
- dataset_role: used
- metric: Overall sample accuracy, number of parameters and inference runtime ratio.
- metric_status: applicable
- limitations: Experimental boundary: the paper validates the framework through FER experiments and IMAGEN style/identity analyses, including AnimeGAN-transformed faces, and does not present a separate author limitations section.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1609/aaai.v38i1.27811; https://ojs.aaai.org/index.php/AAAI/article/view/27811; https://openreview.net/pdf/3af5daef2d93a4db3d041fd1d9d06490ef3a1e10.pdf
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=Experiments section and tables list RAF-DB, AffectNet and FED-RO. | confidence=high
- limitations: evidence=The AAAI/OpenReview paper describes IMAGEN test splits, AnimeGAN-transformed animated faces, t-SNE analyses of emotion/non-emotion features, and concludes that experiments validate the framework's performance, effectiveness and generality. | confidence=medium | tier=tier1_paper_text
- method_summary: evidence=Abstract describes dual pathways, disentangled emotion concepts and emotional-confidence-guided regularization. | confidence=high
- metric: evidence=Experiment section states overall sample accuracy is the metric; Table 1 reports parameters and runtime ratio. | confidence=high
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=The paper uses facial images for AI emotion recognition, not neural recordings. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: A Brain-Inspired Way of Reducing the Network Complexity via Concept-Regularized Coding for Emotion Recognition
- auto_source_url: https://doi.org/10.1609/aaai.v38i1.27811

### A Level Set Theory for Neural Implicit Evolution Under Explicit Flows

Bibliographic:
- year: 2022
- venue: Lecture Notes in Computer Science
- doi: 10.1007/978-3-031-20086-1_41

Paper type:
- type: theory

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: text/speech
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: Parametric level-set evolution for neural implicit surfaces using explicit flow fields from mesh-based energy minimization.
- method_summary: Parametric level-set evolution for neural implicit surfaces using explicit flow fields from mesh-based energy minimization.
- dataset: Empirical evaluations use implicit surfaces/meshes and high-genus inverse-rendering shapes; no named dataset was identified in the main paper text.
- dataset_role: used
- metric: Chamfer distance and PSNR for inverse rendering, plus qualitative smoothing/mean-curvature/editing comparisons.
- metric_status: applicable
- limitations: Experimental boundary: the framework evolves neural implicit surfaces by extracting a Lagrangian surface, deriving an explicit mesh-based flow field, and updating the implicit geometry; validation is shown on surface smoothing/mean-curvature flow, inverse rendering and user-defined shape editing.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1007/978-3-031-20086-1_41; https://arxiv.org/abs/2204.07159; https://cseweb.ucsd.edu/~ravir/ishiteccv22.pdf
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=Paper reports evaluations on surface smoothing, inverse rendering of high-genus shapes and user-defined editing, without naming a standard dataset. | confidence=medium
- limitations: evidence=The paper says the method repeats surface extraction, mesh-based flow derivation and Eulerian flow-based implicit evolution, and validates on three settings: curvature-based deformation, inverse rendering and user-defined editing. | confidence=medium | tier=tier1_paper_text
- method_summary: evidence=Abstract says the method extends classical level-set theory to deform parametric implicit surfaces via flow fields. | confidence=high
- metric: evidence=Table text reports Chamfer distance for geometric consistency and PSNR for photometric reconstruction. | confidence=high
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=Computer vision/graphics neural implicit method; no neural signal modality. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: A Level Set Theory for Neural Implicit Evolution Under Explicit Flows
- auto_source_url: https://doi.org/10.1007/978-3-031-20086-1_41

### A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning

Bibliographic:
- year: 2010
- venue: International Conference on Artificial Intelligence and Statistics
- doi: 10.1184/r1/6550949

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: text/speech
- task_taxonomy: Dataset/benchmark
- paper_objective: Dataset/benchmark
- method_family: DAgger (Dataset Aggregation), an iterative no-regret online-learning reduction for imitation learning and structured prediction.
- method_summary: DAgger (Dataset Aggregation), an iterative no-regret online-learning reduction for imitation learning and structured prediction.
- dataset: Super Tux Kart driving tasks and the Taskar et al. OCR handwriting sequence-labeling benchmark of roughly 6,600 words.
- dataset_role: used
- metric: Task cost/surrogate loss, average falls per lap and acquisition/score-style driving measures, plus OCR word-level performance.
- metric_status: applicable
- limitations: The analysis requires a no-regret method or strongly convex surrogate loss, described by the authors as a stronger assumption.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://www.semanticscholar.org/paper/79ab3c49903ec8cb339437ccf5cf998607fc313e; https://proceedings.mlr.press/v15/ross11a.html; http://proceedings.mlr.press/v15/ross11a/ross11a.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Experiments section lists Super Tux Kart and Taskar OCR dataset with roughly 6,600 words. | confidence=high
- limitations: evidence=Theory section says requiring a no-regret method or strongly convex surrogate loss is a stronger assumption. | confidence=medium
- method_summary: evidence=Paper presents DAGGER as Dataset Aggregation and analyzes it as no-regret online learning. | confidence=high
- metric: evidence=Experiments report average falls per lap for driving and OCR structured prediction performance. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Imitation learning/structured prediction algorithm paper; no neural recordings. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning
- auto_source_url: https://www.semanticscholar.org/paper/79ab3c49903ec8cb339437ccf5cf998607fc313e

### A Vector Quantized Approach for Text to Speech Synthesis on Real-World Spontaneous Speech

Bibliographic:
- year: 2023
- venue: Proceedings of the AAAI Conference on Artificial Intelligence
- doi: 10.1609/aaai.v37i11.26488

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: text/speech
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: MQTTS, a multi-codebook vector-quantized autoregressive TTS system with monotonic alignment, sub-decoder sampling and clean-silence prompting.
- method_summary: MQTTS, a multi-codebook vector-quantized autoregressive TTS system with monotonic alignment, sub-decoder sampling and clean-silence prompting.
- dataset: GigaSpeech Podcast and YouTube speech after cleaning, yielding 896 hours of real-world spontaneous speech; VoxCeleb is used for reconstruction evaluation.
- dataset_role: used
- metric: RCER, WER, MOS-Q, MOS-N, MCD and P-FID.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1609/aaai.v37i11.26488; https://arxiv.org/abs/2302.04215; https://ojs.aaai.org/index.php/AAAI/article/view/26488
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Dataset section says the model uses GigaSpeech Podcast and YouTube speech and the resulting dataset contains 896 hours. | confidence=high
- method_summary: evidence=Abstract and methods describe learned discrete codes, multiple codebooks, monotonic alignment, sub-decoder and silence prompt. | confidence=high
- metric: evidence=Evaluation section lists ASR error rates, MOS, MCD and P-FID. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=TTS system trained on speech audio/text; no neural recordings. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: A Vector Quantized Approach for Text to Speech Synthesis on Real-World Spontaneous Speech
- auto_source_url: https://doi.org/10.1609/aaai.v37i11.26488

### A brain machine interface control algorithm designed from a feedback control perspective

Bibliographic:
- year: 2012
- venue: 2012 Annual International Conference of the IEEE Engineering in Medicine and Biology Society
- doi: 10.1109/embc.2012.6346180

Paper type:
- type: perspective

Evidence fields:
- signal_modality: Intracortical spike counts from a 96-electrode Utah array in macaque PMd/M1.
- input_modality: spiking/electrophysiology
- task_taxonomy: Closed-loop BCI
- paper_objective: Closed-loop BCI
- method_family: Recalibrated feedback intention-trained Kalman filter (ReFIT-KF) for closed-loop BMI control.
- method_summary: Recalibrated feedback intention-trained Kalman filter (ReFIT-KF) for closed-loop BMI control.
- dataset: Online neural control experiments from one male rhesus macaque implanted with a 96-electrode Utah array in PMd/M1 during 2D cursor control.
- dataset_role: used
- metric: Mean target acquisition time and success rate in center-out-and-back cursor tasks.
- metric_status: applicable
- limitations: Experimental boundary and modeling caveat: the study tested ReFIT-KF in one adult male rhesus macaque with a 96-electrode PMd/M1 array on a 2D center-out-and-back cursor task, and assumes the user internalizes cursor position feedback with complete certainty.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/embc.2012.6346180; https://users.ece.cmu.edu/~byronyu/papers/GiljaEMBS2012.pdf; https://pubmed.ncbi.nlm.nih.gov/23366141/
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=Methods state a male rhesus macaque had a 96-electrode Utah array implanted in PMd/M1. | confidence=high
- limitations: evidence=The paper states experiments used an adult male rhesus macaque implanted with a 96-electrode Utah array in PMd/M1, describes the 2D center-out-and-back target task, and explicitly says the filter presumes the user internalizes estimated cursor position with complete certainty. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=Abstract names the recalibrated feedback intention-trained Kalman filter. | confidence=high
- metric: evidence=Results and tables report mean acquisition times and success rates. | confidence=high
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=Paper describes thresholded spike events counted per channel as control inputs. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: A brain machine interface control algorithm designed from a feedback control perspective
- auto_source_url: https://doi.org/10.1109/embc.2012.6346180

### A brain-to-text framework of decoding natural tonal sentences

Bibliographic:
- year: 2024
- venue: Cell Reports
- doi: 10.1016/j.celrep.2024.114924

Paper type:
- type: system

Evidence fields:
- signal_modality: High-density ECoG from speech sensorimotor cortex / invasive neural recordings.
- input_modality: ECoG
- task_taxonomy: Neural decoding, Speech/language decoding
- paper_objective: Neural decoding, Speech/language decoding
- method_family: Brain-to-text decoding framework with multi-stream neural decoders for speech onset/base syllables/lexical tones combined with contextual language modeling via Bayesian likelihood and Viterbi decoding.
- method_summary: Brain-to-text decoding framework with multi-stream neural decoders for speech onset/base syllables/lexical tones combined with contextual language modeling via Bayesian likelihood and Viterbi decoding.
- dataset: High-density ECoG recordings from participants/patients producing natural Mandarin tonal sentences with an associated sentence corpus.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1016/j.celrep.2024.114924; https://www.biorxiv.org/content/10.1101/2024.03.16.585337v3.full-text; https://www.researchgate.net/publication/385467799_A_brain-to-text_framework_for_decoding_natural_tonal_sentences
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Cell Reports/ResearchGate preview describes high-density ECoG recordings and Mandarin natural tonal sentence decoding. | confidence=medium
- method_summary: evidence=Abstract says the modular approach dissects speech onset, base syllables and lexical tones and integrates contextual information through Bayesian likelihood and Viterbi decoder. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Cell Reports preview highlights high-density ECoG grid recordings from ventral sensorimotor cortex. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: A brain-to-text framework for decoding natural tonal sentences
- auto_source_url: https://doi.org/10.1016/j.celrep.2024.114924

### A distributional code for value in dopamine-based reinforcement learning

Bibliographic:
- year: 2020
- venue: Nature
- doi: 10.1038/s41586-019-1924-6

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Single-unit neuronal recordings from mouse ventral tegmental area dopamine-related circuits.
- input_modality: not specified
- task_taxonomy: Testing whether dopamine neurons represent future rewards as a distribution rather than a single expected value.
- paper_objective: Testing whether dopamine neurons represent future rewards as a distribution rather than a single expected value.
- method_family: Reinforcement learning/bandit
- method_summary: Reinforcement learning/bandit
- dataset: Single-unit recordings from mouse ventral tegmental area; neuronal data are available through OSF.
- dataset_role: used
- metric: Reward-response reversal points, asymmetric positive/negative prediction-error scaling, decoded reward distributions, model comparisons and statistical tests.
- metric_status: applicable
- limitations: Experimental boundary: the empirical test of the distributional reinforcement-learning account used single-unit recordings from mouse ventral tegmental area, with neuronal data made available separately.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41586-019-1924-6; https://www.nature.com/articles/s41586-019-1924-6; https://doi.org/10.17605/OSF.IO/UX5RG
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=Nature abstract says predictions were tested using single-unit recordings from mouse ventral tegmental area; data availability links neuronal data. | confidence=high
- limitations: evidence=Nature abstract states the empirical predictions were tested using single-unit recordings from mouse ventral tegmental area; data availability identifies the neuronal data analysed in the work. | confidence=medium | tier=tier1_paper_text
- metric: evidence=Figures and captions discuss reversal points, asymmetric scaling, decoded reward distributions and model comparison statistics. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=Abstract explicitly identifies single-unit recordings from mouse VTA. | confidence=high
- task_taxonomy: evidence=Abstract states the hypothesis that future rewards are represented as a probability distribution. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: A distributional code for value in dopamine-based reinforcement learning
- auto_source_url: https://doi.org/10.1038/s41586-019-1924-6

### A generalist vision–language foundation model for diverse biomedical tasks

Bibliographic:
- year: 2024
- venue: Nature Medicine
- doi: 10.1038/s41591-024-03185-2

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Foundation model/pretraining
- paper_objective: Foundation model/pretraining
- method_family: BiomedGPT, an open-source lightweight vision-language foundation model trained on diverse biomedical data for multiple tasks.
- method_summary: BiomedGPT, an open-source lightweight vision-language foundation model trained on diverse biomedical data for multiple tasks.
- dataset: Public biomedical image, vision-language, clinical text and dialogue datasets including IU X-ray, MedICat, PathVQA, SLAKE, DeepLesion, CheXpert, MIMIC-CXR, MedNLI, MedMNIST v2, ROCO and others.
- dataset_role: used
- metric: State-of-the-art count across 25 experiments, human evaluation, QA/report error rates, summarization preference scores and task-specific downstream metrics.
- metric_status: applicable
- limitations: The authors outline several limitations: data diversity and large-scale high-quality biomedical data constrain unified biomedical AI; automatic evaluation of generative biomedical tasks is imperfect; expanding modalities risks negative transfer; scaling is constrained by compute/storage and brings fine-tuning, speed and memory challenges; text understanding and multiple-input processing remain underdeveloped.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41591-024-03185-2; https://www.nature.com/articles/s41591-024-03185-2; https://github.com/taokz/BiomedGPT; https://ar5iv.labs.arxiv.org/html/2305.17100; https://arxiv.org/abs/2305.17100
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=Nature data availability lists the public datasets used in the study. | confidence=high
- limitations: evidence=Discussion explicitly says it delves into limitations. It identifies public dataset imbalance and scarce large-scale multimodal biomedical data, challenges in automatic evaluation of freeform biomedical generation, negative transfer when expanding modalities, constrained model scaling, and not fully established text comprehension/multiple-input processing. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=Abstract describes BiomedGPT as an open-source lightweight vision-language foundation model. | confidence=high
- metric: evidence=Abstract reports 16/25 experiments and human evaluation error rates of 3.8% and 8.3%. | confidence=high
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=Biomedical vision-language AI model using images/text; no neural recordings. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: A generalist vision–language foundation model for diverse biomedical tasks
- auto_source_url: https://doi.org/10.1038/s41591-024-03185-2

### A streaming brain-to-voice neuroprosthesis to restore naturalistic communication

Bibliographic:
- year: 2025
- venue: Nature Neuroscience
- doi: 10.1038/s41593-025-01905-6

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: High-density surface ECoG from speech sensorimotor cortex; generalization also tested on single-unit recordings and EMG.
- input_modality: ECoG
- task_taxonomy: Neural decoding
- paper_objective: Neural decoding
- method_family: Continuously streaming speech neuroprosthesis using recurrent neural network transducer models to synthesize personalized naturalistic speech from neural activity.
- method_summary: Continuously streaming speech neuroprosthesis using recurrent neural network transducer models to synthesize personalized naturalistic speech from neural activity.
- dataset: Clinical-trial participant with severe paralysis/anarthria recorded with high-density surface ECoG; related ECoG, EMG and MEA data are linked in data availability.
- dataset_role: used
- metric: 80-ms neural decoding/synthesis increments, latency/speed measures, phone/character/word error rates and intelligibility-style decoding metrics.
- metric_status: applicable
- limitations: Experimental boundary: online results were demonstrated in a single clinical-trial participant with severe paralysis and anarthria using high-density surface recordings; data sharing is restricted by the clinical protocol and participant anonymity constraints.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41593-025-01905-6; https://www.nature.com/articles/s41593-025-01905-6; https://doi.org/10.7910/DVN/8TQKC8; https://www.researchgate.net/publication/390354721_A_streaming_brain-to-voice_neuroprosthesis_to_restore_naturalistic_communication
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=Nature abstract describes one clinical-trial participant with high-density surface recordings; data availability lists ECoG, EMG and MEA datasets. | confidence=high
- limitations: evidence=Nature abstract states the system used high-density surface recordings from one clinical-trial participant with severe paralysis and anarthria. Data availability says relevant data are restricted under the clinical trial protocol and cannot be made publicly available, with identifying information excluded. | confidence=medium | tier=tier1_paper_text
- method_summary: evidence=Abstract states RNN-T models drove online large-vocabulary fluent speech synthesis personalized to the participant's preinjury voice. | confidence=high
- metric: evidence=Abstract gives 80-ms increments; ResearchGate/Nature preview material reports phone/character/word error-rate analyses. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=Abstract states high-density surface recordings of speech sensorimotor cortex and generalization to single-unit recordings and EMG. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: A streaming brain-to-voice neuroprosthesis to restore naturalistic communication
- auto_source_url: https://doi.org/10.1038/s41593-025-01905-6

### Accurate digitization of EEG electrode locations by electromagnetic tracking system: The proposed head rotation method and comparison against optical system

Bibliographic:
- year: 2024
- venue: MethodsX
- doi: 10.1016/j.mex.2024.102766

Paper type:
- type: system

Evidence fields:
- signal_modality: EEG
- input_modality: EEG
- task_taxonomy: Accurate EEG electrode localization for EEG source estimation.
- paper_objective: Accurate EEG electrode localization for EEG source estimation.
- method_family: Electromagnetic head-rotation digitization method compared with conventional electromagnetic digitization and an optical system.
- method_summary: Electromagnetic head-rotation digitization method compared with conventional electromagnetic digitization and an optical system.
- dataset: Digitization measurements from mannequin/human head electrode-location experiments comparing optical and electromagnetic systems.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: The paper explicitly states 'Limitations: None.'
- limitation_source: explicit

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1016/j.mex.2024.102766; https://pmc.ncbi.nlm.nih.gov/articles/PMC11131068/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=PMC text describes mannequin head and human head comparisons of EEG electrode digitization. | confidence=medium
- limitations: evidence=Limitations section says 'None.' | confidence=high
- method_summary: evidence=Abstract explains rotating the participant on a swivel chair for consistent electromagnetic digitization and comparing methods. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- task_taxonomy: evidence=Abstract states EEG electrode digitization is crucial for accurate EEG source estimation. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Accurate digitization of EEG electrode locations by electromagnetic tracking system: The proposed head rotation method and comparison against optical system
- auto_source_url: https://doi.org/10.1016/j.mex.2024.102766

### Accurate structure prediction of biomolecular interactions with AlphaFold 3

Bibliographic:
- year: 2026
- venue: Nature
- doi: 10.55277/researchhub.zto7x62j

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: protein sequence/structure
- task_taxonomy: Predicting joint 3D structures of biomolecular complexes including proteins, nucleic acids, ligands, ions and modified residues.
- paper_objective: Predicting joint 3D structures of biomolecular complexes including proteins, nucleic acids, ligands, ions and modified residues.
- method_family: Diffusion/generative model
- method_summary: Diffusion/generative model
- dataset: Protein Data Bank training/evaluation data with cutoffs, PoseBusters, recent PDB evaluation sets and CASP15 RNA targets.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: AF3 predicts static PDB-like structures rather than solution dynamics; conformational coverage is limited, some targets remain challenging, and high accuracy may require many ranked seeds.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.55277/researchhub.zto7x62j; https://www.nature.com/articles/s41586-024-07487-w; https://pubmed.ncbi.nlm.nih.gov/38718835/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Nature article describes PDB training cutoffs and evaluations on PoseBusters, recent PDB and CASP15 RNA. | confidence=high
- limitations: evidence=Discussion explicitly names static-structure prediction, limited conformation coverage and computational cost for many seeds. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Computational structure-prediction model; no neural signal data. | confidence=high
- task_taxonomy: evidence=Abstract says AF3 predicts joint structures of complexes containing proteins, nucleic acids, small molecules, ions and modified residues. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Accurate structure prediction of biomolecular interactions with AlphaFold 3
- auto_source_url: https://doi.org/10.55277/researchhub.zto7x62j

### Accurate transition state generation with an object-aware equivariant elementary reaction diffusion model

Bibliographic:
- year: 2023
- venue: Nature Computational Science
- doi: 10.1038/s43588-023-00563-7

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Generating 3D transition-state structures from reactant and product structures for elementary chemical reactions.
- paper_objective: Generating 3D transition-state structures from reactant and product structures for elementary chemical reactions.
- method_family: Diffusion/generative model
- method_summary: Diffusion/generative model
- dataset: Transition1x dataset.
- dataset_role: used
- metric: Transition-state RMSD to the true TS and reaction-barrier accuracy threshold of 2.6 kcal mol-1, with confidence scoring for uncertainty.
- metric_status: applicable
- limitations: The authors explicitly state two major limitations: representing each elementary reaction as reactant, transition-state and product structures creates a 3N-atom system whose scalar message passing becomes a bottleneck for systems over 100 atoms on a single GPU; the diffusion model's stochastic nature causes sample-quality uncertainty and accumulated runtime from repeated sampling, despite the confidence model workaround.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s43588-023-00563-7; https://www.nature.com/articles/s43588-023-00563-7; https://arxiv.org/abs/2304.06174; https://gitlab.com/matschreiner/Transition1x
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=Nature data availability says the Transition1x dataset was used. | confidence=high
- limitations: evidence=The arXiv/paper text says the current OA-ReactDiff approach has two major limitations: the 3N representation and fully connected graph bottleneck for chemical systems over 100 atoms on one GPU, and unavoidable stochasticity causing uncertainty in generated transition-state quality and repeated-runtime cost. | confidence=high | tier=tier1_paper_text
- metric: evidence=Abstract reports median 0.08 Å RMSD and approaching 2.6 kcal mol-1 barrier accuracy after optimizing the most challenging reactions. | confidence=high
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=Computational chemistry generative model; no neural signal data. | confidence=high
- task_taxonomy: evidence=Abstract states the model generates reactant, transition state and product structures for elementary reactions. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Accurate transition state generation with an object-aware equivariant elementary reaction diffusion model
- auto_source_url: https://doi.org/10.1038/s43588-023-00563-7

### Addressing Spatial-Temporal Heterogeneity: General Mixed Time Series Analysis via Latent Continuity Recovery and Alignment

Bibliographic:
- year: 2024
- venue: Advances in Neural Information Processing Systems 37
- doi: 10.52202/079017-0569

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: Transformer, Linear/encoding baseline
- method_summary: Transformer, Linear/encoding baseline
- dataset: The experiments use 34 mixed time-series benchmark datasets across five task families: UEA 10 subsets, UCR 10 subsets, ETT 4 subsets, Electricity, Weather, SMD, MSL, SMAP, SWaT, PSM, Traffic, Exchange, and ILI; mixed variables are constructed by discretizing half of variables.
- dataset_role: used
- metric: Classification uses Accuracy; extrinsic regression uses MAE and RMSE; imputation and long-term forecasting use MSE and MAE; anomaly detection uses Precision, Recall, and F1-score.
- metric_status: applicable
- limitations: Experimental MiTS inputs are partly synthetic: for each dataset, half of variables are randomly selected, MinMax-normalized, and binarized as discrete variables.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.52202/079017-0569; https://proceedings.neurips.cc/paper_files/paper/2024/file/1feb87871436031bdc0f2beaa62a049b-Paper-Conference.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Paper states SOTA on five tasks with 34 datasets; Table 1 lists UEA, UCR, ETT, Electricity, Weather, SMD, MSL, SMAP, SWaT, PSM, Traffic, Exchange, ILI. | confidence=high
- limitations: evidence=Table 1 note: each dataset randomly selects half of variables as DVs and discretizes them with threshold 0.5. | confidence=medium
- metric: evidence=Table 1 explicitly maps tasks to Accuracy, MAE/RMSE, MSE/MAE, and Precision/Recall/F1-score. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The work is general mixed time-series analysis and does not use neural recordings. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Addressing Spatial-Temporal Heterogeneity: General Mixed Time Series Analysis via Latent Continuity Recovery and Alignment
- auto_source_url: https://doi.org/10.52202/079017-0569

### Adopting a human developmental visual diet yields robust and shape-based AI vision

Bibliographic:
- year: 2026
- venue: Nature Machine Intelligence
- doi: 10.1038/s42256-026-01228-6

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: Developmental Visual Diet (DVD), a human-inspired visual curriculum/preprocessing pipeline modeling development of visual acuity, contrast sensitivity, and colour during training.
- method_summary: Developmental Visual Diet (DVD), a human-inspired visual curriculum/preprocessing pipeline modeling development of visual acuity, contrast sensitivity, and colour during training.
- dataset: mini-ecoset, ecoset, and ImageNet-1K training datasets; IllusionBench-IN and cue-conflict stimuli are used in evaluation.
- dataset_role: used
- metric: Shape bias, ImageNet/object recognition accuracy, shape recall and scene recall, corruption accuracy, and adversarial robustness accuracy.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s42256-026-01228-6; https://www.nature.com/articles/s42256-026-01228-6; https://arxiv.org/abs/2507.03168
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Nature article reports training on mini-ecoset, ecoset, and ImageNet-1K, and evaluates abstract shape recognition with IllusionBench-IN. | confidence=high
- method_summary: evidence=Abstract states DVD considers development of visual acuity, contrast sensitivity and colour. | confidence=high
- metric: evidence=Methods define shape bias and shape/scene recall; robustness sections record accuracy under corruptions and adversarial perturbations. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The study trains artificial vision models and uses behavioral/psychophysical inspiration, not neural recordings. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Adopting a human developmental visual diet yields robust and shape-based AI vision
- auto_source_url: https://doi.org/10.1038/s42256-026-01228-6

### Algorithmic localization of high-density EEG electrode positions using motion capture

Bibliographic:
- year: 2020
- venue: Journal of Neuroscience Methods
- doi: 10.1016/j.jneumeth.2020.108919

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: EEG
- input_modality: EEG
- task_taxonomy: Automatic localization/interpolation of high-density EEG electrode positions for EEG-MRI co-registration and source localization.
- paper_objective: Automatic localization/interpolation of high-density EEG electrode positions for EEG-MRI co-registration and source localization.
- method_family: MoLo, an open-source MATLAB toolbox using spline interpolation to compute 3D high-density EEG electrode coordinates from a subset of motion-capture-measured positions.
- method_summary: MoLo, an open-source MATLAB toolbox using spline interpolation to compute 3D high-density EEG electrode coordinates from a subset of motion-capture-measured positions.
- dataset: Evaluation used 5 different-sized head models and 64-channel EEG electrode localization.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1016/j.jneumeth.2020.108919; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=32853593&retmode=xml
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=PubMed XML abstract: algorithm accuracy was evaluated across 5 different-sized head models and reduced setup time for 64-channel EEG. | confidence=high
- method_summary: evidence=PubMed XML abstract: developed MoLo to compute 3D electrode coordinates from a subset of positions measured in motion capture using spline interpolation. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- task_taxonomy: evidence=Background and conclusion state the goal is precise 3D scalp/electrode measurement for EEG source localization. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Algorithmic localization of high-density EEG electrode positions using motion capture
- auto_source_url: https://doi.org/10.1016/j.jneumeth.2020.108919

### Aligning Model and Macaque Inferior Temporal Cortex Representations Improves Model-to-Human Behavioral Alignment and Adversarial Robustness

Bibliographic:
- year: 2022
- venue: bioRxiv (Cold Spring Harbor Laboratory)
- doi: 10.1101/2022.07.01.498495

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Macaque inferior temporal cortex multi-electrode neural recordings
- input_modality: spiking/electrophysiology
- task_taxonomy: Visual reconstruction, Representation alignment, Dataset/benchmark
- paper_objective: Visual reconstruction, Representation alignment, Dataset/benchmark
- method_family: End-to-end fine-tuning of model late-stage "IT" representations to align with biological macaque IT representations while preserving object recognition accuracy.
- method_summary: End-to-end fine-tuning of model late-stage "IT" representations to align with biological macaque IT representations while preserving object recognition accuracy.
- dataset: Chronic large-scale multi-electrode recordings across macaque inferior temporal cortex in six rhesus macaques, validated on held-out animals across two image sets.
- dataset_role: used
- metric: accuracy, correlation
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1101/2022.07.01.498495; https://openreview.net/forum?id=SMYdcXjJh1q; https://www.biorxiv.org/content/10.1101/2022.07.01.498495v1.full-text
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=OpenReview abstract states recordings were made across IT cortex in six non-human primates and validated on held-out animals across two image sets. | confidence=high
- method_summary: evidence=OpenReview abstract states the model "IT" representations are fine-tuned end-to-end to align with biological IT representations. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=OpenReview keywords and abstract identify primate vision and macaque IT cortex neural population activity. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Aligning Model and Macaque Inferior Temporal Cortex Representations Improves Model-to-Human Behavioral Alignment and Adversarial Robustness
- auto_source_url: https://doi.org/10.1101/2022.07.01.498495

### Aligning individual brains with Fused Unbalanced Gromov-Wasserstein

Bibliographic:
- year: 2022
- venue: Advances in Neural Information Processing Systems 35
- doi: 10.52202/068431-1584

Paper type:
- type: system

Evidence fields:
- signal_modality: Human fMRI
- input_modality: fMRI
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: Fused Unbalanced Gromov-Wasserstein optimal transport for inter-subject cortical surface alignment and functional barycenters.
- method_summary: Fused Unbalanced Gromov-Wasserstein optimal transport for inter-subject cortical surface alignment and functional barycenters.
- dataset: Individual Brain Charting dataset: 12 human subjects, 400 fMRI contrast maps per subject, with 326/43/30 train/validation/test contrast maps.
- dataset_role: used
- metric: Pearson correlation gain between aligned source and target fMRI contrast maps, plus transported mass, vertex displacement, vertex spread, and t-statistic maps for barycenter analyses.
- metric_status: applicable
- limitations: The authors note the cohort may be too small to show a strong unbalanced-vs-balanced OT gain; barycenters rely on predefined fsaverage5 anatomy; the entropic solver adds a strong but hard-to-interpret epsilon hyperparameter.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.52202/068431-1584; https://proceedings.neurips.cc/paper_files/paper/2022/file/8906cac4ca58dcaf17e97a0486ad57ca-Paper-Conference.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Paper dataset section gives Individual Brain Charting, 12 subjects and 400 fMRI maps per subject with split sizes. | confidence=high
- limitations: evidence=Discussion states small cohort, predefined fsaverage5 template, and hard-to-interpret entropic epsilon. | confidence=high
- method_summary: evidence=Abstract and method formulate FUGW as OT alignment over anatomical and functional constraints. | confidence=high
- metric: evidence=Experimental section defines Pearson correlation, transported mass, vertex displacement, vertex spread, and barycenter t-statistics. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Dataset consists of functional MRI contrast maps. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Aligning Individual Brains with Fused Unbalanced Gromov Wasserstein
- auto_source_url: https://doi.org/10.52202/068431-1584

### AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models

Bibliographic:
- year: 2021
- venue: Nucleic Acids Research
- doi: 10.1093/nar/gkab1061

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: protein sequence/structure
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: A public database of AlphaFold v2.0 protein-structure predictions with programmatic access, interactive visualization, atomic coordinates, per-residue confidence, and predicted aligned error.
- method_summary: A public database of AlphaFold v2.0 protein-structure predictions with programmatic access, interactive visualization, atomic coordinates, per-residue confidence, and predicted aligned error.
- dataset: AlphaFold DB initial release contains over 360,000 predicted structures across 21 model-organism proteomes, with planned expansion to representative UniRef90 sequences.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: Predictions include confidence information; the article notes examples where AlphaFold has high confidence in some domain positions but not linker/C-terminal regions, so users must consider per-residue and aligned-error confidence.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1093/nar/gkab1061; https://academic.oup.com/nar/article/50/D1/D439/6430488
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=NAR abstract and Table 1 state the first version has over 360,000 models of 21 species. | confidence=high
- limitations: evidence=NAR article discusses high confidence in some domains but not other regions and provides confidence metrics. | confidence=medium
- method_summary: evidence=Abstract says AlphaFold DB is powered by AlphaFold v2.0 and provides coordinates, confidence estimates, and PAE. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=This is computational protein-structure prediction, not neural data. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models
- auto_source_url: https://doi.org/10.1093/nar/gkab1061

### Are Transformers Effective for Time Series Forecasting?

Bibliographic:
- year: 2023
- venue: Proceedings of the AAAI Conference on Artificial Intelligence
- doi: 10.1609/aaai.v37i9.26317

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Long-term time series forecasting.
- paper_objective: Long-term time series forecasting.
- method_family: Transformer
- method_summary: Transformer
- dataset: Nine real-world multivariate time-series benchmarks: ETTh1, ETTh2, ETTm1, ETTm2, Traffic, Electricity, Exchange-Rate, Weather, and ILI.
- dataset_role: used
- metric: Mean Squared Error (MSE) and Mean Absolute Error (MAE).
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1609/aaai.v37i9.26317; https://ojs.aaai.org/index.php/AAAI/article/view/26317/26089
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=AAAI paper dataset section lists ETT variants, Traffic, Electricity, Weather, ILI, and Exchange-Rate. | confidence=high
- metric: evidence=Evaluation metric section states MSE and MAE are used. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The paper evaluates time-series forecasting models, not neural recordings. | confidence=high
- task_taxonomy: evidence=Abstract and introduction frame the work as long-term time series forecasting. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Are Transformers Effective for Time Series Forecasting?
- auto_source_url: https://doi.org/10.1609/aaai.v37i9.26317

### Attention Is All You Need

Bibliographic:
- year: 2025
- venue: arXiv
- doi: 10.65215/nxvz2v36

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Sequence transduction / neural machine translation.
- paper_objective: Sequence transduction / neural machine translation.
- method_family: Transformer, CNN/RNN deep model
- method_summary: Transformer, CNN/RNN deep model
- dataset: WMT 2014 English-German and WMT 2014 English-French machine translation datasets.
- dataset_role: used
- metric: generation quality
- metric_status: applicable
- limitations: The conclusion identifies future work on other modalities, local/restricted attention for large inputs and outputs, and making generation less sequential.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.65215/nxvz2v36; https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=NeurIPS paper training section states WMT 2014 English-German and English-French datasets. | confidence=high
- limitations: evidence=Conclusion says they plan to extend to other modalities, investigate restricted attention for large inputs/outputs, and make generation less sequential. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The paper is NLP sequence modeling with no neural recordings. | confidence=high
- task_taxonomy: evidence=Abstract reports experiments on two machine translation tasks. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Attention Is All You Need
- auto_source_url: https://doi.org/10.65215/nxvz2v36

### BAD: Bidirectional Auto-regressive Diffusion for Text-to-Motion Generation

Bibliographic:
- year: 2025
- venue: ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)
- doi: 10.1109/icassp49660.2025.10889942

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: text/speech
- task_taxonomy: Text-to-motion generation, with additional text-guided motion inpainting and outpainting experiments.
- paper_objective: Text-to-motion generation, with additional text-guided motion inpainting and outpainting experiments.
- method_family: Diffusion/generative model
- method_summary: Diffusion/generative model
- dataset: HumanML3D and KIT-ML text-to-motion datasets.
- dataset_role: used
- metric: Frechet Inception Distance (FID), R-Precision, and MM-Dist are reported for text-to-motion quality and text-motion consistency.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/icassp49660.2025.10889942; https://arxiv.org/html/2409.10847v1; https://github.com/RohollahHS/BAD; https://doi.org/10.1109/ICASSP49660.2025.10889942
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=arXiv HTML states experiments are based on HumanML3D and KIT-ML. | confidence=high
- metric: evidence=Results discussion states BAD improves FID and also improves R-Precision and MM-Dist. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The inputs are text and 3D human motion, not neural recordings. | confidence=high
- task_taxonomy: evidence=Abstract and introduction define the task as text-to-motion generation. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: BAD: Bidirectional Auto-Regressive Diffusion for Text-to-Motion Generation
- auto_source_url: https://doi.org/10.1109/icassp49660.2025.10889942

### Better models of human high-level visual cortex emerge from natural language supervision with a large and diverse dataset

Bibliographic:
- year: 2023
- venue: Nat. Mac. Intell.
- doi: 10.1038/S42256-023-00753-Y

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Human 7T fMRI
- input_modality: fMRI
- task_taxonomy: Visual reconstruction, Speech/language decoding, Dataset/benchmark
- paper_objective: Visual reconstruction, Speech/language decoding, Dataset/benchmark
- method_family: Voxelwise encoding models based on CLIP image features are used to predict human visual-cortex fMRI responses to real-world images.
- method_summary: Voxelwise encoding models based on CLIP image features are used to predict human visual-cortex fMRI responses to real-world images.
- dataset: Natural Scenes Dataset (NSD), a large-scale fMRI dataset of participants viewing thousands of natural images.
- dataset_role: used
- metric: Explained variance / R^2 in held-out voxel responses, including up to R^2 = 79%.
- metric_status: applicable
- limitations: Experimental boundary: the study uses CLIP-based voxelwise encoding models to predict human high-level visual cortex responses to real-world images from the Natural Scenes Dataset; findings are bounded to this NSD fMRI setting and the compared CLIP/ImageNet/BERT-style model families.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s42256-023-00753-y; https://www.nature.com/articles/s42256-023-00753-y
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=Nature data availability states the study uses NSD. | confidence=high
- limitations: evidence=Nature abstract states the authors used CLIP-pretrained models and voxelwise encoding models to predict brain responses to real-world images, reporting high-level visual cortex results; data availability states they used the Natural Scenes Dataset, a large-scale fMRI dataset of participants viewing thousands of natural images. | confidence=medium | tier=tier1_paper_text
- method_summary: evidence=Nature abstract states voxelwise encoding models based on CLIP image features predict brain responses. | confidence=high
- metric: evidence=Nature abstract reports CLIP ResNet50 explains up to R^2 = 79% variance in held-out voxel responses. | confidence=high
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=NSD is described as an fMRI dataset of participants viewing natural images. | confidence=high

Identity trace:
- auto_verification_status: source-traced via DBLP strict title match
- auto_matched_title: Better models of human high-level visual cortex emerge from natural language supervision with a large and diverse dataset.
- auto_source_url: https://doi.org/10.1038/s42256-023-00753-y

### Better models of human high-level visual cortex emerge from natural language supervision with a large and diverse dataset

Bibliographic:
- year: 2023
- venue: Nat. Mac. Intell.
- doi: 10.1038/S42256-023-00753-Y

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Human 7T fMRI
- input_modality: fMRI
- task_taxonomy: Visual reconstruction, Speech/language decoding, Dataset/benchmark
- paper_objective: Visual reconstruction, Speech/language decoding, Dataset/benchmark
- method_family: Voxelwise encoding models based on CLIP image features are used to predict human visual-cortex fMRI responses to real-world images.
- method_summary: Voxelwise encoding models based on CLIP image features are used to predict human visual-cortex fMRI responses to real-world images.
- dataset: Natural Scenes Dataset (NSD), a large-scale fMRI dataset of participants viewing thousands of natural images.
- dataset_role: used
- metric: Explained variance / R^2 in held-out voxel responses, including up to R^2 = 79%.
- metric_status: applicable
- limitations: Experimental boundary: the study uses CLIP-based voxelwise encoding models to predict human high-level visual cortex responses to real-world images from the Natural Scenes Dataset; findings are bounded to this NSD fMRI setting and the compared CLIP/ImageNet/BERT-style model families.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s42256-023-00753-y; https://www.nature.com/articles/s42256-023-00753-y
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=Nature data availability states the study uses NSD. | confidence=high
- limitations: evidence=Nature abstract states the authors used CLIP-pretrained models and voxelwise encoding models to predict brain responses to real-world images, reporting high-level visual cortex results; data availability states they used the Natural Scenes Dataset, a large-scale fMRI dataset of participants viewing thousands of natural images. | confidence=medium | tier=tier1_paper_text
- method_summary: evidence=Nature abstract states voxelwise encoding models based on CLIP image features predict brain responses. | confidence=high
- metric: evidence=Nature abstract reports CLIP ResNet50 explains up to R^2 = 79% variance in held-out voxel responses. | confidence=high
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=NSD is described as an fMRI dataset of participants viewing natural images. | confidence=high

Identity trace:
- auto_verification_status: source-traced via DBLP strict title match
- auto_matched_title: Better models of human high-level visual cortex emerge from natural language supervision with a large and diverse dataset.
- auto_source_url: https://doi.org/10.1038/s42256-023-00753-y

### BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion

Bibliographic:
- year: 2025
- venue: CoRR
- doi: 10.48550/ARXIV.2508.08241

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: motion
- task_taxonomy: Humanoid motion tracking and zero-shot task-specific control via guided diffusion, including waypoint navigation, joystick teleoperation, motion inpainting, and obstacle avoidance.
- paper_objective: Humanoid motion tracking and zero-shot task-specific control via guided diffusion, including waypoint navigation, joystick teleoperation, motion inpainting, and obstacle avoidance.
- method_family: Diffusion/generative model
- method_summary: Diffusion/generative model
- dataset: About 2.5 hours of diverse human motions, including prior-work datasets, Unitree-retargeted LAFAN1, and online animation data; 30 representative clips were deployed on hardware.
- dataset_role: used
- metric: Velocity tracking error, motion tracking error, human preference/binomial tests for naturalness, ground-reaction-force comparisons, success/stability of tasks, and ablation tracking errors.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.48550/arXiv.2508.08241; https://arxiv.org/pdf/2508.08241; https://arxiv.org/abs/2508.08241
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Paper states training used approximately 2.5 hours of diverse human motions and supplementary material lists prior datasets, Unitree-retargeted LAFAN1, and online animation data. | confidence=medium
- metric: evidence=Results report average velocity tracking error and use preference tests; supplementary figures report motion tracking errors. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The work concerns humanoid robot control from human motion data, not neural recordings. | confidence=high
- task_taxonomy: evidence=Abstract and results list motion tracking, joystick teleoperation, waypoint navigation, inpainting, and obstacle avoidance. | confidence=high

Identity trace:
- auto_verification_status: source-traced via DBLP strict title match
- auto_matched_title: BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion.
- auto_source_url: https://doi.org/10.48550/arXiv.2508.08241

### Bidirectional Diffusion Bridge Models

Bibliographic:
- year: 2025
- venue: KDD
- doi: 10.1145/3711896.3736858

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Bidirectional paired image-to-image translation with a single diffusion bridge model.
- paper_objective: Bidirectional paired image-to-image translation with a single diffusion bridge model.
- method_family: Diffusion/generative model, Variational autoencoder, Linear/encoding baseline
- method_summary: Diffusion/generative model, Variational autoencoder, Linear/encoding baseline
- dataset: Four paired image-to-image translation datasets: Edges-Shoes, Edges-Handbags, DIODE Outdoor, and Night-Day.
- dataset_role: used
- metric: FID, Inception Score (IS), LPIPS, and Diversity in ablations.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1145/3711896.3736858; https://arxiv.org/abs/2502.09655; https://arxiv.org/pdf/2502.09655
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=arXiv paper experimental settings list Edges-Shoes, Edges-Handbags, DIODE Outdoor, and Night-Day. | confidence=high
- metric: evidence=Experimental settings state FID, IS, and LPIPS; ablation table also reports Diversity. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The task is image-to-image translation, not neural data. | confidence=high
- task_taxonomy: evidence=Abstract says BDBM facilitates bidirectional translation between two coupled distributions using a single network. | confidence=high

Identity trace:
- auto_verification_status: source-traced via DBLP strict title match
- auto_matched_title: Bidirectional Diffusion Bridge Models.
- auto_source_url: https://doi.org/10.1145/3711896.3736858

### Brain Treebank: Large-scale intracranial recordings from naturalistic language stimuli

Bibliographic:
- year: 2024
- venue: Advances in Neural Information Processing Systems 37
- doi: 10.52202/079017-3060

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Human intracranial electrophysiology / sEEG intracranial field potentials
- input_modality: EEG
- task_taxonomy: Speech/language decoding, Dataset/benchmark
- paper_objective: Speech/language decoding, Dataset/benchmark
- method_family: sEEG intracranial field potentials recorded during movie viewing, aligned to manually corrected transcripts, word onsets, Universal Dependencies parses, scene labels, speaker annotations, and audio/video/language features.
- method_summary: sEEG intracranial field potentials recorded during movie viewing, aligned to manually corrected transcripts, word onsets, Universal Dependencies parses, scene labels, speaker annotations, and audio/video/language features.
- dataset: Brain Treebank: intracranial electrophysiology from 10 subjects watching 26 movie viewings totaling 43.5 hours, 38,572 sentences, 223,068 words, and 1,688 electrodes.
- dataset_role: used
- metric: GLM significance tests and beta coefficients for language/audio/visual features, Bonferroni-corrected p-values, Cohen's d, and linear-decoding ROC-AUC on held-out test data.
- metric_status: applicable
- limitations: Subjects watched each movie once, so exact-stimulus repetition averaging is unavailable; naturalistic stimuli make confound control difficult; epilepsy/neurosurgery subjects may introduce sampling bias; the corpus includes only English movies at release.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.52202/079017-3060; https://arxiv.org/pdf/2411.08343; https://arxiv.org/html/2411.08343
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Abstract and Table 1 provide subject, sentence, word, hour, movie, and electrode counts. | confidence=high
- limitations: evidence=Limitations paragraph lists single viewing, confounds, epilepsy sampling bias, and English-only corpus. | confidence=high
- method_summary: evidence=Data section describes sEEG probes, transcript correction, word onset annotation, UD parsing, scene/speaker annotations, and feature curation. | confidence=high
- metric: evidence=Analysis sections report GLMs, Bonferroni-corrected significance, effect sizes, and ROC-AUC decoding. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Data acquisition section states sEEG depth probes recorded Intracranial Field Potentials. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Brain Treebank: Large-scale intracranial recordings from naturalistic language stimuli
- auto_source_url: https://doi.org/10.52202/079017-3060

### Brain Treebank: Large-scale intracranial recordings from naturalistic language stimuli

Bibliographic:
- year: 2024
- venue: Advances in Neural Information Processing Systems 37
- doi: 10.52202/079017-3060

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Human intracranial electrophysiology / sEEG intracranial field potentials
- input_modality: EEG
- task_taxonomy: Speech/language decoding, Dataset/benchmark
- paper_objective: Speech/language decoding, Dataset/benchmark
- method_family: sEEG intracranial field potentials recorded during movie viewing, aligned to manually corrected transcripts, word onsets, Universal Dependencies parses, scene labels, speaker annotations, and audio/video/language features.
- method_summary: sEEG intracranial field potentials recorded during movie viewing, aligned to manually corrected transcripts, word onsets, Universal Dependencies parses, scene labels, speaker annotations, and audio/video/language features.
- dataset: Brain Treebank: intracranial electrophysiology from 10 subjects watching 26 movie viewings totaling 43.5 hours, 38,572 sentences, 223,068 words, and 1,688 electrodes.
- dataset_role: used
- metric: GLM significance tests and beta coefficients for language/audio/visual features, Bonferroni-corrected p-values, Cohen's d, and linear-decoding ROC-AUC on held-out test data.
- metric_status: applicable
- limitations: Subjects watched each movie once, so exact-stimulus repetition averaging is unavailable; naturalistic stimuli make confound control difficult; epilepsy/neurosurgery subjects may introduce sampling bias; the corpus includes only English movies at release.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.52202/079017-3060; https://arxiv.org/pdf/2411.08343; https://arxiv.org/html/2411.08343
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Abstract and Table 1 provide subject, sentence, word, hour, movie, and electrode counts. | confidence=high
- limitations: evidence=Limitations paragraph lists single viewing, confounds, epilepsy sampling bias, and English-only corpus. | confidence=high
- method_summary: evidence=Data section describes sEEG probes, transcript correction, word onset annotation, UD parsing, scene/speaker annotations, and feature curation. | confidence=high
- metric: evidence=Analysis sections report GLMs, Bonferroni-corrected significance, effect sizes, and ROC-AUC decoding. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Data acquisition section states sEEG depth probes recorded Intracranial Field Potentials. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Brain Treebank: Large-scale intracranial recordings from naturalistic language stimuli
- auto_source_url: https://doi.org/10.52202/079017-3060

### Brain and Cognitive Science Inspired Deep Learning: A Comprehensive Survey

Bibliographic:
- year: 2025
- venue: IEEE Transactions on Knowledge and Data Engineering
- doi: 10.1109/tkde.2025.3527551

Paper type:
- type: review

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Emotion/cognitive state recognition
- paper_objective: Emotion/cognitive state recognition
- method_family: Comprehensive survey/review of more than 300 papers at the intersection of deep learning and brain/cognitive science, organized into a unified BCS-inspired DL framework.
- method_summary: Comprehensive survey/review of more than 300 papers at the intersection of deep learning and brain/cognitive science, organized into a unified BCS-inspired DL framework.
- dataset: unresolved
- dataset_role: none_review
- metric: unresolved
- metric_status: not_applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/tkde.2025.3527551; https://ieeexplore.ieee.org/document/10834593/; https://www.computer.org/csdl/journal/tk/2025/04/10834593/23ljNrEYCXu; https://doi.org/10.1109/TKDE.2025.3527551
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- method_summary: evidence=IEEE/ResearchGate abstract says the review surveys more than 300 papers and establishes a unified framework for DL inspired by brain and cognitive science. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=This is a literature survey of deep learning methods, not a primary neural recording study. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Brain and Cognitive Science Inspired Deep Learning: A Comprehensive Survey
- auto_source_url: https://doi.org/10.1109/tkde.2025.3527551

### Brain-Machine Coupled Learning Method for Facial Emotion Recognition

Bibliographic:
- year: 2023
- venue: IEEE Transactions on Pattern Analysis and Machine Intelligence
- doi: 10.1109/tpami.2023.3257846

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: EEG plus facial images
- input_modality: EEG
- task_taxonomy: Emotion/cognitive state recognition
- paper_objective: Emotion/cognitive state recognition
- method_family: Brain-machine coupled learning with visual-image and EEG cognitive-domain models, each having common and private interactive channels, to train FER models with both machine visual knowledge and brain cognitive knowledge.
- method_summary: Brain-machine coupled learning with visual-image and EEG cognitive-domain models, each having common and private interactive channels, to train FER models with both machine visual knowledge and brain cognitive knowledge.
- dataset: Facial emotion datasets include CFAPS, CK+, and JAFFE; the method also uses EEG signals evoked by facial emotion images for coupled training.
- dataset_role: used
- metric: Accuracy, precision, recall, and F1 score.
- metric_status: applicable
- limitations: unresolved
- limitation_source: unresolved

Verification:
- final_unresolved_fields: limitations
- verification_status: needs_human_review
- evidence_sources: https://doi.org/10.1109/tpami.2023.3257846; https://www.computer.org/csdl/journal/tp/2023/09/10073607/1Lz1esXO4KI; https://doi.org/10.1109/TPAMI.2023.3257846
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Computer.org snippet names CFAPS, CK+, and JAFFE; abstract/source snippets state the method uses visual images and EEG signals. | confidence=medium
- method_summary: evidence=Abstract states visual images and EEG signals are used to couple-train visual and cognitive domain models with common/private channels. | confidence=high
- metric: evidence=Computer.org snippet states accuracy, precision, recall, and F1 score are employed for quantitative evaluation. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Abstract/source snippets explicitly mention electroencephalogram (EEG) signals paired with facial emotion images. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Brain-Machine Coupled Learning Method for Facial Emotion Recognition
- auto_source_url: https://doi.org/10.1109/tpami.2023.3257846

### BridgeVoC: Neural Vocoder with Schrödinger Bridge

Bibliographic:
- year: 2025
- venue: Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence
- doi: 10.24963/ijcai.2025/903

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: Diffusion/generative model, Linear/encoding baseline
- method_summary: Diffusion/generative model, Linear/encoding baseline
- dataset: LJSpeech and LibriTTS benchmarks, with VCTK used for out-of-distribution evaluation and MUSDB18 used for spectral visualization.
- dataset_role: used
- metric: PESQ, ESTOI, V/UV F1, periodicity RMSE, pitch RMSE, F0 RMSE, VISQOL, UTMOS, MUSHRA, ABX preference, parameter count, MACs, inference speed, and real-time factor.
- metric_status: applicable
- limitations: The authors report the relative objective-metric advantage on VCTK decreases because LibriTTS is probably insufficient for a large NCSN++ network; they also note a sampling-step tradeoff where more steps can accumulate numerical errors.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.24963/ijcai.2025/903; https://www.ijcai.org/proceedings/2025/0903.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=IJCAI paper dataset section lists LJSpeech, LibriTTS, and VCTK; results discuss MUSDB18 visualization. | confidence=high
- limitations: evidence=Results analysis explicitly says LibriTTS amount is probably insufficient for a large NCSN++ and discusses sampling-step error accumulation. | confidence=high
- metric: evidence=Evaluation section lists objective and subjective metrics including PESQ, ESTOI, V/UV F1, RMSEs, VISQOL, UTMOS, MUSHRA and ABX. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=This is a neural vocoder for speech/audio generation, not neural recording data. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: BridgeVoC: Neural Vocoder with Schrödinger Bridge
- auto_source_url: https://doi.org/10.24963/ijcai.2025/903

### Bridging Supervised Learning and Reinforcement Learning in Math Reasoning

Bibliographic:
- year: 2025
- venue: arXiv.org
- doi: 10.48550/arXiv.2505.18116

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: LLM math reasoning training with binary-verifier feedback, comparing supervised fine-tuning and reinforcement-learning-style optimization.
- paper_objective: LLM math reasoning training with binary-verifier feedback, comparing supervised fine-tuning and reinforcement-learning-style optimization.
- method_family: Large language model, Linear/encoding baseline, Reinforcement learning/bandit
- method_summary: Large language model, Linear/encoding baseline, Reinforcement learning/bandit
- dataset: Training uses DAPO-Math-17k; evaluation uses AIME 2024, AIME 2025, AMC 2023, MATH500, OlympiadBench, and Minerva Math.
- dataset_role: used
- metric: Average accuracy; the paper reports avg@32 for AIME24, AIME25, and AMC23 and avg@1 for the other benchmarks.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://www.semanticscholar.org/paper/15f0ebcfef190e6aeac25e08e71e320be0263696; https://arxiv.org/abs/2505.18116; https://arxiv.org/pdf/2505.18116
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Experiment setup states training on DAPO-Math-17k and evaluation on six math benchmarks. | confidence=high
- metric: evidence=Table 1 caption and evaluation section report average accuracy with avg@32/avg@1 conventions. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The paper studies LLM math reasoning, not neural data. | confidence=high
- task_taxonomy: evidence=Abstract describes Negative-aware Fine-Tuning for LLM math reasoning with binary verifier signals. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: Bridging Supervised Learning and Reinforcement Learning in Math Reasoning
- auto_source_url: https://www.semanticscholar.org/paper/15f0ebcfef190e6aeac25e08e71e320be0263696

### Bridging the Gap between Brain and Machine in Interpreting Visual Semantics: Towards Self-adaptive Brain-to-Text Decoding

Bibliographic:
- year: 2025
- venue: 2025 IEEE/CVF International Conference on Computer Vision (ICCV)
- doi: 10.1109/iccv51701.2025.02037

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Human fMRI
- input_modality: fMRI
- task_taxonomy: Neural decoding, Visual reconstruction, Speech/language decoding, Representation alignment, Foundation model/pretraining
- paper_objective: Neural decoding, Visual reconstruction, Speech/language decoding, Representation alignment, Foundation model/pretraining
- method_family: Transformer, Contrastive learning, Masked autoencoder/pretraining
- method_summary: Transformer, Contrastive learning, Masked autoencoder/pretraining
- dataset: Natural Scenes Dataset (NSD), using subjects 1, 2, 5, and 7; for each subject, 8,859 stimulus images / 24,980 fMRI trials for training and 982 stimulus images / 2,770 fMRI trials for testing.
- dataset_role: used
- metric: BLEU-1, BLEU-2, BLEU-3, BLEU-4, METEOR, ROUGE, CIDEr, and SPICE.
- metric_status: applicable
- limitations: The authors identify fixed number of captured image patches as a potential limitation; too few patches may miss important regions and too many may degrade into conventional brain-to-text reconstruction.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/iccv51701.2025.02037; https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_Bridging_the_Gap_between_Brain_and_Machine_in_Interpreting_Visual_ICCV_2025_paper.pdf; https://openaccess.thecvf.com/ICCV2025?day=2025-10-23
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=ICCV paper dataset section names NSD and gives subject IDs and train/test image and fMRI trial counts. | confidence=high
- limitations: evidence=Conclusion/ablation text states fixed number of image patches may be a potential limitation. | confidence=high
- metric: evidence=Evaluation metrics section lists BLEU variants, METEOR, ROUGE, CIDEr, and SPICE. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Paper describes non-invasive brain recordings from fMRI/BOLD signals. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Bridging the Gap Between Brain and Machine in Interpreting Visual Semantics: Towards Self-Adaptive Brain-to-Text Decoding
- auto_source_url: https://doi.org/10.1109/iccv51701.2025.02037

### CAP-Net: A Unified Network for 6D Pose and Size Estimation of Categorical Articulated Parts from a Single RGB-D Image

Bibliographic:
- year: 2025
- venue: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
- doi: 10.1109/cvpr52734.2025.01088

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Representation alignment, Dataset/benchmark
- paper_objective: Representation alignment, Dataset/benchmark
- method_family: Linear/encoding baseline
- method_summary: Linear/encoding baseline
- dataset: RGBD-Art, a realistic RGB-D articulated-object dataset with photorealistic RGB images, simulated real-sensor depth noise, and detailed articulated pose annotations.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/cvpr52734.2025.01088; https://arxiv.org/html/2504.11230v2; https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_CAP-Net_A_Unified_Network_for_6D_Pose_and_Size_Estimation_CVPR_2025_paper.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=The paper introduces RGBD-Art for articulated objects and describes photorealistic RGB images, simulated real-sensor depth noise, and articulated pose annotations. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The task estimates 6D pose and size from a single RGB-D image using RGB-D features and point clouds; it is non-neural computer vision. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: CAP-Net: A Unified Network for 6D Pose and Size Estimation of Categorical Articulated Parts from a Single RGB-D Image
- auto_source_url: https://doi.org/10.1109/cvpr52734.2025.01088

### Category selectivity in human visual cortex: Beyond visual object recognition

Bibliographic:
- year: 2017
- venue: Neuropsychologia
- doi: 10.1016/j.neuropsychologia.2017.03.033

Paper type:
- type: review

Evidence fields:
- signal_modality: Human neuroimaging evidence, especially fMRI responses in ventral temporal and occipitotemporal cortex.
- input_modality: fMRI
- task_taxonomy: Encoding model, Visual reconstruction, Representation alignment
- paper_objective: Encoding model, Visual reconstruction, Representation alignment
- method_family: Narrative/theoretical review of human visual cortex category selectivity, contrasting visual object recognition and DNN-style accounts with evidence from task-associated and nonvisual category responses.
- method_summary: Narrative/theoretical review of human visual cortex category selectivity, contrasting visual object recognition and DNN-style accounts with evidence from task-associated and nonvisual category responses.
- dataset: No primary dataset; review article on category selectivity in human visual cortex beyond visual object recognition.
- dataset_role: none_review
- metric: unresolved
- metric_status: not_applicable
- limitations: The authors argue that a visual-object-recognition-only account is unlikely to fully explain category selectivity because category-selective regions are also implicated in navigation, social cognition, tool use, reading, and nonvisual conditions.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1016/j.neuropsychologia.2017.03.033; https://pubmed.ncbi.nlm.nih.gov/28377161/; https://repository.ubn.ru.nl/bitstream/handle/2066/178519/1/178519.pdf
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=PubMed labels the article as a Review, lists publication type Review, and the abstract argues a conceptual account of category selectivity rather than reporting a dataset. | confidence=high | tier=tier1_paper_text
- limitations: evidence=The abstract and review framing state that object-recognition accounts are insufficient for the full pattern of category-selective responses. | confidence=medium
- method_summary: evidence=The article is a review/opinion paper synthesizing evidence about faces, bodies, tools, scenes, and words in human visual cortex. | confidence=high
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=The paper centers on category-selective responses in human ventral temporal/occipitotemporal cortex measured by neuroimaging studies. | confidence=medium

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Category selectivity in human visual cortex: Beyond visual object recognition
- auto_source_url: https://doi.org/10.1016/j.neuropsychologia.2017.03.033

### CheckManual: A New Challenge and Benchmark for Manual-based Appliance Manipulation

Bibliographic:
- year: 2025
- venue: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
- doi: 10.1109/cvpr52734.2025.02104

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Dataset/benchmark
- paper_objective: Dataset/benchmark
- method_family: Large-model-assisted, human-revised manual generation plus ManualPlan: OCR/MLLM manual parsing, LLM-based manipulation planning, and SoM/Grounding-DINO/SAM part alignment with low-level manipulation modules.
- method_summary: Large-model-assisted, human-revised manual generation plus ManualPlan: OCR/MLLM manual parsing, LLM-based manipulation planning, and SoM/Grounding-DINO/SAM part alignment with low-level manipulation modules.
- dataset: CheckManual, a CAD model-aligned appliance-manual benchmark with generated manuals, appliance CAD models, simulator environments, and three challenge tracks.
- dataset_role: used
- metric: Part alignment success rate, task planning success rate, task execution success rate, and average task completion rate.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/cvpr52734.2025.02104; https://arxiv.org/html/2506.09343v1; https://sites.google.com/view/checkmanual; https://github.com/LYX0501/CheckManual
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=The paper describes CheckManual as a manual-based appliance manipulation benchmark and a CAD model-aligned appliance manual dataset. | confidence=high
- method_summary: evidence=The method section describes LMM-assisted human-revised manual creation and ManualPlan with OCR, MLLM/LLM planning, Grounding-DINO, SAM, and manipulation primitives. | confidence=high
- metric: evidence=The benchmark defines task-level and step-level metrics including alignment, planning, execution, and completion success rates. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The work evaluates robotics, vision, and language systems using manuals/CAD/simulation rather than neural data. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: CheckManual: A New Challenge and Benchmark for Manual-based Appliance Manipulation
- auto_source_url: https://doi.org/10.1109/cvpr52734.2025.02104

### CoCoG-2: Controllable generation of visual stimuli for understanding human concept representation

Bibliographic:
- year: 2025
- venue: Communications in Computer and Information Science
- doi: 10.1007/978-981-96-4001-0_2

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: Training-free guided two-stage concept decoder using prior diffusion over CLIP embeddings and SDXL/IP-Adapter generation with concept, smoothness, semantic, judgment, uncertainty, and pixel guidance losses.
- method_summary: Training-free guided two-stage concept decoder using prior diffusion over CLIP embeddings and SDXL/IP-Adapter generation with concept, smoothness, semantic, judgment, uncertainty, and pixel guidance losses.
- dataset: ImageNet pairs for the prior diffusion component and human concept/similarity-judgment embeddings from the CoCoG framework used to guide generated visual stimuli.
- dataset_role: used
- metric: CLIP similarity matrices for semantic smoothness, cross-entropy loss for target similarity-judgment distributions, and entropy for uncertainty guidance.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1007/978-981-96-4001-0_2; https://link.springer.com/chapter/10.1007/978-981-96-4001-0_2; https://arxiv.org/html/2407.14949; https://github.com/ncclab-sustech/CoCoG-2
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=The paper discusses prior diffusion trained on ImageNet pairs and uses concept/similarity-judgment embeddings in the CoCoG framework. | confidence=medium
- method_summary: evidence=The method introduces training-free guidance losses for controllable visual stimulus generation. | confidence=high
- metric: evidence=The paper defines CLIP-similarity and judgment-distribution objectives, including cross-entropy and entropy terms. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The work generates visual stimuli from behavioral/concept embeddings and image models; it reports no neural recordings. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: CoCoG-2: Controllable Generation of Visual Stimuli for Understanding Human Concept Representation
- auto_source_url: https://doi.org/10.1007/978-981-96-4001-0_2

### Compact deep neural network models of visual cortex

Bibliographic:
- year: 2023
- venue: bioRxiv (Cold Spring Harbor Laboratory)
- doi: 10.1101/2023.11.22.568315

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Macaque V4 electrophysiology / neural spiking responses to visual images.
- input_modality: image/video
- task_taxonomy: Visual reconstruction, Representation alignment
- paper_objective: Visual reconstruction, Representation alignment
- method_family: A data-driven DNN ensemble was trained to predict V4 neural responses, then compressed to compact DNN models and validated with model-generated maximizing/adversarial visual stimuli.
- method_summary: A data-driven DNN ensemble was trained to predict V4 neural responses, then compressed to compact DNN models and validated with model-generated maximizing/adversarial visual stimuli.
- dataset: Macaque V4 electrophysiology responses from 50 recording sessions in 3 monkeys to natural, gaudy, maximizing, and adversarial images; normal images were sampled from YFCC100M.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: The empirical scope is macaque V4 neurons from a finite set of sessions and visual stimuli; the compressed models target recorded V4 response prediction rather than whole-cortex modeling.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1101/2023.11.22.568315; https://pmc.ncbi.nlm.nih.gov/articles/PMC10690296/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=The paper reports 50 recording sessions from 3 monkeys and normal images sampled from the YFCC100M image collection. | confidence=high
- limitations: evidence=The methods and data availability sections bound the study to recorded V4 neurons, session-specific data, and visual-stimulus response modeling. | confidence=medium
- method_summary: evidence=The abstract and methods describe a data-driven V4 response model followed by model compression and image-based validation. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The dataset consists of neural responses from macaque area V4 to visual images. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Compact deep neural network models of visual cortex
- auto_source_url: https://doi.org/10.1101/2023.11.22.568315

### Comparing EEG/ERP-Like and fMRI-Like Techniques for Reading Machine Thoughts

Bibliographic:
- year: 2010
- venue: Lecture Notes in Computer Science
- doi: 10.1007/978-3-642-15314-3_13

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: EEG, fMRI
- input_modality: fMRI
- task_taxonomy: Decode/classify which cognitive task or algorithm a machine is performing and compare fMRI-like versus EEG/ERP-like reader settings.
- paper_objective: Decode/classify which cognitive task or algorithm a machine is performing and compare fMRI-like versus EEG/ERP-like reader settings.
- method_family: Construct fMRI-like snapshot images and ERP/EEG-like time-series activation images from program memory dumps, extract chromatic, texture, and OGD features, then train Decision Tree, Naive Bayes, and IBk classifiers in Weka.
- method_summary: Construct fMRI-like snapshot images and ERP/EEG-like time-series activation images from program memory dumps, extract chromatic, texture, and OGD features, then train Decision Tree, Naive Bayes, and IBk classifiers in Weka.
- dataset: Synthetic machine-thought activation images generated from memory dumps of sorting programs/machines; 21 snapshots per algorithm-data pair were resized to 1024 x 768.
- dataset_role: used
- metric: Classification accuracy under 50/50 train-test, 10-fold cross-validation, and one-machine-out settings.
- metric_status: applicable
- limitations: ERP/EEG-like activation images are coarser and consistently lower in accuracy than fMRI-like snapshots; one-machine-out generalization is much harder and can approach random baseline.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1007/978-3-642-15314-3_13; https://art.uniroma2.it/zanzotto/publications/2010_BI_ZanzottoCroce.pdf; https://link.springer.com/chapter/10.1007/978-3-642-15314-3_13
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=The paper describes collecting process memory dumps at intervals and converting them into activation images for algorithm/data pairs. | confidence=high
- limitations: evidence=The discussion reports a consistent drop for ERP/EEG-like accuracy and difficulty under one-machine-out evaluation. | confidence=high
- method_summary: evidence=The methods define activation-image construction, feature extraction, and Weka classifiers. | confidence=high
- metric: evidence=The experiments tabulate percentage accuracy across generic and one-machine-out evaluation protocols. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- task_taxonomy: evidence=The study is explicitly framed as reading machine thoughts by classifying machine activities from activation images. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Comparing EEG/ERP-Like and fMRI-Like Techniques for Reading Machine Thoughts
- auto_source_url: https://doi.org/10.1007/978-3-642-15314-3_13

### Convergent multi-modular architecturefor adaptive learning in Drosophila and artificial intelligence

Bibliographic:
- year: 2025
- venue: iScience
- doi: 10.1016/j.isci.2025.113799

Paper type:
- type: perspective

Evidence fields:
- signal_modality: Drosophila olfactory learning neural-circuit and anatomical/functional evidence plus artificial-intelligence method comparison.
- input_modality: not specified
- task_taxonomy: Continual/adaptive learning
- paper_objective: Continual/adaptive learning
- method_family: Perspective/review comparing Drosophila olfactory learning anatomy and function with AI multi-modular methods, especially ensemble learning and mixture-of-experts.
- method_summary: Perspective/review comparing Drosophila olfactory learning anatomy and function with AI multi-modular methods, especially ensemble learning and mixture-of-experts.
- dataset: No primary dataset; iScience Perspective reviewing Drosophila olfactory learning/mushroom body architecture and AI analogues. It discusses cited datasets/benchmarks such as SIFT, GLOVE, MNIST, Split CIFAR-100, and Atari only as examples from prior work.
- dataset_role: none_review
- metric: unresolved
- metric_status: not_applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1016/j.isci.2025.113799; https://pubmed.ncbi.nlm.nih.gov/41244560/; https://www.cell.com/iscience/pdf/S2589-0042%2825%2902060-7.pdf; https://pmc.ncbi.nlm.nih.gov/articles/PMC12616022/
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=PMC full text identifies the article type as Perspective, says it reviews recent studies of the Drosophila olfactory learning system, and mentions SIFT/GLOVE/MNIST, Split CIFAR-100, and Atari as validation examples in cited prior work rather than a new dataset for this article. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=The abstract describes a review of Drosophila olfactory learning and a comparison to ensemble learning and mixture-of-experts. | confidence=high
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=The biological component concerns Drosophila olfactory learning circuits rather than a single recording modality. | confidence=medium

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Convergent multi-modular architecturefor adaptive learning in Drosophila and artificial intelligence
- auto_source_url: https://doi.org/10.1016/j.isci.2025.113799

### Data-Driven Approaches to Understanding Visual Neuron Activity

Bibliographic:
- year: 2019
- venue: Annual Review of Vision Science
- doi: 10.1146/annurev-vision-091718-014731

Paper type:
- type: review

Evidence fields:
- signal_modality: Visual-system neurophysiology / neural activity recordings across the visual pathway.
- input_modality: image/video
- task_taxonomy: Visual reconstruction, Closed-loop BCI
- paper_objective: Visual reconstruction, Closed-loop BCI
- method_family: Review of data-driven/statistical modeling approaches for visual neuron activity, including receptive-field, neural-network, and machine-learning models used to predict and interpret neural responses.
- method_summary: Review of data-driven/statistical modeling approaches for visual neuron activity, including receptive-field, neural-network, and machine-learning models used to predict and interpret neural responses.
- dataset: No primary dataset; review of statistical and data-driven models for understanding visual neuron activity.
- dataset_role: none_review
- metric: unresolved
- metric_status: not_applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1146/annurev-vision-091718-014731; https://www.annualreviews.org/content/journals/10.1146/annurev-vision-091718-014731; https://pubmed.ncbi.nlm.nih.gov/31386605/
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=PubMed/E-utilities lists the publication type as Review and the abstract describes different forms of statistical models used to relate neural activity data to models rather than reporting a specific dataset collected by the article. | confidence=high | tier=tier1_paper_text
- method_summary: evidence=The abstract frames the article as a review of statistical models for probing cellular, circuit, and systems-level visual processing. | confidence=high
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=The paper focuses on neurophysiological recordings of neural activity throughout the visual pathway under complex visual stimulation. | confidence=medium

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Data-Driven Approaches to Understanding Visual Neuron Activity
- auto_source_url: https://doi.org/10.1146/annurev-vision-091718-014731

### Decoding Neuronal Ensembles in the Human Hippocampus

Bibliographic:
- year: 2009
- venue: Current Biology
- doi: 10.1016/j.cub.2009.02.033

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: High-spatial-resolution BOLD fMRI in human hippocampus/medial temporal lobe.
- input_modality: fMRI
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: MVPA/searchlight decoding with linear SVM classifiers on hippocampal and MTL BOLD fMRI patterns during stationary target-position periods.
- method_summary: MVPA/searchlight decoding with linear SVM classifiers on hippocampal and MTL BOLD fMRI patterns during stationary target-position periods.
- dataset: High-spatial-resolution BOLD fMRI from participants navigating two well-learned virtual-reality rooms with four target positions each, focused on hippocampus and wider medial temporal lobe.
- dataset_role: used
- metric: Percentage prediction/classification accuracy with 50% pairwise and 25% four-way chance levels, assessed by nonparametric permutation testing.
- metric_status: applicable
- limitations: The experimental boundary was an austere VR environment with visual input and task held constant, analyzed mainly in hippocampus/MTL; fMRI provides indirect voxel-level signals rather than individual-neuron recordings.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1016/j.cub.2009.02.033; https://pmc.ncbi.nlm.nih.gov/articles/PMC2670980/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=The paper describes a VR navigation task with two rooms and four target positions while acquiring high-resolution BOLD fMRI over hippocampus/MTL. | confidence=high
- limitations: evidence=The task was designed to hold visual inputs and task constant; the data are BOLD fMRI and the analysis targets hippocampal/MTL regions. | confidence=medium
- method_summary: evidence=The methods describe training/testing linear SVM classifiers on fMRI activation patterns. | confidence=high
- metric: evidence=The paper reports prediction accuracy and chance thresholds for pairwise and four-way decoding. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The measurements are high-spatial-resolution BOLD fMRI. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Decoding Neuronal Ensembles in the Human Hippocampus
- auto_source_url: https://doi.org/10.1016/j.cub.2009.02.033

### Decoding and synthesizing tonal language speech from brain activity

Bibliographic:
- year: 2023
- venue: Science Advances
- doi: 10.1126/sciadv.adh0478

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Intracranial high-density ECoG, especially 70-150 Hz high-gamma activity during speech production.
- input_modality: ECoG
- task_taxonomy: Neural decoding, Speech/language decoding
- paper_objective: Neural decoding, Speech/language decoding
- method_family: Modular multistream neural network that decodes tone and base syllable from high-gamma ECoG electrode groups using CNN-LSTM streams, then synthesizes Mel spectrograms and sound.
- method_summary: Modular multistream neural network that decodes tone and base syllable from high-gamma ECoG electrode groups using CNN-LSTM streams, then synthesizes Mel spectrograms and sound.
- dataset: High-density ECoG recordings from five native Mandarin-speaking participants during production of eight tonal syllables, paired with speech/audio targets.
- dataset_role: used
- metric: Tone, syllable, and tonal-syllable classification accuracy; synthesis/model comparisons reported with statistical tests.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1126/sciadv.adh0478; https://pmc.ncbi.nlm.nih.gov/articles/PMC10256166/; https://www.science.org/doi/10.1126/sciadv.adh0478
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=The paper reports five native Mandarin-speaking participants with high-density ECoG grids producing designated tonal syllables. | confidence=high
- method_summary: evidence=The model contains tone/syllable streams and a synthesizer operating on ECoG high-gamma inputs and acoustic outputs. | confidence=high
- metric: evidence=The results compare tone/syllable/tonal-syllable decoding accuracy across neural network variants. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The neural input is intracranial ECoG high-gamma activity. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Decoding and synthesizing tonal language speech from brain activity
- auto_source_url: https://doi.org/10.1126/sciadv.adh0478

### Decoding the brain: From neural representations to mechanistic models

Bibliographic:
- year: 2024
- venue: Cell
- doi: 10.1016/j.cell.2024.08.051

Paper type:
- type: review

Evidence fields:
- signal_modality: General neural activity across modalities, including action potentials and signals such as fMRI, EEG, ECoG, and calcium imaging.
- input_modality: fMRI
- task_taxonomy: Neural decoding, Encoding model, Visual reconstruction, Speech/language decoding, Representation alignment
- paper_objective: Neural decoding, Encoding model, Visual reconstruction, Speech/language decoding, Representation alignment
- method_family: Perspective/review of neural encoding and decoding concepts, mathematical tools, deep-learning methods, and case studies in motor, visual, and language processing.
- method_summary: Perspective/review of neural encoding and decoding concepts, mathematical tools, deep-learning methods, and case studies in motor, visual, and language processing.
- dataset: No primary dataset; Cell Perspective/review on neural encoding/decoding. It discusses dataset-scale requirements and cites examples such as MICrONS and Neural Latents Benchmark as prior resources, not as a newly generated dataset.
- dataset_role: none_review
- metric: unresolved
- metric_status: not_applicable
- limitations: The Perspective emphasizes that decoder algorithms do not necessarily link to neural mechanisms, that dataset scale and timescale are major challenges for generalization, and that the field should move toward causal modeling.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1016/j.cell.2024.08.051; https://pmc.ncbi.nlm.nih.gov/articles/PMC11637322/; https://www.cell.com/cell/fulltext/S0092-8674(24)00980-2
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=PMC full text identifies the article as a Perspective and states that it reviews encoding-decoding principles and case studies; it discusses dataset scale needs and prior resources such as MICrONS and Neural Latents Benchmark without reporting a new article-specific dataset. | confidence=high | tier=tier1_paper_text
- limitations: evidence=The introduction states that building decoder algorithms does not necessarily establish neural mechanisms and highlights dataset-scale/timescale challenges before arguing for causal modeling. | confidence=high
- method_summary: evidence=The abstract states that the article details neural encoding/decoding concepts and mathematical tools, including deep learning, with motor, visual, and language case studies. | confidence=high
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=The paper discusses recording from neurons and other signals such as fMRI and EEG; later sections include spikes, fMRI, ECoG, and calcium imaging. | confidence=medium

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Decoding the brain: From neural representations to mechanistic models
- auto_source_url: https://doi.org/10.1016/j.cell.2024.08.051

### Decoding the brain: From neural representations to mechanistic models

Bibliographic:
- year: 2024
- venue: Cell
- doi: 10.1016/j.cell.2024.08.051

Paper type:
- type: review

Evidence fields:
- signal_modality: General neural activity across modalities, including action potentials and signals such as fMRI, EEG, ECoG, and calcium imaging.
- input_modality: fMRI
- task_taxonomy: Neural decoding, Encoding model, Visual reconstruction, Speech/language decoding, Representation alignment
- paper_objective: Neural decoding, Encoding model, Visual reconstruction, Speech/language decoding, Representation alignment
- method_family: Perspective/review of neural encoding and decoding concepts, mathematical tools, deep-learning methods, and case studies in motor, visual, and language processing.
- method_summary: Perspective/review of neural encoding and decoding concepts, mathematical tools, deep-learning methods, and case studies in motor, visual, and language processing.
- dataset: No primary dataset; Cell Perspective/review on neural encoding/decoding. It discusses dataset-scale requirements and cites examples such as MICrONS and Neural Latents Benchmark as prior resources, not as a newly generated dataset.
- dataset_role: none_review
- metric: unresolved
- metric_status: not_applicable
- limitations: The Perspective emphasizes that decoder algorithms do not necessarily link to neural mechanisms, that dataset scale and timescale are major challenges for generalization, and that the field should move toward causal modeling.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1016/j.cell.2024.08.051; https://pmc.ncbi.nlm.nih.gov/articles/PMC11637322/; https://www.cell.com/cell/fulltext/S0092-8674(24)00980-2
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=PMC full text identifies the article as a Perspective and states that it reviews encoding-decoding principles and case studies; it discusses dataset scale needs and prior resources such as MICrONS and Neural Latents Benchmark without reporting a new article-specific dataset. | confidence=high | tier=tier1_paper_text
- limitations: evidence=The introduction states that building decoder algorithms does not necessarily establish neural mechanisms and highlights dataset-scale/timescale challenges before arguing for causal modeling. | confidence=high
- method_summary: evidence=The abstract states that the article details neural encoding/decoding concepts and mathematical tools, including deep learning, with motor, visual, and language case studies. | confidence=high
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=The paper discusses recording from neurons and other signals such as fMRI and EEG; later sections include spikes, fMRI, ECoG, and calcium imaging. | confidence=medium

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Decoding the brain: From neural representations to mechanistic models
- auto_source_url: https://doi.org/10.1016/j.cell.2024.08.051

### Deep Neural Networks Reveal a Gradient in the Complexity of Neural Representations across the Ventral Stream

Bibliographic:
- year: 2015
- venue: Journal of Neuroscience
- doi: 10.1523/jneurosci.5023-14.2015

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Human BOLD fMRI responses in ventral visual cortex to natural images.
- input_modality: fMRI
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: Voxel-wise encoding/decoding using ImageNet-trained DNN feature layers to predict BOLD responses across visual areas and map feature complexity; compared with Gabor wavelet and other DNN models.
- method_summary: Voxel-wise encoding/decoding using ImageNet-trained DNN feature layers to predict BOLD responses across visual areas and map feature complexity; compared with Gabor wavelet and other DNN models.
- dataset: CRCNS vim-1 natural-image fMRI dataset from Kay/Naselaris/Gallant: two male subjects viewing 1,750 training and 120 test grayscale natural images, with BOLD fMRI responses.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: Explained variance was low for many voxels due to low signal-to-noise ratio, missing stimulus features, and mismatch between a DNN plus linear BOLD model and the brain; feedforward DNNs are not a full mechanistic account because visual processing includes feedback.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1523/jneurosci.5023-14.2015; https://www.jneurosci.org/content/35/27/10005; https://crcns.org/data-sets/vc/vim-1/about-vim-1; https://www.researchgate.net/publication/281179168_Deep_Neural_Networks_Reveal_a_Gradient_in_the_Complexity_of_Neural_Representations_across_the_Ventral_Stream
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=The paper states it reanalyzed the Kay/Naselaris fMRI dataset archived at CRCNS, with two male subjects and natural-image train/test stimuli. | confidence=high
- limitations: evidence=The discussion attributes unexplained variance to SNR, feature coverage, and model-brain mismatch, and notes limits of strictly feedforward DNN accounts. | confidence=high
- method_summary: evidence=The study uses pretrained DNN features to build voxel-wise response models and compare representational complexity across ventral stream regions. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The empirical signal is human fMRI BOLD response to natural visual stimuli. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Deep Neural Networks Reveal a Gradient in the Complexity of Neural Representations across the Ventral Stream
- auto_source_url: https://doi.org/10.1523/jneurosci.5023-14.2015

### Deep Residual Network Predicts Cortical Representation and Organization of Visual Features for Rapid Categorization

Bibliographic:
- year: 2018
- venue: Scientific Reports
- doi: 10.1038/s41598-018-22160-9

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Human BOLD fMRI in visual cortex during natural visual stimulation.
- input_modality: fMRI
- task_taxonomy: Encoding model, Visual reconstruction, Speech/language decoding, Representation alignment
- paper_objective: Encoding model, Visual reconstruction, Speech/language decoding, Representation alignment
- method_family: ResNet-50 feature-based voxel-wise encoding model with PCA and L2-regularized linear regression to predict fMRI responses, with comparisons to AlexNet and category-response simulations.
- method_summary: ResNet-50 feature-based voxel-wise encoding model with PCA and L2-regularized linear regression to predict fMRI responses, with comparisons to AlexNet and category-response simulations.
- dataset: Human fMRI responses to natural visual stimuli/movies plus functional localizer images; model category analyses used Google Image sets including 2,000 human face images and about 64,000 images from 80 categories.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: The authors note that category-average representations can be biased by category definitions and human image selection, so individual-image analyses are needed to mitigate bias and ambiguity.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41598-018-22160-9; https://www.nature.com/articles/s41598-018-22160-9
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=The paper describes fMRI response prediction for natural visual stimuli and separately lists Google Image-derived face and category image sets. | confidence=medium
- limitations: evidence=The discussion explicitly warns that category-average representations may be biased by category definitions and image selection. | confidence=high
- method_summary: evidence=The method extracts features from ResNet layers, reduces dimensionality with PCA, and fits regularized linear voxel-wise encoding models. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The empirical response variable is human fMRI BOLD activity in visual cortex. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Deep Residual Network Predicts Cortical Representation and Organization of Visual Features for Rapid Categorization
- auto_source_url: https://doi.org/10.1038/s41598-018-22160-9

### Deep Unsupervised Learning using Nonequilibrium Thermodynamics

Bibliographic:
- year: 2015
- venue: International Conference on Machine Learning
- doi: 10.48550/arxiv.1503.03585

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Unsupervised density estimation/generative modeling and conditional or posterior inference such as image inpainting.
- paper_objective: Unsupervised density estimation/generative modeling and conditional or posterior inference such as image inpainting.
- method_family: Diffusion/generative model
- method_summary: Diffusion/generative model
- dataset: Toy 2D swiss roll, binary heartbeat sequences, MNIST, CIFAR-10, dead-leaves images, and bark texture images.
- dataset_role: used
- metric: Model log likelihood / lower bound, bits per pixel for dead leaves, Parzen-window log-likelihood estimates for MNIST, and qualitative sampling/inpainting.
- metric_status: applicable
- limitations: Computational cost scales with the learned function cost times the number of diffusion time steps; experiments used selected toy/image datasets and MLP reverse-transition functions.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://www.semanticscholar.org/paper/2dcef55a07f8607a819c21fe84131ea269cc2e3c; https://proceedings.mlr.press/v37/sohl-dickstein15.html; https://proceedings.mlr.press/v37/sohl-dickstein15.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=The experiments list swiss roll, binary sequence, MNIST, CIFAR-10, dead leaves, and bark texture data. | confidence=high
- limitations: evidence=The paper states that sampling/computation cost is multiplied by the number of time steps and describes the experimental model class. | confidence=medium
- metric: evidence=The experiments compare likelihood-related quantities, bits per pixel, Parzen-window estimates, and sample/inpainting outputs. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The paper is a general machine-learning generative modeling paper with no neural measurements. | confidence=high
- task_taxonomy: evidence=The abstract frames the method as unsupervised modeling of complex datasets via learned reverse diffusion. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: Deep Unsupervised Learning using Nonequilibrium Thermodynamics
- auto_source_url: https://www.semanticscholar.org/paper/2dcef55a07f8607a819c21fe84131ea269cc2e3c

### Deep Unsupervised Learning using Nonequilibrium Thermodynamics

Bibliographic:
- year: 2015
- venue: International Conference on Machine Learning
- doi: 10.48550/arxiv.1503.03585

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Unsupervised density estimation/generative modeling and conditional or posterior inference such as image inpainting.
- paper_objective: Unsupervised density estimation/generative modeling and conditional or posterior inference such as image inpainting.
- method_family: Diffusion/generative model
- method_summary: Diffusion/generative model
- dataset: Toy 2D swiss roll, binary heartbeat sequences, MNIST, CIFAR-10, dead-leaves images, and bark texture images.
- dataset_role: used
- metric: Model log likelihood / lower bound, bits per pixel for dead leaves, Parzen-window log-likelihood estimates for MNIST, and qualitative sampling/inpainting.
- metric_status: applicable
- limitations: Computational cost scales with the learned function cost times the number of diffusion time steps; experiments used selected toy/image datasets and MLP reverse-transition functions.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://www.semanticscholar.org/paper/2dcef55a07f8607a819c21fe84131ea269cc2e3c; https://proceedings.mlr.press/v37/sohl-dickstein15.html; https://proceedings.mlr.press/v37/sohl-dickstein15.pdf
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=The experiments list swiss roll, binary sequence, MNIST, CIFAR-10, dead leaves, and bark texture data. | confidence=high
- limitations: evidence=The paper states that sampling/computation cost is multiplied by the number of time steps and describes the experimental model class. | confidence=medium
- metric: evidence=The experiments compare likelihood-related quantities, bits per pixel, Parzen-window estimates, and sample/inpainting outputs. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The paper is a general machine-learning generative modeling paper with no neural measurements. | confidence=high
- task_taxonomy: evidence=The abstract frames the method as unsupervised modeling of complex datasets via learned reverse diffusion. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: Deep Unsupervised Learning using Nonequilibrium Thermodynamics
- auto_source_url: https://www.semanticscholar.org/paper/2dcef55a07f8607a819c21fe84131ea269cc2e3c

### DiffEditor: Boosting Accuracy and Flexibility on Diffusion-Based Image Editing

Bibliographic:
- year: 2024
- venue: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
- doi: 10.1109/cvpr52733.2024.00811

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Fine-grained diffusion-based image editing, including object moving, resizing, content dragging, appearance replacing, and object pasting.
- paper_objective: Fine-grained diffusion-based image editing, including object moving, resizing, content dragging, appearance replacing, and object pasting.
- method_family: Diffusion/generative model
- method_summary: Diffusion/generative model
- dataset: LAION training data for image-prompt training, processed to 512x512; evaluation includes the same DragonDiff face-manipulation test set of 800 aligned CelebA-HQ training-set faces and 16 editing samples for each object pasting, object moving, and appearance replacing task.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: The authors state that the method still struggles with large content imagination, such as rotating a car by dragging its front, because the base Stable Diffusion model lacks 3D perception of individual objects.
- limitation_source: explicit

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/cvpr52733.2024.00811; https://openaccess.thecvf.com/content/CVPR2024/papers/Mou_DiffEditor_Boosting_Accuracy_and_Flexibility_on_Diffusion-based_Image_Editing_CVPR_2024_paper.pdf; https://arxiv.org/abs/2402.02583; https://openaccess.thecvf.com/content/CVPR2024/html/Mou_DiffEditor_Boosting_Accuracy_and_Flexibility_on_Diffusion-based_Image_Editing_CVPR_2024_paper.html
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=The CVF paper states that image prompt training uses LAION data at 512x512, the face-manipulation comparison uses DragonDiff's 800 aligned faces from CelebA-HQ training set, and object pasting/moving/replacing quantization uses 16 editing samples per task. | confidence=high | tier=tier1_paper_text
- limitations: evidence=The CVPR paper's limitations section identifies large-content/3D-imagination failures tied to Stable Diffusion's lack of object-level 3D perception. | confidence=high
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=The paper is an image-editing diffusion model paper and reports no neural data. | confidence=high
- task_taxonomy: evidence=The abstract and task description list fine-grained image-editing operations such as moving, resizing, dragging, replacing, and pasting. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: DiffEditor: Boosting Accuracy and Flexibility on Diffusion-Based Image Editing
- auto_source_url: https://doi.org/10.1109/cvpr52733.2024.00811

### Diffusion Schrödinger Bridge Matching

Bibliographic:
- year: 2023
- venue: Advances in Neural Information Processing Systems 36
- doi: 10.52202/075280-2717

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Schrodinger bridge / distribution transport and generative modeling, including domain transfer and unpaired super-resolution or downscaling.
- paper_objective: Schrodinger bridge / distribution transport and generative modeling, including domain transfer and unpaired super-resolution or downscaling.
- method_family: Diffusion/generative model, Linear/encoding baseline
- method_summary: Diffusion/generative model, Linear/encoding baseline
- dataset: Synthetic 2D Gaussian-mixture transport tasks, high-dimensional Gaussian transport, MNIST-EMNIST, CelebA, AFHQ cat-to-wild, CIFAR-10, and unpaired geophysical fluid-flow downscaling data.
- dataset_role: used
- metric: 2-Wasserstein distance, path energy, FID, LPIPS, KL for Gaussian marginals, and fluid-flow spectral/distance measures; CIFAR-10 FID is computed on generated samples.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.52202/075280-2717; https://proceedings.neurips.cc/paper_files/paper/2023/file/c428adf74782c2092d254329b6b02482-Paper-Conference.pdf; https://openreview.net/forum?id=qy07OHsJT5; https://arxiv.org/abs/2303.16852
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=The experiments cover synthetic transport, image-domain transfer, CIFAR-10 generation, and unpaired fluid-flow downscaling. | confidence=high
- metric: evidence=The results report transport metrics such as 2-Wasserstein distance and path energy, image metrics such as FID and LPIPS, and task-specific fluid-flow measures. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The paper is a generative modeling and optimal transport method paper with no neural measurements. | confidence=high
- task_taxonomy: evidence=The abstract and experiments frame DSBM as a method for Schrodinger bridge matching and distribution transport/generation. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Diffusion Schrödinger Bridge Matching
- auto_source_url: https://doi.org/10.52202/075280-2717

### Dimensions That Matter – Interpretable Object Dimensions in Humans and Deep Neural Networks

Bibliographic:
- year: 2023
- venue: 2023 Conference on Cognitive Computational Neuroscience
- doi: 10.32470/ccn.2023.1291-0

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: Triplet odd-one-out similarity task applied to humans and VGG-16 as an in-silico observer, approximate Bayesian embedding, and in-silico interpretability tests including activation maximization, Grad-CAM, and color/shape manipulations.
- method_summary: Triplet odd-one-out similarity task applied to humans and VGG-16 as an in-silico observer, approximate Bayesian embedding, and in-silico interpretability tests including activation maximization, Grad-CAM, and color/shape manipulations.
- dataset: THINGS image database and human similarity-judgment embeddings: 24,102 images from 1,854 categories with 13 exemplars; simulated 20 million triplets from VGG-16 features; human embedding from Hebart et al.
- dataset_role: used
- metric: Human-DNN embedding correlations per dimension, predictive power of low-dimensional embeddings, and similarity-matrix/triplet-choice modeling.
- metric_status: applicable
- limitations: The authors report that differences remain in individual-object activations despite positive human-DNN embedding correlations, indicating remaining room for DNN-human alignment improvement; the work is motivated by limits of RSA/CKA in directly revealing underlying factors.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.32470/ccn.2023.1291-0; https://2023.ccneuro.org/view_paperbe5a.html?PaperNum=1291; https://2023.ccneuro.org/proceedings/0000763.pdf?s=W&pn=1291; https://repository.ubn.ru.nl/bitstream/handle/2066/297725/297725.pdf?sequence=1
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=The paper describes VGG-16 features for 24,102 THINGS images across 1,854 categories and uses human similarity embeddings from prior work. | confidence=high
- limitations: evidence=The discussion states that individual-object activation differences remain and motivates the method by the interpretability limits of classical representational comparisons. | confidence=medium
- method_summary: evidence=The paper uses odd-one-out triplets, Bayesian embedding, and in-silico tests to compare human and DNN representations. | confidence=high
- metric: evidence=The results compare embedding correlations, predictive dimensionality, and triplet/similarity-based representations. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The study compares behavioral similarity judgments and DNN representations; it reports no neural recordings. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Dimensions That Matter – Interpretable Object Dimensions in Humans and Deep Neural Networks
- auto_source_url: https://doi.org/10.32470/ccn.2023.1291-0

### Dimensions That Matter – Interpretable Object Dimensions in Humans and Deep Neural Networks

Bibliographic:
- year: 2023
- venue: 2023 Conference on Cognitive Computational Neuroscience
- doi: 10.32470/ccn.2023.1291-0

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: Triplet odd-one-out similarity task applied to humans and VGG-16 as an in-silico observer, approximate Bayesian embedding, and in-silico interpretability tests including activation maximization, Grad-CAM, and color/shape manipulations.
- method_summary: Triplet odd-one-out similarity task applied to humans and VGG-16 as an in-silico observer, approximate Bayesian embedding, and in-silico interpretability tests including activation maximization, Grad-CAM, and color/shape manipulations.
- dataset: THINGS image database and human similarity-judgment embeddings: 24,102 images from 1,854 categories with 13 exemplars; simulated 20 million triplets from VGG-16 features; human embedding from Hebart et al.
- dataset_role: used
- metric: Human-DNN embedding correlations per dimension, predictive power of low-dimensional embeddings, and similarity-matrix/triplet-choice modeling.
- metric_status: applicable
- limitations: The authors report that differences remain in individual-object activations despite positive human-DNN embedding correlations, indicating remaining room for DNN-human alignment improvement; the work is motivated by limits of RSA/CKA in directly revealing underlying factors.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.32470/ccn.2023.1291-0; https://2023.ccneuro.org/view_paperbe5a.html?PaperNum=1291; https://2023.ccneuro.org/proceedings/0000763.pdf?s=W&pn=1291; https://repository.ubn.ru.nl/bitstream/handle/2066/297725/297725.pdf?sequence=1
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=The paper describes VGG-16 features for 24,102 THINGS images across 1,854 categories and uses human similarity embeddings from prior work. | confidence=high
- limitations: evidence=The discussion states that individual-object activation differences remain and motivates the method by the interpretability limits of classical representational comparisons. | confidence=medium
- method_summary: evidence=The paper uses odd-one-out triplets, Bayesian embedding, and in-silico tests to compare human and DNN representations. | confidence=high
- metric: evidence=The results compare embedding correlations, predictive dimensionality, and triplet/similarity-based representations. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The study compares behavioral similarity judgments and DNN representations; it reports no neural recordings. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Dimensions That Matter – Interpretable Object Dimensions in Humans and Deep Neural Networks
- auto_source_url: https://doi.org/10.32470/ccn.2023.1291-0

### Direct Diffusion Bridge using Data Consistency for Inverse Problems

Bibliographic:
- year: 2023
- venue: Advances in Neural Information Processing Systems 36
- doi: 10.52202/075280-0313

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Image inverse-problem reconstruction/restoration with direct diffusion bridges and data consistency.
- paper_objective: Image inverse-problem reconstruction/restoration with direct diffusion bridges and data consistency.
- method_family: Diffusion/generative model, Linear/encoding baseline
- method_summary: Diffusion/generative model, Linear/encoding baseline
- dataset: ImageNet 256x256 benchmark with 1,000 validation images; degradations include 4x super-resolution, deblurring, inpainting, and JPEG restoration.
- dataset_role: used
- metric: PSNR, SSIM, LPIPS, FID, neural function evaluations (NFE).
- metric_status: applicable
- limitations: Assumes prior knowledge of the forward operator; scoped to non-blind inverse problems; some inpainting quantitative metrics can decrease; inherited priors may intensify social bias.
- limitation_source: explicit

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.52202/075280-0313; https://www.proceedings.com/content/075/075280-0313open.pdf; https://openreview.net/forum?id=497CevPdOg
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Paper states all experiments are based on ImageNet 256x256 and test sr4x, deblur, JPEG restoration with 1k validation images. | confidence=high
- limitations: evidence=Limitations section states prior forward operator knowledge, non-blind scope, quantitative decreases for some inpainting, and learned-prior bias risk. | confidence=high
- metric: evidence=Tables report PSNR, SSIM, LPIPS, FID; discussion compares NFE and Pareto frontier. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The work is a computer-vision diffusion inverse-problem method, not neural data. | confidence=high
- task_taxonomy: evidence=The method modifies direct diffusion bridge inference for image inverse problems by imposing data consistency. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Direct Diffusion Bridge using Data Consistency for Inverse Problems
- auto_source_url: https://doi.org/10.52202/075280-0313

### Discovering faster matrix multiplication algorithms with reinforcement learning

Bibliographic:
- year: 2022
- venue: Nature
- doi: 10.1038/s41586-022-05172-4

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: not specified
- task_taxonomy: Reinforcement-learning search for efficient tensor decompositions / matrix multiplication algorithms.
- paper_objective: Reinforcement-learning search for efficient tensor decompositions / matrix multiplication algorithms.
- method_family: Reinforcement learning/bandit
- method_summary: Reinforcement learning/bandit
- dataset: Synthetic TensorGame training data: 5 million tensor-factorization pairs plus previous high-scoring games; target tensors represent matrix multiplication operations.
- dataset_role: used
- metric: Rank/number of scalar multiplications for matrix multiplication algorithms, plus hardware-tailored runtime for some use cases.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41586-022-05172-4; https://www.nature.com/articles/s41586-022-05172-4; https://pmc.ncbi.nlm.nih.gov/articles/PMC9534758/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Nature methods describe a synthetic demonstrations buffer of 5 million tensor-factorization pairs generated by random factors. | confidence=high
- metric: evidence=Nature abstract/results emphasize outperforming state-of-the-art complexity by reducing scalar multiplications and optimizing actual runtime for hardware-specific algorithms. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=This is algorithm discovery over tensors and synthetic games, not neural measurements. | confidence=high
- task_taxonomy: evidence=AlphaTensor is trained to solve TensorGame and find efficient matrix multiplication algorithms. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Discovering faster matrix multiplication algorithms with reinforcement learning
- auto_source_url: https://doi.org/10.1038/s41586-022-05172-4

### Distributed representations of behaviour-derived object dimensions in the human visual system

Bibliographic:
- year: 2024
- venue: Nature Human Behaviour
- doi: 10.1038/s41562-024-01980-y

Paper type:
- type: system

Evidence fields:
- signal_modality: fMRI BOLD responses in human visual cortex
- input_modality: fMRI
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: Voxel-wise fMRI encoding model using 66 behavior-derived object dimensions, with CLIP-ViT used to extend dimensions to individual images.
- method_summary: Voxel-wise fMRI encoding model using 66 behavior-derived object dimensions, with CLIP-ViT used to extend dimensions to individual images.
- dataset: THINGS-data collection: fMRI responses to 8,740 object images from 720 categories in 3 participants, plus 4.7 million behavioral similarity judgements.
- dataset_role: used
- metric: Noise-ceiling-corrected R2 / explained variance as prediction accuracy in 12-fold between-session cross-validation.
- metric_status: applicable
- limitations: The behavioral similarity embedding was trained on only one image for each of 1,854 THINGS categories, so the dimensions may only partially capture the full image set's visual richness.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41562-024-01980-y; https://www.nature.com/articles/s41562-024-01980-y
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Nature article reports THINGS-data with fMRI and behavioral responses; 3 participants each saw 8,740 unique object images. | confidence=high
- limitations: evidence=Results section states the embedding's one-image-per-category training may only partially capture visual richness of the full image set. | confidence=high
- method_summary: evidence=Figure/method text says an encoding model predicts fMRI responses from object dimension embeddings; CLIP-ViT predicts dimensions for the image set. | confidence=high
- metric: evidence=Figure 2 caption defines prediction accuracy as noise-ceiling-corrected R2 on held-out data in 12-fold cross-validation. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The study maps behavior-derived object dimensions to fMRI BOLD responses in human visual cortex. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Distributed representations of behaviour-derived object dimensions in the human visual system
- auto_source_url: https://doi.org/10.1038/s41562-024-01980-y

### Distributed representations of behaviour-derived object dimensions in the human visual system

Bibliographic:
- year: 2024
- venue: Nature Human Behaviour
- doi: 10.1038/s41562-024-01980-y

Paper type:
- type: system

Evidence fields:
- signal_modality: fMRI BOLD responses in human visual cortex
- input_modality: fMRI
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: Voxel-wise fMRI encoding model using 66 behavior-derived object dimensions, with CLIP-ViT used to extend dimensions to individual images.
- method_summary: Voxel-wise fMRI encoding model using 66 behavior-derived object dimensions, with CLIP-ViT used to extend dimensions to individual images.
- dataset: THINGS-data collection: fMRI responses to 8,740 object images from 720 categories in 3 participants, plus 4.7 million behavioral similarity judgements.
- dataset_role: used
- metric: Noise-ceiling-corrected R2 / explained variance as prediction accuracy in 12-fold between-session cross-validation.
- metric_status: applicable
- limitations: The behavioral similarity embedding was trained on only one image for each of 1,854 THINGS categories, so the dimensions may only partially capture the full image set's visual richness.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41562-024-01980-y; https://www.nature.com/articles/s41562-024-01980-y
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Nature article reports THINGS-data with fMRI and behavioral responses; 3 participants each saw 8,740 unique object images. | confidence=high
- limitations: evidence=Results section states the embedding's one-image-per-category training may only partially capture visual richness of the full image set. | confidence=high
- method_summary: evidence=Figure/method text says an encoding model predicts fMRI responses from object dimension embeddings; CLIP-ViT predicts dimensions for the image set. | confidence=high
- metric: evidence=Figure 2 caption defines prediction accuracy as noise-ceiling-corrected R2 on held-out data in 12-fold cross-validation. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The study maps behavior-derived object dimensions to fMRI BOLD responses in human visual cortex. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Distributed representations of behaviour-derived object dimensions in the human visual system
- auto_source_url: https://doi.org/10.1038/s41562-024-01980-y

### Dynamical flexible inference of nonlinear latent factors and structures in neural population activity

Bibliographic:
- year: 2023
- venue: Nature Biomedical Engineering
- doi: 10.1038/s41551-023-01106-1

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Neural population activity: smoothed neuronal firing rates and local field potentials (LFP)
- input_modality: not specified
- task_taxonomy: Flexible inference of low-dimensional nonlinear latent factors and latent structures in neural population activity, including causal/non-causal and missing-observation settings.
- paper_objective: Flexible inference of low-dimensional nonlinear latent factors and latent structures in neural population activity, including causal/non-causal and missing-observation settings.
- method_family: Linear/encoding baseline
- method_summary: Linear/encoding baseline
- dataset: Four neural datasets across macaque saccade, 3D reach-and-grasp, 2D random-target reaching, and 2D grid reaching tasks, plus simulations; modalities include smoothed firing rates and LFP.
- dataset_role: used
- metric: 5-fold cross-validation; behavior prediction measured by AUC for classifiers and Pearson correlation for regressions; neural prediction/reconstruction and NRMSE; TDA for manifold structure.
- metric_status: applicable
- limitations: DFINE can learn suboptimal results because dynamics are linear on the nonlinear manifold; combining sessions is not implemented; other output distributions and input modeling are future work.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41551-023-01106-1; https://www.nature.com/articles/s41551-023-01106-1
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Methods describe analyses on four diverse datasets with distinct behavioral tasks, brain regions, and neural modalities. | confidence=high
- limitations: evidence=Future directions section lists linear manifold dynamics as a design choice, no cross-session combination, Gaussian outputs, and future input modeling. | confidence=high
- metric: evidence=Results/methods state 5-fold CV; AUC/CC for behavior, one-step-ahead neural prediction, NRMSE, and TDA. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Article states it models smoothed neuronal firing rates and LFP and tests field potentials as well as firing rates. | confidence=high
- task_taxonomy: evidence=Abstract states DFINE models lower-dimensional nonlinear latent factors and structures with flexible inference under missing observations. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Dynamical flexible inference of nonlinear latent factors and structures in neural population activity
- auto_source_url: https://doi.org/10.1038/s41551-023-01106-1

### EEG Electrodes and Where to Find Them: Automated Localization From 3D Scans

Bibliographic:
- year: 2024
- venue: Journal of Neural Engineering
- doi: 10.1088/1741-2552/ad7c7e

Paper type:
- type: system

Evidence fields:
- signal_modality: EEG
- input_modality: EEG
- task_taxonomy: Automated localization of EEG electrode positions from 3D scans for source-localization workflows.
- paper_objective: Automated localization of EEG electrode positions from 3D scans for source-localization workflows.
- method_family: Two-tier end-to-end framework for landmark/fiducial localization and EEG electrode localization from 3D scans, designed to work without MRI but compatible with MRI.
- method_summary: Two-tier end-to-end framework for landmark/fiducial localization and EEG electrode localization from 3D scans, designed to work without MRI but compatible with MRI.
- dataset: Over 400 3D scans from 278 subjects.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1088/1741-2552/ad7c7e; https://pubmed.ncbi.nlm.nih.gov/39293479/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=PubMed/OpenAlex abstract states validation on an extensive dataset containing over 400 3D scans from 278 subjects. | confidence=high
- method_summary: evidence=Abstract says the solution uses landmark/fiducial localization and electrode localization in an end-to-end framework. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- task_taxonomy: evidence=Objective/significance sections emphasize accurate EEG electrode position localization for source localization. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: EEG electrodes and where to find them: automated localization from 3D scans
- auto_source_url: https://doi.org/10.1088/1741-2552/ad7c7e

### EEG electrode digitization with commercial virtual reality hardware

Bibliographic:
- year: 2018
- venue: PLOS ONE
- doi: 10.1371/journal.pone.0207516

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: EEG
- input_modality: EEG
- task_taxonomy: EEG electrode digitization / 3D localization for EEG source localization and imaging.
- paper_objective: EEG electrode digitization / 3D localization for EEG source localization and imaging.
- method_family: Open-source VRDigitizer software using consumer HTC Vive VR tracking hardware, endpoint calibration, and optional head tracking to digitize EEG fiducials/electrodes.
- method_summary: Open-source VRDigitizer software using consumer HTC Vive VR tracking hardware, endpoint calibration, and optional head tracking to digitize EEG fiducials/electrodes.
- dataset: Experimental evaluations in a phantom head model and 12 human subjects; data available via Zenodo.
- dataset_role: used
- metric: Mean electrode localization error/RMSE; reported mean error 3.74 mm for VRDigitizer versus 1.73 mm and 2.98 mm for commercial systems.
- metric_status: applicable
- limitations: Reference Brainsight measurements were treated as ground truth but could contain consistent bias/geometric distortion; more rigorous phantom measurements are suggested for future accuracy assessment.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1371/journal.pone.0207516; https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0207516; https://pmc.ncbi.nlm.nih.gov/articles/PMC6248988/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=PLOS abstract states evaluations were performed in a phantom head model and in 12 human subjects; data availability points to Zenodo. | confidence=high
- limitations: evidence=Discussion notes Brainsight reference may have consistent bias or distortion and suggests precise rigid phantom measurements for future work. | confidence=high
- method_summary: evidence=Methods describe MATLAB/Python VRDigitizer using OpenVR/Vive controllers/trackers, calibration, fiducials, and head tracking. | confidence=high
- metric: evidence=Abstract reports mean error values; figure/analysis text describes localization errors and RMSE. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- task_taxonomy: evidence=The paper's stated goal is measuring EEG electrode locations using accessible VR hardware. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: EEG electrode digitization with commercial virtual reality hardware
- auto_source_url: https://doi.org/10.1371/journal.pone.0207516

### EEG electrode localization with 3D iPhone scanning using point-cloud electrode selection (PC-ES)

Bibliographic:
- year: 2023
- venue: Journal of Neural Engineering
- doi: 10.1088/1741-2552/ad12db

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: EEG
- input_modality: EEG
- task_taxonomy: Portable, low-cost EEG scalp electrode localization/digitization for EEG source imaging.
- paper_objective: Portable, low-cost EEG scalp electrode localization/digitization for EEG source imaging.
- method_family: 3D scanning on modern iPhones plus semi-automated point-cloud electrode selection (PC-ES), a custom MATLAB desktop application; compared against photogrammetry.
- method_summary: 3D scanning on modern iPhones plus semi-automated point-cloud electrode selection (PC-ES), a custom MATLAB desktop application; compared against photogrammetry.
- dataset: Human study with over 6,000 electrodes labeled by both iPhone/PC-ES and photogrammetry; 8 subjects with 256-electrode hdEEG caps.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1088/1741-2552/ad12db; https://iopscience.iop.org/article/10.1088/1741-2552/ad12db/pdf; https://pubmed.ncbi.nlm.nih.gov/38055968/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=OpenAlex/IOP abstract reports over 6000 electrodes labeled using each method; PDF methods state 8 subjects with 256-electrode caps. | confidence=high
- method_summary: evidence=Abstract says iPhone scanning is combined with semi-automated image processing using PC-ES in MATLAB. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- task_taxonomy: evidence=Objective states accurate scalp-electrode localization is instrumental to ESI and the method addresses localization access barriers. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: EEG electrode localization with 3D iPhone scanning using point-cloud electrode selection (PC-ES)
- auto_source_url: https://doi.org/10.1088/1741-2552/ad12db

### Efficient Estimation of Word Representations in Vector Space

Bibliographic:
- year: 2020
- venue: Journal of Innovations in Engineering Education
- doi: 10.3126/jiee.v3i1.34327

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: text/speech
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: Nepali Word2Vec-style word representation using Skip-gram with NCE loss; compares/mentions TF-IDF and CBOW baselines.
- method_summary: Nepali Word2Vec-style word representation using Skip-gram with NCE loss; compares/mentions TF-IDF and CBOW baselines.
- dataset: Raw Nepali text scraped from Nepali news portals, Nepali tweets, and Nepali Wiktionary.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: The authors describe scarce raw Nepali data, fewer resources, complex syntactic structures, and follow-up work on common word phrases and frequent-word reduction.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.3126/jiee.v3i1.34327; https://www.researchgate.net/publication/348525097_Efficient_Estimation_of_Nepali_Word_Representations_in_Vector_Space
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Full-text section 'Data Collection' states data source is online portals: Nepali news portals, Nepali tweets, and Nepali Wiktionary. | confidence=high
- limitations: evidence=Conclusion/follow-up says data are scarce, Nepali has fewer resources and complex syntax, and proposes phrase handling/frequent word deletion. | confidence=medium
- method_summary: evidence=Abstract says the model is based on Skip-gram with NCE loss; methodology describes TF-IDF, CBOW, Skip-gram, and NCE. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=This is an NLP word-embedding paper over Nepali text, not neural measurements. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Efficient Estimation of Nepali Word Representations in Vector Space
- auto_source_url: https://doi.org/10.3126/jiee.v3i1.34327

### Efficient processing of natural scenes in visual cortex

Bibliographic:
- year: 2022
- venue: Frontiers in Cellular Neuroscience
- doi: 10.3389/fncel.2022.1006703

Paper type:
- type: review

Evidence fields:
- signal_modality: Visual cortex neural circuits / visual-system responses
- input_modality: ECoG
- task_taxonomy: Visual reconstruction
- paper_objective: Visual reconstruction
- method_family: Narrative/theoretical review of efficient coding and adaptation to natural visual statistics across retina, V1, V2 and higher visual cortex, including human and animal evidence.
- method_summary: Narrative/theoretical review of efficient coding and adaptation to natural visual statistics across retina, V1, V2 and higher visual cortex, including human and animal evidence.
- dataset: No new dataset; this is a review synthesizing studies of natural-scene spatial/temporal statistics, texture perception, object recognition, and visual-cortex adaptation.
- dataset_role: none_review
- metric: unresolved
- metric_status: not_applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.3389/fncel.2022.1006703; https://www.frontiersin.org/journals/cellular-neuroscience/articles/10.3389/fncel.2022.1006703/full
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Frontiers page labels the article as a review and its abstract says it reviews recent developments rather than introducing a new empirical dataset. | confidence=high
- method_summary: evidence=Outline and abstract cover adaptation to spatial statistics, temporal statistics, texture perception and object recognition under efficient coding. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The article discusses neural circuits in visual systems and adaptation in visual cortex. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Efficient processing of natural scenes in visual cortex
- auto_source_url: https://doi.org/10.3389/fncel.2022.1006703

### EgoLM: Multi-Modal Language Model of Egocentric Motions

Bibliographic:
- year: 2025
- venue: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
- doi: 10.1109/cvpr52734.2025.00503

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Multimodal neural data, Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Egocentric motion understanding and generation, including motion tracking from sparse sensors/video, motion narration, text-to-motion, and sensor-to-text.
- paper_objective: Egocentric motion understanding and generation, including motion tracking from sparse sensors/video, motion narration, text-to-motion, and sensor-to-text.
- method_family: Large language model
- method_summary: Large language model
- dataset: Nymeria dataset: Xsens full-body motion, Aria egocentric videos, and human motion narrations; tracking train/test are 147.89/41.93 hours, understanding train/test are 16,673/7,468 segments.
- dataset_role: used
- metric: Motion tracking uses joint position errors and joint angle errors; motion narration uses BERT, BLEU, and ROUGE scores.
- metric_status: applicable
- limitations: The authors explicitly list three limitations: the motion tokenizer introduces reconstruction errors and bounds tracking performance; CLIP compresses each video frame to a one-dimensional vector, making object interaction identification difficult; EgoLM can hallucinate like other language models.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/cvpr52734.2025.00503; https://openaccess.thecvf.com/content/CVPR2025/papers/Hong_EgoLM_Multi-Modal_Language_Model_of_Egocentric_Motions_CVPR_2025_paper.pdf; https://arxiv.org/abs/2409.18127
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=CVPR PDF experiment setup states Nymeria contains Xsens mocap, Aria egocentric videos, and human narrations, with train/test durations and segment counts. | confidence=high
- limitations: evidence=CVF paper Discussion has a Limitations paragraph stating these three issues directly after the discussion of EgoLM's multimodal multi-task training. | confidence=high | tier=tier1_paper_text
- metric: evidence=Evaluation protocols section lists joint position/angle errors for tracking and BERT/BLEU/ROUGE for narration. | confidence=high
- record: confidence=high | tier=tier1_paper_text
- task_taxonomy: evidence=Abstract says it unifies motion narration from video or motion data and motion generation from text or sparse sensor data, plus text from sparse sensors. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: EgoLM: Multi-Modal Language Model of Egocentric Motions
- auto_source_url: https://doi.org/10.1109/cvpr52734.2025.00503

### EmotionKD: A Cross-Modal Knowledge Distillation Framework for Emotion Recognition Based on Physiological Signals

Bibliographic:
- year: 2023
- venue: Proceedings of the 31st ACM International Conference on Multimedia
- doi: 10.1145/3581783.3612277

Paper type:
- type: system

Evidence fields:
- signal_modality: Multimodal neural data
- input_modality: ECoG
- task_taxonomy: Emotion recognition from physiological signals.
- paper_objective: Emotion recognition from physiological signals.
- method_family: Cross-modal knowledge distillation from fused EEG+GSR multimodal features into a unimodal GSR model, with adaptive feedback during distillation.
- method_summary: Cross-modal knowledge distillation from fused EEG+GSR multimodal features into a unimodal GSR model, with adaptive feedback during distillation.
- dataset: Two public emotion-recognition datasets (names not visible in trusted accessible abstract).
- dataset_role: used
- metric: Accuracy (Acc) and F1-score for arousal and valence emotion recognition
- metric_status: applicable
- limitations: EEG acquisition is described as high-cost and inconvenient, motivating distillation into an easier-to-acquire GSR model with some sacrificed performance.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1145/3581783.3612277; https://dl.acm.org/doi/10.1145/3581783.3612277; https://api.openalex.org/works/https://doi.org/10.1145/3581783.3612277; https://www.researchgate.net/publication/375032220_EmotionKD_A_Cross-Modal_Knowledge_Distillation_Framework_for_Emotion_Recognition_Based_on_Physiological_Signals
- evidence_tier: tier2_author_uploaded_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=OpenAlex abstract says experiments are on two public datasets but does not name them. | confidence=medium
- limitations: evidence=ACM/OpenAlex abstract says EEG acquisition cost and inconvenience hinder real-world use, and the method reduces multimodal reliance with lower sacrificed performance. | confidence=medium
- method_summary: evidence=Abstract describes cross-modal KD modeling GSR/EEG heterogeneity and interactivity, transferring fused multimodal features to unimodal GSR. | confidence=high
- metric: evidence=The paper tables for DEAP and HCI-Tagging compare methods on Arousal and Valence columns labeled Acc and F1-score, after explaining that all methods are evaluated on GSR data for the EmotionNet-Student comparisons. | confidence=medium | tier=tier2_author_uploaded_paper_text
- record: confidence=medium | tier=tier2_author_uploaded_paper_text
- task_taxonomy: evidence=Title and abstract identify emotion recognition based on physiological signals. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: EmotionKD: A Cross-Modal Knowledge Distillation Framework for Emotion Recognition Based on Physiological Signals
- auto_source_url: https://doi.org/10.1145/3581783.3612277

### EnerVerse-AC: Envisioning Embodied Environments with Action Condition

Bibliographic:
- year: 2025
- venue: Preprints.org
- doi: 10.20944/preprints202505.1193.v1

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Dataset/benchmark
- paper_objective: Dataset/benchmark
- method_family: EVAC action-conditioned embodied world model using video diffusion, multi-level action conditioning, end-effector projection action maps, delta-action encodings, multi-view/ray-map conditioning, and failure-trajectory data.
- method_summary: EVAC action-conditioned embodied world model using video diffusion, multi-level action conditioning, end-effector projection action maps, delta-action encodings, multi-view/ray-map conditioning, and failure-trajectory data.
- dataset: AgiBot World training data with over 210 tasks and 1 million trajectories, augmented with mined and newly collected real-world failure trajectories.
- dataset_role: used
- metric: Success rate (SR) for policy evaluation/data augmentation; qualitative multi-view video generation and evaluator alignment with real-world success trends.
- metric_status: applicable
- limitations: Gripper-openness unit-circle representation may not generalize to complex end-effectors; wrist-camera background noise limits multi-view inference to 10 chunks vs 30 chunks for single-view generation.
- limitation_source: explicit

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.20944/preprints202505.1193.v1; https://arxiv.org/abs/2505.09723; https://arxiv.org/html/2505.09723
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=arXiv section 4.1 states EVAC training data primarily comes from AgiBot World, with over 210 tasks and 1 million trajectories, plus failure cases. | confidence=high
- limitations: evidence=Limitations section names gripper representation generalization and wrist-camera background noise/multi-view chunk limits. | confidence=high
- method_summary: evidence=Abstract/method describe multi-level action condition injection, ray maps, action maps, delta-action encodings, and video diffusion. | confidence=high
- metric: evidence=Experiments table reports success rate from 0.28 to 0.36 with augmented data; evaluator sections compare success rates/trends. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Robotics video/action world-model paper, not neural data. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: EnerVerse-AC: Envisioning Embodied Environments with Action Condition
- auto_source_url: https://doi.org/10.20944/preprints202505.1193.v1

### Explorations of using a convolutional neural network to understand brain activations during movie watching

Bibliographic:
- year: 2024
- venue: Psychoradiology
- doi: 10.1093/psyrad/kkae021

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: fMRI BOLD during naturalistic movie watching
- input_modality: fMRI
- task_taxonomy: Map hierarchical VGG-16 video features to brain activations during naturalistic movie viewing.
- paper_objective: Map hierarchical VGG-16 video features to brain activations during naturalistic movie viewing.
- method_family: CNN/RNN deep model
- method_summary: CNN/RNN deep model
- dataset: OpenNeuro ds000228 adult fMRI data; effective sample 29 adults after exclusions; participants watched Pixar's 'Partly Cloudy' animation for about 6 minutes.
- dataset_role: used
- metric: Voxel-wise GLM association/statistical activation maps linking VGG-16 kernel time series to fMRI responses.
- metric_status: applicable
- limitations: Exploratory analysis used averaged VGG-16 kernel activations and a straightforward GLM; authors note fMRI is coarse and they chose this crude approach over more sophisticated methods such as RSA.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1093/psyrad/kkae021; https://academic.oup.com/psyrad/article/doi/10.1093/psyrad/kkae021/7875223; https://pmc.ncbi.nlm.nih.gov/articles/PMC10849516/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Materials and Methods states fMRI came from OpenNeuro ds000228; n=33 adults before exclusions, effective sample 17 female and 12 male, watched 'Partly Cloudy'. | confidence=high
- limitations: evidence=Methods states activation maps were averaged to streamline analysis, fMRI is a coarse measure, and RSA was not used in this initial exploratory analysis. | confidence=high
- metric: evidence=Methods describes using each kernel's 1D activation time series in GLM on fMRI data. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The study analyzes functional MRI data acquired during cartoon-video watching. | confidence=high
- task_taxonomy: evidence=Abstract states the objective is linking VGG-16 layer activations to brain activations and visual-processing hierarchy. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Explorations of using a convolutional neural network to understand brain activations during movie watching
- auto_source_url: https://doi.org/10.1093/psyrad/kkae021

### Fast neural distance field-based three-dimensional reconstruction method for geometrical parameter extraction of walnut shell from multiview images

Bibliographic:
- year: 2024
- venue: Computers and Electronics in Agriculture
- doi: 10.1016/j.compag.2024.109189

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Dataset/benchmark
- paper_objective: Dataset/benchmark
- method_family: Neural distance field-based 3D reconstruction to generate scale-colored meshes and extract walnut-shell geometrical parameters from multiview images.
- method_summary: Neural distance field-based 3D reconstruction to generate scale-colored meshes and extract walnut-shell geometrical parameters from multiview images.
- dataset: Multiview image sequences of walnut shells for 3D reconstruction and geometrical parameter extraction.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: unresolved
- limitation_source: unresolved

Verification:
- final_unresolved_fields: limitations
- verification_status: needs_human_review
- evidence_sources: https://doi.org/10.1016/j.compag.2024.109189; https://www.researchgate.net/publication/382306439_Fast_neural_distance_field-based_three-dimensional_reconstruction_method_for_geometrical_parameter_extraction_of_walnut_shell_from_multiview_images; https://api.crossref.org/works/10.1016/j.compag.2024.109189
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=ResearchGate/metadata abstract snippet states the method extracts geometrical parameters of walnut shells from multiview image sequences. | confidence=medium
- method_summary: evidence=Title and accessible abstract snippet state a neural distance field-based 3D reconstruction method for scale colored mesh generation and parameter extraction. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Agricultural computer-vision/3D reconstruction from images, not neural measurements. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Fast neural distance field-based three-dimensional reconstruction method for geometrical parameter extraction of walnut shell from multiview images
- auto_source_url: https://doi.org/10.1016/j.compag.2024.109189

### Fg-T2M: Fine-Grained Text-Driven Human Motion Generation via Diffusion Model

Bibliographic:
- year: 2023
- venue: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
- doi: 10.1109/iccv51070.2023.02014

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: text/speech
- task_taxonomy: Fine-grained text-driven human motion generation / text-to-motion synthesis with diffusion.
- paper_objective: Fine-grained text-driven human motion generation / text-to-motion synthesis with diffusion.
- method_family: Diffusion/generative model, Graph neural network
- method_summary: Diffusion/generative model, Graph neural network
- dataset: HumanML3D and KIT Motion-Language datasets; HumanML3D has 14,616 motions and 44,970 descriptions, KIT has 3,911 motion sequences and 6,353 descriptions.
- dataset_role: used
- metric: R-precision, FID, multimodal distance, diversity, and multimodality for text-conditional motion synthesis.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/iccv51070.2023.02014; https://openaccess.thecvf.com/content/ICCV2023/papers/Wang_Fg-T2M_Fine-Grained_Text-Driven_Human_Motion_Generation_via_Diffusion_Model_ICCV_2023_paper.pdf; https://doi.org/10.1109/ICCV51070.2023.02014
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=ICCV PDF section 5.1 names HumanML3D and KIT and gives motion/description counts and durations. | confidence=high
- metric: evidence=Evaluation Metrics section defines R-precision, FID, multimodal distance, diversity, and multimodality. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Computer-vision motion-generation benchmark using text and human motion data, not neural signals. | confidence=high
- task_taxonomy: evidence=Abstract and experiments describe text-driven human motion generation. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Fg-T2M: Fine-Grained Text-Driven Human Motion Generation via Diffusion Model
- auto_source_url: https://doi.org/10.1109/iccv51070.2023.02014

### Flexible Motion In-betweening with Diffusion Models

Bibliographic:
- year: 2024
- venue: Special Interest Group on Computer Graphics and Interactive Techniques Conference Conference Papers
- doi: 10.1145/3641519.3657414

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: text/speech
- task_taxonomy: Text-conditioned human motion in-betweening / keyframe motion completion with diffusion models.
- paper_objective: Text-conditioned human motion in-betweening / keyframe motion completion with diffusion models.
- method_family: Diffusion/generative model
- method_summary: Diffusion/generative model
- dataset: HumanML3D dataset: 14,646 text-annotated human motion sequences from AMASS and HumanAct12, padded to 196 frames at 20 fps.
- dataset_role: used
- metric: FID, R-Precision, Diversity, Foot Skating Ratio, and Keyframe Error.
- metric_status: applicable
- limitations: Generated motions can show minor footskate and jitter for highly dynamic motions; HumanML3D includes skating/swimming outliers; random keyframe selection and redundant keyframe representation create partial-keyframe challenges.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1145/3641519.3657414; https://dl.acm.org/doi/10.1145/3641519.3657414; https://dl.acm.org/doi/fullHtml/10.1145/3641519.3657414; https://arxiv.org/abs/2405.11126
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=arXiv/ACM text says evaluation uses HumanML3D with 14,646 text-annotated sequences from AMASS and HumanAct12. | confidence=high
- limitations: evidence=Conclusion section explicitly lists footskate/jitter, skating/swimming data, random keyframes, and redundant representation issues. | confidence=high
- metric: evidence=Evaluation Metrics section lists FID, R-Precision, Diversity, Foot Skating Ratio, and Keyframe Error. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Motion animation/generation benchmark, not neural data. | confidence=high
- task_taxonomy: evidence=Abstract defines motion in-betweening as generating sequences that interpolate user-provided keyframe constraints. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Flexible Motion In-betweening with Diffusion Models
- auto_source_url: https://doi.org/10.1145/3641519.3657414

### Flow Matching Posterior Sampling: A Training-free Conditional Generation for Flow Matching

Bibliographic:
- year: 2026
- venue: IEEE Transactions on Image Processing
- doi: 10.1109/tip.2026.3698367

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Training-free conditional generation/posterior sampling for flow matching, including linear/non-linear inverse problems and text-style generation.
- paper_objective: Training-free conditional generation/posterior sampling for flow matching, including linear/non-linear inverse problems and text-style generation.
- method_family: Diffusion/generative model, Linear/encoding baseline
- method_summary: Diffusion/generative model, Linear/encoding baseline
- dataset: CelebA-HQ for linear and non-linear inverse problems; AFHQ in ablations; 1,000 text-image pairs from PartiPrompts with style images from FreeDom for text-style generation.
- dataset_role: used
- metric: SSIM, LPIPS, FID for linear inverse problems; norm distance, FID, KID for non-linear inverse problems; CLIP score and Gram-matrix style distance for text-style generation.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/tip.2026.3698367; https://arxiv.org/abs/2411.07625; https://arxiv.org/html/2411.07625
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=arXiv section 5.1 states CelebA-HQ is used for linear/non-linear inverse problems; text prompts are from PartiPrompts and style images from FreeDom; table uses AFHQ for ablation. | confidence=high
- metric: evidence=Evaluation Metrics paragraph explicitly lists SSIM/LPIPS/FID, distance/FID/KID, and CLIP/Gram matrix metrics. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Image-generation/inverse-problem method, not neural recordings. | confidence=high
- task_taxonomy: evidence=Abstract states FMPS enables posterior sampling for flow matching and extends conditional FMs beyond linear inverse problems. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Flow-Matching Posterior Sampling: A Training-Free Conditional Generation for Flow Matching
- auto_source_url: https://doi.org/10.1109/tip.2026.3698367

### Functional Connectivity of Imagined Speech and Visual Imagery based on Spectral Dynamics

Bibliographic:
- year: 2021
- venue: 2021 9th International Winter Conference on Brain-Computer Interface (BCI)
- doi: 10.1109/bci51272.2021.9385302

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: EEG
- input_modality: EEG
- task_taxonomy: Neural decoding, Visual reconstruction, Speech/language decoding, Dataset/benchmark
- paper_objective: Neural decoding, Visual reconstruction, Speech/language decoding, Dataset/benchmark
- method_family: Functional connectivity analysis using phase-locking value across seven cortical regions and four frequency ranges, compared with resting state.
- method_summary: Functional connectivity analysis using phase-locking value across seven cortical regions and four frequency ranges, compared with resting state.
- dataset: EEG dataset of 16 subjects performing 13-class imagined speech and visual imagery tasks.
- dataset_role: used
- metric: Phase-locking value (PLV) and statistical decreases/increases in functional connectivity relative to resting state.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/bci51272.2021.9385302; https://arxiv.org/abs/2012.03520; https://doi.org/10.1109/BCI51272.2021.9385302
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=arXiv abstract states the dataset contains sixteen subjects performing thirteen-class imagined speech and visual imagery. | confidence=high
- method_summary: evidence=Abstract states PLV was analyzed in seven cortical regions with four frequency ranges and compared to resting state. | confidence=high
- metric: evidence=The paper's stated connectivity measure is phase-locking value; results report significant decreases. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Title/abstract are EEG-based BCI imagined speech and visual imagery. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Functional Connectivity of Imagined Speech and Visual Imagery based on Spectral Dynamics
- auto_source_url: https://doi.org/10.1109/bci51272.2021.9385302

### Generalized radiograph representation learning via cross-supervision between images and free-text radiology reports

Bibliographic:
- year: 2022
- venue: Nature Machine Intelligence
- doi: 10.1038/s42256-021-00425-9

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: image/video
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: REFERS: cross-supervised representation learning using original free-text radiology reports as supervision for radiographs, with a vision transformer and multi-view patient-study representations.
- method_summary: REFERS: cross-supervised representation learning using original free-text radiology reports as supervision for radiographs, with a vision transformer and multi-view patient-study representations.
- dataset: MIMIC-CXR-JPG, NIH Chest X-ray, VinBigData Chest X-Ray Abnormalities Detection, Shenzhen Tuberculosis, and COVID-19 Image Data Collection are listed in data availability; article says evaluation used four well-known X-ray datasets under limited supervision.
- dataset_role: used
- metric: Area under the ROC curve (AUC)
- metric_status: applicable
- limitations: Experimental boundary: REFERS is a radiograph representation pretraining method using free-text radiology reports and multi-view patient studies, evaluated on four X-ray datasets under extremely limited supervision; data sources include MIMIC-CXR-JPG, NIH Chest X-ray, VinBigData, Shenzhen Tuberculosis and COVID-19 image collections.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s42256-021-00425-9; https://www.nature.com/articles/s42256-021-00425-9; https://www.medrxiv.org/content/10.1101/2021.11.02.21265838v1.full.pdf
- evidence_tier: tier1_paper_text
- confidence: medium

Field evidence:
- dataset: evidence=Nature data availability lists MIMIC-CXR-JPG, NIH, VinBigData, Shenzhen TB, and COVID-19 image collections; abstract mentions four X-ray datasets. | confidence=medium
- limitations: evidence=Nature abstract describes REFERS as using original radiology reports and multiple views within each patient study, outperforming baselines on four X-ray datasets under extremely limited supervision. Data availability lists the specific radiograph datasets used. | confidence=medium | tier=tier1_paper_text
- method_summary: evidence=Abstract describes reviewing free-text reports for supervision (REFERS), using reports accompanying radiographs and a vision transformer with multi-view study representations. | confidence=high
- metric: evidence=Nature Machine Intelligence extended-data captions for NIH ChestX-ray and VinBigData comparisons state that the evaluation metric is Area under the ROC Curve (AUC). | confidence=high | tier=tier1_paper_text
- record: confidence=medium | tier=tier1_paper_text
- signal_modality: evidence=Radiograph image/text representation learning, not neural signals. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Generalized radiograph representation learning via cross-supervision between images and free-text radiology reports
- auto_source_url: https://doi.org/10.1038/s42256-021-00425-9

### Generating Long Videos of Dynamic Scenes

Bibliographic:
- year: 2022
- venue: Advances in Neural Information Processing Systems 35
- doi: 10.52202/068431-2303

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline: natural video frames/dynamic visual scenes.
- input_modality: image/video
- task_taxonomy: Representation alignment, Dataset/benchmark
- paper_objective: Representation alignment, Dataset/benchmark
- method_family: Long-video GAN/video generation model that prioritizes the time axis, redesigns the temporal latent representation, and uses two-phase training with longer low-resolution videos and shorter high-resolution videos.
- method_summary: Long-video GAN/video generation model that prioritizes the time axis, redesigns the temporal latent representation, and uses two-phase training with longer low-resolution videos and shorter high-resolution videos.
- dataset: Two long-video benchmark datasets introduced for long-term dynamics, including horseback-riding and sky/time-lapse style dynamic-scene videos.
- dataset_role: created
- metric: Video-generation evaluation using quantitative video metrics including FVD-style comparisons for generated videos, plus benchmark comparisons against prior video generators.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.52202/068431-2303; https://papers.neurips.cc/paper_files/paper/2022/file/ce208d95d020b023cba9e64031db2584-Paper-Conference.pdf; https://arxiv.org/abs/2206.03429; https://openreview.net/forum?id=VnAwNNJiwDb
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=The NeurIPS/arXiv abstract states the paper introduces two benchmark datasets focused on long-term temporal dynamics; the PDF example describes a horseback-riding dataset. | confidence=medium
- method_summary: evidence=The abstract says the authors redesign the temporal latent representation and train in two phases: long low-resolution videos and short high-resolution videos. | confidence=high
- metric: evidence=The paper evaluates generated videos quantitatively against video-generation baselines; search-visible paper text identifies video-generation benchmark metrics. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=OpenReview keywords are video generation/GAN/generative model/dynamics; there is no neural recording or BCI signal. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Generating Long Videos of Dynamic Scenes
- auto_source_url: https://doi.org/10.52202/068431-2303

### Glove: Global Vectors for Word Representation

Bibliographic:
- year: 2014
- venue: Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)
- doi: 10.3115/v1/d14-1162

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline: text corpora/NLP word co-occurrence statistics.
- input_modality: text/speech
- task_taxonomy: Representation alignment
- paper_objective: Representation alignment
- method_family: Linear/encoding baseline
- method_summary: Linear/encoding baseline
- dataset: Large text corpora used for training word vectors, including Wikipedia 2014 plus Gigaword 5 and Common Crawl corpora.
- dataset_role: used
- metric: Word analogy accuracy, word similarity evaluation, and NER benchmark performance.
- metric_status: applicable
- limitations: The paper's empirical scope is bounded to static word-vector evaluations on word analogy, word similarity, and NER benchmarks.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.3115/v1/d14-1162; https://aclanthology.org/D14-1162.pdf; https://nlp.stanford.edu/projects/glove/
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=ACL paper describes training on global word-word co-occurrence counts from large corpora; the Stanford GloVe page lists Wikipedia/Gigaword and Common Crawl vector releases. | confidence=high
- limitations: evidence=The paper reports evidence through word analogy, word similarity, and NER experiments; no neural or multimodal evaluation is claimed. | confidence=medium
- metric: evidence=The ACL abstract reports 75% accuracy on the word analogy dataset and additional word similarity and NER benchmark evaluations. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The method learns word vectors from text co-occurrence counts, not neural measurements. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Glove: Global Vectors for Word Representation
- auto_source_url: https://doi.org/10.3115/v1/d14-1162

### Grandmaster level in StarCraft II using multi-agent reinforcement learning

Bibliographic:
- year: 2019
- venue: Nature
- doi: 10.1038/s41586-019-1724-z

Paper type:
- type: system

Evidence fields:
- signal_modality: Non-neural AI baseline: StarCraft II game-state observations and actions.
- input_modality: not specified
- task_taxonomy: Learn to play full StarCraft II at Grandmaster level using multi-agent reinforcement learning.
- paper_objective: Learn to play full StarCraft II at Grandmaster level using multi-agent reinforcement learning.
- method_family: Reinforcement learning/bandit
- method_summary: Reinforcement learning/bandit
- dataset: StarCraft II environment data, initialized from human player replays and improved through multi-agent self-play league training.
- dataset_role: used
- metric: Grandmaster league/MMR-style ranking and match performance against human players.
- metric_status: applicable
- limitations: Experimental scope is the StarCraft II game environment; the agent uses game observations/actions rather than real-world embodied sensory data.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41586-019-1724-z; https://storage.googleapis.com/deepmind-media/research/alphastar/AlphaStar_unformatted.pdf; https://www.nature.com/articles/s41586-019-1724-z
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=DeepMind PDF describes AlphaStar as a StarCraft II agent trained for professional esport play with multi-agent reinforcement learning. | confidence=medium
- limitations: evidence=The Nature article and DeepMind PDF define the evaluated domain as StarCraft II, a computer-game benchmark. | confidence=medium
- metric: evidence=The paper's central reported outcome is achieving Grandmaster level, the highest human player league. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Inputs are StarCraft II observations/actions, not biological signals. | confidence=high
- task_taxonomy: evidence=Title and abstract state the goal: Grandmaster-level StarCraft II using multi-agent reinforcement learning. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Grandmaster level in StarCraft II using multi-agent reinforcement learning
- auto_source_url: https://doi.org/10.1038/s41586-019-1724-z

### Grounded Language-Image Pre-training

Bibliographic:
- year: 2022
- venue: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
- doi: 10.1109/cvpr52688.2022.01069

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline: image-text/vision-language data.
- input_modality: image/video
- task_taxonomy: Representation alignment, Foundation model/pretraining
- paper_objective: Representation alignment, Foundation model/pretraining
- method_family: Masked autoencoder/pretraining
- method_summary: Masked autoencoder/pretraining
- dataset: 27M grounding data for pre-training, including 3M human-annotated and 24M web-crawled image-text pairs; evaluated on COCO, LVIS, and 13 downstream detection tasks.
- dataset_role: used
- metric: Average Precision (AP) for object detection/grounding transfer, including COCO and LVIS AP.
- metric_status: applicable
- limitations: The authors leave a detailed study of how GLIP scales with text-image data size to future work.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/cvpr52688.2022.01069; https://openaccess.thecvf.com/content/CVPR2022/html/Li_Grounded_Language-Image_Pre-Training_CVPR_2022_paper.html; https://openaccess.thecvf.com/content/CVPR2022/papers/Li_Grounded_Language-Image_Pre-Training_CVPR_2022_paper.pdf; https://arxiv.org/abs/2112.03857
- evidence_tier: tier1_paper_text
- confidence: high

Field evidence:
- dataset: evidence=CVF/arXiv abstract states GLIP is pre-trained on 27M grounding data: 3M human-annotated and 24M web-crawled image-text pairs. | confidence=high
- limitations: evidence=CVF paper conclusion states that GLIP shows promising zero-shot and fine-tuning results on established benchmarks and 13 downstream tasks, then explicitly leaves detailed study of scaling with text-image data size to future work. | confidence=high | tier=tier1_paper_text
- metric: evidence=CVF abstract reports 49.8 AP on COCO, 26.9 AP on LVIS, and 60.8/61.5 AP after COCO fine-tuning. | confidence=high
- record: confidence=high | tier=tier1_paper_text
- signal_modality: evidence=The paper unifies object detection and phrase grounding over images and language. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Grounded Language-Image Pre-training
- auto_source_url: https://doi.org/10.1109/cvpr52688.2022.01069

### Growing a Neural Network in Breadth, Depth, and Time

Bibliographic:
- year: 2026
- venue: arXiv (Cornell University)
- doi: 10.48550/arxiv.2605.25174

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline: image-classification datasets plus human behavioral reaction-time data, with no neural recording.
- input_modality: image/video
- task_taxonomy: Resource-constrained visual object recognition/classification while optimizing breadth, depth, and recurrent processing time.
- paper_objective: Resource-constrained visual object recognition/classification while optimizing breadth, depth, and recurrent processing time.
- method_family: CNN/RNN deep model
- method_summary: CNN/RNN deep model
- dataset: MNIST, CIFAR-10, Tiny ImageNet, and CIFAR-10H for human reaction-time/classification-distribution comparisons.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://www.semanticscholar.org/paper/be9b0e8ed3d5c9e34df278b0356ccb35fc83f479; https://arxiv.org/html/2605.25174v1; https://arxiv.org/abs/2605.25174
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=arXiv HTML states the experiments use CIFAR-10 as the main dataset, compare MNIST/CIFAR-10/Tiny ImageNet, and use CIFAR-10H for human reaction times. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The paper studies recurrent convolutional networks and human reaction-time correlations rather than EEG/fMRI/spikes. | confidence=high
- task_taxonomy: evidence=The abstract describes optimizing breadth, depth, and time costs jointly with task errors in a recurrent convolutional network. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Semantic Scholar strict title match
- auto_matched_title: Growing a Neural Network in Breadth, Depth, and Time
- auto_source_url: https://www.semanticscholar.org/paper/be9b0e8ed3d5c9e34df278b0356ccb35fc83f479

### HSI-GPT: A General-Purpose Large Scene-Motion-Language Model for Human Scene Interaction

Bibliographic:
- year: 2025
- venue: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
- doi: 10.1109/cvpr52734.2025.00670

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline
- input_modality: text/speech
- task_taxonomy: General-purpose scene-motion-language modeling for text-conditioned HSI generation, multi-modal controlled HSI generation, HSI captioning, and HSI completion.
- paper_objective: General-purpose scene-motion-language modeling for text-conditioned HSI generation, multi-modal controlled HSI generation, HSI captioning, and HSI completion.
- method_family: Large language model
- method_summary: Large language model
- dataset: HumanML3D and HUMANISE for human-scene interaction experiments; HUMANISE aligns 19.6K AMASS motion sequences with 643 ScanNet indoor scenes, with PROX discussed as related HSI data.
- dataset_role: used
- metric: FID, Multi-modal Distance, R-Precision, Diversity, Multi-Modality, Goal Distance, APD, Contact, Non-collision, BLEU, ROUGE, CIDEr, BERTScore, ADE, and FDE across tasks.
- metric_status: applicable
- limitations: In multi-modal controlled HSI generation, reduced APD/diversity is attributed to constrained trajectories and strict pre-defined pose adherence.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/cvpr52734.2025.00670; https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_HSI-GPT_A_General-Purpose_Large_Scene-Motion-Language_Model_for_Human_Scene_Interaction_CVPR_2025_paper.pdf; https://doi.org/10.1109/CVPR52734.2025.00670
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=CVPR PDF lines describe HUMANISE as 19.6K AMASS motion sequences aligned with 643 ScanNet scenes and report experiments on HumanML3D/HUMANISE. | confidence=high
- limitations: evidence=CVPR PDF states reduced diversity in APD is primarily due to constrained motion trajectories and strict pre-defined pose adherence. | confidence=medium
- metric: evidence=CVPR PDF metrics paragraph lists FID/MM Dist/R-Precision/Diversity/Multi-Modality, APD/contact/non-collision, BLEU/ROUGE/CIDEr/BERTScore, ADE/FDE. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- task_taxonomy: evidence=Abstract and experiments describe a general-purpose large scene-motion-language model supporting multiple HSI-related tasks. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: HSI-GPT: A General-Purpose Large Scene-Motion-Language Model for Human Scene Interaction
- auto_source_url: https://doi.org/10.1109/cvpr52734.2025.00670

### HiDe-PET: Continual Learning via Hierarchical Decomposition of Parameter-Efficient Tuning

Bibliographic:
- year: 2025
- venue: IEEE Transactions on Pattern Analysis and Machine Intelligence
- doi: 10.1109/tpami.2025.3562534

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline: image classification datasets for continual learning.
- input_modality: image/video
- task_taxonomy: Representation alignment, Continual/adaptive learning
- paper_objective: Representation alignment, Continual/adaptive learning
- method_family: Hierarchical Decomposition PET decomposes continual learning into within-task prediction, task-identity inference, and task-adaptive prediction, implemented with parameter-efficient tuning variants such as prompts/LoRA/adapters.
- method_summary: Hierarchical Decomposition PET decomposes continual learning into within-task prediction, task-identity inference, and task-adaptive prediction, implemented with parameter-efficient tuning variants such as prompts/LoRA/adapters.
- dataset: Split CIFAR-100, Split ImageNet-R, Split CUB-200, and Split Cars-196, each split into 10 disjoint class-incremental tasks.
- dataset_role: used
- metric: Final Average Accuracy (FAA) and Cumulative Average Accuracy (CAA).
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1109/tpami.2025.3562534; https://arxiv.org/pdf/2407.05229; https://www.computer.org/csdl/journal/tp/2025/08/10970405/260SjSC9R0k; https://doi.org/10.1109/TPAMI.2025.3562534
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=arXiv PDF benchmark section lists CIFAR-100, ImageNet-R, CUB-200, and Cars-196 split into 10 target tasks. | confidence=high
- method_summary: evidence=Abstract states the CL objective is decomposed into WTP, TII, and TAP and optimized by HiDe-PET. | confidence=high
- metric: evidence=Table 1 labels FAA (%) and CAA (%) as overall continual-learning performance metrics. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Benchmarks are image datasets; no neural measurements are used. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: HiDe-PET: Continual Learning via Hierarchical Decomposition of Parameter-Efficient Tuning
- auto_source_url: https://doi.org/10.1109/tpami.2025.3562534

### High-Resolution Image Reconstruction With Latent Diffusion Models From Human Brain Activity

Bibliographic:
- year: 2022
- venue: bioRxiv (Cold Spring Harbor Laboratory)
- doi: 10.1101/2022.11.18.517004

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Human 7T fMRI brain activity during visual perception.
- input_modality: fMRI
- task_taxonomy: Visual reconstruction
- paper_objective: Visual reconstruction
- method_family: Diffusion/generative model
- method_summary: Diffusion/generative model
- dataset: Natural Scenes Dataset (NSD), using 7T fMRI data from four subjects who completed all imaging sessions.
- dataset_role: used
- metric: Objective perceptual similarity/two-way identification metrics using CLIP and AlexNet layers, plus subjective human-rater identification.
- metric_status: applicable
- limitations: Experiments are per-subject and use four of the eight NSD subjects, with fMRI-to-LDM mappings fit by L2-regularized linear regression.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1101/2022.11.18.517004; https://openaccess.thecvf.com/content/CVPR2023/papers/Takagi_High-Resolution_Image_Reconstruction_With_Latent_Diffusion_Models_From_Human_Brain_CVPR_2023_paper.pdf; https://sites.google.com/view/stablediffusion-with-brain/; https://www.biorxiv.org/content/10.1101/2022.11.18.517004v2.full
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=CVPR PDF states the project used NSD, a 7T fMRI dataset, and analyzed four completed subjects. | confidence=high
- limitations: evidence=Methods state models were built per subject and estimated from training data; only four completed NSD subjects were analyzed. | confidence=medium
- metric: evidence=CVPR PDF says reconstruction was evaluated objectively with perceptual similarity metrics and subjectively by human raters, using CLIP and AlexNet layers. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Project page and paper state reconstruction from human brain activity obtained via fMRI. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: High-resolution image reconstruction with latent diffusion models from human brain activity
- auto_source_url: https://doi.org/10.1101/2022.11.18.517004

### High-performance brain-to-text communication via handwriting

Bibliographic:
- year: 2021
- venue: Nature
- doi: 10.1038/s41586-021-03506-2

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Intracortical motor-cortex microelectrode array recordings/spiking-threshold neural activity.
- input_modality: spiking/electrophysiology
- task_taxonomy: Neural decoding
- paper_objective: Neural decoding
- method_family: Intracortical BCI decoding attempted handwriting from motor-cortex activity in real time using a recurrent neural network and optional language-model/autocorrect post-processing.
- method_summary: Intracortical BCI decoding attempted handwriting from motor-cortex activity in real time using a recurrent neural network and optional language-model/autocorrect post-processing.
- dataset: Dryad dataset with all neural activity from the handwriting BCI experiments: 1,000 sentences, 43,501 characters, 10.7 hours, one participant, two 96-electrode microelectrode arrays in hand motor cortex.
- dataset_role: used
- metric: Typing speed, raw accuracy, character error rate, word error rate, and accuracy with autocorrect.
- metric_status: applicable
- limitations: The study was conducted in a single participant and was not yet a complete clinically viable system; future work aimed to test participants unable to speak and expand character sets.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41586-021-03506-2; https://www.nature.com/articles/s41586-021-03506-2; https://datadryad.org/dataset/doi:10.5061/dryad.wh70rxwmv; https://pmc.ncbi.nlm.nih.gov/articles/PMC8163299/; https://neuroscience.stanford.edu/news/composing-thoughts-mental-handwriting-produces-brain-activity-can-be-turned-text
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Dryad record describes 1,000 sentences, 43,501 characters over 10.7 hours, recorded with two 96-electrode arrays. | confidence=high
- limitations: evidence=PMC/search-accessible paper text notes single participant and not yet clinically viable; Stanford/HHMI coverage reports future testing and character-set expansion. | confidence=medium
- method_summary: evidence=Nature abstract says attempted handwriting movements were decoded from motor cortex and translated to text in real time using an RNN. | confidence=high
- metric: evidence=Nature abstract reports 90 characters per minute, 94.1% raw online accuracy, and >99% offline accuracy with autocorrect; PMC snippet reports CER/WER. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Dryad and Nature describe intracortical neural activity from microelectrode arrays in hand motor cortex. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: High-performance brain-to-text communication via handwriting
- auto_source_url: https://doi.org/10.1038/s41586-021-03506-2

### Highly accurate protein structure prediction for the human proteome

Bibliographic:
- year: 2021
- venue: Nature
- doi: 10.1038/s41586-021-03828-1

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline: protein amino-acid sequences and structural bioinformatics data.
- input_modality: protein sequence/structure
- task_taxonomy: Dataset/benchmark
- paper_objective: Dataset/benchmark
- method_family: AlphaFold2 proteome-scale prediction pipeline with MSA construction, template search, inference with five models, model ranking by mean pLDDT, and constrained relaxation.
- method_summary: AlphaFold2 proteome-scale prediction pipeline with MSA construction, template search, inference with five models, model ranking by mean pLDDT, and constrained relaxation.
- dataset: Human reference proteome sequences from UniProt release 2021_02; validation also used a recent PDB dataset filtered to post-training-cutoff structures.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: Proteome-scale prediction excluded sequences outside 16-2700 amino acids and sequences containing ambiguous residue codes; the 2700-residue ceiling was chosen to keep runtimes manageable.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41586-021-03828-1; https://www.nature.com/articles/s41586-021-03828-1; https://pubmed.ncbi.nlm.nih.gov/34293799/; https://alphafold.ebi.ac.uk/about
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Nature methods state human reference proteome sequences came from UniProt release 2021_02 and recent PDB structures were used for validation. | confidence=high
- limitations: evidence=Nature methods explicitly state length and residue-code exclusions and explain the length ceiling as a runtime-management choice. | confidence=high
- method_summary: evidence=Nature methods list the five-step AlphaFold prediction process and proteome-scale modifications. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The paper predicts protein structures from sequence/MSA/template data, not neural signals. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Highly accurate protein structure prediction for the human proteome
- auto_source_url: https://doi.org/10.1038/s41586-021-03828-1

### Highly accurate protein structure prediction with AlphaFold

Bibliographic:
- year: 2021
- venue: Nature
- doi: 10.1038/s41586-021-03819-2

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline: protein sequences, MSAs, templates, and experimentally determined structures.
- input_modality: protein sequence/structure
- task_taxonomy: Representation alignment, Dataset/benchmark
- paper_objective: Representation alignment, Dataset/benchmark
- method_family: AlphaFold2 neural network architecture using MSA and pair representations, Evoformer blocks, structure module, recycling, templates/MSAs, supervised PDB training plus self-distillation, and confidence-based model selection.
- method_summary: AlphaFold2 neural network architecture using MSA and pair representations, Evoformer blocks, structure module, recycling, templates/MSAs, supervised PDB training plus self-distillation, and confidence-based model selection.
- dataset: CASP14 targets, PDB training/evaluation data, and self-distillation data generated from about 350,000 diverse Uniclust30 sequences.
- dataset_role: used
- metric: accuracy
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/s41586-021-03819-2; https://www.nature.com/articles/s41586-021-03819-2
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: high

Field evidence:
- dataset: evidence=Nature article reports validation on CASP14, evaluation on recent PDB structures, supervised learning on PDB data, and self-distillation on about 350,000 Uniclust30 sequences. | confidence=high
- method_summary: evidence=Nature article describes the AlphaFold architecture, Evoformer blocks, recycling, five trained models, inference, and confidence scoring. | confidence=high
- record: confidence=high | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The inputs are protein sequence/structure bioinformatics data rather than biological neural recordings. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Highly accurate protein structure prediction with AlphaFold
- auto_source_url: https://doi.org/10.1038/s41586-021-03819-2

### Hippocampal place cells construct reward related sequences through unexplored space

Bibliographic:
- year: 2015
- venue: eLife
- doi: 10.7554/elife.06063

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Rodent hippocampal place-cell electrophysiology/spiking activity.
- input_modality: not specified
- task_taxonomy: Visual reconstruction, Representation alignment
- paper_objective: Visual reconstruction, Representation alignment
- method_family: Record place-cell firing during task/rest/exploration and decode/preplay hippocampal sequences representing future journeys through viewed but unexplored space.
- method_summary: Record place-cell firing during task/rest/exploration and decode/preplay hippocampal sequences representing future journeys through viewed but unexplored space.
- dataset: Rat hippocampal place-cell recordings during a T-shaped track task with inaccessible arms, reward placement, rest periods, and later exploration.
- dataset_role: used
- metric: Decoded probability/preplay analyses comparing the number and content of events for cued versus uncued arms.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.7554/elife.06063; https://elifesciences.org/articles/06063; https://elifesciences.org/articles/06063.pdf; https://doi.org/10.7554/eLife.06063
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=eLife summary states rats viewed inaccessible T-track arms, food was placed in one arm, and place-cell firing was recorded before and after exploration. | confidence=high
- method_summary: evidence=eLife summary describes place-cell patterns pre-activating journeys to and from the food-containing arm during rest. | confidence=high
- metric: evidence=eLife PDF/search text states the authors compared total number of events and preplay for cued versus uncued arms and used decoding probability matrices. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The article records firing of hippocampal place cells in rats. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Hippocampal place cells construct reward related sequences through unexplored space
- auto_source_url: https://doi.org/10.7554/elife.06063

### How to sample the world for understanding the visual system

Bibliographic:
- year: 2025
- venue: Proceedings of Cognitive Computational Neuroscience 2025
- doi: 10.32470/rfgh6r8

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Visual stimulus images plus functional MRI/neuroimaging analyses.
- input_modality: fMRI
- task_taxonomy: Visual reconstruction, Speech/language decoding, Representation alignment, Dataset/benchmark
- paper_objective: Visual reconstruction, Speech/language decoding, Representation alignment, Dataset/benchmark
- method_family: Contrastive learning
- method_summary: Contrastive learning
- dataset: LAION-natural, a curated subset of 120 million natural photographs filtered from LAION-2B, plus existing massive neuroimaging/fMRI datasets used for coverage and generalization analyses.
- dataset_role: used
- metric: CLIP-embedding visual-semantic coverage/representational gaps and out-of-distribution generalization in simulations and fMRI analyses.
- metric_status: applicable
- limitations: The authors state existing neuroimaging datasets cover only a restricted subset of LAION-natural visual-semantic space, causing impaired out-of-distribution generalization and limiting model comparison/generalizable inference.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.32470/rfgh6r8; https://openreview.net/forum?id=T9k6KkZoca; https://2025.ccneuro.org/poster-sessions/?view=all
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=OpenReview abstract introduces LAION-natural as 120M natural photographs filtered from LAION-2B and mentions fMRI data analyses. | confidence=high
- limitations: evidence=OpenReview abstract explicitly says existing datasets cover a restricted subset and highlights limitations in generalizability and model comparison. | confidence=high
- metric: evidence=OpenReview abstract describes analysis of CLIP embeddings, representational gaps, simulations, and fMRI out-of-distribution generalization. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The submission is about visual-system neuroimaging/fMRI datasets and natural-image stimuli. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: How to sample the world for understanding the visual system
- auto_source_url: https://doi.org/10.32470/rfgh6r8

### How to sample the world for understanding the visual system

Bibliographic:
- year: 2025
- venue: Proceedings of Cognitive Computational Neuroscience 2025
- doi: 10.32470/rfgh6r8

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Visual stimulus images plus functional MRI/neuroimaging analyses.
- input_modality: fMRI
- task_taxonomy: Visual reconstruction, Speech/language decoding, Representation alignment, Dataset/benchmark
- paper_objective: Visual reconstruction, Speech/language decoding, Representation alignment, Dataset/benchmark
- method_family: Contrastive learning
- method_summary: Contrastive learning
- dataset: LAION-natural, a curated subset of 120 million natural photographs filtered from LAION-2B, plus existing massive neuroimaging/fMRI datasets used for coverage and generalization analyses.
- dataset_role: used
- metric: CLIP-embedding visual-semantic coverage/representational gaps and out-of-distribution generalization in simulations and fMRI analyses.
- metric_status: applicable
- limitations: The authors state existing neuroimaging datasets cover only a restricted subset of LAION-natural visual-semantic space, causing impaired out-of-distribution generalization and limiting model comparison/generalizable inference.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.32470/rfgh6r8; https://openreview.net/forum?id=T9k6KkZoca; https://2025.ccneuro.org/poster-sessions/?view=all
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=OpenReview abstract introduces LAION-natural as 120M natural photographs filtered from LAION-2B and mentions fMRI data analyses. | confidence=high
- limitations: evidence=OpenReview abstract explicitly says existing datasets cover a restricted subset and highlights limitations in generalizability and model comparison. | confidence=high
- metric: evidence=OpenReview abstract describes analysis of CLIP embeddings, representational gaps, simulations, and fMRI out-of-distribution generalization. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The submission is about visual-system neuroimaging/fMRI datasets and natural-image stimuli. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: How to sample the world for understanding the visual system
- auto_source_url: https://doi.org/10.32470/rfgh6r8

### How to sample the world for understanding the visual system

Bibliographic:
- year: 2025
- venue: Proceedings of Cognitive Computational Neuroscience 2025
- doi: 10.32470/rfgh6r8

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Visual stimulus images plus functional MRI/neuroimaging analyses.
- input_modality: fMRI
- task_taxonomy: Visual reconstruction, Speech/language decoding, Representation alignment, Dataset/benchmark
- paper_objective: Visual reconstruction, Speech/language decoding, Representation alignment, Dataset/benchmark
- method_family: Contrastive learning
- method_summary: Contrastive learning
- dataset: LAION-natural, a curated subset of 120 million natural photographs filtered from LAION-2B, plus existing massive neuroimaging/fMRI datasets used for coverage and generalization analyses.
- dataset_role: used
- metric: CLIP-embedding visual-semantic coverage/representational gaps and out-of-distribution generalization in simulations and fMRI analyses.
- metric_status: applicable
- limitations: The authors state existing neuroimaging datasets cover only a restricted subset of LAION-natural visual-semantic space, causing impaired out-of-distribution generalization and limiting model comparison/generalizable inference.
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.32470/rfgh6r8; https://openreview.net/forum?id=T9k6KkZoca; https://2025.ccneuro.org/poster-sessions/?view=all
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=OpenReview abstract introduces LAION-natural as 120M natural photographs filtered from LAION-2B and mentions fMRI data analyses. | confidence=high
- limitations: evidence=OpenReview abstract explicitly says existing datasets cover a restricted subset and highlights limitations in generalizability and model comparison. | confidence=high
- metric: evidence=OpenReview abstract describes analysis of CLIP embeddings, representational gaps, simulations, and fMRI out-of-distribution generalization. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The submission is about visual-system neuroimaging/fMRI datasets and natural-image stimuli. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: How to sample the world for understanding the visual system
- auto_source_url: https://doi.org/10.32470/rfgh6r8

### Human-level control through deep reinforcement learning

Bibliographic:
- year: 2015
- venue: Nature
- doi: 10.1038/nature14236

Paper type:
- type: primary_research

Evidence fields:
- signal_modality: Non-neural AI baseline: Atari game pixels and reward/game-score signals.
- input_modality: not specified
- task_taxonomy: Learn control policies for many Atari 2600 games directly from high-dimensional sensory input using deep reinforcement learning.
- paper_objective: Learn control policies for many Atari 2600 games directly from high-dimensional sensory input using deep reinforcement learning.
- method_family: Reinforcement learning/bandit
- method_summary: Reinforcement learning/bandit
- dataset: Arcade Learning Environment / 49 classic Atari 2600 games.
- dataset_role: used
- metric: Game score normalized against professional human game-tester performance and prior algorithms.
- metric_status: applicable
- limitations: Experimental boundary is Atari 2600 game control from pixels and game score; the paper does not establish real-world robotic or neural-control performance.
- limitation_source: experimental_boundary

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1038/nature14236; https://www.nature.com/articles/nature14236
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=Nature page states the DQN was tested on 49 classic Atari 2600 games and references the Arcade Learning Environment. | confidence=high
- limitations: evidence=Nature abstract/page bounds inputs to pixels and game score in Atari games. | confidence=medium
- metric: evidence=Nature page states performance was comparable to an expert human player and surpassed previous algorithms across 49 games. | confidence=high
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=Inputs are game pixels and score, not neural data. | confidence=high
- task_taxonomy: evidence=Nature page describes a deep Q-network learning successful policies from high-dimensional sensory input with end-to-end RL. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Human-level control through deep reinforcement learning
- auto_source_url: https://doi.org/10.1038/nature14236

### Human2Robot: Learning Robot Actions from Paired Human-Robot Videos

Bibliographic:
- year: 2026
- venue: Proceedings of the AAAI Conference on Artificial Intelligence
- doi: 10.1609/aaai.v40i13.38086

Paper type:
- type: benchmark

Evidence fields:
- signal_modality: Non-neural AI baseline: paired human/robot videos and robot action trajectories.
- input_modality: image/video
- task_taxonomy: Representation alignment, Dataset/benchmark
- paper_objective: Representation alignment, Dataset/benchmark
- method_family: Two-stage Human2Robot framework: train a video prediction model to generate robot videos conditioned on human videos, then freeze it and train an action decoder using the VPM motion features to predict robot actions.
- method_summary: Two-stage Human2Robot framework: train a video prediction model to generate robot videos conditioned on human videos, then freeze it and train an action decoder using the VPM motion features to predict robot actions.
- dataset: H&R dataset: 2,600 paired human-robot video episodes, each 300-600 frames, with 4 basic task types and 6 long-horizon tasks collected via VR teleoperation.
- dataset_role: used
- metric: Multi-task and generalization success rates over real-world tasks; video-generation/action metrics include position and appearance comparisons.
- metric_status: applicable
- limitations: source-traced limitation/caveat sentence
- limitation_source: discussion

Verification:
- final_unresolved_fields: none
- verification_status: agent-source-traced
- evidence_sources: https://doi.org/10.1609/aaai.v40i13.38086; https://ojs.aaai.org/index.php/AAAI/article/view/38086/42048; https://arxiv.org/html/2502.16587v3
- evidence_tier: tier1_paper_text_or_trusted_public_source
- confidence: medium

Field evidence:
- dataset: evidence=AAAI/arXiv text states H&R contains 2,600 episodes, 300-600 frames per episode, covering 4 basic tasks and 6 long-horizon tasks. | confidence=high
- method_summary: evidence=AAAI/arXiv text describes the VPM stage and downstream action decoder stage. | confidence=high
- metric: evidence=AAAI/arXiv tables report multi-task and generalization success rates with 20 trials per task and discuss position/appearance metrics. | confidence=medium
- record: confidence=medium | tier=tier1_paper_text_or_trusted_public_source
- signal_modality: evidence=The paper learns from paired human and robot videos; no neural data are involved. | confidence=high

Identity trace:
- auto_verification_status: source-traced via Crossref strict title match
- auto_matched_title: Human2Robot: Learning Robot Actions from Paired Human-Robot Videos
- auto_source_url: https://doi.org/10.1609/aaai.v40i13.38086
