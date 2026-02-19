from src.pieces.strategies import QueenStrategy
from src.board import Board
from src.core import Position
from src.core import Colour
from src.pieces import Queen

def test_queen_moves_orthogonally_and_diagonally():
    strategy = QueenStrategy()
    queen = Queen(Position(3, 3), Colour.WHITE)

    moves = strategy.get_legal_moves(queen, board=Board())

    assert len(moves) == 27


def test_queen_blocked_by_friendly():
    strategy = QueenStrategy()
    queen = Queen(Position(3, 3), Colour.WHITE)
    friendly = Queen(Position(5, 5), Colour.WHITE)

    board = Board()
    board.add_piece(queen)
    board.add_piece(friendly)

    moves = strategy.get_legal_moves(queen, board)

    assert Position(5, 5) not in moves
    assert Position(6, 6) not in moves
    assert Position(7, 7) not in moves
    assert Position(2, 2) in moves

def test_queen_blocked_by_enemy():
    strategy = QueenStrategy()
    queen = Queen(Position(3, 3), Colour.WHITE)
    enemy = Queen(Position(5, 5), Colour.BLACK)

    board = Board()
    board.add_piece(queen)
    board.add_piece(enemy)

    moves = strategy.get_legal_moves(queen, board)

    assert Position(5, 5) in moves
    assert Position(6, 6) not in moves
    assert Position(7, 7) not in moves
    assert Position(2, 2) in moves