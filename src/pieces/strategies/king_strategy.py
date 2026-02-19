"""King movement strategy.

This module provides the KingStrategy for single-square movement
in any direction.
"""

from src.board.board import Board
from src.core.position import Position
from src.pieces.base.piece import Piece
from .move_strategy import MoveStrategy
from src.core.direction import Direction

KING_MOVES: list[Direction] = [
    Direction(0, 1),    # Up
    Direction(1, 1),    # Up-right
    Direction(1, 0),    # Right
    Direction(1, -1),   # Down-right
    Direction(0, -1),   # Down
    Direction(-1, -1),  # Down-left
    Direction(-1, 0),   # Left
    Direction(-1, 1)    # Up-left
]
"""All eight directions a king can move (one square each)."""


class KingStrategy(MoveStrategy):
    """Movement strategy for kings.

    Kings move one square in any of the eight directions. This strategy
    does not currently implement castling or check detection.
    """

    def get_legal_moves(self, piece: Piece, board: 'Board') -> list[Position]:
        """Calculate all legal single-square moves for the king.

        Args:
            piece: The king to calculate moves for.
            board: The current board state.

        Returns:
            A list of valid destination positions.
        """
        moves: list[Position] = []
        for move in KING_MOVES:
            target = piece.position + move
            if target.is_valid():
                if board.has_friendly_piece(target, piece.colour):
                    continue
                moves.append(target)
        return moves