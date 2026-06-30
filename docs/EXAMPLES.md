# Examples

This file is intentionally lightweight until real demo cases are added. Do not invent results or anonymized logs. Add examples only when they come from an inspected project artifact or a user-approved summary.

## Example Template

```text
Title:
Task prompt:
Project context:
Agent workflow used:
Key checks performed:
Bug or risk found:
Action taken:
Outcome:
Reusable lesson:
Files or references updated:
```

## Inspected Demo Cases

- [Vec2Text paper readiness package](cases/vec2text-paper-readiness.md): evidence-gated EEG-to-language paper demo distilled from inspected paper, compile, readiness, reproduction, and reviewer-risk artifacts.

## Planned Demo Cases

- EEG diffusion scale/normalization failure: generated EEG variance explodes despite low denoising loss.
- EEG diffusion objective mismatch: epsilon DDPM weakly uses image condition; direct or x0 predictor becomes the next required probe.
- Reviewer-facing paper audit: claims are narrowed after baseline, leakage, and metric checks.

Each demo should show how the skill changes agent behavior, not just the final answer.
