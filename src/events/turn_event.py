from .game_event import GameEvent
from dataclasses import dataclass
from src.core.colour import Colour

@dataclass
class TurnEvent(GameEvent):
    colour: 'Colour'