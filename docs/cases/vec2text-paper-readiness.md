# Vec2Text Paper Readiness Demo

This case study shows how NeuroFlow should package a complex AI x brain research project for paper-facing review without turning the workflow into an automatic paper factory.

## Source Artifacts

The demo is distilled from an inspected `vec2text` research workspace. The public NeuroFlow repository keeps only this summary, not the full paper directory, raw experiment outputs, local paths, datasets, checkpoints, or LaTeX build products.

Example paper artifact: [vec2text-paper-demo.pdf](assets/vec2text-paper-demo.pdf).

The PDF is included as a compact paper artifact showing the type of submission package NeuroFlow audits. It should be read together with the readiness, reproduction, and claim-boundary summary below. It is not presented as evidence that NeuroFlow automatically generated a complete paper.

Inspected source artifact types:

- Paper draft and compiled PDF.
- PDF compile report.
- AAAI-style submission readiness audit.
- External SOTA reproduction audit.
- Reproducibility checklist.
- Claim-support, split-leakage, ablation, route-switch, and baseline-matrix artifacts.

Verification status: source-traced from inspected project artifacts.

## User Task

```text
Prepare this EEG-to-language project as a reviewer-facing paper package.
Check whether the paper claims, SOTA positioning, ablations, reproducibility,
and PDF readiness are safe enough for a submission-style demo.
```

## Naive AutoResearch Risk

A generic agent could make the project look stronger by polishing the abstract, expanding related work, or describing the result as open-ended brain-to-text reconstruction. That would hide the important scientific boundary: the inspected artifacts support a visual EEG-to-language semantic bottleneck audit, not unrestricted sentence reconstruction.

## NeuroFlow Route

```text
neuro-orchestrator
-> paper-rag-plus
-> repro-pack
-> experiment-copilot
-> reviewer-simulator
-> oral-writer
```

Primary artifact: paper readiness package.

Evidence gates:

- Claim-evidence consistency.
- Protocol and SOTA comparability.
- Split leakage and candidate-bank declaration.
- External-code reproduction status.
- Negative and no-gain ablation handling.
- PDF compile status.
- Reviewer-risk and remaining-goal boundary.

## What NeuroFlow Should Produce

### Claim Boundary

Allowed framing:

- The project is a visual EEG-to-language semantic evidence audit.
- Semantic Prototype Stabilization is presented as a leakage-controlled protocol.
- Closed candidate-bank retrieval is a rank diagnostic, not deployable reconstruction.
- No-test-target memory retrieval is constrained semantic-neighbor verbalization, not exact held-out sentence recovery.

Blocked framing:

- Public-SOTA EEG-to-text superiority.
- Unrestricted generated-sentence reconstruction.
- Direct metric comparison against language-evoked EEG-to-text systems with incompatible protocols.
- Treating visual retrieval top-k as generated text quality.

### Evidence Map

| Evidence area | Demo artifact | Reviewer-facing role |
|---|---|---|
| Paper compile | PDF compile report | Confirms the paper artifact is buildable and page-bounded. |
| Claim support | Reviewer claim-support audit | Maps headline claims to inspected evidence and safer wording. |
| SOTA positioning | Protocol comparison and cross-metric alignment artifacts | Separates same-protocol evidence from task-adjacent context. |
| Reproduction | External SOTA reproduction audit | Records checked repos, commits, dependency status, and runnable gates. |
| Benchmark validity | Split-leakage and candidate-bank audits | Prevents closed-set retrieval from being overclaimed as deployment. |
| Ablation coverage | Ablation evidence matrix | Keeps negative, no-gain, marginal, and tradeoff results visible. |
| Readiness | Submission readiness audit | Summarizes blockers, mitigations, and remaining reviewer risks. |

### Example Findings

- Detailed caption supervision can fail even when text inversion works; the bottleneck is EEG-to-language alignment and target granularity.
- A reproduced visual EEG decoder can be useful as a semantic bridge, but visual retrieval evidence is not the same as generated-sentence evidence.
- Several post-hoc repair routes are explicitly rejected or marked as bounded tradeoffs, which prevents the paper from overclaiming.
- The remaining final-goal gap is a real same-protocol auditory or reading sentence EEG benchmark with proper nulls and alignment checks.

## Final Demo Judgment

This is a strong NeuroFlow demo because the workflow makes the paper safer rather than louder. The value is not that an agent generated a complete paper; the value is that the agent produced an auditable paper readiness package with explicit claim scope, reproduction status, negative evidence, and reviewer-facing limitations.

Recommended public title:

```text
Paper Readiness Demo: Evidence-Gated EEG-to-Language Submission Package
```

Do not present this demo as:

```text
Fully automatic paper generation
```

or:

```text
AI-written EEG-to-text SOTA paper
```

## Reusable Lesson

For paper demos, NeuroFlow should expose the artifacts that make a claim defensible:

```markdown
Claim:
Evidence source:
Protocol boundary:
Reproduction status:
Negative evidence:
Reviewer risk:
Final allowed wording:
Remaining blocker:
```

Polished paper text is only acceptable after those fields are inspected.
