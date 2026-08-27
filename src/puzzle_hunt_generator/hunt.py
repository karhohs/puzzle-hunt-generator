"""Puzzle hunt orchestration — combines individual puzzles into a full hunt."""

from __future__ import annotations

from pathlib import Path

from puzzle_hunt_generator.puzzle import Puzzle


class PuzzleHunt:
    """Orchestrates a collection of puzzles into a complete hunt."""

    def __init__(self, name: str, output_dir: str | Path = "puzzles") -> None:
        self.name = name
        self.output_dir = Path(output_dir)
        self.puzzles: list[Puzzle] = []

    def add_puzzle(self, puzzle: Puzzle) -> None:
        """Add a puzzle to the hunt."""
        self.puzzles.append(puzzle)

    def generate(self) -> list[Path]:
        """Generate all puzzles and return their output paths."""
        paths: list[Path] = []
        for puzzle in self.puzzles:
            paths.append(puzzle.save(self.output_dir))
        return paths
