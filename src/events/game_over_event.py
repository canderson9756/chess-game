from dataclasses import dataclass

from .game_event import GameEvent
from src.core.colour import Colour

@dataclass
class GameOverEvent(GameEvent):
    result: 'str'
    winner: 'Colour | None'