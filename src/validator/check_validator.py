"""Check validator to ensure moves don't leave the king in check.

This module provides the CheckValidator class which validates that a move
doesn't result in the moving player's king being in check.
"""

from .validator import Validator

from src.board.board import Board
from src.moves.move import Move
from src.pieces.base.piece import Piece


class CheckValidator(Validator):
    """Validator that ensures a move doesn't leave the king in check.

    This validator temporarily executes the move, checks if the king would
    be in check, then undoes the move. The move is only valid if the king
    is not in check after the move.
    """

    def _do_validate(self, move: Move, board: Board) -> bool:
        """Check if the move would leave the king in check.

        Args:
            move: The move to validate.
            board: The current board state.

        Returns:
            True if the king is NOT in check after the move, False otherwise.
        """
        move.execute(board)
        king: 'Piece' = board.find_king(move.piece.colour)

        in_check = board.is_square_attacked(king.position, move.piece.colour.opposite())

        move.undo(board)

        return not in_check


 