# Git Publish Safety Gate

Use this gate before committing, pushing, deleting branches, or claiming that local and remote repository state is synchronized.

## Failure Pattern

An executor may finish a useful implementation but publish it to an unintended branch, leave the user with an extra remote branch, or claim synchronization before checking the actual upstream. This is especially likely when work started on a temporary branch and the user later asks to push directly to `main`.

## Required Checks

Before `git push`, run or reason from equivalent evidence:

1. `git status --short --branch`
2. `git branch --all --verbose --no-abbrev`
3. `git remote -v`
4. `git fetch origin` when the operation touches a remote branch.
5. `git merge-base --is-ancestor <target-remote> HEAD` before pushing to a protected or user-named target branch.

## Branch Target Rules

- If the user names a target branch, push to that branch, not the current branch by habit.
- If the user says "main" or "directly to main", update `origin/main` and make local `main` match it.
- If work is on a temporary branch, do not leave that branch as the final delivery state unless the user asked for a PR or separate branch.
- If the remote target changed after the last check, fetch and re-evaluate ancestry before pushing again.
- Prefer fast-forward updates. Do not force-push unless the user explicitly asks and the risk has been stated.

## Cleanup Rules

After a successful direct-to-main delivery:

1. Check out `main`.
2. Fast-forward local `main` to `origin/main`.
3. Delete temporary local branches only after their commits are reachable from `main`.
4. Delete temporary remote branches when the user asks to remove extra branches.
5. Run `git fetch --prune origin`.
6. Verify `git status --short --branch` and `git branch --all --verbose --no-abbrev`.

## Required Output

When reporting completion, include:

```markdown
Target branch:
Remote branch:
Latest commit:
Temporary branches removed: yes/no/not requested
Validation:
```

Do not say "synced" unless `HEAD`, the local target branch, and the remote target branch point to the intended commit.
