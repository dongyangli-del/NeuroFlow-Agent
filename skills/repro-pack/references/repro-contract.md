# Reproduction Contract

Every reproduction plan must make the target, inputs, command, and expected output explicit.

```markdown
Target artifact:
Repository status:
Environment:
Data:
Weights:
Minimal command:
Expected output:
Sanity checks:
Full reproduction path:
Failure recovery:
Missing evidence:
Next skill:
Memory candidate:
```

## Reproduction Levels

| Level | Meaning |
|---|---|
| Smoke run | Code starts, loads minimal data or mock input, writes expected files. |
| Baseline run | A known baseline completes under the documented protocol. |
| Table/figure reproduction | A specific paper result is regenerated. |
| Full reproduction | All required results for a paper claim are regenerated under matched settings. |

Do not call a smoke run a full reproduction.
