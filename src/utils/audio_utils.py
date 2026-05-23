"""Audio utility functions."""

import base64
from pathlib import Path


def audio_to_base64(path: str) -> str:
    data = Path(path).read_bytes()
    return base64.b64encode(data).decode("utf-8")
