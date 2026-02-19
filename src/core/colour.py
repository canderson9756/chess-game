"""Colour enumeration for chess pieces.

This module defines the Colour enum used to represent the two sides
in a chess game: WHITE and BLACK.
"""

from enum import Enum, auto


class Colour(Enum):
    """Represents the colour of a chess piece.

    Attributes:
        WHITE: The white side, which moves first and advances up the board.
        BLACK: The black side, which moves second and advances down the board.
    """

    WHITE = auto()
    BLACK = auto()

    def opposite(self) -> "Colour":
        """Return the opposing colour.

        Returns:
            Colour.WHITE if this is BLACK, Colour.BLACK if this is WHITE.
        """
        return Colour.WHITE if self == Colour.BLACK else Colour.BLACK

    def direction(self) -> int:
        """Return the forward direction for pawns of this colour.

        Returns:
            1 for WHITE (advancing up ranks), -1 for BLACK (advancing down ranks).
        """
        return 1 if self == Colour.WHITE else -1
