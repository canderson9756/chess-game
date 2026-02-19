from src.core.direction import Direction

def test_direction_has_dx_dy():
    d = Direction(1, 0)
    assert d.dx == 1
    assert d.dy == 0

def test_direction_multiply():
    d = Direction(0, 1)
    result = d * 2
    assert result == Direction(0, 2)

def test_parallel_directions():
    assert Direction(1, 0).is_parallel(Direction(2, 0))     # Both horizontal
    assert Direction(0, 1).is_parallel(Direction(0, 2))     # Both vertical
    assert Direction(1, 1).is_parallel(Direction(2, 2))     # Both diagonal