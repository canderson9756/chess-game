"""Move event fired when a piece moves.

This module provides the MoveEvent class published when any piece
moves from one position to another.
"""

from dataclasses import dataclass
from .game_event import GameEvent

from src.core.position import Position
from src.pieces.base.piece import Piece


@dataclass
class MoveEvent(GameEvent):
    """Event fired when a piece moves.

    Attributes:
        piece: The piece that moved.
        origin: The starting position.
        destination: The ending position.
    """

    piece: 'Piece | None' = None
    origin: 'Position | None' = None
    destination: 'Position | None' = None