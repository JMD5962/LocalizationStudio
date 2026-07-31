"""
Application document model.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class Document:
    """Current opened localization document."""

    path: Path | None = None

    data: dict[str, Any] = field(default_factory=dict)

    modified: bool = False

    @property
    def filename(self) -> str:
        if self.path is None:
            return "Untitled"

        return self.path.name

    @property
    def is_open(self) -> bool:
        return self.path is not None