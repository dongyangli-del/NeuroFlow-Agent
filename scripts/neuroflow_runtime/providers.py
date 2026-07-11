"""Model-provider adapters used for candidate generation and independent review."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from typing import Any, Protocol

import httpx


@dataclass(frozen=True)
class ModelRequest:
    prompt: str
    system: str = ""
    temperature: float = 0.0
    max_tokens: int = 4096
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ModelResponse:
    text: str
    provider: str
    model: str
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float = 0.0
    raw: dict[str, Any] = field(default_factory=dict)


class ModelProvider(Protocol):
    name: str
    model: str

    async def generate(self, request: ModelRequest) -> ModelResponse: ...


class ProviderError(RuntimeError):
    pass


class OpenAICompatibleProvider:
    name = "openai"

    def __init__(self, model: str, api_key: str, base_url: str = "https://api.openai.com/v1") -> None:
        self.model = model
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    async def generate(self, request: ModelRequest) -> ModelResponse:
        messages = []
        if request.system:
            messages.append({"role": "system", "content": request.system})
        messages.append({"role": "user", "content": request.prompt})
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": request.temperature,
            "max_tokens": request.max_tokens,
        }
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = await _post_json(f"{self.base_url}/chat/completions", payload, headers)
        try:
            text = data["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise ProviderError("OpenAI-compatible response is missing message content") from exc
        usage = data.get("usage", {})
        return ModelResponse(
            text=str(text),
            provider=self.name,
            model=self.model,
            input_tokens=int(usage.get("prompt_tokens", 0)),
            output_tokens=int(usage.get("completion_tokens", 0)),
            cost_usd=float(usage.get("cost_usd", data.get("cost_usd", 0.0))),
            raw=data,
        )


class AnthropicProvider:
    name = "anthropic"

    def __init__(self, model: str, api_key: str, base_url: str = "https://api.anthropic.com") -> None:
        self.model = model
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    async def generate(self, request: ModelRequest) -> ModelResponse:
        payload: dict[str, Any] = {
            "model": self.model,
            "messages": [{"role": "user", "content": request.prompt}],
            "temperature": request.temperature,
            "max_tokens": request.max_tokens,
        }
        if request.system:
            payload["system"] = request.system
        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
        }
        data = await _post_json(f"{self.base_url}/v1/messages", payload, headers)
        try:
            text = "".join(block.get("text", "") for block in data["content"] if block.get("type") == "text")
        except (KeyError, TypeError) as exc:
            raise ProviderError("Anthropic response is missing text content") from exc
        usage = data.get("usage", {})
        return ModelResponse(
            text=text,
            provider=self.name,
            model=self.model,
            input_tokens=int(usage.get("input_tokens", 0)),
            output_tokens=int(usage.get("output_tokens", 0)),
            cost_usd=float(usage.get("cost_usd", data.get("cost_usd", 0.0))),
            raw=data,
        )


class OllamaProvider:
    name = "ollama"

    def __init__(self, model: str, base_url: str = "http://127.0.0.1:11434") -> None:
        self.model = model
        self.base_url = base_url.rstrip("/")

    async def generate(self, request: ModelRequest) -> ModelResponse:
        messages = []
        if request.system:
            messages.append({"role": "system", "content": request.system})
        messages.append({"role": "user", "content": request.prompt})
        data = await _post_json(
            f"{self.base_url}/api/chat",
            {
                "model": self.model,
                "messages": messages,
                "stream": False,
                "options": {"temperature": request.temperature, "num_predict": request.max_tokens},
            },
            {},
        )
        try:
            text = data["message"]["content"]
        except (KeyError, TypeError) as exc:
            raise ProviderError("Ollama response is missing message content") from exc
        return ModelResponse(
            text=str(text),
            provider=self.name,
            model=self.model,
            input_tokens=int(data.get("prompt_eval_count", 0)),
            output_tokens=int(data.get("eval_count", 0)),
            raw=data,
        )


class MockProvider:
    name = "mock"

    def __init__(self, model: str = "deterministic", response: str | None = None) -> None:
        self.model = model
        self.response = response

    async def generate(self, request: ModelRequest) -> ModelResponse:
        text = self.response
        if text is None:
            text = str(request.metadata.get("mock_response", request.metadata.get("expected_output", request.prompt)))
        return ModelResponse(
            text=text,
            provider=self.name,
            model=self.model,
            input_tokens=len(request.prompt.split()),
            output_tokens=len(text.split()),
        )


def load_provider(role: str, explicit_name: str = "") -> ModelProvider:
    prefix = f"NEUROFLOW_{role.upper()}_"
    name = (explicit_name or os.environ.get(f"{prefix}PROVIDER", "mock")).strip().lower()
    model = os.environ.get(f"{prefix}MODEL", "").strip()
    base_url = os.environ.get(f"{prefix}BASE_URL", "").strip()
    api_key = os.environ.get(f"{prefix}API_KEY", "").strip()
    if name in {"openai", "openai-compatible"}:
        model = model or "gpt-5-mini"
        api_key = api_key or os.environ.get("OPENAI_API_KEY", "")
        if not api_key:
            raise ProviderError(f"{prefix}API_KEY or OPENAI_API_KEY is required")
        return OpenAICompatibleProvider(model, api_key, base_url or "https://api.openai.com/v1")
    if name == "anthropic":
        model = model or "claude-sonnet-4-5"
        api_key = api_key or os.environ.get("ANTHROPIC_API_KEY", "")
        if not api_key:
            raise ProviderError(f"{prefix}API_KEY or ANTHROPIC_API_KEY is required")
        return AnthropicProvider(model, api_key, base_url or "https://api.anthropic.com")
    if name == "ollama":
        return OllamaProvider(model or "qwen3:8b", base_url or "http://127.0.0.1:11434")
    if name == "mock":
        return MockProvider(model or "deterministic", os.environ.get(f"{prefix}MOCK_RESPONSE"))
    raise ProviderError(f"Unknown model provider: {name}")


def reviewers_are_independent(executor: ModelProvider, reviewer: ModelProvider) -> bool:
    return (executor.name, executor.model) != (reviewer.name, reviewer.model)


async def _post_json(url: str, payload: dict[str, Any], headers: dict[str, str]) -> dict[str, Any]:
    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(120.0)) as client:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
    except (httpx.HTTPError, json.JSONDecodeError) as exc:
        raise ProviderError(f"Provider request failed for {url}: {exc}") from exc
    if not isinstance(result, dict):
        raise ProviderError(f"Provider returned a non-object response for {url}")
    return result
