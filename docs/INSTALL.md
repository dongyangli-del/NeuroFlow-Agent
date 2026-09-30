# Installation

NeuroFlow supports Codex first, but it also ships templates for Claude Code, Cursor, Gemini CLI, OpenCode, and generic `AGENTS.md`-aware agents. The multi-platform installer is intentionally lightweight: it links skills where the target supports installed skills, and copies small managed instruction templates where the target uses project or user-level rule files.

## Quick Install

```bash
git clone https://github.com/dongyangli-del/NeuroFlow-Agent.git
cd NeuroFlow-Agent
python3 scripts/install --target all --check
python3 scripts/install --target codex --update
```

The legacy Codex entry still works:

```bash
bash install.sh
```

To use trace schema v2, executable evals, provider-backed workflow execution, or semi-automatic evolution, install the Python runtime separately:

```bash
python3 -m pip install -e '.[dev]'
neuroflow evolve init
```

Skill-only installation does not require these Python dependencies. Evolution runtime configuration is documented in [Semi-Automatic Evolution](EVOLUTION.md).

## Installer Modes

```bash
python3 scripts/install --check
python3 scripts/install --update
python3 scripts/install --prune
python3 scripts/install --target cursor --project /path/to/project --update
```

| Flag | Meaning |
|---|---|
| `--check` | Report installed, missing, different, or conflicting files without writing. |
| `--update` | Refresh NeuroFlow-managed symlinks and template files. |
| `--prune` | Remove NeuroFlow-managed symlinks and generated template files. |
| `--target` | Choose `codex`, `claude-code`, `cursor`, `gemini-cli`, `opencode`, `generic`, or `all`. |
| `--project` | Project directory for Cursor, Gemini CLI, and generic `AGENTS.md` installs. |
| `--force` | Overwrite an unmanaged template file. Use only after review. |
| `--dry-run` | Print planned writes/removals without changing files. |

Managed template files include a `neuroflow-managed` marker. The installer does not overwrite unmanaged project files unless `--force` is provided.

## Platform Targets

| Target | Installed artifact | Default location |
|---|---|---|
| `codex` | Symlinks for `skills/`, `_shared`, and Codex-specific `neuro-orchestrator`. | `$CODEX_HOME/skills` or `~/.codex/skills` |
| `claude-code` | Slash-command template for NeuroFlow routing. | `~/.claude/commands/neuroflow.md` |
| `cursor` | Project rule template. | `<project>/.cursor/rules/neuroflow-agent.mdc` |
| `gemini-cli` | Project context template. | `<project>/GEMINI.md` |
| `opencode` | User-level agent instruction template. | `~/.config/opencode/AGENTS.md` |
| `generic` | Project-level `AGENTS.md` template. | `<project>/AGENTS.md` |

## Slash Command and Rule Lifecycle

NeuroFlow uses a simple lifecycle for generated command/rule templates:

1. **Install**: copy a managed template or create a symlink.
2. **Check**: compare the installed file to the current repository template.
3. **Update**: refresh only managed files or symlinks.
4. **Prune**: remove managed files when a tool is no longer used.

This keeps project-specific edits safe while still allowing versioned workflow updates.

## Compatibility Notes

- Claude Code supports custom slash-command files under `.claude/commands`.
- Cursor supports project rules under `.cursor/rules/*.mdc`.
- Gemini CLI supports project context through `GEMINI.md`.
- OpenCode and many coding agents can use `AGENTS.md`-style project instructions.

If a tool changes its rule-file convention, keep the NeuroFlow template content and update only the installer destination.

## Verify

```bash
python3 scripts/install --target all --check
make validate
make test
make eval
```

Restart or reload the target agent after installation so it reads the new rules.
