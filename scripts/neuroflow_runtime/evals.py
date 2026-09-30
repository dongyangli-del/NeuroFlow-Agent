"""Executable evaluation harness for NeuroFlow skills and workflow candidates."""

from __future__ import annotations

import asyncio
import json
import re
import shlex
import statistics
import subprocess
import time
from collections import defaultdict
from collections.abc import Iterable
from pathlib import Path
from typing import Any

import jsonschema

from .models import (
    AssertionResult,
    AssertionType,
    EvalAssertion,
    EvalCase,
    EvalCaseResult,
    EvalDimension,
    EvalPartition,
    EvalRunSummary,
)
from .privacy import sanitize_remote_text
from .providers import MockProvider, ModelProvider, ModelRequest

ALLOWED_COMMANDS = {"python", "python3", "make", "git"}
SAFE_MAKE_TARGETS = {
    "hook-smoke",
    "install-check",
    "lint",
    "runtime-list",
    "runtime-smoke",
    "skill-competition",
    "test",
    "validate",
}
SAFE_GIT_COMMANDS = {
    ("diff", "--check"),
    ("rev-parse", "HEAD"),
    ("status", "--porcelain"),
}


class EvalLoadError(ValueError):
    pass


def load_eval_cases(
    root: Path,
    *,
    partitions: set[EvalPartition] | None = None,
    include_hidden: bool = False,
) -> list[EvalCase]:
    paths = sorted(root.glob("skills*/**/evals/evals.json"))
    protected = root / "evals" / "protected.json"
    if protected.exists():
        paths.append(protected)
    incident_dir = root / ".private" / "evolution" / "evals" / "incidents"
    if incident_dir.exists():
        paths.extend(sorted(incident_dir.glob("*.json")))
    if include_hidden:
        hidden = root / ".private" / "evolution" / "evals" / "hidden.json"
        if hidden.exists():
            paths.append(hidden)
    cases: list[EvalCase] = []
    for path in paths:
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict) or not isinstance(payload.get("evals"), list):
            raise EvalLoadError(f"{path} must contain an evals list")
        skill_name = str(payload.get("skill_name", path.parent.parent.name))
        source_key = (
            str(path.parent.parent.relative_to(root)).replace("/", ":")
            if path.is_relative_to(root)
            else skill_name
        )
        if path.parent.parent == root:
            source_key = skill_name
        for index, raw_case in enumerate(payload["evals"], start=1):
            if not isinstance(raw_case, dict):
                raise EvalLoadError(f"{path} eval {index} must be an object")
            normalized = dict(raw_case)
            original_id = str(normalized.get("id", index))
            normalized["id"] = f"{source_key}:{original_id}"
            normalized["skill_name"] = skill_name
            normalized["source_path"] = str(path.relative_to(root))
            normalized["skill_root"] = str(path.parent.parent.relative_to(root)) if "skills" in path.parts else "."
            normalized["assertions"] = [_normalize_assertion(item) for item in normalized.get("assertions", [])]
            if "partition" not in normalized:
                normalized["partition"] = EvalPartition.REGRESSION
            if "repeats" not in normalized and any(
                item["type"] == AssertionType.LLM_RUBRIC for item in normalized["assertions"]
            ):
                normalized["repeats"] = 3
            case = EvalCase.model_validate(normalized)
            if case.partition == EvalPartition.HIDDEN_HOLDOUT and not include_hidden:
                continue
            if partitions and case.partition not in partitions:
                continue
            cases.append(case)
    return cases


def _normalize_assertion(raw: Any) -> dict[str, Any]:
    if isinstance(raw, str):
        return {"type": AssertionType.LLM_RUBRIC, "text": raw}
    if not isinstance(raw, dict):
        raise EvalLoadError("Eval assertions must be strings or objects")
    item = dict(raw)
    item.setdefault("type", AssertionType.LLM_RUBRIC)
    item.setdefault("dimension", _infer_dimension(str(item.get("text", ""))))
    item.setdefault("critical", item["dimension"] == EvalDimension.SAFETY)
    return item


