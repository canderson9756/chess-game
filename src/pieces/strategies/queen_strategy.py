"""Queen movement strategy.

This module provides the QueenStrategy combining rook and bishop movement.
"""

from .sliding_strategy import SlidingStrategy
from src.core.direction import Direction


class QueenStrategy(SlidingStrategy):
    """Movement strategy for queens.

    Queens combine rook and bishop movement, sliding any number of
    squares in all eight directions (horizontal, vertical, and diagonal).
    """

    @property
    def directions(self) -> list[Direction]:
        """Get all eight directions (cardinal and diagonal)."""
        return [
            # Diagonal directions
            Direction(1, 1),  # Up-right
            Direction(-1, 1),  # Up-left
            Direction(-1, -1),  # Down-left
            Direction(1, -1),  # Down-right
            # Cardinal directions
            Direction(1, 0),  # Right
            Direction(-1, 0),  # Left
            Direction(0, 1),  # Up
            Direction(0, -1),  # Down
        ]
