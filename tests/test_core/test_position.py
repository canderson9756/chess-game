from src.core.position import Position
import pytest

def test_position_has_rank_and_file():
    p = Position(0, 2)
    assert p.file == 0
    assert p.rank == 2

def test_position_is_immutable():
    p = Position(0,0)
    with pytest.raises(AttributeError):
        # Attempt reasignment
        p.file = 5

def test_position_equality_by_value():
      assert Position(3, 3) == Position(3, 3)
      assert Position(3, 3) != Position(3, 4)

@pytest.mark.parametrize("file,rank,expected", [
     (0, 0, True),
     (7, 7, True),
     (-1, 0, False),
     (8, 0, False),
     (0, 8, False)
     ])

def test_position_is_valid(file,rank,expected):
    assert Position(file, rank).is_valid() == expected