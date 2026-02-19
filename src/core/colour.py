from enum import Enum, auto
class Colour(Enum):
    WHITE = auto()
    BLACK = auto()

    def oposite(self) -> 'Colour':
        return Colour.WHITE if self == Colour.BLACK else Colour.BLACK