<div align="center">
  <a href="https://github.com/dongyangli-del/NeuroFlow-Agent">
    <img src="docs/NeuroFlow_logo.png" alt="NeuroFlow Agent" width="450">
  </a>

  <p>
    <b>A domain-knowledge-correct AutoResearch and human-in-the-loop workflow agent for ML x BCI x neuroscience.</b><br>
    NeuroFlow-Agent distills lessons from strong general skill libraries, research workflows, and real project failures into a conference-grade skill library, domain knowledge base, and self-evolving index graph.
  </p>

  <p>
    <a href="docs/EVOLUTION.md"><img alt="Self-evolving" src="https://img.shields.io/badge/system-self--evolving-0f766e"></a>
    <a href="docs/WORKFLOWS.md#agent-workflow-thesis"><img alt="Workflow-centric" src="https://img.shields.io/badge/design-workflow--centric-2563eb"></a>
    <a href="docs/WORKFLOWS.md#complete-skill-system"><img alt="Single entry" src="https://img.shields.io/badge/entry-neuro--orchestrator-7c3aed"></a>
    <a href="docs/WORKFLOWS.md#task-depth-routing"><img alt="Task depth" src="https://img.shields.io/badge/tasks-shallow%20to%20deep-16a34a"></a>
  </p>

  <p>
    <a href="README_CN.md"><img alt="中文文档" src="https://img.shields.io/badge/README-中文-0f766e"></a>
    <a href="docs/WORKFLOWS.md"><img alt="Workflows" src="https://img.shields.io/badge/docs-workflows-2563eb"></a>
    <a href="docs/PLAYBOOKS.md"><img alt="Playbooks" src="https://img.shields.io/badge/docs-playbooks-7c3aed"></a>
    <a href="docs/DEMO_GALLERY.md"><img alt="Demos" src="https://img.shields.io/badge/docs-demo%20gallery-0f766e"></a>
    <a href="docs/TROUBLESHOOTING.md"><img alt="Troubleshooting" src="https://img.shields.io/badge/docs-troubleshooting-92400e"></a>
    <a href="docs/VALIDATION.md"><img alt="Validation" src="https://img.shields.io/badge/validation-make%20validate-16a34a"></a>
  </p>

  <p>
    <img src="docs/NeuroFlow_framework.png" alt="NeuroFlow Agent framework: an evidence-gated human-AI research harness for machine learning, BCI, and neuroscience" width="1000">
  </p>
</div>

---

## Featured Demo: Paper Readiness Package

NeuroFlow includes a real inspected paper-readiness demo, distilled from an EEG-to-language research project rather than fabricated logs.

| Demo | What to inspect | Why it matters |
|---|---|---|
| [Vec2Text Paper Readiness Demo](docs/cases/vec2text-paper-readiness.md) | [Example paper artifact](docs/cases/assets/vec2text-paper-demo.pdf), claim boundaries, SOTA protocol audit, reproduction status, negative ablations, and reviewer-facing limitations. | Shows NeuroFlow as an evidence-gated submission harness, not an automatic paper generator. |

## NeuroFlow at a Glance

NeuroFlow-Agent turns inefficient human-in-the-loop AutoResearch into an evidence-gated research harness for machine learning, brain-computer interfaces, and neuroscience. It is built from lessons learned across strong general skills, open workflow systems, paper-writing skills, reproduction playbooks, reviewer simulators, and real ML x brain research sessions.

The project is not a narrow prompt pack. It is a maintained workflow-agent repository with three goals:

- **Domain-knowledge-correct AutoResearch**: keep AI agents inside valid ML x BCI x neuroscience assumptions before they write claims, design experiments, or summarize papers.
- **Submission-facing skills**: support work aimed at top machine learning conferences and flagship or specialty neuroscience journals, including claim grounding, experiment design, reproduction, review simulation, and paper writing.
- **Self-evolving knowledge system**: maintain a domain knowledge base, reference index, paper maps, evals, and workflow memory that can improve as the user works with the agent.

The framework has four visible stages:

