from src.pieces import Rook
from src.core import Position
from src.core import Colour

def test_rook_is_piece():
    rook = Rook(Position(0,0), Colour.WHITE)
    assert rook.position == Position(0,0)
    assert rook.colour == Colour.WHITE

def test_rook_delegates_to_strategy():
    rook = Rook(Position(3, 3), Colour.WHITE)

    moves = rook.get_legal_moves(board=None)

    assert len(moves) == 14