# ECC Hooks Audit for NeuroFlow

Reviewed source: <https://github.com/affaan-m/ecc> at local revision `2bc924f`.

## What ECC Gets Right

ECC treats agent behavior as event-driven runtime policy. Its hook surface covers session lifecycle, tool preflight, tool postflight, compaction, stop-time summaries, quality gates, memory persistence, and observability. The important design ideas are:

- lifecycle events such as `SessionStart`, `PreCompact`, `Stop`, and `SessionEnd`;
- tool gates such as `PreToolUse` and `PostToolUse`;
- profile controls such as `minimal`, `standard`, and `strict`;
- per-hook disabling through environment variables;
- bounded stdin, timeout, async, and fail-open/fail-closed behavior;
- trace and activity recording instead of relying on chat memory.

## What NeuroFlow Should Borrow

NeuroFlow should borrow the event model, not the full generic hook pack. The highest-value hooks are research workflow hooks:

- `session_start`: classify the natural-language research task and choose a NeuroFlow chain before the agent drifts into ad hoc reasoning.
- `pre_artifact`: check evidence gates before public claims, references, README text, or memory are written.
- `post_tool`: record source-traced searches, paper lookups, scripts, and verification summaries in a private trace.
- `pre_commit`: run repository validation before a commit or push.
- `session_end`: summarize unresolved work, next actions, and memory candidates.

## What NeuroFlow Should Not Borrow Yet

NeuroFlow should avoid hooks that add latency or hidden side effects before the hook runtime has eval coverage:

- automatic web search;
- automatic multi-agent spawning;
- automatic edits to public knowledge files;
- broad language-formatting hooks unrelated to research workflow reliability;
- global Codex, Claude, Cursor, or Git hook installation.

## Current Implementation Target

The repository implements a lightweight hook adapter inside `scripts/neuroflow_runtime`. It writes private traces under `.private/runs/`, uses `NEUROFLOW_HOOK_PROFILE=minimal|standard|strict`, supports `NEUROFLOW_DISABLED_HOOKS`, and keeps workflow hooks explicit through:

```bash
python3 scripts/neuroflow_runtime/cli.py hook --event session_start --task "..."
python3 scripts/neuroflow_runtime/cli.py hook --event pre_artifact --artifact ARTIFACT.md --kind claim
python3 scripts/neuroflow_runtime/cli.py hook --event post_tool --run-id RUN_ID --tool web --summary "..."
python3 scripts/neuroflow_runtime/cli.py hook --event session_end --run-id RUN_ID
python3 scripts/neuroflow_runtime/cli.py hook --event pre_commit
```

This keeps NeuroFlow's default behavior narrow: natural research tasks trigger workflow routing and evidence gates, while irreversible or slow automation remains explicit.