| Stage | What it does |
|---|---|
| Brain Data | Starts from neural signals, BCI streams, behavioral traces, benchmarks, repositories, papers, or experiment logs. |
| Evidence Harness | Routes the task through papers, claims, experiments, reproduction, and review gates before artifacts are polished. |
| Human + AI Loop | Keeps the human researcher and AI agent in a verify-revise loop instead of relying on one-shot prompting. |
| Research Artifacts | Produces claim ledgers, experiment matrices, reproduction contracts, reviewer-risk maps, and evidence-scoped writing. |

This makes NeuroFlow a practical open-source workflow layer for researchers who want AI agents to help with real ML x BCI and NeuroAI projects without drifting into unsupported claims, citation noise, unreproduced results, or low-quality automated paper writing.

## Core Thesis: Workflow Is the Vertical Layer

An agent has three practical components: the model, the tools, and the workflow. Models and tools are increasingly shared infrastructure. The vertical layer is the workflow: the domain-specific execution policy that decides which context to replay, which evidence gates are non-negotiable, how deep the task should go, how a result becomes a claim, and what should persist after the session.

NeuroFlow-Agent is built around that thesis. It is not a prompt pack, a generic neuroscience note dump, or a collection of narrow downstream-task helpers. It is a maintained workflow-agent repository for ML x BCI x neuroscience research, built by absorbing lessons from general-purpose skill libraries and turning them into domain-specific execution policy.

The system is designed to make AutoResearch and human-in-the-loop agent work scientifically useful rather than merely fluent. Frontier ML methods, foundation models, agents, generative models, representation learning, continual learning, and BCI/neuroscience pipelines should be routed through domain evidence gates before they become experiments, papers, claims, or memory.

## Skill Physics: Fewer, Sharper Skills

NeuroFlow intentionally avoids turning every useful behavior into a new top-level skill. Evolvent's research note [More Skills, Worse Results? The Hidden Physics of Agent Skill Libraries](https://evolvent.co/en/research/agent-physics-skill-part1) argues that skill libraries can fail from local semantic competition: adding similar skills makes routing less reliable, especially in multi-step pipelines.

NeuroFlow applies that lesson as a project rule:

- `neuro-orchestrator` stays the single pre-routing entry point.
- Specialist skills remain few, high-contrast, and artifact-specific.
- Reusable behavior should usually become a reference, shared core gate, eval, case study, or runtime check before it becomes a new skill.
- High-use manifests must declare routeable anchors, a primary output contract, `do_not_use_when`, `prefer_over`, `defer_to`, and `competes_with`.
- Workflow edges declare whether handoffs are `tight`, `loose`, or `independent`, so multi-step pipelines can be audited for fragility.
- Deep handoffs must carry the original user intent and operational anchors so the middle of the workflow does not drift.

Run the local competition audit with:

```bash
make skill-competition
make skill-competition-report
make skill-simulate CANDIDATE=path/to/manifest.yaml
```

## What NeuroFlow-Agent Is

NeuroFlow-Agent is a compact operating layer for rigorous ML x BCI x neuroscience research agents. It uses `neuro-orchestrator` as the single default workflow entry point, then selects optional specialist modules for literature grounding, benchmark auditing, reproduction, experiment design, reviewer simulation, writing, and durable memory.

The repository combines three layers:

| Layer | What NeuroFlow maintains |
|---|---|
| Skill library | Submission-facing skills for top ML conferences and flagship or specialty neuroscience journals: paper grounding, benchmark audit, experiment design, reproduction, reviewer simulation, and paper writing. |
| Domain knowledge base | AI x BCI and neuroscience-specific assumptions, paper maps, dataset and method taxonomies, claim-to-citation memory, and reviewer-risk playbooks. |
| Self-evolving index graph | Manifests, evals, references, runtime traces, and memory rules that let the workflow improve as the user repeatedly applies it. |

The project covers a broad research surface:

| Research surface | What NeuroFlow controls |
|---|---|
| Neural encoding | Stimulus-to-brain modeling, feature alignment, encoding metrics, and baseline parity. |
| Neural decoding | Brain-to-label, brain-to-language, brain-to-image, and brain-to-action decoding with leakage checks. |
| Neural data analysis | EEG/iEEG/fMRI/MEG/LFP/spike preprocessing assumptions, split validity, statistics, and reproducibility. |
| Representation learning | Brain-language, brain-vision, multimodal, latent-space, and mechanistic representation alignment. |
| Modulation and closed-loop BCI | Offline/online boundaries, safety, calibration, latency, feedback, and human-subject constraints. |
| Behavior, cognition, and psychology | Behavioral signals, cognitive variables, task design, interpretation boundaries, and causal caution. |
| Brain-inspired algorithms | Inductive biases, learning rules, memory, attention, adaptation, and biologically motivated architectures. |
| Embodied AI and physical agents | Perception-action loops, world models, multimodal grounding, and closed-loop interaction claims. |
| Frontier AI methods | MLLMs, generative models, diffusion, foundation models, agents, RL, continual learning, and test-time adaptation. |

