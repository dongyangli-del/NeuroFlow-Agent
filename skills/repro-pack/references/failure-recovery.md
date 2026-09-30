# Failure Recovery

## Environment Failures

- Identify Python, CUDA, PyTorch, and package manager constraints from inspected files.
- Prefer the repository's documented setup before inventing a new environment.
- Record incompatible dependencies instead of silently upgrading core libraries.

## Data Failures

- Distinguish unavailable, gated, corrupted, mislocated, and wrong-version datasets.
- Confirm expected directory structure before changing code.
- Use tiny smoke inputs only when full data is not needed for a sanity check.

## Weight Failures

- Verify checkpoint path, architecture compatibility, and expected key names.
- Separate pretrained backbone weights from task-specific checkpoints.
- Do not fabricate download links.

## Metric Failures

- Confirm evaluator input format, split protocol, target normalization, and aggregation.
- Check whether reported metrics require multiple seeds or repeated sampling.
- Treat large gaps from the paper as possible protocol mismatch until checked.
