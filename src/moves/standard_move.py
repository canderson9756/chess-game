"""Standard move implementation for chess pieces.

This module provides the StandardMove class which handles basic chess piece
movements from one position to another. It implements the Command pattern,
allowing moves to be executed and undone.
"""

from src.board.board import Board
from .move import Move


class StandardMove(Move):
    """A standard chess move that relocates a piece from one position to another.

    Represents a basic move where a piece moves from its origin to a destination
    square, with no captures or special rules. Inherits piece, origin, and
    destination from Move.

    Example:
        >>> move = StandardMove(pawn, Position(1, 2), Position(1, 4))
        >>> move.execute(board)  # Moves the pawn to the new position
        >>> move.undo(board)     # Returns the pawn to its original position
    """

    def execute(self, board: 'Board') -> None:
        """Move the piece from origin to destination on the board.

        Args:
            board: The board to update.
        """
        board.move_piece(self.origin, self.destination)

    def undo(self, board: 'Board') -> None:
        """Reverse the move by returning the piece from destination to origin.

        Args:
            board: The board to revert.
        """
        board.move_piece(self.destination, self.origin)