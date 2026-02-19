"""Core domain objects for the chess game.

This package provides the fundamental building blocks for representing
chess concepts: board positions, piece colours, and movement directions.

Classes:
    Colour: Enum representing piece colours (WHITE, BLACK).
    Direction: Immutable vector for movement calculations.
    Position: Immutable board square with algebraic notation support.
"""

from .colour import Colour
from .direction import Direction
from .position import Position

__all__ = ["Colour", "Direction", "Position"]
