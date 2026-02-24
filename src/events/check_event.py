"""Check event fired when a king is in check.

This module provides the CheckEvent class published when a player's
king is under attack.
"""

from .game_event import GameEvent
from dataclasses import dataclass
from src.core.colour import Colour


@dataclass
class CheckEvent(GameEvent):
    """Event fired when a king is placed in check.

    Attributes:
        colour_in_check: The colour of the king that is in check.
    """

    colour_in_check: 'Colour'