"""King piece implementation.

This module provides the King class representing the king chess piece
with single-square movement in any direction.
"""

from src.core.position import Position
from src.pieces.base.piece import Piece
from src.core.colour import Colour
from src.pieces.strategies.king_strategy import KingStrategy
from src.board.board import Board


class King(Piece):
    """A king chess piece.

    Kings can move one square in any direction (horizontally, vertically,
    or diagonally). The king is the most important piece; the game ends
    when a king is checkmated.
    """

    def __init__(self, position: "Position", colour: "Colour"):
        """Initialize a king at the given position.

        Args:
            position: The starting position.
            colour: The king's colour.
        """
        super().__init__(position, colour)
        self._strategy = KingStrategy()

    def get_legal_moves(self, board: "Board") -> list[Position]:
        """Get all legal moves for this king.

        Args:
            board: The current board state.

        Returns:
            List of valid positions the king can move to.
        """
        return self._strategy.get_legal_moves(self, board)
    
    def get_attack_moves(self, board: 'Board') -> list[Position]:
        return self._strategy.get_attack_moves(self, board)
