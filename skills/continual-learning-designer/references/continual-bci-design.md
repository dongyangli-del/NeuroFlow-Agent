# Continual BCI Design

## Required Design Axes

| Axis | Questions |
|---|---|
| Shift | Is the shift across subject, session, device, task, stimulus, label space, or environment? |
| Stream | What arrives sequentially, and in what order? |
| Feedback | Are labels, rewards, corrections, or implicit signals available? |
| Memory | What raw samples, features, prototypes, adapters, or summaries can be stored? |
| Update | Is adaptation batch, streaming, test-time, replay-based, regularized, adapter-based, or meta-learned? |
| Deployment | Is this offline replay, simulated online, or true online human-subject interaction? |

## Baseline Families

- Frozen model with no adaptation.
- Subject/session-specific fine-tuning.
- Replay or exemplar memory.
- Regularization against previous solution.
- Adapter, LoRA, prompt, or normalization adaptation.
- Test-time adaptation without labels.
- Meta-learning or initialization-based adaptation.

Choose baselines that match the available feedback and deployment setting.
