"""Pawn piece implementation.

This module provides the Pawn class representing the pawn chess piece
with its unique movement rules.
"""

from src.core.position import Position
from src.pieces.base.piece import Piece
from src.core.colour import Colour
from src.pieces.strategies.pawn_strategy import PawnStrategy
from src.board.board import Board


class Pawn(Piece):
    """A pawn chess piece.

    Pawns move forward one square (or two on their first move) and
    capture diagonally. They are the only pieces that move differently
    when capturing vs. advancing.

    Attributes:
        first_move: True if the pawn hasn't moved yet, enabling the
            two-square advance option.
    """

    def __init__(self, position: 'Position', colour: 'Colour'):
        """Initialize a pawn at the given position.

        Args:
            position: The starting position.
            colour: The pawn's colour.
        """
        super().__init__(position, colour)
        self._strategy = PawnStrategy()
        self.first_move = True

    def get_legal_moves(self, board: 'Board') -> list[Position]:
        """Get all legal moves for this pawn.

        Args:
            board: The current board state.

        Returns:
            List of valid positions the pawn can move to.
        """
        return self._strategy.get_legal_moves(self, board)