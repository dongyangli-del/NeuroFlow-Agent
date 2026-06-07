# Modality Opportunity Map

Use this map to force ideas through a concrete modality and task axis.

| Modality | Opportunity axis | Non-skippable risk |
|---|---|---|
| EEG | low-cost visual, language, auditory, attention, or closed-loop decoding | split leakage, repetition leakage, low SNR, subject transfer |
| iEEG | high temporal and spatial precision for speech, motor, and semantic decoding | small cohorts, electrode coverage, patient-specific anatomy |
| fMRI | spatially detailed perception and semantic reconstruction | low temporal resolution, stimulus leakage, subject-specific mapping |
| MEG | higher-quality non-invasive temporal decoding | access cost, preprocessing complexity, dataset scarcity |
| LFP | population dynamics, motor control, closed-loop adaptation | invasive setting, session drift, online safety |
| Spike | fine-grained motor, speech, and population dynamics modeling | context shifts, unit instability, small data |

## Idea Axes

- Data axis: new pairing, split, augmentation, benchmark, or modality bridge.
- Objective axis: contrastive, generative, predictive, reconstruction, control, or continual adaptation.
- Model axis: foundation encoder, adapter, world model, diffusion, autoregressive model, or state-space model.
- Evaluation axis: stronger baseline, robustness, leakage audit, online/offline gap, or noise ceiling.
- Interaction axis: closed-loop update, user personalization, calibration, or safety constraints.
