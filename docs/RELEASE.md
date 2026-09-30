# Release Process

Use this process when publishing a public NeuroFlow-Agent release.

## Pre-Release Checklist

1. Run validation:

   ```bash
   make validate
   python3 scripts/install --target all --check
   ```

2. Check public documentation:

   - README and README_CN render locally.
   - `docs/KNOWLEDGE_GRAPH.md` and `docs/VERIFICATION_DASHBOARD.md` reflect current public maps.
   - `CHANGELOG.md` contains user-facing changes.
   - No private paths, raw logs, human-subject data, or unpublished results are committed.

3. Check installer lifecycle:

   ```bash
   python3 scripts/install --target codex --check
   python3 scripts/install --target cursor --project . --dry-run --update
   python3 scripts/install --target gemini-cli --project . --dry-run --update
   ```

4. Create a version tag:

   ```bash
   git tag vYYYY.MM.DD
   git push origin vYYYY.MM.DD
   ```

5. Draft GitHub release notes from `CHANGELOG.md`.

## Release Note Template

````markdown
## Highlights

-

## Added

-

## Changed

-

## Validation

- `make validate`
- `python3 scripts/install --target all --check`

## Upgrade

```bash
git pull --ff-only
python3 scripts/install --target codex --update
```
````
