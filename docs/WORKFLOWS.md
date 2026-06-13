# Workflows

This project is built around a small set of reusable AI x BCI research workflows. Each workflow should give an agent enough structure to act rigorously without loading unrelated memory.

## Agent Workflow Thesis

An agent has three practical components: model, tools, and workflow. The model and tools can usually be shared across domains, but the workflow must be customized for AI x BCI research because it encodes domain-specific inspection order, validity checks, evidence thresholds, and memory updates.

In this repository, workflow means a persistent operating procedure, not a one-time checklist. A good workflow should decide:

1. which memory to replay before acting;
2. which validity checks must happen before interpretation;
3. which output is appropriate for the task;
4. which lesson should be consolidated for future sessions.

## Complete Skill System

The NeuroFlow skill system has one default entry point, `neuro-orchestrator`. It separates routing from optional modules for ideation, literature grounding, benchmark discovery, reproduction, continual adaptation, experiment design, reviewer simulation, oral-level writing, memory consolidation, and shared AI x BCI guardrails.

```text
skills/
  neuro-orchestrator/             # single entry point, task routing, and session control
  neuro-idea-finder/              # EEG/iEEG/fMRI/MEG/LFP/spike/BCI idea generation
  paper-rag-plus/                 # literature grounding and claim-to-citation mapping
  eeg-benchmark-hunter/           # open benchmark discovery, license, split, and leakage audits
  repro-pack/                     # reproducibility contract and failure recovery
  continual-learning-designer/    # continual BCI adaptation and personalization design
  experiment-copilot/             # experiment matrix, ablations, controls, statistics
  reviewer-simulator/             # strict conference review and rebuttal planning
  oral-writer/                    # oral-level thesis, figure narrative, and paper writing
  neuro-memory/                   # session compression and long-term memory routing
  ai-bci-research/                # shared AI x BCI domain guardrails and public workflow memory
```

Default deep flow:

```text
Task enters Neuro-Orchestrator
-> choose one pipeline chain
-> invoke optional modules only when their check order is needed
-> apply evidence gates
-> produce the requested artifact
-> decide whether Neuro-Memory should persist the lesson
-> use ai-bci-research as shared domain constraints throughout
```

Use an optional module only when it contributes a distinct first-read set, check order, output template, failure mode, or eval. The workflow should still make progress when only `neuro-orchestrator` is loaded.

See [SKILL_LIBRARY_SPEC.md](SKILL_LIBRARY_SPEC.md) for the gap analysis, promotion rule, and phased implementation criteria.

## Task Depth Routing

| Depth | Use when | Route behavior |
|---|---|---|
| Shallow | The user needs a narrow answer or next check. | Orchestrator direct answer, minimal first reads, no broad chain. |
| Standard | The user needs a concrete artifact. | One optional module plus one evidence gate. |
| Deep | The task spans ideas, papers, benchmarks, experiments, writing, or reproduction. | A named pipeline chain with explicit handoffs. |
| Persistent | The session should change future agent behavior. | End with `neuro-memory` and a memory candidate. |

## Named Pipeline Chains

| Chain | Optional module route |
|---|---|
| idea-to-experiment | `neuro-idea-finder` -> `paper-rag-plus` -> `experiment-copilot` -> `reviewer-simulator` -> `neuro-memory` |
| paper-to-repro | `paper-rag-plus` -> `repro-pack` -> `experiment-copilot` -> `neuro-memory` |
| benchmark-to-baseline | `eeg-benchmark-hunter` -> `experiment-copilot` -> `reviewer-simulator` |
| continual-adaptation | `continual-learning-designer` -> `experiment-copilot` -> `reviewer-simulator` |
| experiment-to-paper | `experiment-copilot` -> `reviewer-simulator` -> `oral-writer` -> `neuro-memory` |
| paper-to-rebuttal | `paper-rag-plus` -> `reviewer-simulator` -> `oral-writer` |
| session-to-memory | `neuro-memory` with `ai-bci-research` guardrails |

## Persistent Memory Loop

Use after any meaningful paper review, repository inspection, experiment debugging session, or rebuttal.