NeuroFlow does not treat these as isolated downstream tasks. It treats them as connected research workflows where data assumptions, model assumptions, experimental evidence, reviewer risk, and long-term memory have to stay aligned.

| Use it for | What the workflow makes the agent do |
|---|---|
| Scientific triage | Replay the smallest relevant memory and identify the next valid check. |
| Research framing | Convert broad AI x brain ideas into scoped claims, evidence needs, baselines, and reviewer risks. |
| Literature and positioning | Ground novelty, closest prior work, datasets, metrics, and method claims before writing. |
| Experiment design | Build ablations, controls, metrics, statistics, stop rules, and reproducibility checks. |
| Debugging and reproduction | Check scale, sampling variance, condition use, split localization, output routing, and evaluator parity before changing model capacity. |
| Paper writing and rebuttal | Convert claims into reviewer-facing, evidence-scoped scientific writing. |
| Closed-loop and embodied planning | Separate offline replay from online interaction claims and surface safety, calibration, latency, and controls. |
| Long research sessions | Consolidate reusable findings into workflow memory, evals, playbooks, and future first-read rules. |

## Single Entry Pipeline and Optional Modules

The repository contains several specialist skills, but users should not rely on Codex to auto-trigger them. The default entry is always `neuro-orchestrator`. It classifies the task, chooses one pipeline chain, names the artifact, applies evidence gates, and then uses specialist skills only as optional modules.

| Skill | Status | Purpose | Natural triggers |
|---|---|---|---|
| `neuro-orchestrator` | Stable | Single default entry point; routes tasks, controls depth, chooses the pipeline, and coordinates optional modules. | "what should I check next", "why is this result worse", "help me plan this experiment", "下一步查什么" |
| `neuro-idea-finder` | Stable | Generates testable AI x neural/cognitive/behavioral hypotheses. | "new EEG idea", "hypothesis", "fast validation", "研究 idea" |
| `paper-rag-plus` | Stable | Grounds claims in papers, builds claim ledgers, maps claims to citations, and organizes related work. | "support this claim", "closest prior work", "claim ledger", "相关工作" |
| `eeg-benchmark-hunter` | Stable | Finds and audits open neural, behavioral, and BCI benchmarks, access, licenses, splits, baselines, metrics, and leakage risks. | "find EEG dataset", "is this benchmark fair", "leakage risk", "找 EEG 数据集" |
| `repro-pack` | Stable | Builds reproduction contracts with environment, data, weights, commands, expected outputs, recovery paths, and L0/L1/L2/L3 observability levels. | "make this reproducible", "smoke test", "observability level", "复现" |
| `continual-learning-designer` | Beta | Designs cross-subject/session/device adaptation, streaming calibration, forgetting protocols, and online/offline boundaries. | "online adaptation", "cross-session", "forgetting", "持续学习" |
| `experiment-copilot` | Stable | Designs experiment matrices, ablations, controls, statistics, and stop rules. | "design ablations", "baseline is stronger", "metric gap", "实验矩阵" |
| `reviewer-simulator` | Stable | Audits papers, claims, rebuttals, root causes, fixability, method-vs-presentation risks, and research-integrity mismatches as strict conference reviewers. | "review this claim", "what will reviewers attack", "integrity risk", "方法问题还是表述问题" |
| `oral-writer` | Beta | Turns evidence into thesis, figure narrative, scoped claims, reviewer-facing paper text, writing operations, captions, LaTeX result tables, and numeric consistency checks. | "write abstract", "polish this paragraph", "check these numbers", "去 AI 味" |
| `neuro-memory` | Stable | Compresses completed sessions into durable workflow, playbook, finding, case, or eval memory. | "make this reusable", "save this lesson", "memory candidate", "沉淀经验" |
| `ai-bci-research` | Stable | Supplies shared AI x BCI assumptions, failure-mode checks, and public workflow memory; not the default router. | "BCI validity", "signal leakage", "closed loop", "脑机接口检查" |

