from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.position import Position
    from src.game.game import Game

class GameState(ABC):
    @abstractmethod
    def handle_move(self, game: 'Game', origin: 'Position', destination: 'Position') -> bool:
        pass

    @abstractmethod
    def get_status(self) -> str:
        """Return current game status"""
        pass

    @abstractmethod
    def is_game_over(self) -> bool:
        """Is the game finished?"""
        pass

