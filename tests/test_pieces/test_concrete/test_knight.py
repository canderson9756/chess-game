from src.pieces import Knight
from src.core import Position
from src.core import Colour

def test_knight_is_piece():
    knight = Knight(Position(0,0), Colour.WHITE)
    assert knight.position == Position(0,0)
    assert knight.colour == Colour.WHITE

# def test_knight_moves_in_l_shape():
#     knight = Knight(Position(3, 3), Colour.WHITE)
