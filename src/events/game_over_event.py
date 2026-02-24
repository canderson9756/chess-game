"""Game over event fired when the game ends.

This module provides the GameOverEvent class published when a game
concludes by checkmate, stalemate, or other conditions.
"""

from dataclasses import dataclass

from .game_event import GameEvent
from src.core.colour import Colour


@dataclass
class GameOverEvent(GameEvent):
    """Event fired when the game ends.

    Attributes:
        result: Description of how the game ended (e.g., "Checkmate", "Stalemate").
        winner: The winning colour, or None for draws.
    """

    result: 'str'
    winner: 'Colour | None'