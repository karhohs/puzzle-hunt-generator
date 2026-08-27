"""Base class and helpers for individual puzzle generation."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class Puzzle:
    """Represents a single puzzle in a hunt."""

    name: str
    data: dict[str, Any] = field(default_factory=dict)

    def generate(self) -> dict[str, Any]:
        """Generate puzzle content.  Override in subclasses."""
        return self.data

    def save(self, output_dir: Path) -> Path:
        """Persist the puzzle to *output_dir* as a JSON file."""
        import json

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        dest = output_dir / f"{self.name}.json"
        dest.write_text(json.dumps(self.generate(), indent=2))
        return dest
