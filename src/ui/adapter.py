"""Abstract UI adapter interface.

This module provides the GameAdapter abstract class that defines
the interface for different UI implementations.
"""

from abc import ABC, abstractmethod

from src.core.position import Position
from src.core.colour import Colour
from src.board.board import Board


class GameAdapter(ABC):
    """Abstract interface for game UI implementations.

    GameAdapter defines the contract for user interface components.
    Implement this interface to create CLI, GUI, or web-based interfaces.

    Example:
        >>> class CLIAdapter(GameAdapter):
        ...     def display_board(self, board):
        ...         # Print ASCII board representation
        ...         pass
    """

    @abstractmethod
    def display_board(self, board: 'Board') -> None:
        """Display the current board state.

        Args:
            board: The board to display.
        """
        pass

    @abstractmethod
    def get_move_input(self) -> 'tuple[Position, Position]':
        """Get move input from the user.

        Returns:
            A tuple of (origin, destination) positions.
        """
        pass

    @abstractmethod
    def show_message(self, message: 'str') -> None:
        """Display an informational message to the user.

        Args:
            message: The message to display.
        """
        pass

    @abstractmethod
    def show_error(self, error: 'str') -> None:
        """Display an error message to the user.

        Args:
            error: The error message to display.
        """
        pass

    @abstractmethod
    def show_game_over(self, result: 'str', winner: 'Colour | None') -> None:
        """Display the game over screen.

        Args:
            result: Description of how the game ended.
            winner: The winning colour, or None for draws.
        """
        pass