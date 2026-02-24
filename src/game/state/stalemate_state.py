"""Stalemate state representing game over by stalemate.

This module provides the StalemateState class for when a player has
no legal moves but is not in check (draw).
"""

from src.core.position import Position

from .game_state import GameState

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game.game import Game


class StalemateState(GameState):
    """Game over state - stalemate (draw).

    The current player is not in check but has no legal moves.
    All move attempts are rejected.
    """

    def handle_move(self, game: 'Game', origin: 'Position', destination: 'Position') -> 'bool':
        """Reject all moves - game is over.

        Returns:
            Always False as no moves are allowed after stalemate.
        """
        return False

    def get_status(self) -> 'str':
        """Return 'Stalemate' status."""
        return "Stalemate"

    def is_game_over(self) -> 'bool':
        """Game is over in stalemate state."""
        return True