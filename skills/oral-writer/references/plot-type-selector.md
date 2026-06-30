# Plot Type Selector

Use this reference when selecting a figure type for AI x brain, BCI, NeuroAI, or paper-result visualization.

## Selection Rule

Choose the simplest plot that matches the comparison structure and the claim. If the intended claim needs variance, repeated subjects, or a protocol boundary, the plot must show it or the caption must state it.

## Recommended Plot Types

| Result structure | Preferred plot | Use when | Required caveat |
|---|---|---|---|
| Few methods on one metric | Bar chart or dot plot with error bars | Comparing primary accuracy, F1, AUC, MAE, or correlation. | Show variance if available; otherwise avoid significance language. |
| Many methods or long labels | Horizontal bar chart | Baseline comparisons with long method names. | Group only comparable protocols. |
| Accuracy over subjects/sessions | Paired line plot, subject-level dot plot, or small multiples | Showing cross-subject/session variability or calibration effects. | Do not average away subject/session instability. |
| Metric over calibration rounds/time | Line plot with confidence band | Online adaptation, continual learning, or calibration curves. | State whether data are online, simulated, or replayed offline. |
| Accuracy vs latency/compute | Pareto plot | Speed-accuracy, parameter-performance, or deployment tradeoff. | Include units and comparable hardware/protocol. |
| Ablation of components | Grouped bar chart or slope chart | Showing contribution of modules, losses, or inputs. | The ablation must isolate the claimed mechanism. |
| Multiple metrics per method | Small multiples or metric table | Accuracy, latency, parameters, calibration time, and robustness jointly matter. | Avoid radar charts unless all axes are comparable and normalized. |
| Confusion across classes/states | Confusion matrix | Class-level decoding or cognitive-state recognition. | Include class balance or chance baseline if relevant. |
| Reconstruction examples | Paired examples plus quantitative panel | Showing qualitative neural reconstruction outputs. | Pair with metric and control; examples alone are not evidence. |
| Error/failure cases | Stratified examples or subgroup plot | Explaining where the method fails. | Mark as error analysis, not main performance proof. |

## Caption Gate

Every recommended plot should come with:

```markdown
Plot type:
What comparison it supports:
Metric direction:
Protocol boundary:
Required uncertainty or control:
Caption seed:
```

## Avoid

- Decorative radar charts when one clear table or small multiple would be easier to read.
- 3D plots for ordinary metric comparisons.
- Averaged bars without subject/session visibility when personalization or generalization is the claim.
- Qualitative-only figures for strong decoding, reconstruction, or closed-loop claims.
