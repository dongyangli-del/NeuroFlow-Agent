# Validation

Run validation before committing skill changes:

```bash
make validate
```

The current validation checks:

- required repository and skill files exist;
- `AGENT_GUIDE.md`, `LICENSE`, `SECURITY.md`, the Codex-specific `neuro-orchestrator`, and the GitHub Actions validation workflow exist;
- `SKILL.md` has required frontmatter keys;
- `evals/evals.json` is valid JSON;
- optional `manifest.yaml` files include required routing and verification fields;
- the lightweight runtime registry can list chains and create a dry-run private trace scaffold;
- local Markdown links resolve;
- large generated files are not accidentally committed;
- obvious local path, private key, and API-token patterns are not present in public files.

Validation ignores local private overlays under `.private/`.

After adding or editing references, rebuild the compact index:

```bash
make index
make validate
```

Future validation should add deeper schema checks for eval structure, `agents/openai.yaml`, manifest path references, allowed `verification_status` values, and optional smoke tests for bundled scripts.
