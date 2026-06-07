# Continual Evaluation Protocol

## Metrics

- Current-task performance.
- Average performance across seen subjects, sessions, or tasks.
- Forgetting or backward transfer.
- Forward transfer to new subjects, sessions, or tasks.
- Calibration time or number of labeled samples.
- Update compute, latency, and memory footprint.
- Safety or failure-rate metric for online settings.

## Protocol Checks

- Keep adaptation data separate from final test data unless the protocol explicitly allows online test-time updates.
- Report stream order and seeds.
- Use identical preprocessing across baseline and proposed method.
- Evaluate no-adaptation and simple adaptation baselines.
- Separate offline replay claims from real-time BCI claims.

## Reviewer Risks

- Hidden test-time supervision.
- Reporting only final performance without forgetting.
- Ignoring calibration cost.
- Comparing methods under different memory budgets.
- Claiming deployment readiness without latency or safety evidence.
