"""Bishop movement strategy.

This module provides the BishopStrategy for diagonal sliding movement.
"""

from .sliding_strategy import SlidingStrategy
from src.core.direction import Direction


class BishopStrategy(SlidingStrategy):
    """Movement strategy for bishops.

    Bishops move diagonally any number of squares in the four
    diagonal directions.
    """
    @property
    def directions(self) -> list[Direction]:
        """Get the four diagonal directions."""
        return [
            Direction(1, 1),  # Up-right
            Direction(-1, 1),  # Up-left
            Direction(-1, -1),  # Down-left
            Direction(1, -1),  # Down-right
        ]
