"""Board management module for the chess game.

This package provides the Board class for managing piece placement,
querying board state, and executing piece movements.
"""

from .board import Board
from .builder import BoardBuilder

__all__ = ["Board", 'BoardBuilder']
