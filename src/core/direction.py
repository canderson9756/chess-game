"""Direction vector for chess piece movement.

This module provides the Direction dataclass for representing movement
vectors on the chess board.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Direction:
    """An immutable movement vector representing direction on the board.

    Direction is used to calculate piece movements by adding to Position
    objects. It supports scalar multiplication for extending moves.

    Attributes:
        dx: Horizontal displacement (positive = right, negative = left).
        dy: Vertical displacement (positive = up ranks, negative = down ranks).

    Example:
        >>> up = Direction(0, 1)
        >>> diagonal = Direction(1, 1)
        >>> extended = diagonal * 3  # Direction(3, 3)
    """

    dx: int
    dy: int

    def is_parallel(self, direction: "Direction") -> bool:
        """Check if this direction is parallel to another.

        Two directions are parallel if they lie on the same vertical,
        horizontal, or diagonal line.

        Args:
            direction: The direction to compare against.

        Returns:
            True if the directions are parallel, False otherwise.
        """
        if (self.dx == direction.dx) and (self.dy != direction.dy):
            # On the same vertical line
            return True
        elif (self.dx != direction.dx) and (self.dy == direction.dy):
            # On the same horizontal line
            return True
        elif self.dx - direction.dx == self.dy - direction.dy:
            # On same diagonal line
            return True
        else:
            return False

    def __mul__(self, scalar: int) -> "Direction":
        """Multiply the direction by a scalar value.

        Args:
            scalar: The multiplier for both dx and dy.

        Returns:
            A new Direction with scaled components.
        """
        return Direction(self.dx * scalar, self.dy * scalar)
