from .sliding_strategy import SlidingStrategy
from src.core.direction import Direction

class RookStrategy(SlidingStrategy):
    @property
    def directions(self):
        return [Direction(1,0), 
                Direction(-1,0),
                Direction(0, 1),
                Direction(0,-1)]