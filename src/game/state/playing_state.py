from src.core.position import Position
from .transitions import determine_next_state

from typing import TYPE_CHECKING
from .game_state import GameState

if TYPE_CHECKING:
    from src.game.game import Game

class PlayingState(GameState):
    def handle_move(self, game: 'Game', origin: 'Position', destination: 'Position') -> bool:
        status = game.execute_move(origin, destination)
        if status:
            next_state = determine_next_state(game)
            game.set_state(next_state)
        return status
    
    def get_status(self) -> str:
        return "Playing"
    
    def is_game_over(self) -> bool:
        return False
    