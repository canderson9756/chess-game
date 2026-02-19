"""Pawn movement strategy.

This module provides the PawnStrategy for pawn movement including
forward advancement and diagonal captures.
"""

from src.board.board import Board
from src.core.position import Position
from src.pieces.base.piece import Piece
from .move_strategy import MoveStrategy
from src.core.direction import Direction


class PawnStrategy(MoveStrategy):
    """Movement strategy for pawns.

    Pawns have unique movement rules:
    - Move forward one square (two squares on first move)
    - Cannot move forward if blocked
    - Capture diagonally
    - This implementation does not include en passant or promotion.
    """

    def get_legal_moves(self, piece: Piece, board: 'Board') -> list[Position]:
        """Calculate all legal moves for a pawn.

        Includes forward movement (one or two squares on first move)
        and diagonal captures.

        Args:
            piece: The pawn to calculate moves for.
            board: The current board state.

        Returns:
            A list of valid destination positions.
        """
        moves: list[Position] = []
        direction = piece.colour.direction()

        # Forward movement
        forward = piece.position + Direction(0, direction)
        if forward.is_valid() and not board.is_occupied(forward):
            moves.append(forward)
            # Two-square advance on first move
            if piece.first_move:  # type: ignore
                forward = forward + Direction(0, direction)
                if forward.is_valid() and not board.is_occupied(forward):
                    moves.append(forward)

        # Diagonal captures
        dx = [-1, 1]
        for capture_direction in dx:
            diagonal = piece.position + Direction(capture_direction, direction)
            if diagonal.is_valid() and board.has_enemy_piece(diagonal, piece.colour):
                moves.append(diagonal)

        return moves