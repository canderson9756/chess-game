"""Knight piece implementation.

This module provides the Knight class representing the knight chess piece
with its L-shaped movement pattern.
"""

from src.core.position import Position
from src.pieces.base.piece import Piece
from src.core.colour import Colour
from src.pieces.strategies.knight_strategy import KnightStrategy
from src.board.board import Board


class Knight(Piece):
    """A knight chess piece.

    Knights move in an L-shape: two squares in one direction and one
    square perpendicular. Knights can jump over other pieces.
    """

    def __init__(self, position: "Position", colour: "Colour"):
        """Initialize a knight at the given position.

        Args:
            position: The starting position.
            colour: The knight's colour.
        """
        super().__init__(position, colour)
        self._strategy = KnightStrategy()

    def get_legal_moves(self, board: "Board") -> list[Position]:
        """Get all legal moves for this knight.

        Args:
            board: The current board state.

        Returns:
            List of valid positions the knight can move to.
        """
        return self._strategy.get_legal_moves(self, board)
