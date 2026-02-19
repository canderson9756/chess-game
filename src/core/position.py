from dataclasses import dataclass
from .direction import Direction
from .constants import FILE_TO_LETTER, LETTER_TO_FILE

@dataclass(frozen=True)
class Position:
    file: int
    rank: int

    def is_valid(self) -> bool:
        return 0<=self.file<=7 and 0<=self.rank<=7
    
    def to_algebraic(self) -> str:
        return FILE_TO_LETTER[self.file] + str(self.rank + 1)
    
    @classmethod
    def from_algebraic(cls, notation: str) -> 'Position':
        return cls(LETTER_TO_FILE[notation[0]], int(notation[1])-1)

    def __add__(self, direction: 'Direction') -> 'Position':
        return Position(self.file+direction.dx, self.rank+direction.dy)