from src.core.position import Position

from .game_state import GameState

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game.game import Game


class StalemateState(GameState):
    def handle_move(self, game: 'Game', origin: 'Position', destination: 'Position') -> 'bool':
        return False    # No legal moves game over
    
    def get_status(self) -> 'str':
        return "Stalemate"
    
    def is_game_over(self) -> 'bool':
        return True