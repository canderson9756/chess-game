from src.pieces import King, Piece
from src.pieces.strategies import KingStrategy
from src.core import *
from src.board import Board

def test_king_moves_one_square_in_all_directions():
    king = King(Position(3, 3), Colour.WHITE)
    strategy = KingStrategy()
    board = Board()
    board.add_piece(king)

    moves = strategy.get_legal_moves(king, board)

    expected = [
        Position(3,4),
        Position(4,4),
        Position(4,3),
        Position(4,2),
        Position(3,2),
        Position(2,2),
        Position(2,3),
        Position(2,4)
    ]

    assert set(moves) == set(expected)
    assert len(moves) == 8

def test_king_in_corner_as_limited_moves():
    king = King(Position(0, 0), Colour.WHITE)
    strategy = KingStrategy()
    board = Board()
    board.add_piece(king)

    moves = strategy.get_legal_moves(king, board)

    expected = [
        Position(0,1),
        Position(1,1),
        Position(1,0)
    ]

    assert set(moves) == set(expected)
    assert len(moves) == 3

def test_king_on_edge_has_limited_moves():
    king = King(Position(0, 3), Colour.WHITE)
    strategy = KingStrategy()
    board = Board()
    board.add_piece(king)

    moves = strategy.get_legal_moves(king, board)

    expected = [
        Position(0,4),
        Position(1,4),
        Position(1,3),
        Position(1,2),
        Position(0,2)
    ]

    assert set(moves) == set(expected)
    assert len(moves) == 5

def test_king_cannot_capture_friendly():
    class DummyPiece(Piece):
        def get_legal_moves(self) -> list['Position']:
            return []
    king = King(Position(0, 3), Colour.WHITE)
    strategy = KingStrategy()
    friendly = DummyPiece(Position(1, 3), Colour.WHITE)
    board = Board()
    board.add_piece(king)
    board.add_piece(friendly)

    moves = strategy.get_legal_moves(king, board)

    expected = [
        Position(0,4),
        Position(1,4),
        Position(1,2),
        Position(0,2)
    ]

    assert Position(1,3) not in moves
    assert set(moves) == set(expected)
    assert len(moves) == 4

def test_king_can_capture_enemy():
    class DummyPiece(Piece):
        def get_legal_moves(self) -> list['Position']:
            return []
    king = King(Position(0, 3), Colour.WHITE)
    strategy = KingStrategy()
    enemy = DummyPiece(Position(1, 3), Colour.BLACK)
    board = Board()
    board.add_piece(king)
    board.add_piece(enemy)

    moves = strategy.get_legal_moves(king, board)

    expected = [
        Position(0,4),
        Position(1,4),
        Position(1,3),
        Position(1,2),
        Position(0,2)
    ]

    assert set(moves) == set(expected)
    assert len(moves) == 5
    assert Position(1,3) in moves