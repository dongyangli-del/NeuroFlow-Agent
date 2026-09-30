# Review Rubric

## Scoring Dimensions

- Novelty.
- Technical soundness.
- Neuro validity.
- Dataset and split validity.
- Baseline fairness.
- Metric validity.
- Claim calibration.
- Reproducibility.
- Ethics and safety.
- Writing clarity.

## Blocking Issues

- Leakage or invalid splits.
- Weak or unfair baselines.
- Unsupported broad claims.
- Qualitative-only reconstruction evidence.
- Online closed-loop claims from offline data.
- Missing implementation details.
- Unclear participant, session, or stimulus protocol.

## Pre-Submission Severity Gate

Classify issues before recommending polish:

- **Blocking**: invalid split, leakage, missing baseline, unsupported main claim, fabricated or unverified citation, unavailable data required by the claim, online claim from offline evidence, privacy or IRB risk.
- **Major**: weak ablation, unclear metric, incomplete reproducibility, mismatched figure/story, vague contribution, overbroad novelty, missing limitation.
- **Minor**: wording, formatting, grammar, caption polish, citation style, small LaTeX issues.

Review in this order:

1. logic chain and claim support;
2. experiment and benchmark validity;
3. figure and table evidence;
4. writing clarity and scoped claims;
5. reproducibility, ethics, safety, and data governance.

Do not let minor language polish hide blocking scientific issues.
