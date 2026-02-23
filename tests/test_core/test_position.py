from src.core.position import Position
from src.core.direction import Direction
import pytest


def test_position_has_rank_and_file():
    p = Position(0, 2)
    assert p.file == 0
    assert p.rank == 2


def test_position_is_immutable():
    p = Position(0, 0)
    with pytest.raises(AttributeError):
        # Attempt reasignment
        p.file = 5  # type: ignore


def test_position_equality_by_value():
    assert Position(3, 3) == Position(3, 3)
    assert Position(3, 3) != Position(3, 4)


@pytest.mark.parametrize(
    "file,rank,expected",
    [(0, 0, True), (7, 7, True), (-1, 0, False), (8, 0, False), (0, 8, False)],
)
def test_position_is_valid(file: int, rank: int, expected: bool):
    assert Position(file, rank).is_valid() == expected


## Adding direcitons


def test_position_add_direction():
    p = Position(0, 0)
    d = Direction(0, 1)
    assert p + d == Position(0, 1)


def test_position_add_direction_can_go_off_board():
    p = Position(0, 0)
    d = Direction(0, -1)
    result = p + d
    assert result == Position(0, -1)
    assert not result.is_valid()


## Algebraic notation


@pytest.mark.parametrize(
    "file,rank,expected", [(0, 0, "a1"), (7, 7, "h8"), (5, 5, "f6"), (3, 2, "d3")]
)
def test_to_algebraic(file: int, rank: int, expected: bool):
    assert Position(file, rank).to_algebraic() == expected


@pytest.mark.parametrize(
    "notation, expected",
    [
        ("a1", Position(0, 0)),
        ("h8", Position(7, 7)),
        ("f6", Position(5, 5)),
        ("d3", Position(3, 2)),
    ],
)
def test_from_algebraic(notation: str, expected: 'Position'):
    assert Position.from_algebraic(notation) == expected
