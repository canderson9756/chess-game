"""Chess pieces module.

This package provides all chess piece implementations including the
abstract Piece base class and concrete implementations for each piece type.
Pieces use the Strategy pattern for movement calculation.

Classes:
    Piece: Abstract base class for all chess pieces.
    Pawn: Pawn piece with forward movement and diagonal captures.
    Knight: Knight piece with L-shaped movement.
    Bishop: Bishop piece with diagonal sliding movement.
    Rook: Rook piece with horizontal/vertical sliding movement.
    Queen: Queen piece combining rook and bishop movement.
    King: King piece with single-square movement.
"""

from .concrete.knight import Knight
from .concrete.rook import Rook
from .concrete.bishop import Bishop
from .base.piece import Piece
from .concrete.queen import Queen
from .concrete.pawn import Pawn
from .concrete.king import King

__all__ = ["Piece", "Knight", "Rook", "Bishop", "Queen", "Pawn", "King"]
