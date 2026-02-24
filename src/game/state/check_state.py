"""Check state for when the king is in check.

This module provides the CheckState class representing the game state
when the current player's king is under attack.
"""

from .game_state import GameState
from src.core.position import Position
from .transitions import determine_next_state
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game.game import Game


class CheckState(GameState):
    """Game state when the current player's king is in check.

    The player must make a move that gets out of check. The validator
    ensures only legal moves (that escape check) are allowed.
    """

    def handle_move(self, game: 'Game', origin: 'Position', destination: 'Position') -> 'bool':
        """Execute a move that must escape check.

        Args:
            game: The game instance.
            origin: Starting position.
            destination: Target position.

        Returns:
            True if the move was successful and escapes check.
        """
        status = game.execute_move(origin, destination)
        if status:
            next_state = determine_next_state(game)
            game.set_state(next_state)
        return status

    def get_status(self) -> 'str':
        """Return 'Check' status."""
        return "Check"

    def is_game_over(self) -> 'bool':
        """Game is not over in check state (player can still move)."""
        return False
