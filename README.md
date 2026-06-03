# Codex AI x BCI Research Skill

<p align="center">
  <b>The Codex Skill for rigorous AI x BCI research</b><br>
  Research memory, debugging playbooks, and reviewer-facing workflows for EEG decoding, neural reconstruction, brain-language alignment, and closed-loop NeuroAI.
</p>

<p align="center">
  <a href="README_CN.md">中文</a> | <a href="docs/WORKFLOWS.md">Workflows</a> | <a href="docs/PLAYBOOKS.md">Playbooks</a> | <a href="docs/EXAMPLES.md">Examples</a> | <a href="docs/VALIDATION.md">Validation</a>
</p>

<p align="center">
  <img alt="Codex skill" src="https://img.shields.io/badge/Codex-Skill-111827">
  <img alt="Domain" src="https://img.shields.io/badge/Domain-AI%20x%20BCI-2563eb">
  <img alt="Focus" src="https://img.shields.io/badge/Focus-EEG%20%7C%20NeuroAI%20%7C%20Diffusion-7c3aed">
  <img alt="Validation" src="https://img.shields.io/badge/Validation-make%20validate-16a34a">
</p>

---

## What It Is

`ai-bci-research` is a specialized Codex skill that turns an agent into a more reliable collaborator for AI x brain-computer interface research.

It is not a generic neuroscience note dump. It is an opinionated operating layer for fragile research work where split leakage, target normalization, feature alignment, stochastic generation, and reviewer-facing claims can silently break conclusions.

| Use it for | What the skill makes the agent do |
|---|---|
| EEG diffusion/debugging | Check scale, sampling variance, condition use, train/val/test localization, and evaluator parity before blaming model capacity. |
| Neural decoding/reconstruction | Audit splits, repetition handling, stimulus identity, baselines, metrics, and noise ceilings. |
| Paper writing/rebuttal | Convert claims into reviewer-facing, evidence-scoped scientific writing. |
| Experiment memory | Distill raw logs into dated findings, playbooks, acceptance criteria, and next probes. |
| Closed-loop BCI planning | Separate offline replay from online claims and surface safety, calibration, latency, and controls. |

## Quick Start

Install with the Codex skill installer:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo dongyangli-del/codex-ai-bci-research-skill \
  --path skills/ai-bci-research
```

Or install manually:

```bash
git clone https://github.com/dongyangli-del/codex-ai-bci-research-skill.git
cd codex-ai-bci-research-skill
bash install.sh
```

Restart Codex after installation.

Then ask Codex with the skill name:

```text
Use ai-bci-research to debug why my EEG diffusion model is far below the linear baseline.
```

```text
Use ai-bci-research to design ablations for an EEG-guided visual reconstruction paper.
```

```text
Use ai-bci-research to turn these experiment logs into reviewer-facing claims and limitations.
```

## The BCI-RIGOR Loop

The core workflow is `BCI-RIGOR`: a repeatable loop for research-grade AI x BCI work.

```mermaid
flowchart LR
    A[Inspect repo and artifacts] --> B[Verify data, split, target, metric]
    B --> C[Reproduce strongest baseline]
    C --> D[Audit leakage, scale, alignment, routing]
    D --> E[Localize with probes and ablations]
    E --> F[Write dated finding and next action]
    F --> G[Produce code, paper text, or experiment plan]
```

This loop is intentionally conservative: surprising results are treated as possible protocol or implementation bugs until the checks are exhausted.

## Why AI x BCI Needs a Skill

General-purpose agents often miss domain-specific failure modes:

- EEG repetitions, session splits, subject splits, and stimulus identities can leak silently.
- DNN features and EEG targets can be off by one image, layer, token format, or split order.
- Generated EEG can have plausible correlation but broken explained variance due to scale errors.
- Epsilon diffusion can learn denoising shortcuts while weakly using image-specific condition tokens.
- Reconstruction and closed-loop papers require precise claim boundaries and reviewer-ready baselines.

This skill packages those guardrails so future sessions begin with the right defaults.

## Architecture

```mermaid
flowchart TD
    P[User prompt] --> S[SKILL.md routing]
    S --> R[Relevant reference]
    R --> W[Workflow or playbook]
    W --> T[Scripts and validation]
    T --> O[Grounded output]

    R --> RP[research-profile.md]
    R --> BW[bci-workflows.md]
    R --> DP[debugging-playbooks.md]
    R --> EF[experiment-findings.md]
    R --> RO[reviewer-objections.md]
