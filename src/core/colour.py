from enum import Enum, auto
class Colour(Enum):
    WHITE = auto()
    BLACK = auto()

    def oposite(self) -> 'Colour':
        return Colour.WHITE if self == Colour.BLACK else Colour.BLACK
    
    def direction(self) -> int:
        return 1 if self == Colour.WHITE else -1