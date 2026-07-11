"""Approval, promotion, canary validation, and rollback controls."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Any

from .evolution import EvolutionEngine, EvolutionError
from .models import CandidateStatus, EvolutionMode, PromotionDecision, RiskLevel
from .providers import ModelProvider, reviewers_are_independent
from .risk import inspect_patch


class PromotionError(RuntimeError):
    pass


class PromotionController:
    def __init__(self, root: Path, engine: EvolutionEngine | None = None) -> None:
        self.root = root.resolve()
        self.engine = engine or EvolutionEngine(self.root)
        self.store = self.engine.store

    @property
    def mode(self) -> EvolutionMode:
        raw = os.environ.get("NEUROFLOW_EVOLUTION_MODE", EvolutionMode.SHADOW.value)
        try:
            return EvolutionMode(raw)
        except ValueError:
            return EvolutionMode.SHADOW

    def review(
        self,
        candidate_id: str,
        *,
        approve: bool,
        actor: str,
        reason: str,
        reviewer: ModelProvider | None = None,
    ) -> PromotionDecision:
        candidate = self.store.get_candidate(candidate_id)
        if self.mode == EvolutionMode.OFF:
            raise PromotionError("Evolution is disabled by NEUROFLOW_EVOLUTION_MODE=off")
        if candidate.status not in {
            CandidateStatus.PROPOSED,
            CandidateStatus.SHADOW_TESTING,
            CandidateStatus.AWAITING_REVIEW,
        }:
            raise PromotionError(f"Candidate cannot be reviewed from {candidate.status}")
        pre_shadow = candidate.status in {CandidateStatus.PROPOSED, CandidateStatus.SHADOW_TESTING}
        decision = PromotionDecision(
            candidate_id=candidate.id,
            decision="shadow_approved" if approve and pre_shadow else ("approved" if approve else "rejected"),
            actor=actor,
            reason=reason,
            automatic=False,
            reviewer_provider=reviewer.name if reviewer else "human",
            reviewer_model=reviewer.model if reviewer else "human",
        )
        self.store.add_decision(decision)
        if not approve:
            self.engine.transition(candidate, CandidateStatus.REJECTED)
        return decision

    def promote(
        self,
        candidate_id: str,
        *,
        actor: str = "neuroflow-auto",
        automatic: bool = False,
        executor: ModelProvider | None = None,
        reviewer: ModelProvider | None = None,
    ) -> dict[str, Any]:
        if self.mode == EvolutionMode.OFF:
            raise PromotionError("Evolution is disabled by NEUROFLOW_EVOLUTION_MODE=off")
        candidate = self.store.get_candidate(candidate_id)
        if candidate.status != CandidateStatus.AWAITING_REVIEW:
            raise PromotionError(f"Candidate is not promotable from {candidate.status}")
        comparison = candidate.metadata.get("comparison", {})
        if not comparison.get("eligible"):
            raise PromotionError("Candidate did not pass the parent/holdout comparison gate")
        review_verdict = candidate.metadata.get("review_verdict", {})
        if review_verdict and review_verdict.get("verdict") != "pass":
            raise PromotionError("Independent candidate review did not pass")
        try:
            patch_text = self.engine.read_verified_patch(candidate)
        except EvolutionError as exc:
            raise PromotionError(str(exc)) from exc
        inspection = inspect_patch(patch_text)
        hidden = self.root / ".private" / "evolution" / "evals" / "hidden.json"
        if hidden.exists() and not candidate.metadata.get("hidden_holdout_evaluated"):
            raise PromotionError("The configured hidden holdout was not included in this candidate evaluation")
        self._ensure_parent_revision(candidate.parent_id)
        decisions = self.store.list_decisions(candidate.id)
        human_approved = any(item["decision"] == "approved" and not item["automatic"] for item in decisions)
        if automatic:
            if self.mode != EvolutionMode.SEMI_AUTO:
                raise PromotionError("Automatic promotion requires NEUROFLOW_EVOLUTION_MODE=semi-auto")
            if inspection.risk_level != RiskLevel.LOW:
                raise PromotionError("Only low-risk candidates can be promoted automatically")
            if inspection.public_reference:
                if not executor or not reviewer or not reviewers_are_independent(executor, reviewer):
                    raise PromotionError("Public reference auto-promotion requires an independent reviewer")
                if review_verdict.get("verdict") != "pass" or not review_verdict.get("source_trace_valid"):
                    raise PromotionError("Public reference auto-promotion requires a passing source-trace review")
                review_meta = candidate.metadata.get("reviewer", {})
                if (review_meta.get("provider"), review_meta.get("model")) != (reviewer.name, reviewer.model):
                    raise PromotionError("The supplied reviewer did not adjudicate this candidate evaluation")
        elif candidate.requires_human and not human_approved:
            raise PromotionError("High- and medium-risk candidates require an explicit human approval")

        self._ensure_touched_paths_clean(inspection.paths)
        self.engine.transition(candidate, CandidateStatus.CANARY)
        try:
            with self.engine.shadow_workspaces(candidate, patch_text) as (_, canary_workspace):
                validation = subprocess.run(
                    ["make", "validate"],
                    cwd=canary_workspace,
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    timeout=240,
                    check=False,
                )
        except (EvolutionError, OSError, subprocess.TimeoutExpired) as exc:
            validation_output = str(exc)
            validation_returncode = 1
        else:
            validation_output = validation.stdout
            validation_returncode = validation.returncode
        if validation_returncode != 0:
            self.engine.transition(candidate, CandidateStatus.ROLLED_BACK)
            decision = PromotionDecision(
                candidate_id=candidate.id,
                decision="canary_failed_rollback",
                actor=actor,
                reason=validation_output[-2000:],
                automatic=automatic,
                rollback_target=candidate.id,
                metadata={"stable_worktree_changed": False},
            )
            self.store.add_decision(decision)
            raise PromotionError("Canary validation failed; candidate was rolled back")
        try:
            self._ensure_parent_revision(candidate.parent_id)
            self._ensure_touched_paths_clean(inspection.paths)
            self._git_apply(patch_text, check=True)
            self._git_apply(patch_text, check=False)
        except PromotionError as exc:
            self.engine.transition(candidate, CandidateStatus.ROLLED_BACK)
            decision = PromotionDecision(
                candidate_id=candidate.id,
                decision="apply_failed_rollback",
                actor=actor,
                reason=str(exc),
                automatic=automatic,
                rollback_target=candidate.id,
                metadata={"stable_worktree_changed": False},
            )
            self.store.add_decision(decision)
            raise
        self.engine.transition(candidate, CandidateStatus.PROMOTED)
        decision = PromotionDecision(
            candidate_id=candidate.id,
            decision="promoted",
            actor=actor,
            reason="Candidate passed shadow comparison and detached canary validation.",
            automatic=automatic,
            reviewer_provider=reviewer.name if reviewer else "human",
            reviewer_model=reviewer.model if reviewer else "human",
            rollback_target=candidate.id,
            metadata={"validation_tail": validation_output[-1000:]},
        )
        self.store.add_decision(decision)
        return {
            "candidate_id": candidate.id,
            "status": CandidateStatus.PROMOTED.value,
            "automatic": automatic,
            "decision_id": decision.id,
        }

    def rollback(self, candidate_id: str, *, actor: str, reason: str) -> dict[str, Any]:
        candidate = self.store.get_candidate(candidate_id)
        if candidate.status != CandidateStatus.PROMOTED:
            raise PromotionError(f"Only promoted candidates can be rolled back, got {candidate.status}")
        try:
            patch_text = self.engine.read_verified_patch(candidate)
        except EvolutionError as exc:
            raise PromotionError(str(exc)) from exc
        self._git_apply(patch_text, reverse=True, check=True)
        self._git_apply(patch_text, reverse=True, check=False)
        self.engine.transition(candidate, CandidateStatus.ROLLED_BACK)
        decision = PromotionDecision(
            candidate_id=candidate.id,
            decision="rolled_back",
            actor=actor,
            reason=reason,
            rollback_target=candidate.id,
        )
        self.store.add_decision(decision)
        return {"candidate_id": candidate.id, "status": CandidateStatus.ROLLED_BACK.value, "decision_id": decision.id}

    def _ensure_touched_paths_clean(self, paths: tuple[str, ...]) -> None:
        completed = subprocess.run(
            ["git", "status", "--porcelain", "--", *paths],
            cwd=self.root,
            text=True,
            capture_output=True,
            check=False,
        )
        if completed.returncode != 0 or completed.stdout.strip():
            raise PromotionError("Candidate target paths contain uncommitted changes; promotion is blocked")

    def _ensure_parent_revision(self, parent_id: str | None) -> None:
        if not parent_id or not parent_id.startswith("git:"):
            return
        completed = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=self.root,
            text=True,
            capture_output=True,
            check=False,
        )
        if completed.returncode != 0 or completed.stdout.strip() != parent_id.removeprefix("git:"):
            raise PromotionError(
                "Repository HEAD changed since candidate creation; rebase and re-evaluate the candidate"
            )

    def _git_apply(self, patch: str, *, reverse: bool = False, check: bool = False) -> None:
        command = ["git", "apply"]
        if reverse:
            command.append("--reverse")
        if check:
            command.append("--check")
        command.append("-")
        completed = subprocess.run(
            command,
            cwd=self.root,
            input=patch,
            text=True,
            capture_output=True,
            check=False,
        )
        if completed.returncode != 0:
            raise PromotionError(f"git apply failed: {completed.stderr.strip()}")