The orchestrator can answer shallow tasks directly, route standard tasks through one optional module plus an evidence gate, or run deep tasks through literature grounding, benchmark selection, reproduction, experiment design, review simulation, writing, and memory consolidation.

Each high-use skill may also include a `manifest.yaml` that declares status, verification status, natural triggers, default reads, task axes, and on-demand references. `status` describes workflow maturity; `verification_status` describes the evidence behind the workflow or memory, such as `unverified`, `source-traced`, `reproduced`, `user-validated`, or `expert-reviewed`.

Shared workflow primitives live in `skills/_shared/core/` so specialist skills can reuse evidence gates, source traceability, claim discipline, BCI validity checks, reviewer risk checks, research planning protocol, output contracts, research-integrity forensics, cross-model review, and git publish safety without duplicating long instructions.

Research-integrity checks are concrete evidence forensics: every concern should be anchored to a claim, source span, number, citation, table, figure, command, or repository path, with an observability level and false-positive caveat. NeuroFlow does not use writing style or AI-detector signals as verdict evidence.

For high-risk outputs, NeuroFlow treats cross-model review as a default gate rather than a premium add-on: the executor model produces the claim ledger, experiment matrix, reproduction contract, or review; a reviewer model independently checks it; and the final gate cannot be self-approved by the same model or same uninterrupted reasoning pass. If independent review is unavailable, the artifact must say `required_but_not_run` and lower its confidence.

For repository delivery, NeuroFlow also treats git publishing as a gate rather than a routine shell step. Commit, push, branch deletion, and sync tasks must confirm the user-named target branch, fetch current remote state, verify ancestry before pushing, and remove temporary branches only after the target branch contains the intended commits.

## Anti Low-Quality AutoResearch

NeuroFlow is designed to resist low-quality AutoResearch: agentic research that produces fluent ideas, paper text, citation lists, or benchmark claims before the evidence has been inspected. The goal is not to slow agents down; it is to stop them from converting weak automation into scientific-looking artifacts.

The core failure modes NeuroFlow guards against are:

| Low-quality AutoResearch pattern | NeuroFlow safeguard |
|---|---|
| Claim-first writing: a broad claim is drafted before evidence, baselines, or closest prior work are checked. | `paper-rag-plus` builds claim ledgers with source spans, evidence tiers, support status, weakest links, and safer wording. |
| Citation laundering: a citation is attached because it is nearby in topic, not because it supports the exact modality, task, dataset, metric, or conclusion. | Claim grounding requires citation fit and marks mismatched or uninspected citations as unresolved. |
| Numeric drift: abstracts, tables, captions, Results paragraphs, and conclusions silently disagree on values, deltas, ranks, or significance. | `oral-writer` applies numeric self-consistency checks before strengthening result prose or table captions. |
| Protocol inflation: offline, within-subject, same-session, or qualitative evidence is used to imply online, cross-subject, cross-session, robust, or closed-loop capability. | Evidence gates force protocol truthfulness and reviewer-facing scope boundaries before paper text is polished. |
| Reproduction theater: a repository link or README command is treated as reproduction proof. | `repro-pack` assigns L0/L1/L2/L3 observability levels and only calls a target reproduced after a documented command produces expected output. |
| Style-based integrity judgments: fluent or generic writing is treated as proof of misconduct or poor science. | `reviewer-simulator` uses span-anchored integrity forensics and forbids AI-detector or writing-style signals as verdict evidence. |
| Memory pollution: unresolved summaries, failed matches, or private raw logs become durable project knowledge. | `neuro-memory` requires privacy filtering, verification status, and a target artifact before persistence. |

In practice, this means NeuroFlow should turn an automated research session into explicit intermediate artifacts: claim ledger, benchmark audit, reproduction contract, reviewer-risk map, numeric audit, or memory candidate. A polished paragraph is acceptable only after the relevant evidence gate has made its scope clear.

## Task Depths and Research Modes

NeuroFlow is designed for tasks with different scope and depth:

