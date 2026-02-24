"""Checkmate state representing game over by checkmate.

This module provides the CheckmateState class for when a player's king
is in check with no legal moves to escape.
"""

from src.core.position import Position

from .game_state import GameState

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game.game import Game


class CheckmateState(GameState):
    """Game over state - checkmate.

    The king is in check and there are no legal moves to escape.
    All move attempts are rejected.
    """

    def handle_move(self, game: 'Game', origin: 'Position', destination: 'Position') -> 'bool':
        """Reject all moves - game is over.

        Returns:
            Always False as no moves are allowed after checkmate.
        """
        return False

    def is_game_over(self) -> bool:
        """Game is over in checkmate state."""
        return True

    def get_status(self) -> str:
        """Return 'Checkmate' status."""
        return "Checkmate"