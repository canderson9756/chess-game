"""Abstract base class for chess moves.

This module defines the Move abstract class implementing the Command
pattern for chess move execution and reversal.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.position import Position
    from src.pieces.base.piece import Piece


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

    def __init__(self, piece: 'Piece', origin: 'Position', destination: 'Position'):
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
    def execute(self) -> None:
        """Execute the move, updating the game state.

        Subclasses must implement this to apply the move's effects
        to the board and pieces.
        """
        pass

    @abstractmethod
    def undo(self) -> None:
        """Undo the move, reverting to the previous state.

        Subclasses must implement this to reverse the move's effects
        and restore the previous game state.
        """
        pass