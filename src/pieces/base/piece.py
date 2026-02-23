"""Abstract base class for chess pieces.

This module defines the Piece abstract class that all concrete chess
pieces inherit from.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from src.core.colour import Colour
from src.core.position import Position

if TYPE_CHECKING:
    from src.board.board import Board


class Piece(ABC):
    """Abstract base class for all chess pieces.

    Piece defines the common interface and attributes shared by all
    chess pieces. Concrete implementations must provide the get_legal_moves
    method to calculate valid moves based on their movement rules.

    Attributes:
        position: The current position of the piece on the board.
        colour: The colour (WHITE or BLACK) of the piece.

    Example:
        >>> class Knight(Piece):
        ...     def get_legal_moves(self, board):
        ...         # Implementation for L-shaped movement
        ...         pass
    """

    def __init__(self, position: "Position", colour: "Colour"):
        """Initialize a piece with position and colour.

        Args:
            position: The starting position on the board.
            colour: The colour of the piece.
        """
        self._position = position
        self._colour = colour

    @property
    def position(self) -> "Position":
        """Get the current position of the piece."""
        return self._position

    @property
    def colour(self) -> "Colour":
        """Get the colour of the piece."""
        return self._colour

    @abstractmethod
    def get_legal_moves(self, board: "Board") -> list["Position"]:
        """Calculate all legal moves for this piece.

        Args:
            board: The current board state for collision detection.

        Returns:
            A list of valid destination positions.
        """

    @abstractmethod
    def get_attack_moves(self, board: "Board") -> list["Position"]:
        """Calculate all squares that this piece can 'see'.

        Args:
            board: The current board state for collision detection.

        Returns:
            A list of valid destination positions.
        """

    def move_to(self, position: "Position") -> None:
        """Move the piece to a new position.

        Args:
            position: The destination position.
        """
        self._position = position

    def is_enemy(self, colour: "Colour") -> bool:
        """Check if a colour represents an enemy piece.

        Args:
            colour: The colour to check.

        Returns:
            True if the colour is different from this piece's colour.
        """
        return colour != self.colour

    def set_position(self, position: "Position") -> None:
        """Set the piece's position directly.

        Args:
            position: The new position for the piece.
        """
        self._position = position
    
    @property
    def is_king(self) -> 'bool':
        return False    # Overriden by king piece
