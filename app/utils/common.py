import os
from typing import Any


def getenv_or_404(key: str, default: Any = None):
    import os

    value = os.environ.get(key, default)
    if not value:
        raise ValueError(f"Environment variable {key} required but not found")
    return value