1. Replay only the relevant memory: profile, paper map, repo notes, BCI workflow, debugging playbook, writing style, or reviewer objections.
2. Execute the domain workflow and keep raw artifacts outside the skill repository.
3. Distill reusable experience into the smallest durable unit: dated finding, playbook update, reviewer objection, workflow rule, eval prompt, or profile update.
4. Rebuild `references/knowledge-index.md`.
5. Run validation and verify that the new memory would change a future agent's behavior.

This is the self-evolution path for the repo. The system should improve through consolidation, not by accumulating long transcripts.

## Skill Factory Loop

Use after a real research task when the session contains reusable behavior.

1. Ask the five compression questions: reusable check order, common failure pattern, next first-read file, non-skippable judgment criteria, and memory type.
2. Emit a `Memory candidate` block with repo decision, target file, minimal patch, leakage risk, and suggested eval.
3. Route the memory to the smallest durable unit:
   - workflow: reusable task sequence in `references/workflows/`;
   - playbook: repeated failure mode in `references/playbooks/` or `references/debugging-playbooks.md`;
   - finding: dated inspected result in `references/experiment-findings.md`;
   - case: public demonstration in `references/cases/`;
   - eval: behavior constraint in `evals/evals.json`;
   - private: ignored memory under `references/private/` or `.private/`;
   - no-repo: one-off context that should stay out.
4. Rebuild `references/knowledge-index.md` and run validation.

The goal is automatic compression into behavior-changing memory, not saving conversation history.

## BCI-RIGOR Loop

Use for experiment debugging, reproduction, and model-gap diagnosis.

1. Inspect the local repository and run configuration.
2. Identify the exact dataset, split protocol, target representation, model checkpoint, and metric.
3. Reproduce or verify the strongest deterministic baseline before changing the proposed method.
4. Audit leakage, normalization, output routing, condition alignment, checkpoint choice, and evaluator parity.
5. Localize the issue with train/validation/test probes and ablations.
6. Record the finding as symptom, confirmed facts, ruled-out causes, next probe, and acceptance criteria.

## Paper-to-Reviewer Loop

Use for abstracts, method sections, rebuttals, and submission readiness.

1. Establish the paper claim and the closest prior work.
2. Check whether the evidence actually supports the claim.
3. Separate decoding, reconstruction, alignment, and closed-loop claims.
4. Flag missing baselines, invalid splits, weak metrics, and unclear reproducibility details.
5. Rewrite claims with concrete nouns, measured evidence, and scoped limitations.

## Experiment Memory Loop

Use after new logs or debugging results are available.

1. Keep raw logs in the experiment workspace, not this skill repo.
2. Summarize only reusable conclusions in `references/experiment-findings.md`.
3. Add failure-mode procedures to `references/debugging-playbooks.md`.
4. Rebuild `references/knowledge-index.md`.
5. Add or update eval prompts when the new workflow should change agent behavior.

## Memory Replay and Consolidation Rules

Use these rules to decide where new information belongs.

| New information | Store as |
|---|---|
| A stable research preference or long-term mission shift | `references/research-profile.md` |
| A paper, dataset, venue, or citation-positioning note | `references/papers-index.md` or `references/venue-workflows.md` |
| A repository setup, structure, or reproducibility note | `references/repositories.md` |
| A repeated experiment failure mode | `references/debugging-playbooks.md` |
| A reusable session-level failure mode | `references/playbooks/*.md` |
| A reusable operating sequence | `references/workflows/*.md` |
| A dated, inspected result that changes future decisions | `references/experiment-findings.md` |
| A public demonstration case | `references/cases/*.md` |
| A claim risk or likely reviewer objection | `references/reviewer-objections.md` |
| A behavior that future agents must preserve | `evals/evals.json` |

## Closed-Loop BCI Planning Loop

Use for EEG-guided stimulus optimization, neural feedback, or bidirectional BCI proposals.

1. Define objective, observation, action, policy, safety constraints, calibration, and evaluation.
2. Separate offline replay from online human-subject claims.
3. Include sham/random/fixed-stimulus controls and fatigue/adverse-response handling.
4. Report latency, calibration time, stop criteria, and statistical testing.
