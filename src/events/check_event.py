from .game_event import GameEvent
from dataclasses import dataclass
from src.core.colour import Colour

@dataclass
class CheckEvent(GameEvent):
    colour_in_check: 'Colour'