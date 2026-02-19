from src.pieces.strategies import BishopStrategy
from src.pieces import Bishop
from src.core import *
from src.board import Board

def test_bishop_moves_orthogonally():
    strategy = BishopStrategy()
    bishop = Bishop(Position(3, 3), Colour.WHITE)

    moves = strategy.get_legal_moves(bishop, board=Board())

    assert len(moves) == 13

def test_bishop_blocked_by_friendly():
    strategy = BishopStrategy()
    bishop = Bishop(Position(3, 3), Colour.WHITE)
    friendly = Bishop(Position(5, 5), Colour.WHITE)

    board = Board()
    board.add_piece(bishop)
    board.add_piece(friendly)

    moves = strategy.get_legal_moves(bishop, board)

    assert Position(5, 5) not in moves
    assert Position(6, 6) not in moves
    assert Position(7, 7) not in moves
    assert Position(2, 2) in moves

def test_bishop_blocked_by_enemy():
    strategy = BishopStrategy()
    bishop = Bishop(Position(3, 3), Colour.WHITE)
    enemy = Bishop(Position(5, 5), Colour.BLACK)

    board = Board()
    board.add_piece(bishop)
    board.add_piece(enemy)

    moves = strategy.get_legal_moves(bishop, board)

    assert Position(5, 5) in moves
    assert Position(6, 6) not in moves
    assert Position(7, 7) not in moves
    assert Position(2, 2) in moves
