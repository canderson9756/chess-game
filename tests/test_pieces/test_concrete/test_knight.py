from src.pieces import Knight
from src.core import Position
from src.core import Colour

def test_knight_is_piece():
    knight = Knight(Position(0,0), Colour.WHITE)
    assert knight.position == Position(0,0)
    assert knight.colour == Colour.WHITE

def test_knight_delegates_to_strategy():
    knight = Knight(Position(3, 3), Colour.WHITE)

    moves = knight.get_legal_moves(board=None)

    expected = [
        Position(1, 2), Position(1, 4),
        Position(5, 2), Position(5, 4),
        Position(2, 1), Position(4, 1),
        Position(2, 5), Position(4, 5),
      ]
    assert set(moves) == set(expected)