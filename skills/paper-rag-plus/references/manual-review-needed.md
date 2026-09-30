# Manual Review Needed

Schema version: structured-manual-review-v1

This report uses the structured Paper-RAG++ review schema. It separates bibliographic facts, paper type, evidence fields, and final verification state so review/perspective papers can be closed with explicit `not_applicable` statuses instead of ambiguous unresolved fields.

## Summary

- entries: 6
- entries with final unresolved fields: 6
- unresolved doi: 4
- unresolved limitations: 2
- paper types: benchmark=1, primary_research=5

## Schema

Bibliographic: year, venue, doi.
Paper type: primary_research | review | perspective | theory | benchmark | dataset | system.
Evidence fields: signal_modality, input_modality, task_taxonomy, paper_objective, method_family, method_summary, dataset, dataset_role, metric, metric_status, limitations, limitation_source.
Verification: final_unresolved_fields, verification_status, evidence_sources, evidence_tier, confidence.

## Priority Entries

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
