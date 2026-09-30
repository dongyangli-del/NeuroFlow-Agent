# Semi-Automatic Evolution

NeuroFlow evolves workflow policy, memory, references, evals, routing, and tools through a measured candidate lifecycle. It does not train or rewrite the underlying model weights.

## Control Loop

```text
versioned workflow run
-> structured feedback
-> failure clustering
-> candidate patch plus incident eval
-> parent/candidate shadow evaluation
-> risk and reviewer gates
-> canary validation
-> promotion or rollback
```

The runtime is local-first. SQLite stores control-plane metadata under `.private/evolution/`; patches, eval results, worktrees, and reports remain in the ignored private overlay. Public skill and reference files change only during an approved promotion.

The public Python contracts live in `neuroflow_runtime.models`: `FeedbackEvent`, `EvolutionCandidate`, `EvalCase`, `EvalRunSummary`, and `PromotionDecision`. They use Pydantic schema validation; SQLAlchemy rows are an internal persistence detail. Candidate status, risk level, eval partition, assertion type, feedback type, and evolution mode are closed enums.

## Install

```bash
python -m pip install -e '.[dev]'
neuroflow evolve init
```

The same commands can be invoked through `python scripts/neuroflow_runtime/cli.py` without relying on the installed console script. For PostgreSQL, install `.[postgres]` and set `NEUROFLOW_DATABASE_URL`; CLI output redacts database passwords.

## Run and Ingest

Create a trace scaffold without calling a model:

```bash
neuroflow run \
  --chain benchmark-to-baseline \
  --task "My EEG result is worse than the baseline" \
  --dry-run
```

Execute every stage with the configured executor provider:

```bash
neuroflow run \
  --chain benchmark-to-baseline \
  --task "Audit this EEG benchmark" \
  --execute
```

Import a user correction or a failed trace:

```bash
neuroflow evolve ingest \
  --run-id RUN_ID \
  --summary "The workflow skipped subject-wise leakage" \
  --event-type user_correction \
  --failure-tag benchmark:leakage
```

Trace schema v2 records the selected route, candidate routes, skill versions, stage status, artifact hashes, evidence-gate outcomes, cost, failure tags, and final outcome. Version-1 traces remain readable.

An external agent can return one stage without gaining write access to the stable skill library:

```bash
neuroflow import-result \
  --run-id RUN_ID \
  --step 1 \
  --artifact STAGE_OUTPUT.md \
  --status passed \
  --metric tokens=1200 \
  --metric cost_usd=0.04
```

The runtime copies the stage artifact into the private run, recomputes its hash and evidence gates, and updates the aggregate trace.

## Provider Configuration

Executor and reviewer settings are independent:

```bash
export NEUROFLOW_EXECUTOR_PROVIDER=openai
export NEUROFLOW_EXECUTOR_MODEL=gpt-5-mini
export NEUROFLOW_EXECUTOR_API_KEY=...

export NEUROFLOW_REVIEWER_PROVIDER=anthropic
export NEUROFLOW_REVIEWER_MODEL=claude-sonnet-4-5
export NEUROFLOW_REVIEWER_API_KEY=...
```

Supported providers are `openai`, `anthropic`, `ollama`, and `mock`. OpenAI-compatible endpoints can override `NEUROFLOW_EXECUTOR_BASE_URL` or `NEUROFLOW_REVIEWER_BASE_URL`. Ollama defaults to `http://127.0.0.1:11434`.

Public-reference auto-promotion requires the executor and reviewer to use different provider/model identities. Provider failure never falls back to self-approval.

Before any remote provider call, task, feedback, incident-eval, expected-output, and reference text is screened for local paths, credential patterns, and participant-like identifiers. Candidate generation receives only the failure type, tag, sanitized summary, and source; raw trace evidence is not sent. Candidate patches containing sensitive material are rejected.

## Candidate Lifecycle

Generate two candidate mutations for the largest unhandled failure cluster:

```bash
neuroflow evolve propose --variants 2
```

Import a prepared candidate instead:

```bash
neuroflow evolve propose --patch candidate.patch --target paper-rag-plus
```

Candidate states are:

```text
observed -> clustered -> proposed -> shadow_testing
-> awaiting_review -> canary -> promoted
```

