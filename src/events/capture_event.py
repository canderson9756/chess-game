"""Capture event fired when a piece is captured.

This module provides the CaptureEvent class published when one piece
captures another.
"""

from .game_event import GameEvent
from src.pieces.base.piece import Piece
from dataclasses import dataclass


@dataclass
class CaptureEvent(GameEvent):
    """Event fired when a piece is captured.

    Attributes:
        captured_piece: The piece that was captured.
        capturing_piece: The piece that made the capture.
    """

    captured_piece: 'Piece'
    capturing_piece: 'Piece'