| Depth | Example task | Expected behavior |
|---|---|---|
| Shallow | "Explain this metric gap." | Load the smallest relevant memory, identify likely failure modes, and give a concise next check. |
| Standard | "Design ablations for this neural representation model." | Use domain guardrails plus experiment planning to produce a reproducible matrix. |
| Deep | "Prepare this AI x brain project for a conference submission." | Coordinate literature, benchmarks, experiments, claims, reviewer objections, writing, and limitations. |
| Persistent | "Turn this debugging session into reusable knowledge." | Compress the lesson into a finding, playbook, workflow rule, eval, or index update. |

NeuroFlow also separates research modes before acting:

| Mode | Question the workflow asks |
|---|---|
| Encoding | What stimulus, task, or model feature explains neural or behavioral responses? |
| Decoding | What information can be recovered from neural or behavioral signals under valid splits? |
| Analysis | What preprocessing, statistics, uncertainty, and controls make the interpretation defensible? |
| Representation | Which latent spaces are being aligned, compared, or causally interpreted? |
| Modulation | What feedback, stimulation, intervention, or closed-loop claim is actually supported? |
| Embodied interaction | What perception-action loop, world model, or online agent behavior is being claimed? |

## Why Workflow Is the Vertical Layer

For this project, "workflow" means more than a checklist. It is the durable execution policy that decides how an agent should read context, inspect code, run diagnostics, update memory, and turn results into paper-facing claims across AI, neural data, behavior, cognition, psychology, and embodied interaction.

| Agent component | What is usually shared | What this repo customizes |
|---|---|---|
| Model | General reasoning, coding, writing, multimodal generation, and tool use. | How frontier AI methods should be constrained by scientific evidence and domain validity. |
| Tools | Shell, Python, Git, search, plotting, validation, and document utilities. | Deterministic maintenance scripts for repo inventory, knowledge indexing, and skill validation. |
| Workflow | Generic task decomposition and tool use. | AI x brain research loops, memory replay, experiment consolidation, leakage audits, baseline checks, safety boundaries, and claim discipline. |

The central artifact is the explicit NeuroFlow pipeline. `neuro-orchestrator` is the entry point; specialist skills are optional modules; durable behavior lives across references, docs, evals, and scripts.

## Quick Start

Install the full NeuroFlow skill library for Codex:

```bash
git clone https://github.com/dongyangli-del/NeuroFlow-Agent.git
cd NeuroFlow-Agent
python3 scripts/install --target codex --update
```

The installer links every specialist skill into your Codex skills directory and installs the Codex-specific `neuro-orchestrator` override from `skills-codex/`. Restart Codex after installation.

For Claude Code, Cursor, Gemini CLI, OpenCode, and generic `AGENTS.md`-aware tools, see [docs/INSTALL.md](docs/INSTALL.md):

```bash
python3 scripts/install --target all --check
python3 scripts/install --target cursor --project /path/to/project --update
python3 scripts/install --target claude-code --update
python3 scripts/install --target gemini-cli --project /path/to/project --update
python3 scripts/install --target opencode --update
```

To install only the default entry with the Codex skill installer, pass the Codex-specific path explicitly:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo dongyangli-del/NeuroFlow-Agent \
  --path skills-codex/neuro-orchestrator
