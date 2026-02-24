"""Normal playing state for chess games.

This module provides the PlayingState class representing normal gameplay
where the king is not in check.
"""

from src.core.position import Position
from .transitions import determine_next_state

from typing import TYPE_CHECKING
from .game_state import GameState

if TYPE_CHECKING:
    from src.game.game import Game


class PlayingState(GameState):
    """Normal gameplay state where the king is not in check.

    Moves are processed normally and the game transitions to the
    appropriate next state after each move.
    """

    def handle_move(self, game: 'Game', origin: 'Position', destination: 'Position') -> bool:
        """Execute the move and transition to the next state.

        Args:
            game: The game instance.
            origin: Starting position.
            destination: Target position.

        Returns:
            True if the move was successful.
        """
        status = game.execute_move(origin, destination)
        if status:
            next_state = determine_next_state(game)
            game.set_state(next_state)
        return status

    def get_status(self) -> str:
        """Return 'Playing' status."""
        return "Playing"

    def is_game_over(self) -> bool:
        """Game is not over in playing state."""
        return False
    