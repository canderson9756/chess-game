from src.core.position import Position

from .game_state import GameState

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game.game import Game

class CheckmateState(GameState):
    def handle_move(self, game: 'Game', origin: 'Position', destination: 'Position') -> 'bool':
        return False    # Checkmate, all moves rejected
    
    def is_game_over(self) -> bool:
        return True
    
    def get_status(self) -> str:
        return "Checkmate"