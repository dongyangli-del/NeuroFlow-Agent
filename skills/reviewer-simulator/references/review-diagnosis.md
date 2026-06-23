# Review Diagnosis

Use this reference to distinguish scientific defects from writing defects and to decide whether a paper weakness is repairable before a submission or rebuttal.

## Diagnosis Order

For each major weakness, classify it in this order:

1. **Claim affected**: the exact claim, table, figure, section, or contribution at risk.
2. **Evidence status**: supported, partially supported, missing, invalid, or unverified.
3. **Root cause**: why the weakness exists.
4. **Defect type**: method defect, experiment defect, analysis defect, reproducibility defect, citation defect, or presentation defect.
5. **Fixability**: what level of work is needed to reduce risk.
6. **Reviewer consequence**: likely score impact and the attack surface in review or rebuttal.

## Root-Cause Classes

| Root cause | Meaning | Typical repair |
|---|---|---|
| `invalid-assumption` | The paper relies on a premise that is false, untested, or incompatible with the protocol. | Narrow the claim, redesign the protocol, or add a direct validity check. |
| `missing-evidence` | The claim may be true but the paper lacks the required experiment, citation, proof, or analysis. | Add the specific evidence or mark the claim as hypothesis/limitation. |
| `unfair-comparison` | Baselines, splits, model capacity, tuning budget, data access, or metric definitions are not comparable. | Re-run or document parity checks; downgrade claims until parity is established. |
| `analysis-gap` | Results exist but do not isolate the mechanism, failure mode, variance, or robustness needed by the claim. | Add ablations, uncertainty, error analysis, subgroup analysis, or sensitivity checks. |
| `reproducibility-gap` | The reader cannot reproduce the result from the described data, code, environment, seeds, or checkpoints. | Add commands, configs, seeds, data access, expected outputs, and smoke tests. |
| `citation-gap` | Novelty or factual positioning depends on unverified or missing prior work. | Use `paper-rag-plus`; add verified citations or mark as citation-needed. |
| `presentation-gap` | The evidence may be adequate, but the writing, figure order, terminology, or limitation framing hides it. | Rewrite framing, align figures/tables to claims, and make limitations explicit. |

## Defect Type Gate

Do not recommend language polish until the defect type is clear.

| Defect type | Reviewer interpretation | Safe action |
|---|---|---|
| `method-defect` | The method cannot support the stated capability under the claimed setting. | Narrow the claim or add a new method/protocol; rebuttal alone is usually weak. |
| `experiment-defect` | The method might work, but the evaluation is incomplete, unfair, or invalid. | Add targeted experiments, parity checks, or validity controls. |
| `analysis-defect` | The main numbers exist but the mechanism or boundary is unclear. | Add ablation, uncertainty, error analysis, or sensitivity analysis. |
| `reproducibility-defect` | The result may be correct but cannot be checked. | Add implementation details, configs, release plan, and smoke-run evidence. |
| `citation-defect` | Novelty or factual claims are not grounded. | Verify closest prior work before claiming novelty. |
| `presentation-defect` | The evidence is present but the narrative obscures it. | Rewrite claims, captions, limitations, and contribution framing. |

## Fixability Scale

| Fixability | Meaning | Rebuttal/submission action |
|---|---|---|
| `quick-revision` | Can be fixed with wording, caption, limitation, table clarification, or citation verification. | Patch text and explicitly point reviewers to the corrected location. |
| `feasible-extra-experiment` | Can be addressed with a small controlled run, ablation, seed sweep, or analysis using existing data. | Run it if time allows; otherwise narrow the claim and state it as future work. |
| `major-new-evidence` | Requires new dataset, new baseline family, human study, online experiment, or full rerun. | Do not overpromise; decide whether to delay submission or scope down. |
| `structural-method-risk` | The current method or protocol cannot support the main claim. | Reframe the paper around a weaker valid contribution or redesign the work. |

## Required Output Block

For each critical or major issue, include:

```markdown
Issue:
Affected claim:
Root cause:
Defect type:
Fixability:
Reviewer consequence:
Best repair:
Safer wording:
```

## Common Misclassifications

- Missing cross-subject evaluation is not a writing issue when the claim is cross-subject generalization.
- A vague contribution statement is a presentation issue only if the experiments already support the actual contribution.
- Offline evidence cannot be repaired into an online closed-loop claim by wording alone.
- Missing variance is an analysis defect; claiming significance without variance is also a claim-calibration defect.
- A missing closest-prior-work comparison is both a citation defect and a novelty-risk issue.
