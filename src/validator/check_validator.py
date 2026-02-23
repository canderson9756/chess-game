from .validator import Validator

from src.board.board import Board
from src.moves.move import Move
from src.pieces.concrete.king import King

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.colour import Colour

class CheckValidator(Validator):
    def _do_validate(self, move: Move, board: Board) -> bool:
        move.execute(board)
        king: 'King' = board.find_king(move.piece.colour)

        in_check = board.is_square_attacked(king.position, move.piece.colour.opposite())

        move.undo(board)

        return not in_check


 