"""Bishop piece implementation.

This module provides the Bishop class representing the bishop chess piece
with diagonal sliding movement.
"""

from src.core.position import Position
from src.pieces.base.piece import Piece
from src.core.colour import Colour
from src.pieces.strategies.bishop_strategy import BishopStrategy
from src.board.board import Board


class Bishop(Piece):
    """A bishop chess piece.

    Bishops move diagonally any number of squares. They cannot jump
    over other pieces.
    """

    def __init__(self, position: "Position", colour: "Colour"):
        """Initialize a bishop at the given position.

        Args:
            position: The starting position.
            colour: The bishop's colour.
        """
        super().__init__(position, colour)
        self._strategy = BishopStrategy()

    def get_legal_moves(self, board: "Board") -> list[Position]:
        """Get all legal moves for this bishop.

        Args:
            board: The current board state.

        Returns:
            List of valid positions the bishop can move to.
        """
        return self._strategy.get_legal_moves(self, board)
