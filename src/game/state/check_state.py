from .game_state import GameState
from src.core.position import Position

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.game.game import Game

class CheckState(GameState):
    def handle_move(self, game: 'Game', origin: 'Position', destination: 'Position') -> 'bool':
        status = game.execute_move(origin, destination)
        if status:
            self._determine_next_state(game)
        return status
    
    def get_status(self) -> 'str':
        return "Check"
    
    def is_game_over(self) -> 'bool':
        return False
    
    def _determine_next_state(self, game: 'Game'):
        pass