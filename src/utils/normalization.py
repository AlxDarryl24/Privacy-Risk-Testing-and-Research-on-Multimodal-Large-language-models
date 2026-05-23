"""Utility functions for label normalization."""


def normalize_text(value: str) -> str:
    if value is None:
        return "unknown"
    return str(value).strip().lower()


def normalize_unknown(value: str) -> str:
    value = normalize_text(value)
    if value in {"", "n/a", "none", "not sure", "unknown", "uncertain"}:
        return "unknown"
    return value
