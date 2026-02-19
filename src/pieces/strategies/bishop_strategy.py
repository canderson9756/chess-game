from .sliding_strategy import SlidingStrategy
from src.core.direction import Direction

class BishopStrategy(SlidingStrategy):
    @property
    def directions(self) -> list['Direction']:
        return [
            Direction(1, 1),
            Direction(-1, 1),
            Direction(-1, -1),
            Direction(1, -1)
        ]