Any pre-promotion state can be rejected where allowed. Canary failures and promoted candidates can transition to `rolled_back`.

Low-risk content candidates can enter shadow evaluation directly. Medium-, high-, and critical-risk candidates may execute changed code during validation, so inspect the diff and grant a separate shadow approval first:

```bash
neuroflow evolve review CANDIDATE_ID \
  --approve \
  --actor project-owner \
  --reason "Reviewed for safe shadow execution"
```

This records `shadow_approved` without approving promotion. Then evaluate the candidate against two detached worktrees at the exact recorded parent revision:

```bash
neuroflow eval run --candidate CANDIDATE_ID
```

A detached Git worktree isolates the comparison state, not the host process or network. Treat shadow approval as permission to execute the touched code locally; inspect high-risk diffs before granting it.

If `.private/evolution/evals/hidden.json` exists, candidate evaluation includes it by default and refuses `--exclude-hidden`. The evaluation gate requires:

- every protected safety, privacy, and integrity assertion to pass;
- no regression on a case the parent passed consistently;
- at least `0.03` target-slice mean improvement;
- candidate cost no greater than `1.25x` parent cost unless quality improves by at least `0.05`.

## Approval and Promotion

Low-risk candidates are newly created Markdown memory under `.private/memory/`, `.private/references/`, or a skill's `references/private/`; non-executable additive evals; or additive source-traced public references. Private-memory incident checks and patch review stay local and deterministic. Public references must contain inspected source markers and no unresolved fields. Evals containing `command_exit` are high risk.

`SKILL.md`, manifests, routing, pipeline topology, scripts, tooling, deletion, protected gates, and broad claim changes are never unattended promotions.

```bash
neuroflow evolve review CANDIDATE_ID \
  --approve \
  --actor project-owner \
  --reason "Independent review passed"

neuroflow evolve promote CANDIDATE_ID --actor project-owner
```

Enable low-risk automatic promotion explicitly:

```bash
export NEUROFLOW_EVOLUTION_MODE=semi-auto
neuroflow evolve promote CANDIDATE_ID \
  --auto \
  --executor-provider openai \
  --reviewer-provider anthropic
```

For medium-, high-, and critical-risk candidates, run `evolve review --approve` again after evaluation; this second decision records the final `approved` state used by promotion. The default mode is `shadow`. Valid values are `off`, `shadow`, and `semi-auto`; `off` blocks creation, evaluation, review, and promotion while leaving emergency rollback available.

The canary first applies the patch and runs `make validate` in a disposable detached worktree. Only a passing canary is applied to the stable local worktree. Promotion never commits, pushes, or publishes.

Rollback verifies that the reverse patch still applies before changing files:

```bash
neuroflow evolve rollback CANDIDATE_ID \
  --actor project-owner \
  --reason "Post-promotion regression"
```

## Evaluation Partitions

- `incident`: generated from a real correction or failure.
- `regression`: tracked skill behavior that future versions must preserve.
- `protected`: immutable safety, privacy, runtime, and research-integrity behavior.
- `hidden_holdout`: private cases excluded from candidate prompts and repository patches.

Tracked eval JSON uses schema version 2. A hidden suite may be placed at `.private/evolution/evals/hidden.json`; candidate generation never reads it. Run:

```bash
make eval
make evolution-smoke
make evolution-report
```

Reports are emitted as Markdown and static HTML under `.private/evolution/reports/`.

## Operational Invariants

- A candidate cannot modify `evals/protected.json`.
- A candidate patch cannot escape the repository or modify `.git`.
- Binary and symbolic-link candidate patches are rejected, and both source and destination paths are risk-classified.
- The stored patch path and SHA-256 are verified before shadow evaluation, promotion, and rollback.
- Command assertions allow only repository scripts and a narrow set of read-only or validation commands.
- Canary commands run in a disposable candidate worktree; a failed canary does not modify stable files.
- Promotion is blocked when a touched path has uncommitted user changes.
- Public artifacts do not persist private paths, credentials, participant data, or raw logs.
- Hidden holdout results may decide promotion but may not be used to generate a mutation.
- Same-model review is diagnostic only and cannot authorize public-reference auto-promotion.
- Every promoted candidate retains its patch, evaluation lineage, decision, and rollback target.
