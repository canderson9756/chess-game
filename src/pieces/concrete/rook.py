"""Rook piece implementation.

This module provides the Rook class representing the rook chess piece
with horizontal and vertical sliding movement.
"""

from src.core.position import Position
from src.pieces.base.piece import Piece
from src.core.colour import Colour
from src.pieces.strategies.rook_strategy import RookStrategy
from src.board.board import Board


class Rook(Piece):
    """A rook chess piece.

    Rooks move horizontally or vertically any number of squares.
    They cannot jump over other pieces.
    """

    def __init__(self, position: "Position", colour: "Colour"):
        """Initialize a rook at the given position.

        Args:
            position: The starting position.
            colour: The rook's colour.
        """
        super().__init__(position, colour)
        self._strategy = RookStrategy()

    def get_legal_moves(self, board: "Board") -> list[Position]:
        """Get all legal moves for this rook.

        Args:
            board: The current board state.

        Returns:
            List of valid positions the rook can move to.
        """
        return self._strategy.get_legal_moves(self, board)
