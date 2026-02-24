"""Turn event fired when the active player changes.

This module provides the TurnEvent class published when the turn
switches from one player to the other.
"""

from .game_event import GameEvent
from dataclasses import dataclass
from src.core.colour import Colour


@dataclass
class TurnEvent(GameEvent):
    """Event fired when the turn changes.

    Attributes:
        colour: The colour of the player whose turn it now is.
    """

    colour: 'Colour'