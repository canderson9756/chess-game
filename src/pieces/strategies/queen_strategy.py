from .sliding_strategy import SlidingStrategy
from src.core.direction import Direction

class QueenStrategy(SlidingStrategy):
    @property
    def directions(self) -> list['Direction']:
        return [
            Direction(1, 1),
            Direction(-1, 1),
            Direction(-1, -1),
            Direction(1, -1),
            Direction(1,0), 
            Direction(-1,0),
            Direction(0, 1),
            Direction(0,-1)
        ]