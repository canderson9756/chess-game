from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    file: int
    rank: int

    def is_valid(self) -> bool:
        return 0<=self.file<=7 and 0<=self.rank<=7
