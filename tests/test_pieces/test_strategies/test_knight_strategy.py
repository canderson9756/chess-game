from src.pieces import Knight
from src.pieces.strategies import KnightStrategy
from src.core import Position
from src.core import Colour
from src.board import Board

def test_knight_moves_in_l_shape():
    strategy = KnightStrategy()
    knight = Knight(Position(3, 3), Colour.WHITE)

    moves = strategy.get_legal_moves(knight, board=Board())

    expected = [
        Position(1, 2), Position(1, 4),
        Position(5, 2), Position(5, 4),
        Position(2, 1), Position(4, 1),
        Position(2, 5), Position(4, 5),
      ]
    assert set(moves) == set(expected)
  
def test_knight_cannot_capture_friendly():
    board = Board()
    knight = Knight(Position(3, 3), Colour.WHITE)
    friendly = Knight(Position(5, 4), Colour.WHITE)  # Blocking square
    board.add_piece(knight)
    board.add_piece(friendly)

    strategy = KnightStrategy()
    moves = strategy.get_legal_moves(knight, board)

    assert Position(5, 4) not in moves  # Blocked

def test_knight_can_capture_enemy():
    board = Board()
    knight = Knight(Position(3, 3), Colour.WHITE)
    enemy = Knight(Position(5, 4), Colour.BLACK)  # Capturable
    board.add_piece(knight)
    board.add_piece(enemy)

    strategy = KnightStrategy()
    moves = strategy.get_legal_moves(knight, board)
    assert Position(5, 4) in moves  # Can capture

def test_knight_in_corner_limited_moves():
    board = Board()
    knight = Knight(Position(0, 0), Colour.WHITE)
    board.add_piece(knight)

    strategy = KnightStrategy()
    moves = strategy.get_legal_moves(knight, board)

    expected = [Position(1, 2), Position(2, 1)]

    assert len(moves) == 2
    assert set(moves) == set(expected)
  
def test_knight_on_edge_limited_moves():
    board = Board()
    knight = Knight(Position(0, 3), Colour.WHITE)
    board.add_piece(knight)

    strategy = KnightStrategy()
    moves = strategy.get_legal_moves(knight, board)

    expected = [Position(1, 5), Position(2, 4), Position(2, 2), Position(1, 1)]

    assert len(moves) == 4
    assert set(moves) == set(expected)