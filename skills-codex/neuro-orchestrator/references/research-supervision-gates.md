# Research Supervision Gates

This is the Codex-facing summary of NeuroFlow's advisor-style supervision gates. It is an original abstraction inspired by HKUSTDial/Supervisor-Skills, not a copy of its CC BY-NC-SA 4.0 text.

Source for inspiration: https://github.com/HKUSTDial/Supervisor-Skills

## Gates

1. **Idea Commitment**: a project needs a falsifiable hypothesis, task mode, data path, strongest baseline, cheap kill test, reviewer objection, and capability fit check before implementation.
2. **Paper Logic Chain**: research setting -> closest limitation -> key principle or goal -> challenges -> method or experiment choices -> evidence -> contributions. If this chain breaks, fix the science before prose.
3. **Benchmark Substance**: a benchmark must define a measurement gap, construction path, quality control, evaluation taxonomy, baseline suite, empirical findings, and data governance.
4. **Figure Narrative**: every main figure needs one job, a caption takeaway, claim-panel mapping, readable design, honest axes, and no decorative complexity that hides evidence.
5. **Pre-Submission Review**: classify issues as Blocking, Major, or Minor across logic, evidence, figures, writing, reproducibility, ethics, and safety.
6. **AI-Assisted Research Integrity**: AI may accelerate code, figures, polish, organization, and review; the researcher owns novelty, experiment design, facts, citations, interpretation, and disclosure.

## Routing

| Pipeline chain | Required supervision gates |
|---|---|
| idea-to-experiment | Idea Commitment, Paper Logic Chain |
| paper-to-repro | Paper Logic Chain, Pre-Submission Review, AI-Assisted Research Integrity |
| benchmark-to-baseline | Benchmark Substance, Figure Narrative, Pre-Submission Review |
| continual-adaptation | Idea Commitment, Benchmark Substance, AI-Assisted Research Integrity |
| experiment-to-paper | Paper Logic Chain, Figure Narrative, Pre-Submission Review |
| paper-to-rebuttal | Paper Logic Chain, Pre-Submission Review |
| session-to-memory | AI-Assisted Research Integrity plus privacy review |
