"""Rook movement strategy.

This module provides the RookStrategy for horizontal and vertical
sliding movement.
"""

from .sliding_strategy import SlidingStrategy
from src.core.direction import Direction


class RookStrategy(SlidingStrategy):
    """Movement strategy for rooks.

    Rooks move horizontally or vertically any number of squares
    in the four cardinal directions.
    """

    @property
    def directions(self) -> list[Direction]:
        """Get the four cardinal directions (up, down, left, right)."""
        return [
            Direction(1, 0),   # Right
            Direction(-1, 0),  # Left
            Direction(0, 1),   # Up
            Direction(0, -1)   # Down
        ]