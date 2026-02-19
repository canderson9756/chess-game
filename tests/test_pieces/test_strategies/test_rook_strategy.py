from src.pieces.strategies import RookStrategy
from src.board import Board
from src.core import Position
from src.core import Colour
from src.pieces import Rook

def test_rook_moves_orthogonally():
    strategy = RookStrategy()
    rook = Rook(Position(3, 3), Colour.WHITE)

    moves = strategy.get_legal_moves(rook, board=Board())
    
    assert len(moves) == 14

def test_rook_blocked_by_friendly():
    board = Board()
    rook = Rook(Position(0, 0), Colour.WHITE)
    blocker = Rook(Position(0, 3), Colour.WHITE)
    board.add_piece(rook)
    board.add_piece(blocker)

    strategy = RookStrategy()
    moves = strategy.get_legal_moves(rook, board)

    # Can't move to (0,3) or beyond
    assert Position(0, 3) not in moves
    assert Position(0, 4) not in moves
    assert Position(0, 2) in moves  # Can still reach squares before blocker
