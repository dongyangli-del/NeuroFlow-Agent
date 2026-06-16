# Troubleshooting

Use this guide when Codex gives a generic answer instead of applying NeuroFlow.

## Quick Checks

1. Restart Codex after installation or after editing skill metadata.
2. Confirm `neuro-orchestrator` is installed as the Codex entry skill.
3. Confirm `_shared` resources are installed with the skill library.
4. Start a fresh session if the previous context strongly anchored a generic workflow.
5. Use one of the verification prompts below.

## Verify Installation

Run:

```bash
bash install.sh
ls -la ~/.codex/skills/neuro-orchestrator
ls -la ~/.codex/skills/_shared
```

Expected behavior:

- `neuro-orchestrator` points to the Codex-specific entry under `skills-codex/`.
- `_shared` points to the shared NeuroFlow resources under `skills/_shared/`.

## Verification Prompts

Use prompts that do not mention workflow, plan, routing, or skills. NeuroFlow should still apply the internal preflight.

```text
My EEG reconstruction result is worse than the baseline. What should I check next?
```

Expected route:

```text
neuro-orchestrator -> experiment or benchmark debugging -> BCI validity checks
```

```text
Help me turn these experiment results into a paper claim.
```

Expected route:

```text
neuro-orchestrator -> experiment-to-paper -> evidence gates -> scoped claim
```

```text
Is this EEG benchmark fair for a cross-subject claim?
```

Expected route:

```text
neuro-orchestrator -> benchmark-to-baseline -> split/leakage/baseline audit
```

## If It Still Does Not Trigger

- Ask explicitly once: `Use neuro-orchestrator for this task.`
- Check that `AGENTS.md` is present in the repository root.
- Check that `skills-codex/neuro-orchestrator/SKILL.md` includes natural trigger language.
- Run validation:

```bash
make validate
```

## Common Failure Modes

| Symptom | Likely cause | Fix |
|---|---|---|
| Generic paper-writing answer | `neuro-orchestrator` was not loaded | Restart Codex and use a verification prompt. |
| Specialist skill answers directly | Single-entry rule was skipped | Route through `neuro-orchestrator`; specialists are optional modules. |
| Full planning table appears for a tiny task | Preflight was exposed too aggressively | Keep preflight internal for shallow and standard tasks. |
| Missing shared references | `_shared` was not installed | Re-run `bash install.sh`. |
| The agent invents dataset facts | Benchmark evidence gate was skipped | Use `eeg-benchmark-hunter` and mark unknown fields as `needs verification`. |
