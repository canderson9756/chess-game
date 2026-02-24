from abc import ABC, abstractmethod

from src.core.position import Position
from src.core.colour import Colour
from src.board.board import Board

class GameAdapter(ABC):

    @abstractmethod
    def display_board(self, board: 'Board') -> None:
        pass

    @abstractmethod
    def get_move_input(self) -> 'tuple[Position, Position]':
        pass

    @abstractmethod
    def show_message(self, message: 'str') -> None:
        pass

    @abstractmethod
    def show_error(self, error: 'str') -> None:
        pass

    @abstractmethod
    def show_game_over(self, result: 'str', winner: 'Colour | None') -> None:
        pass