```

Then ask Codex naturally. The `AGENTS.md` and `neuro-orchestrator` entry should apply the internal preflight even if you do not mention workflow or skills:

```text
My EEG reconstruction result is worse than the baseline. What should I check next?
```

```text
Help me turn these experiment results into a paper claim.
```

Common writing and review requests can stay natural; the orchestrator routes them to the right specialist workflow:

| Natural request | NeuroFlow route | What it checks |
|---|---|---|
| "Analyze this result table for the Results section." | `experiment-to-paper` -> `oral-writer` experiment analysis | Metric direction, exact margins, uncertainty, missing variance, and claim scope. |
| "What plot should I use for these EEG results?" | `experiment-to-paper` -> `oral-writer` plot recommendation | Subject/session visibility, comparison structure, variance, protocol boundary, and caption seed. |
| "Make this figure/table caption reviewer-facing." | `experiment-to-paper` -> `oral-writer` caption/table writing | Takeaway, dataset/protocol, metric direction, evidence boundary, and limitations. |
| "Is this paper ready to submit?" | `experiment-to-paper` or `paper-to-rebuttal` -> `reviewer-simulator` | Acceptance readiness, blockers, fixability, method vs presentation defects, and submit/delay decision. |
| "Is this a method flaw or just bad writing?" | `reviewer-simulator` diagnosis | Root cause, defect type, best repair, reviewer consequence, and safer wording. |
| "Check this paper for integrity risks." | `paper-to-rebuttal` -> `reviewer-simulator` integrity forensics | Span-anchored claim-evidence, citation, numeric, protocol, and reproduction-observability findings. |
| "Build a claim ledger for this draft." | `paper-rag-plus` claim ledger | Claim type, source span, evidence tier, support status, weakest link, citation fit, and safer wording. |
| "Are these table numbers consistent with the caption?" | `oral-writer` numeric self-consistency | Preserved values, margins, metric direction, comparable rows, missing uncertainty, and safe wording. |
| "What has actually been reproduced in this repo?" | `paper-to-repro` -> `repro-pack` observability audit | L0/L1/L2/L3 level, observed artifacts, unobserved surfaces, blockers, and upgrade path. |

If Codex gives a generic answer, see [Troubleshooting](docs/TROUBLESHOOTING.md). For concrete before/after workflows, see the [Demo Gallery](docs/DEMO_GALLERY.md). AI agents should follow [AGENTS.md](AGENTS.md) first; [AGENT_GUIDE.md](AGENT_GUIDE.md) provides the longer explanation.

For traceable workflows and the semi-automatic evolution control plane, install the runtime and use the CLI:

```bash
python3 -m pip install -e '.[dev]'
python3 scripts/neuroflow_runtime/cli.py list --kind chains
python3 scripts/neuroflow_runtime/cli.py run --chain paper-to-repro --task "reproduce this paper baseline" --dry-run
python3 scripts/neuroflow_runtime/cli.py kb search "cross-subject EEG"
```

Runtime runs write private traces and artifacts under `.private/runs/` by default. Trace schema v2 records route candidates, skill versions, stage outcomes, artifact hashes, evidence-gate results, cost, failure tags, and final outcomes. Use `--execute` with a configured OpenAI-compatible, Anthropic, or Ollama provider to execute stages; without it the runtime creates a reviewable scaffold.

Completed traces can enter a measured evolution loop: feedback ingestion, failure clustering, candidate patch generation, exact-parent evaluation, independent review, risk-gated promotion, and rollback. Non-low-risk patches require human approval before shadow execution and again before promotion; only non-executable low-risk evals and source-traced references are eligible for explicit `semi-auto` promotion. See [Semi-Automatic Evolution](docs/EVOLUTION.md).

The runtime also includes explicit workflow hooks inspired by event-driven agent harnesses such as ECC:

```bash
python3 scripts/neuroflow_runtime/cli.py hook --event session_start --task "My EEG reconstruction result is worse than the baseline"
python3 scripts/neuroflow_runtime/cli.py hook --event pre_artifact --artifact ARTIFACT.md --kind claim
python3 scripts/neuroflow_runtime/cli.py hook --event post_tool --run-id RUN_ID --tool web --summary "source-traced lookup completed"
python3 scripts/neuroflow_runtime/cli.py hook --event session_end --run-id RUN_ID
python3 scripts/neuroflow_runtime/cli.py hook --event pre_commit
```

Hooks are explicit CLI adapters, not hidden global shell hooks. They use `NEUROFLOW_HOOK_PROFILE=minimal|standard|strict` and `NEUROFLOW_DISABLED_HOOKS`, write only private traces by default, and avoid automatic web search, public file edits, or multi-agent spawning.

## Persistent Workflow System

The repository is organized as a compact operating system for research agents:

```mermaid
flowchart TD
    accTitle: NeuroFlow Persistent Workflow
    accDescr: A task enters through Neuro-Orchestrator, follows one explicit pipeline, optionally uses specialist modules, checks AI x BCI evidence rules, and consolidates durable memory when needed.

    task[Research task] --> triage[Neuro-Orchestrator<br/>task type and depth]
    triage --> shallow[Shallow answer<br/>targeted memory replay]
    triage --> standard[Standard workflow<br/>one optional module plus evidence gate]
    triage --> deep[Deep workflow<br/>explicit pipeline chain]

    standard --> skill_pool[Optional specialist modules]
    deep --> skill_pool

    skill_pool --> idea[Neuro-Idea-Finder<br/>testable hypotheses]
    skill_pool --> rag[Paper-RAG++<br/>literature grounding]
    skill_pool --> benchmark[EEG-Benchmark-Hunter<br/>datasets and protocols]
    skill_pool --> repro[Repro-Pack<br/>runnable reproduction]
    skill_pool --> continual[Continual-Learning-Designer<br/>adaptation protocols]
    skill_pool --> experiment[Experiment-Copilot<br/>ablations and controls]
    skill_pool --> review[Reviewer-Simulator<br/>risk audit]
    skill_pool --> oral[Oral-Writer<br/>thesis and figure narrative]
    skill_pool --> bci[ai-bci-research<br/>domain guardrails]

    shallow --> evidence[Evidence checks<br/>splits, baselines, metrics, claims]
    idea --> evidence
    rag --> evidence
    benchmark --> evidence
    repro --> evidence
    continual --> evidence
    experiment --> evidence
    review --> evidence
    oral --> evidence
    bci --> evidence

    evidence --> output[Output<br/>answer, code, plan, paper text, or review]
    output --> memory[Neuro-Memory<br/>finding, playbook, workflow, case, eval, or index]
    memory --> replay[Future memory replay]
    replay --> triage
