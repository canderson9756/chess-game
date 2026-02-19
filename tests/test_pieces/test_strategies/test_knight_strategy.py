from src.pieces import Knight
from src.pieces.strategies import KnightStrategy
from src.core import Position
from src.core import Colour

def test_knight_moves_in_l_shape():
    strategy = KnightStrategy()
    knight = Knight(Position(3, 3), Colour.WHITE)

    moves = strategy.get_legal_moves(knight, board=None)

    expected = [
        Position(1, 2), Position(1, 4),
        Position(5, 2), Position(5, 4),
        Position(2, 1), Position(4, 1),
        Position(2, 5), Position(4, 5),
      ]
    assert set(moves) == set(expected)