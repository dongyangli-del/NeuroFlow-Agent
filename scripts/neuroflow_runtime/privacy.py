"""Shared redaction rules for text crossing the local runtime boundary."""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class SensitivePattern:
    pattern: re.Pattern[str]
    label: str
    replacement: str


SENSITIVE_PATTERNS = (
    SensitivePattern(
        re.compile(r"(?<![A-Za-z0-9:])" + "/" + r"vePFS-[^\s)>\"]+"),
        "private path",
        "[private-path]",
    ),
    SensitivePattern(
        re.compile(r"(?<![A-Za-z0-9:])/home/[^\s)>\"]+"),
        "private path",
        "[private-path]",
    ),
    SensitivePattern(
        re.compile(r"(?<![A-Za-z0-9:])" + "/" + r"Users/[^\s)>\"]+"),
        "private path",
        "[private-path]",
    ),
    SensitivePattern(re.compile(r"AKIA[0-9A-Z]{16}"), "AWS credential", "[credential]"),
    SensitivePattern(re.compile(r"AIza[0-9A-Za-z_-]{35}"), "Google credential", "[credential]"),
    SensitivePattern(re.compile(r"gh[pousr]_[0-9A-Za-z_]{20,}"), "GitHub credential", "[credential]"),
    SensitivePattern(re.compile(r"sk-[A-Za-z0-9]{20,}"), "API credential", "[credential]"),
    SensitivePattern(
        re.compile(r"BEGIN (?:RSA|OPENSSH|EC|DSA) PRIVATE KEY"),
        "private key",
        "[private-key]",
    ),
    SensitivePattern(
        re.compile(r"\b(?:participant|subject)[-_ ]?(?:id[-_ ]?)?[A-Z]*\d{2,}\b", re.IGNORECASE),
        "participant identifier",
        "[participant-id]",
    ),
)


def sensitive_labels(text: str) -> list[str]:
    """Return stable labels for sensitive patterns present in text."""
    return sorted({item.label for item in SENSITIVE_PATTERNS if item.pattern.search(text)})


def sanitize_remote_text(text: str, *, max_chars: int | None = None) -> str:
    """Redact local paths, credentials, and participant-like identifiers."""
    sanitized = text
    for item in SENSITIVE_PATTERNS:
        sanitized = item.pattern.sub(item.replacement, sanitized)
    return sanitized[:max_chars] if max_chars is not None else sanitized
