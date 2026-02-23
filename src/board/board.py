"""Chess board implementation.

This module provides the Board class which manages all pieces on the
chess board and provides methods for querying and manipulating board state.
"""

from src.core.position import Position
from src.core.colour import Colour
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.pieces.base.piece import Piece


class Board:
    """Manages the chess board state and piece positions.

    The Board class maintains a collection of pieces and provides methods
    for querying positions, checking occupancy, and moving pieces.

    Attributes:
        bounds: A tuple (0, 7) representing valid file/rank indices.

    Example:
        >>> board = Board()
        >>> board.add_piece(pawn)
        >>> board.is_occupied(Position.from_algebraic("e2"))
        True
    """

    def __init__(self):
        """Initialize an empty board."""
        self._pieces: list["Piece"] = []

    @property
    def bounds(self) -> tuple[int, int]:
        """Return the valid index range for files and ranks.

        Returns:
            A tuple (0, 7) representing the minimum and maximum valid indices.
        """
        return (0, 7)

    def add_piece(self, piece: "Piece") -> None:
        """Add a piece to the board.

        Args:
            piece: The piece to add.
        """
        self._pieces.append(piece)

    def get_piece_at(self, position: "Position") -> "Piece | None":
        """Get the piece at a specific position.

        Args:
            position: The position to check.

        Returns:
            The piece at the position, or None if the square is empty.
        """
        for piece in self._pieces:
            if piece.position == position:
                return piece
        return None

    def is_occupied(self, position: "Position") -> bool:
        """Check if a position has any piece on it.

        Args:
            position: The position to check.

        Returns:
            True if a piece occupies the position, False otherwise.
        """
        piece = self.get_piece_at(position)
        return True if piece else False

    def has_friendly_piece(self, position: "Position", colour: "Colour") -> bool:
        """Check if a position has a piece of the specified colour.

        Args:
            position: The position to check.
            colour: The friendly colour to check for.

        Returns:
            True if a piece of the same colour occupies the position.
        """
        piece = self.get_piece_at(position)
        if piece:
            return True if piece.colour == colour else False
        return False

    def has_enemy_piece(self, position: "Position", colour: "Colour") -> bool:
        """Check if a position has an enemy piece.

        Args:
            position: The position to check.
            colour: The friendly colour (enemy is the opposite).

        Returns:
            True if a piece of the opposite colour occupies the position.
        """
        piece = self.get_piece_at(position)
        if piece:
            return True if piece.colour != colour else False
        return False

    def get_pieces(self, colour: "Colour | None" = None) -> list["Piece"]:
        """Get all pieces, optionally filtered by colour.

        Args:
            colour: If specified, only return pieces of this colour.

        Returns:
            A list of pieces on the board.
        """
        if colour is None:
            return self._pieces
        return [p for p in self._pieces if p.colour == colour]

    def move_piece(self, move_from: "Position", move_to: "Position") -> None:
        """Move a piece from one position to another.

        Args:
            move_from: The current position of the piece.
            move_to: The destination position.

        Raises:
            LookupError: If no piece exists at the source position.
        """
        piece = self.get_piece_at(move_from)
        if piece:
            piece.set_position(move_to)
        else:
            raise LookupError("Move from position not found. Look at other logic")

    def remove_piece(self, remove_position: "Position") -> None:
        """Remove a piece from the board.

        Args:
            remove_position: The position of the piece to remove.

        Raises:
            TypeError: If no piece exists at the specified position.
        """
        piece = self.get_piece_at(remove_position)
        if piece:
            self._pieces.remove(piece)
        else:
            raise TypeError(f"No piece at the given location: {remove_position}")

    def is_square_attacked(self, position: 'Position', colour: 'Colour') -> 'bool':
        for piece in self.get_pieces():
            if piece.colour != colour:
                continue
            attacks = piece.get_attack_moves(self)
            if position in attacks:
                return True
        return False

    def find_king(self, colour: 'Colour') -> 'Piece':
        for piece in self._pieces:
            if piece.is_king and piece.colour == colour:
                return piece
        raise ValueError(f"No {colour} king found")
