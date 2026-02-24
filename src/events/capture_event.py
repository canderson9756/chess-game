from .game_event import GameEvent
from src.pieces.base.piece import Piece
from dataclasses import dataclass

@dataclass
class CaptureEvent(GameEvent):
    captured_piece: 'Piece'
    capturing_piece: 'Piece'