```

The design uses progressive disclosure: `SKILL.md` stays compact, and detailed knowledge lives in references that are loaded only when needed.

## Repository Layout

```text
skills/ai-bci-research/
├── SKILL.md                         # compact routing and operating workflow
├── agents/openai.yaml               # UI metadata
├── evals/evals.json                 # behavior checks for the skill
├── references/
│   ├── research-profile.md          # mission, scope, and guardrails
│   ├── bci-workflows.md             # decoding/reconstruction/closed-loop checklists
│   ├── debugging-playbooks.md       # reusable failure-mode diagnostics
│   ├── experiment-findings.md       # compact dated experiment conclusions
│   ├── experiment-log-template.md   # reproducibility template
│   ├── papers-index.md              # user paper map and positioning
│   ├── repositories.md              # local/public repo memory
│   ├── reviewer-objections.md       # review risk and rebuttal patterns
│   ├── venue-workflows.md           # conference workflow guidance
│   ├── writing-style.md             # preferred scientific style
│   └── knowledge-index.md           # generated reference index
└── scripts/
    ├── repo_inventory.py
    └── update_knowledge_index.py
```

Project-level docs:

| File | Purpose |
|---|---|
| [docs/WORKFLOWS.md](docs/WORKFLOWS.md) | Named research loops and operating procedures. |
| [docs/PLAYBOOKS.md](docs/PLAYBOOKS.md) | Catalog of detailed references and when to load them. |
| [docs/EXAMPLES.md](docs/EXAMPLES.md) | Demo-case template and planned real examples. |
| [docs/VALIDATION.md](docs/VALIDATION.md) | Local checks and validation expectations. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Rules for adding durable skill memory. |
| [README_CN.md](README_CN.md) | Chinese project overview. |

## Current Playbooks

| Playbook | When it matters |
|---|---|
| EEG diffusion underperforms regression | Generated EEG has wrong scale or collapses despite low denoising loss. |
| Output directory routing bug | Fixed experiments accidentally write to stale directories. |
| EEG diffusion vs linear baseline large gap | Need to separate evaluator bugs, sampling variance, condition use, and architecture issues. |
| Conditional EEG diffusion objective mismatch | Epsilon DDPM weakly uses image condition; x0/direct predictors become the next required probe. |

## Validation

Run local validation before committing changes:

```bash
make validate
```

The validator checks required files, `SKILL.md` frontmatter, eval JSON syntax, local Markdown links, and accidental large files.

When reference files change, rebuild the compact index:

```bash
make index
make validate
```

A GitHub Actions workflow template is provided at [docs/ci-validate.yml](docs/ci-validate.yml). Copy it to `.github/workflows/validate.yml` when pushing with a token that has GitHub `workflow` scope.

## Demo Cases

Real demos should come from inspected artifacts or user-approved summaries. They are intentionally not fabricated here.

Planned demo slots:

- EEG diffusion scale/normalization failure.
- EEG diffusion objective mismatch and weak condition use.
- Reviewer-facing paper audit for leakage, baselines, and metric validity.

Use [docs/EXAMPLES.md](docs/EXAMPLES.md) to add a demo once the underlying artifact is ready.

## Update Workflow

After adding papers, repository notes, datasets, or experiment findings:

```bash
cd codex-ai-bci-research-skill/skills/ai-bci-research
python3 scripts/update_knowledge_index.py --root .
cd ../..
make validate
```

Keep raw logs, checkpoints, private data, and large generated outputs outside this repository.

## Roadmap

- Add real, inspected demo cases for EEG diffusion debugging and paper audit workflows.
- Expand eval prompts for experiment debugging, rebuttal, and closed-loop BCI planning.
- Add schema checks for `agents/openai.yaml` and eval structure.
- Publish a compact technical note explaining why AI x BCI agents need domain-specific guardrails.
- Keep the project narrow and deep: the best Codex skill for AI x BCI research.

## Quality Bar

A change improves the project only if it makes future agents more reliable. Prefer concise playbooks, dated findings, explicit acceptance criteria, verified project facts, and eval prompts over broad notes or invented examples.
