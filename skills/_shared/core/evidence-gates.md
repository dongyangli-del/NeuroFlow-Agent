# Evidence Gates

Use these gates before turning NeuroFlow work into claims, experiments, figures, or persistent memory.

## Novelty

- Identify the closest inspected prior work or mark the novelty as unverified.
- Separate a new task setting, new method mechanism, new benchmark protocol, and new empirical finding.
- Do not convert an intuition into a contribution unless the supporting evidence is named.
- Record source location and verification status for closest-prior-work facts.

## Benchmark

- Verify access route, license or use restrictions, modality, subject/session structure, split protocol, metric, and strongest baseline.
- Mark unknown fields as `needs verification`.
- Check leakage through subject, session, stimulus, repetition, preprocessing, target representation, or temporal adjacency.
- List missing information and deviations from convention before recommending use.

## Experiment

- Match train/validation/test protocol, preprocessing, metric, and evaluator across baselines and proposed methods.
- Define must-run baselines, ablations, negative controls, robustness checks, and stop rules.
- Treat surprising improvements or collapses as possible protocol bugs until ruled out.
- Trace numerical parameters to a paper, config, log, dataset page, or user-validated source.

## Reproduction

- Name environment, data, weights, commands, expected output, smoke test, and failure recovery path.
- Prefer the smallest runnable path before refactoring or extending code.
- Do not claim reproducibility if data, weights, or expected outputs are missing.
- Separate source-traced instructions from reproduced outputs.

## Closed Loop

- Separate offline replay, simulated interaction, and online human-subject claims.
- State calibration, latency, safety constraints, fatigue handling, sham or random controls, and stop criteria.

## Memory

- Persist only reusable behavior-changing lessons.
- Route private notes, raw logs, unpublished results, credentials, and human-subject details outside public skill files.
