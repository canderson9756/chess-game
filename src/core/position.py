"""Position representation for chess board squares.

This module provides the Position dataclass for representing squares
on the chess board with support for algebraic notation conversion.
"""

from dataclasses import dataclass
from .direction import Direction
from .constants import FILE_TO_LETTER, LETTER_TO_FILE


@dataclass(frozen=True)
class Position:
    """An immutable position representing a square on the chess board.

    Positions use zero-indexed file (column) and rank (row) values.
    The Position class supports algebraic notation conversion and
    arithmetic with Direction objects.

    Attributes:
        file: Column index (0-7, where 0='a' and 7='h').
        rank: Row index (0-7, where 0=rank 1 and 7=rank 8).

    Example:
        >>> pos = Position.from_algebraic("e4")
        >>> pos.file, pos.rank
        (4, 3)
        >>> pos.to_algebraic()
        'e4'
        >>> new_pos = pos + Direction(1, 1)  # Move diagonally
        >>> new_pos.to_algebraic()
        'f5'
    """

    file: int
    rank: int

    def is_valid(self) -> bool:
        """Check if the position is within board bounds.

        Returns:
            True if both file and rank are in range 0-7, False otherwise.
        """
        return 0 <= self.file <= 7 and 0 <= self.rank <= 7

    def to_algebraic(self) -> str:
        """Convert the position to algebraic notation.

        Returns:
            A string in algebraic notation (e.g., "e4", "a1", "h8").
        """
        return FILE_TO_LETTER[self.file] + str(self.rank + 1)

    @classmethod
    def from_algebraic(cls, notation: str) -> "Position":
        """Create a Position from algebraic notation.

        Args:
            notation: A string in algebraic notation (e.g., "e4").

        Returns:
            A new Position instance corresponding to the notation.
        """
        return cls(LETTER_TO_FILE[notation[0]], int(notation[1]) - 1)

    def __add__(self, direction: "Direction") -> "Position":
        """Add a direction to get a new position.

        Args:
            direction: The Direction to add.

        Returns:
            A new Position offset by the direction. Note that the result
            may be invalid (off the board).
        """
        return Position(self.file + direction.dx, self.rank + direction.dy)