def _infer_dimension(text: str) -> EvalDimension:
    lower = text.lower()
    if any(token in lower for token in ("privacy", "leak", "safety", "unsupported", "invent", "private")):
        return EvalDimension.SAFETY
    if any(token in lower for token in ("cost", "token", "time", "efficient")):
        return EvalDimension.EFFICIENCY
    if any(token in lower for token in ("general", "held-out", "cross-domain", "novel")):
        return EvalDimension.GENERALIZATION
    if any(token in lower for token in ("preserve", "retain", "existing", "backward")):
        return EvalDimension.RETENTION
    return EvalDimension.ADAPTIVITY


class EvalHarness:
    def __init__(
        self,
        root: Path,
        executor: ModelProvider,
        reviewer: ModelProvider,
    ) -> None:
        self.root = root
        self.executor = executor
        self.reviewer = reviewer

    async def run(
        self,
        cases: Iterable[EvalCase],
        *,
        candidate_id: str | None = None,
        partition_label: str = "all",
    ) -> EvalRunSummary:
        results: list[EvalCaseResult] = []
        for case in cases:
            for repeat in range(case.repeats):
                result = await self.run_case(case)
                if case.repeats > 1:
                    result.case_id = f"{result.case_id}#{repeat + 1}"
                results.append(result)
        summary = summarize_results(results, candidate_id=candidate_id, partition=partition_label)
        return summary

    async def run_case(self, case: EvalCase) -> EvalCaseResult:
        started = time.monotonic()
        prompt = self._render_prompt(case)
        deterministic_only = bool(case.assertions) and all(
            assertion.type in {
                AssertionType.FILE_EXISTS,
                AssertionType.FILE_DIFF,
                AssertionType.ARTIFACT_FIELD,
                AssertionType.COMMAND_EXIT,
            }
            for assertion in case.assertions
        )
        if deterministic_only:
            output = ""
            response_tokens = 0
            response_cost = 0.0
        else:
            response = await self.executor.generate(
                ModelRequest(
                    prompt=prompt,
                    system="Follow the supplied NeuroFlow skill references and return the requested research artifact.",
                    metadata={"expected_output": sanitize_remote_text(case.expected_output)},
                )
            )
            output = response.text
            response_tokens = response.input_tokens + response.output_tokens
            response_cost = response.cost_usd
        assertion_results = []
        for assertion in case.assertions:
            assertion_results.append(await self._evaluate_assertion(case, assertion, output))
        total_weight = sum(item.assertion.weight for item in assertion_results) or 1.0
        score = sum(item.score * item.assertion.weight for item in assertion_results) / total_weight
        critical_pass = all(item.passed for item in assertion_results if item.assertion.critical)
        return EvalCaseResult(
            case_id=case.id,
            partition=case.partition,
            output=output,
            assertions=assertion_results,
            score=round(score, 6),
            critical_pass=critical_pass,
            duration_ms=int((time.monotonic() - started) * 1000),
            tokens=response_tokens + sum(item.tokens for item in assertion_results),
            cost_usd=response_cost + sum(item.cost_usd for item in assertion_results),
        )

    def _render_prompt(self, case: EvalCase) -> str:
        sections = [case.prompt]
        base = self.root / case.skill_root
        for relative in case.files:
            path = (base / relative).resolve()
            try:
                path.relative_to(self.root.resolve())
            except ValueError:
                continue
            if path.exists() and path.is_file():
                text = path.read_text(encoding="utf-8", errors="ignore")
                sections.append(f"\n--- Reference: {path.relative_to(self.root)} ---\n{text[:30000]}")
        return sanitize_remote_text("\n".join(sections))

    async def _evaluate_assertion(
        self,
        case: EvalCase,
        assertion: EvalAssertion,
        output: str,
    ) -> AssertionResult:
        if assertion.type == AssertionType.CONTAINS:
            needle = str(assertion.value or assertion.text)
            passed = needle.lower() in output.lower()
            return _result(assertion, passed, f"Expected output to contain {needle!r}")
        if assertion.type == AssertionType.NOT_CONTAINS:
            needle = str(assertion.value or assertion.text)
            passed = needle.lower() not in output.lower()
            return _result(assertion, passed, f"Expected output not to contain {needle!r}")
        if assertion.type == AssertionType.REGEX:
            pattern = str(assertion.pattern or assertion.value)
            passed = re.search(pattern, output, re.MULTILINE | re.IGNORECASE) is not None
            return _result(assertion, passed, f"Regex {pattern!r} did not match")
        if assertion.type == AssertionType.JSON_PATH:
            return self._json_path_result(assertion, output)
        if assertion.type == AssertionType.JSON_SCHEMA:
            return self._json_schema_result(assertion, output)
        if assertion.type == AssertionType.FILE_EXISTS:
            target = (self.root / assertion.path).resolve()
            passed = target.exists() and _inside(target, self.root)
            return _result(assertion, passed, f"File does not exist: {assertion.path}")
        if assertion.type == AssertionType.FILE_DIFF:
            return self._file_diff_result(assertion)
        if assertion.type == AssertionType.ARTIFACT_FIELD:
            return self._artifact_field_result(assertion)
        if assertion.type == AssertionType.COMMAND_EXIT:
            return self._command_result(assertion)
        return await self._rubric_result(case, assertion, output)

    def _json_path_result(self, assertion: EvalAssertion, output: str) -> AssertionResult:
        try:
            value: Any = json.loads(output)
            for component in assertion.path.strip("$").strip(".").split("."):
                if component:
                    value = value[int(component)] if isinstance(value, list) else value[component]
            passed = assertion.value is None or value == assertion.value
            return _result(assertion, passed, f"JSON path {assertion.path!r} resolved to {value!r}")
        except (ValueError, KeyError, IndexError, TypeError, json.JSONDecodeError) as exc:
            return _result(assertion, False, f"JSON path check failed: {exc}")

    def _json_schema_result(self, assertion: EvalAssertion, output: str) -> AssertionResult:
        try:
            payload = json.loads(output)
            jsonschema.validate(payload, assertion.schema_def)
            return _result(assertion, True, "Output matches JSON schema")
        except (json.JSONDecodeError, jsonschema.ValidationError, jsonschema.SchemaError) as exc:
            return _result(assertion, False, f"JSON schema check failed: {exc}")

    def _file_diff_result(self, assertion: EvalAssertion) -> AssertionResult:
        actual = (self.root / assertion.path).resolve()
        expected = (self.root / assertion.expected_path).resolve()
        if not _inside(actual, self.root) or not _inside(expected, self.root):
            return _result(assertion, False, "File diff path escapes repository root")
        if not actual.exists() or not expected.exists():
            return _result(assertion, False, "File diff input is missing")
        passed = actual.read_bytes() == expected.read_bytes()
        return _result(assertion, passed, f"Compared {assertion.path} with {assertion.expected_path}")

    def _artifact_field_result(self, assertion: EvalAssertion) -> AssertionResult:
        target = (self.root / assertion.path).resolve()
        if not _inside(target, self.root) or not target.exists():
            return _result(assertion, False, f"Artifact is missing: {assertion.path}")
        text = target.read_text(encoding="utf-8", errors="ignore")
        match = re.search(
            rf"^(?:[-*]\s*)?{re.escape(assertion.field)}\s*:\s*(.+?)\s*$",
            text,
            re.MULTILINE | re.IGNORECASE,
        )
        if not match:
            return _result(assertion, False, f"Artifact field is missing: {assertion.field}")
        value = match.group(1).strip()
        passed = assertion.value is None or value == str(assertion.value)
        return _result(assertion, passed, f"Artifact field {assertion.field} resolved to {value!r}")

    def _command_result(self, assertion: EvalAssertion) -> AssertionResult:
        executable = Path(assertion.command[0]).name
        if executable not in ALLOWED_COMMANDS:
            return _result(assertion, False, f"Command is not allowlisted: {executable}")
        command_error = self._validate_command(assertion.command)
        if command_error:
            return _result(assertion, False, command_error)
        try:
            completed = subprocess.run(
                assertion.command,
                cwd=self.root,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=180,
                check=False,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            return _result(assertion, False, f"Command execution failed: {exc}")
        passed = completed.returncode == assertion.expected_exit
        if assertion.value:
            passed = passed and str(assertion.value).lower() in completed.stdout.lower()
        message = f"Command {shlex.join(assertion.command)} exited {completed.returncode}: {completed.stdout[-500:]}"
        return _result(assertion, passed, message)

    def _validate_command(self, command: list[str]) -> str:
        executable = Path(command[0]).name
        if command[0] != executable:
            return "Command assertions must use an allowlisted executable name without a path"
        if executable in {"python", "python3"}:
            if len(command) < 2 or command[1].startswith("-"):
                return "Python command assertions must invoke a repository script directly"
            script = (self.root / command[1]).resolve()
            if not _inside(script, self.root) or not script.is_file() or script.suffix != ".py":
                return "Python command assertion script is missing or outside the repository"
            relative = script.relative_to(self.root.resolve())
            if not relative.parts or relative.parts[0] != "scripts":
                return "Python command assertions are restricted to scripts/"
            return ""
        if executable == "make":
            if len(command) != 2 or command[1] not in SAFE_MAKE_TARGETS:
                return "Make command assertion target is not allowlisted"
            return ""
        if executable == "git":
            if tuple(command[1:]) not in SAFE_GIT_COMMANDS:
                return "Git command assertion is not an allowlisted read-only operation"
            return ""
        return f"Command is not allowlisted: {executable}"

    async def _rubric_result(
        self,
        case: EvalCase,
        assertion: EvalAssertion,
        output: str,
    ) -> AssertionResult:
        if isinstance(self.reviewer, MockProvider):
            expected = sanitize_remote_text(case.expected_output)
            passed = output.strip() == expected.strip() if expected else bool(output.strip())
            return _result(assertion, passed, "Mock reviewer compared output with the canonical expected output")
        prompt = (
            "Judge one assertion about an agent output. Return only JSON with keys passed (boolean), "
            "score (0 to 1), and reason (string).\n\n"
            f"Task:\n{sanitize_remote_text(case.prompt)}\n\n"
            f"Expected behavior:\n{sanitize_remote_text(case.expected_output)}\n\n"
            f"Assertion:\n{sanitize_remote_text(assertion.text)}\n\n"
            f"Agent output:\n{sanitize_remote_text(output)}"
        )
        response = await self.reviewer.generate(ModelRequest(prompt=prompt, temperature=0.0, max_tokens=500))
        try:
            payload = _extract_json(response.text)
            passed = bool(payload["passed"])
            score = max(0.0, min(1.0, float(payload.get("score", 1.0 if passed else 0.0))))
            return AssertionResult(
                assertion=assertion,
                passed=passed,
                score=score,
                message=str(payload.get("reason", "")),
                tokens=response.input_tokens + response.output_tokens,
                cost_usd=response.cost_usd,
            )
        except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
            return _result(assertion, False, f"Reviewer returned invalid adjudication: {exc}")


def summarize_results(
    results: list[EvalCaseResult],
    *,
    candidate_id: str | None,
    partition: str,
) -> EvalRunSummary:
    score = sum(result.score for result in results) / len(results) if results else 0.0
    by_dimension: dict[str, list[float]] = defaultdict(list)
    for result in results:
        for assertion_result in result.assertions:
            by_dimension[assertion_result.assertion.dimension.value].append(assertion_result.score)
    dimensions = {
        dimension: round(sum(values) / len(values), 6)
        for dimension, values in sorted(by_dimension.items())
        if values
    }
    grouped_scores: dict[str, list[float]] = defaultdict(list)
    for result in results:
        grouped_scores[result.case_id.split("#", 1)[0]].append(result.score)
    case_statistics = {
        case_id: {
            "mean": round(statistics.fmean(values), 6),
            "variance": round(statistics.pvariance(values), 6) if len(values) > 1 else 0.0,
            "repeats": float(len(values)),
        }
        for case_id, values in sorted(grouped_scores.items())
    }
    return EvalRunSummary(
        candidate_id=candidate_id,
        partition=partition,
        score=round(score, 6),
        dimension_scores=dimensions,
        case_statistics=case_statistics,
        critical_pass=all(result.critical_pass for result in results),
        cost={
            "tokens": float(sum(result.tokens for result in results)),
            "cost_usd": round(sum(result.cost_usd for result in results), 8),
            "duration_ms": float(sum(result.duration_ms for result in results)),
        },
        results=results,
    )


def compare_runs(parent: EvalRunSummary, candidate: EvalRunSummary) -> dict[str, Any]:
    parent_cases = _aggregate_cases(parent.results)
    candidate_cases = _aggregate_cases(candidate.results)
    regressions = [
        case_id
        for case_id, parent_score in parent_cases.items()
        if parent_score >= 0.999 and candidate_cases.get(case_id, 0.0) < 0.999
    ]
    parent_target = _target_slice(parent.results)
    candidate_target = _target_slice(candidate.results)
    parent_target_score = statistics.fmean(parent_target.values()) if parent_target else parent.score
    candidate_target_score = statistics.fmean(candidate_target.values()) if candidate_target else candidate.score
    quality_gain = candidate_target_score - parent_target_score
    overall_gain = candidate.score - parent.score
    parent_cost = parent.cost.get("cost_usd", 0.0) or parent.cost.get("tokens", 0.0)
    candidate_cost = candidate.cost.get("cost_usd", 0.0) or candidate.cost.get("tokens", 0.0)
    cost_ratio = candidate_cost / parent_cost if parent_cost else 1.0
    old_parent = _aggregate_cases([item for item in parent.results if item.partition != EvalPartition.INCIDENT])
    old_candidate = _aggregate_cases([item for item in candidate.results if item.partition != EvalPartition.INCIDENT])
    old_deltas = [old_candidate.get(case_id, 0.0) - value for case_id, value in old_parent.items()]
    forgetting = statistics.fmean(max(0.0, -delta) for delta in old_deltas) if old_deltas else 0.0
    backward_transfer = statistics.fmean(old_deltas) if old_deltas else 0.0
    incremental_cost = max(0.0, candidate_cost - parent_cost)
    cost_per_gain = incremental_cost / quality_gain if quality_gain > 0 else float("inf")
    eligible = (
        candidate.critical_pass
        and not regressions
        and quality_gain >= 0.03
        and (cost_ratio <= 1.25 or quality_gain >= 0.05)
    )
    return {
        "eligible": eligible,
        "quality_gain": round(quality_gain, 6),
        "overall_gain": round(overall_gain, 6),
        "target_partition": "incident" if parent_target else "all",
        "target_cases": sorted(parent_target),
        "cost_ratio": round(cost_ratio, 6),
        "cost_per_gain": round(cost_per_gain, 6) if cost_per_gain != float("inf") else "inf",
        "forgetting": round(forgetting, 6),
        "backward_transfer": round(backward_transfer, 6),
        "regressions": regressions,
        "critical_pass": candidate.critical_pass,
    }


def write_eval_result(root: Path, summary: EvalRunSummary) -> Path:
    path = root / ".private" / "evolution" / "eval_runs" / f"{summary.id}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(summary.model_dump_json(indent=2), encoding="utf-8")
    return path


def run_sync(coro: Any) -> Any:
    return asyncio.run(coro)


def _result(assertion: EvalAssertion, passed: bool, message: str) -> AssertionResult:
    return AssertionResult(assertion=assertion, passed=passed, score=1.0 if passed else 0.0, message=message)


def _inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root.resolve())
        return True
    except ValueError:
        return False


def _extract_json(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```(?:json)?\s*|\s*```$", "", stripped, flags=re.IGNORECASE)
    start = stripped.find("{")
    end = stripped.rfind("}")
    if start < 0 or end < start:
        raise json.JSONDecodeError("No JSON object", stripped, 0)
    payload = json.loads(stripped[start : end + 1])
    if not isinstance(payload, dict):
        raise TypeError("Reviewer JSON must be an object")
    return payload


def _aggregate_cases(results: list[EvalCaseResult]) -> dict[str, float]:
    grouped: dict[str, list[float]] = defaultdict(list)
    for result in results:
        grouped[result.case_id.split("#", 1)[0]].append(result.score)
    return {key: sum(values) / len(values) for key, values in grouped.items()}


def _target_slice(results: list[EvalCaseResult]) -> dict[str, float]:
    incident = [result for result in results if result.partition == EvalPartition.INCIDENT]
    return _aggregate_cases(incident) if incident else {}
