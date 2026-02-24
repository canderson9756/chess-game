"""Abstract base class for game states.

This module defines the GameState interface used by the State pattern
to handle moves differently based on the current game situation.
"""

from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.position import Position
    from src.game.game import Game


class GameState(ABC):
    """Abstract base class for game states in the State pattern.

    Each state handles moves according to its rules and transitions
    to appropriate states after moves are made.
    """

    @abstractmethod
    def handle_move(self, game: 'Game', origin: 'Position', destination: 'Position') -> bool:
        """Handle a move attempt in this state.

        Args:
            game: The game instance.
            origin: Starting position.
            destination: Target position.

        Returns:
            True if move was successful, False otherwise.
        """
        pass

    @abstractmethod
    def get_status(self) -> str:
        """Return the current game status string.

        Returns:
            Status description (e.g., "Playing", "Check", "Checkmate").
        """
        pass

    @abstractmethod
    def is_game_over(self) -> bool:
        """Check if the game has ended in this state.

        Returns:
            True if game is over, False if play continues.
        """
        pass

