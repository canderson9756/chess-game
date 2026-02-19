from abc import ABC, abstractmethod
from src.core.colour import Colour
from src.core.position import Position

class Piece(ABC):
    
    def __init__(self, position: 'Position', colour: 'Colour'):
        self._position = position
        self._colour = colour

    @property
    def position(self) -> 'Position':
        return self._position

    @property
    def colour(self) -> 'Colour':
        return self._colour
    
    @abstractmethod
    def get_legal_moves(self, board: 'Board') -> list['Position']:
        pass

    def move_to(self, position: 'Position') -> None:
        self._position = position

    def is_enemy(self, colour: 'Colour'):
        return True if colour!=self.colour else False