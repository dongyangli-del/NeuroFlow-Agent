# Validation

Run validation before committing skill changes:

```bash
make validate
```

The current validation checks:

- required repository and skill files exist;
- `SKILL.md` has required frontmatter keys;
- `evals/evals.json` is valid JSON;
- local Markdown links resolve;
- large generated files are not accidentally committed;
- obvious local path, private key, and API-token patterns are not present in public files.

Validation ignores local private overlays under `.private/`.

After adding or editing references, rebuild the compact index:

```bash
make index
make validate
```

Future validation should add schema checks for eval structure, `agents/openai.yaml`, and optional smoke tests for bundled scripts.