```

This loop is designed to become more useful over time. New experience should be distilled into reusable memory rather than left as a one-off chat transcript.

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

## Why AI x Brain Research Needs a Workflow System

General-purpose agents often miss domain-specific failure modes that determine whether an AI x brain result is scientifically meaningful:

- Neural and behavioral datasets can leak through subject, session, stimulus, repetition, or task structure.
- Encoding and decoding targets can be misaligned by image, token, layer, time window, trial order, or preprocessing version.
- Representation comparisons can confuse geometric similarity, predictive utility, causal interpretation, and mechanistic explanation.
- Generative and foundation-model pipelines can produce plausible outputs while failing scale, variance, condition-use, or subject-generalization checks.
- Modulation, closed-loop, and embodied-agent claims require clear online/offline boundaries, safety constraints, calibration, latency, and feedback assumptions.
- Cognitive science and psychology interpretations require task validity, behavioral controls, uncertainty, and careful separation of correlation from mechanism.

This workflow system packages those guardrails so future sessions begin with the right defaults before applying stronger models, larger datasets, or more complex agents.

## Architecture

```mermaid
flowchart TD
    accTitle: NeuroFlow Architecture
    accDescr: The architecture uses Neuro-Orchestrator as the single entry point, then selects optional specialist modules, shared domain memory, deterministic maintenance scripts, validation, and self-evolution.

    user[User prompt] --> orchestrator[neuro-orchestrator]
    orchestrator --> depth[Task-depth policy<br/>shallow, standard, deep, persistent]
    depth --> specialists[Optional specialist modules]

    specialists --> paper[paper-rag-plus]
    specialists --> idea[neuro-idea-finder]
    specialists --> benchmark[eeg-benchmark-hunter]
    specialists --> repro[repro-pack]
    specialists --> continual[continual-learning-designer]
    specialists --> exp[experiment-copilot]
    specialists --> reviewer[reviewer-simulator]
    specialists --> oral[oral-writer]
    specialists --> memory_skill[neuro-memory]
    specialists --> shared[ai-bci-research]

    shared --> refs[Reference memory]
    refs --> profile[research-profile.md]
    refs --> workflows[bci-workflows.md]
    refs --> debugging[debugging-playbooks.md]
    refs --> findings[experiment-findings.md]
    refs --> objections[reviewer-objections.md]
    refs --> writing_style_ref[writing-style.md]

    paper --> grounded[Grounded research output]
    idea --> grounded
    benchmark --> grounded
    repro --> grounded
    continual --> grounded
    exp --> grounded
    reviewer --> grounded
    oral --> grounded
    shared --> grounded

    grounded --> consolidate[Consolidation decision]
    consolidate --> durable[Durable memory update]
    durable --> index[knowledge-index.md]
    durable --> evals[evals.json]
    durable --> validation[make validate]
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
| [docs/INSTALL.md](docs/INSTALL.md) | Multi-platform install paths for Codex, Claude Code, Cursor, Gemini CLI, OpenCode, and generic agents. |
| [docs/KNOWLEDGE_GRAPH.md](docs/KNOWLEDGE_GRAPH.md) | Public knowledge graph entry point, taxonomy diagram, and KB search contract. |
| [docs/RELEASE.md](docs/RELEASE.md) | Versioned release process and release-note template. |
| [docs/VERIFICATION_DASHBOARD.md](docs/VERIFICATION_DASHBOARD.md) | Verification status by knowledge category and public map readiness. |
| [docs/SKILL_LIBRARY_SPEC.md](docs/SKILL_LIBRARY_SPEC.md) | Full 10-skill library gap analysis, contracts, task chains, and phase criteria. |
| [docs/EXAMPLES.md](docs/EXAMPLES.md) | Demo-case template and planned real examples. |
| [docs/VALIDATION.md](docs/VALIDATION.md) | Local checks and validation expectations. |
| [docs/PUBLIC_READY.md](docs/PUBLIC_READY.md) | Public-release checklist and private-memory policy. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Rules for adding durable skill memory. |
| [CHANGELOG.md](CHANGELOG.md) | User-facing changes and release history. |
| [LICENSE](LICENSE) | MIT license for public use and reuse. |
| [README_CN.md](README_CN.md) | Chinese project overview. |

