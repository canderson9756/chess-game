from src.board.board import Board
from src.moves.move import Move
from .validator import Validator

class CheckValidator(Validator):
    def _do_validate(self, move: Move, board: Board) -> bool:
        return False