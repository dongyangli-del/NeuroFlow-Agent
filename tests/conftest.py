from __future__ import annotations

import subprocess
from pathlib import Path

import pytest


def run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=True)


@pytest.fixture
def git_repo(tmp_path: Path) -> Path:
    root = tmp_path / "repo"
    root.mkdir()
    run(["git", "init"], root)
    run(["git", "config", "user.email", "test@example.com"], root)
    run(["git", "config", "user.name", "NeuroFlow Test"], root)
    (root / ".gitignore").write_text(".private/\n", encoding="utf-8")
    (root / "Makefile").write_text("validate:\n\t@echo 'Skill repository validation passed.'\n", encoding="utf-8")
    skill = root / "skills" / "example"
    (skill / "references").mkdir(parents=True)
    (skill / "evals").mkdir()
    (skill / "SKILL.md").write_text("---\nname: example\ndescription: test\n---\n# Example\n", encoding="utf-8")
    (skill / "references" / "base.md").write_text("# Base\n", encoding="utf-8")
    (skill / "evals" / "evals.json").write_text(
        '{"schema_version": 2, "skill_name": "example", "evals": []}\n', encoding="utf-8"
    )
    run(["git", "add", "."], root)
    run(["git", "commit", "-m", "base"], root)
    return root


@pytest.fixture
def additive_reference_patch() -> str:
    return """diff --git a/skills/example/references/evolved.md b/skills/example/references/evolved.md
new file mode 100644
index 0000000..7ff4d5e
--- /dev/null
+++ b/skills/example/references/evolved.md
@@ -0,0 +1,5 @@
+# Evolved Check
+
+Verification status: source-traced
+Evidence: https://example.org/source
+Require a regression eval before promotion.
"""
