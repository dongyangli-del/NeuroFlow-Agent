# Statistics and Stop Rules

## Statistical Record

- Unit of analysis: subject, session, stimulus, trial, or run.
- Split protocol and seed.
- Metric definition.
- Confidence interval or variance estimate.
- Multiple comparison handling when relevant.
- Noise ceiling or human/repetition reliability when available.

## Stop Rules

Stop or pause runs when:

- Output scale is implausible.
- Evaluator cannot reproduce a known baseline.
- Data split or target alignment is uncertain.
- New runs write into stale output directories.
- Training loss is low but task metric collapses.

Treat surprising results as bugs until the protocol checks pass.
