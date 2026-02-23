from abc import ABC, abstractmethod
from src.moves.move import Move
from src.board.board import Board

class Validator(ABC):

    def __init__(self):
        self._next: 'Validator | None' = None

    def set_next(self, next_validator: 'Validator'):
        self._next = next_validator

    def validate(self, move: 'Move', board: 'Board') -> 'bool | None | Validator':
        if not self._do_validate(move, board): 
            return False
        if self._next:
            return self._next.validate(move, board) #type: ignore
        return True
            
    @abstractmethod
    def _do_validate(self, move: 'Move', board: 'Board') -> 'bool':
        pass