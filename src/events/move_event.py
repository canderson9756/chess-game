from dataclasses import dataclass
from .game_event import GameEvent

from src.core.position import Position
from src.pieces.base.piece import Piece

@dataclass
class MoveEvent(GameEvent):
    piece: 'Piece | None' = None
    origin: 'Position | None'  = None
    destination: 'Position | None' = None