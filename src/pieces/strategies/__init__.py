"""Movement strategies for chess pieces.

This package implements the Strategy pattern for piece movement calculation.
Each strategy encapsulates the movement rules for a specific piece type,
allowing pieces to delegate move calculation to their strategy.

Classes:
    MoveStrategy: Abstract base strategy defining the interface.
    SlidingStrategy: Base for pieces that slide (Rook, Bishop, Queen).
    RookStrategy: Horizontal and vertical sliding movement.
    BishopStrategy: Diagonal sliding movement.
    QueenStrategy: Combined rook and bishop movement.
    KnightStrategy: L-shaped jumping movement.
    KingStrategy: Single-square movement in any direction.
    PawnStrategy: Forward movement with diagonal captures.
"""

from .move_strategy import MoveStrategy
from .knight_strategy import KnightStrategy
from .sliding_strategy import SlidingStrategy
from .rook_strategy import RookStrategy
from .bishop_strategy import BishopStrategy
from .queen_strategy import QueenStrategy
from .pawn_strategy import PawnStrategy
from .king_strategy import KingStrategy

__all__ = ['MoveStrategy', 'KnightStrategy', 'SlidingStrategy', 'RookStrategy', 'BishopStrategy', 'QueenStrategy', 'PawnStrategy', 'KingStrategy']