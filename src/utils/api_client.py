"""Placeholder API client.

Replace this file with your actual OpenAI/OpenRouter/Gemini API calling logic.
Never hard-code API keys in this file. Use environment variables instead.
"""

import os


def get_api_key(env_name: str) -> str:
    key = os.getenv(env_name)
    if not key:
        raise RuntimeError(f"Missing API key environment variable: {env_name}")
    return key


def call_model(prompt: str, model: str, **kwargs) -> str:
    raise NotImplementedError("Add your model API calling logic here.")
