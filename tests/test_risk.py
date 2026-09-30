from __future__ import annotations

import pytest
from neuroflow_runtime.models import RiskLevel
from neuroflow_runtime.risk import UnsafePatch, inspect_patch


def test_additive_source_traced_reference_is_low_risk(additive_reference_patch: str) -> None:
    result = inspect_patch(additive_reference_patch)
    assert result.risk_level == RiskLevel.LOW
    assert result.public_reference
    assert result.source_traced
    assert not result.requires_human


def test_skill_policy_is_high_risk() -> None:
    patch = """diff --git a/skills/example/SKILL.md b/skills/example/SKILL.md
--- a/skills/example/SKILL.md
+++ b/skills/example/SKILL.md
@@ -1 +1 @@
-old
+new
"""
    result = inspect_patch(patch)
    assert result.risk_level == RiskLevel.HIGH
    assert result.requires_human


def test_protected_eval_is_critical() -> None:
    patch = """diff --git a/evals/protected.json b/evals/protected.json
--- a/evals/protected.json
+++ b/evals/protected.json
@@ -1 +1 @@
-{}
+{"disabled": true}
"""
    assert inspect_patch(patch).risk_level == RiskLevel.CRITICAL


def test_patch_path_traversal_is_rejected() -> None:
    with pytest.raises(UnsafePatch):
        inspect_patch("diff --git a/x b/../outside\n+++ b/../outside\n+@@ -0,0 +1 @@\n+x\n")


def test_sensitive_patch_content_is_rejected() -> None:
    patch = """diff --git a/skills/example/references/note.md b/skills/example/references/note.md
new file mode 100644
--- /dev/null
+++ b/skills/example/references/note.md
@@ -0,0 +1 @@
+Raw file: /home/researcher/private/participant.csv
"""
    with pytest.raises(UnsafePatch, match="sensitive material"):
        inspect_patch(patch)


def test_source_path_prevents_rename_from_downgrading_risk() -> None:
    patch = """diff --git a/scripts/tool.py b/skills/example/references/tool.md
similarity index 100%
rename from scripts/tool.py
rename to skills/example/references/tool.md
"""
    result = inspect_patch(patch)
    assert "scripts/tool.py" in result.paths
    assert result.risk_level == RiskLevel.HIGH


def test_symbolic_link_patch_is_rejected() -> None:
    patch = """diff --git a/skills/example/references/link.md b/skills/example/references/link.md
new file mode 120000
--- /dev/null
+++ b/skills/example/references/link.md
@@ -0,0 +1 @@
+../../private.txt
"""
    with pytest.raises(UnsafePatch, match="symbolic links"):
        inspect_patch(patch)


def test_executable_eval_is_high_risk() -> None:
    patch = """diff --git a/skills/example/evals/evals.json b/skills/example/evals/evals.json
--- a/skills/example/evals/evals.json
+++ b/skills/example/evals/evals.json
@@ -1 +1,2 @@
 {"schema_version": 2, "skill_name": "example", "evals": []}
+{"type": "command_exit", "command": ["python3", "-c", "print('unsafe')"]}
"""
    result = inspect_patch(patch)
    assert result.risk_level == RiskLevel.HIGH
    assert result.requires_human


def test_participant_identifier_is_rejected_without_blocking_generic_subject_text() -> None:
    sensitive = """diff --git a/skills/example/references/note.md b/skills/example/references/note.md
new file mode 100644
--- /dev/null
+++ b/skills/example/references/note.md
@@ -0,0 +1 @@
+Participant-P001 failed the run.
"""
    with pytest.raises(UnsafePatch, match="participant identifier"):
        inspect_patch(sensitive)

    generic = sensitive.replace("Participant-P001 failed", "Subject-specific decoding failed")
    assert inspect_patch(generic).risk_level == RiskLevel.MEDIUM


def test_only_additive_markdown_private_memory_is_low_risk() -> None:
    memory = """diff --git a/.private/references/lesson.md b/.private/references/lesson.md
new file mode 100644
--- /dev/null
+++ b/.private/references/lesson.md
@@ -0,0 +1 @@
+# Reusable local lesson
"""
    result = inspect_patch(memory)
    assert result.risk_level == RiskLevel.LOW
    assert result.new_files == (".private/references/lesson.md",)

    runtime_state = memory.replace(".private/references/lesson.md", ".private/runs/run.md")
    assert inspect_patch(runtime_state).risk_level == RiskLevel.MEDIUM

    modification = memory.replace("new file mode 100644\n--- /dev/null", "--- a/.private/references/lesson.md")
    assert inspect_patch(modification).risk_level == RiskLevel.MEDIUM
