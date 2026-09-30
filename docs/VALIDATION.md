# Validation

Run validation before committing skill changes:

```bash
make validate
```

Install runtime and test dependencies first:

```bash
python -m pip install -e '.[dev]'
```

The current validation checks:

- required repository and skill files exist;
- `AGENT_GUIDE.md`, `LICENSE`, `SECURITY.md`, the Codex-specific `neuro-orchestrator`, and the GitHub Actions validation workflow exist;
- `SKILL.md` has required frontmatter keys;
- `evals/evals.json` is valid schema-v2 JSON with unique executable case IDs;
- protected evals and the SQLite/Alembic evolution schema are valid;
- optional `manifest.yaml` files include required routing and verification fields;
- high-use manifests include routeable anchors, primary output contracts, routing boundaries, and workflow dependency edges;
- the skill-competition scorecard can be generated as JSON and includes pair, skill, library, and pipeline-edge diagnostics;
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

Run executable checks with:

```bash
make test
make eval
make evolution-smoke
```

`make test` runs unit and end-to-end tests in temporary repositories and enforces at least 80% runtime coverage. `make eval` executes the protected eval partition through deterministic mock providers. `make evolution-smoke` exercises feedback, candidate privacy, patch integrity, pre-shadow approval, hidden-holdout enforcement, promotion, and rollback without modifying tracked project files.

Future validation should add deeper checks for `agents/openai.yaml`, manifest path references, and provider-specific live smoke tests.

Before adding a new top-level skill, simulate the candidate manifest:

```bash
make skill-simulate CANDIDATE=path/to/manifest.yaml
```

If the candidate competes strongly with an existing skill, keep the behavior as a reference, shared gate, eval, or runtime check until its anchors and output contract are genuinely distinct.