## Content Organization Principle

Keep the repo organized by how memory is used, not by where it came from:

- `SKILL.md`: routing, first reads, and high-level operating rules only.
- `references/`: consolidated research memory that should change future agent behavior.
- `docs/`: public-facing explanation of workflows, playbooks, examples, and validation.
- `scripts/`: deterministic maintenance utilities, not research experiments.
- `evals/`: behavioral tests that prevent regression in agent conduct.

Raw logs, large artifacts, datasets, checkpoints, and private human-subject material should stay outside this repository. Only the durable lesson belongs here.

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

The validator checks required files, `SKILL.md` frontmatter, executable eval schema, Alembic migrations, local Markdown links, and accidental large files. Run the complete local suite with:

```bash
make validate
make test
make eval
```

When reference files change, rebuild the compact index:

```bash
make index
make validate
```

The GitHub Actions validation workflow lives at [.github/workflows/validate.yml](.github/workflows/validate.yml) and runs structural validation, tests, and the protected eval partition on push and pull requests.

## Demo Cases

Real demos should come from inspected artifacts or user-approved summaries. They are intentionally not fabricated here.

Current inspected demo:

- [Vec2Text paper readiness package](docs/cases/vec2text-paper-readiness.md): an evidence-gated EEG-to-language submission package showing claim boundaries, SOTA protocol audit, reproduction status, negative ablations, PDF compile readiness, and reviewer-facing limitations.

Planned demo slots:

- EEG diffusion scale/normalization failure.
- EEG diffusion objective mismatch and weak condition use.
- Reviewer-facing paper audit for leakage, baselines, and metric validity.

Use [docs/EXAMPLES.md](docs/EXAMPLES.md) to add a demo once the underlying artifact is ready.

## Update Workflow

After adding papers, repository notes, datasets, or experiment findings:

```bash
cd NeuroFlow-Agent/skills/ai-bci-research
python3 scripts/update_knowledge_index.py --root .
cd ../..
make validate
```

Keep raw logs, checkpoints, private data, and large generated outputs outside this repository.

## Roadmap

- Add real, inspected demo cases for EEG diffusion debugging and paper audit workflows.
- Expand task-depth routing evals so shallow, standard, deep, and persistent tasks trigger different memory and skill budgets.
- Strengthen single-entry pipeline rules across the full optional-module library.
- Expand self-evolution rules: when a new failure mode becomes a finding, playbook, workflow, eval, or profile update.
- Expand eval prompts for orchestration, experiment debugging, rebuttal, and closed-loop BCI planning.
- Add schema checks for `agents/openai.yaml` and eval structure.
- Publish a compact technical note explaining why workflow, not only model or tool choice, is the vertical layer for AI x BCI agents.
- Keep the project narrow and deep: the best persistent workflow system for AI x BCI research agents.

## Quality Bar

A change improves the project only if it makes future agents more reliable. Prefer concise playbooks, dated findings, explicit acceptance criteria, verified project facts, replayable workflows, and eval prompts over broad notes or invented examples.

## License

NeuroFlow-Agent is released under the [MIT License](LICENSE).
