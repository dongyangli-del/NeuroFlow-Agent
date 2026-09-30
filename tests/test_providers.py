from __future__ import annotations

import neuroflow_runtime.providers as providers
import pytest
from neuroflow_runtime.providers import (
    AnthropicProvider,
    ModelRequest,
    OllamaProvider,
    OpenAICompatibleProvider,
    reviewers_are_independent,
)


@pytest.mark.parametrize(
    ("provider", "payload", "expected"),
    [
        (
            OpenAICompatibleProvider("openai-model", "key"),
            {"choices": [{"message": {"content": "openai"}}], "usage": {"prompt_tokens": 2, "completion_tokens": 1}},
            "openai",
        ),
        (
            AnthropicProvider("anthropic-model", "key"),
            {"content": [{"type": "text", "text": "anthropic"}], "usage": {"input_tokens": 2, "output_tokens": 1}},
            "anthropic",
        ),
        (
            OllamaProvider("ollama-model"),
            {"message": {"content": "ollama"}, "prompt_eval_count": 2, "eval_count": 1},
            "ollama",
        ),
    ],
)
def test_provider_adapters_parse_responses(
    provider,
    payload: dict,
    expected: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    async def fake_post(url, body, headers):
        return payload

    monkeypatch.setattr(providers, "_post_json", fake_post)
    response = __import__("asyncio").run(provider.generate(ModelRequest(prompt="test")))
    assert response.text == expected
    assert response.input_tokens == 2
    assert response.output_tokens == 1


def test_reviewer_independence_uses_provider_and_model_identity() -> None:
    assert reviewers_are_independent(
        OpenAICompatibleProvider("executor", "key"),
        AnthropicProvider("reviewer", "key"),
    )
    assert not reviewers_are_independent(
        OpenAICompatibleProvider("same", "key"),
        OpenAICompatibleProvider("same", "key"),
    )
