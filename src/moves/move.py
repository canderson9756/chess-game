"""Abstract base class for chess moves.

This module defines the Move abstract class implementing the Command
pattern for chess move execution and reversal.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.position import Position
    from src.pieces.base.piece import Piece
    from src.board.board import Board


class Move(ABC):
    """Abstract base class for chess moves using the Command pattern.

    Move encapsulates a chess move as an object with execute and undo
    capabilities. This allows for move history tracking, game replay,
    and move reversal.

    Attributes:
        piece: The piece being moved.
        origin: The starting position of the move.
        destination: The target position for the move.

    Example:
        >>> move = StandardMove(knight, Position(1, 0), Position(2, 2))
        >>> move.execute()  # Apply the move
        >>> move.undo()     # Revert to previous state
    """

    def __init__(self, piece: "Piece", origin: "Position", destination: "Position"):
        """Initialize a move with piece and positions.

        Args:
            piece: The piece being moved.
            origin: The starting position.
            destination: The target position.
        """
        self.piece = piece
        self.origin = origin
        self.destination = destination

    @abstractmethod
    def execute(self, board: "Board") -> None:
        """Apply the move to the board.

        Args:
            board: The board to update.
        """
        pass

    @abstractmethod
    def undo(self, board: "Board") -> None:
        """Reverse the move on the board.

        Args:
            board: The board to revert.
        """
        pass
