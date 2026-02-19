"""Knight movement strategy.

This module provides the KnightStrategy for L-shaped jumping movement.
"""

from .move_strategy import MoveStrategy
from src.core.direction import Direction
from src.core.position import Position
from src.pieces.base.piece import Piece
from src.board.board import Board

KNIGHT_MOVES: list[Direction] = [
    Direction(1, 2), Direction(2, 1),
    Direction(-1, 2), Direction(-2, 1),
    Direction(1, -2), Direction(2, -1),
    Direction(-1, -2), Direction(-2, -1),
]
"""All eight possible L-shaped moves for a knight."""


class KnightStrategy(MoveStrategy):
    """Movement strategy for knights.

    Knights move in an L-shape: two squares in one direction and one
    square perpendicular. Unlike other pieces, knights can jump over
    pieces in their path.
    """

    def get_legal_moves(self, piece: 'Piece', board: 'Board') -> list['Position']:
        """Calculate all legal L-shaped moves for the knight.

        Args:
            piece: The knight to calculate moves for.
            board: The current board state.

        Returns:
            A list of valid destination positions.
        """
        moves: list['Position'] = []
        for move in KNIGHT_MOVES:
            target = piece.position + move
            if target.is_valid():
                if board.has_friendly_piece(target, piece.colour):
                    continue
                moves.append(target)
        return moves