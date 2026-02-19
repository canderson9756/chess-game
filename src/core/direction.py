from dataclasses import dataclass

@dataclass(frozen=True)
class Direction:
    dx: int
    dy: int

    def is_parallel(self, direction: 'Direction') -> bool:
        if (self.dx==direction.dx) and (self.dy != direction.dy):
            # On the same vertical line
            return True
        elif (self.dx!=direction.dx) and (self.dy==direction.dy):
            # On the same horizontal line
            return True
        elif (self.dx-direction.dx==self.dy-direction.dy):
            # On same diagonal line
            return True
        else:
            return False

    def __mul__(self, scalar: int) -> 'Direction':
        return Direction(self.dx * scalar, self.dy * scalar)