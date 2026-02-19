from src.pieces import Pawn
from src.pieces.strategies import PawnStrategy
from src.core import *
from src.board import Board

def test_white_pawn_moves_forward():
    strategy = PawnStrategy()
    pawn = Pawn(Position(4, 1), Colour.WHITE)  # e2
    board = Board()
    board.add_piece(pawn)

    moves = strategy.get_legal_moves(pawn, board)

    assert Position(4, 2) in moves  # e3

def test_black_pawn_moves_forward():
    strategy = PawnStrategy()
    pawn = Pawn(Position(4, 6), Colour.BLACK)  # e7
    board = Board()
    board.add_piece(pawn)

    moves = strategy.get_legal_moves(pawn, board)

    assert Position(4, 5) in moves  # e6

def test_pawn_blocked_by_piece():
    board = Board()
    pawn = Pawn(Position(4, 1), Colour.WHITE)
    blocker = Pawn(Position(4, 2), Colour.BLACK)
    board.add_piece(pawn)
    board.add_piece(blocker)

    strategy = PawnStrategy()
    moves = strategy.get_legal_moves(pawn, board)

    assert Position(4, 2) not in moves  # Blocked

def test_pawn_double_move_on_first_turn():
    board = Board()
    pawn = Pawn(Position(4, 1), Colour.WHITE)
    pawn.first_move = True
    board.add_piece(pawn)

    strategy = PawnStrategy()
    moves = strategy.get_legal_moves(pawn, board)

    assert Position(4, 2) in moves  # Single
    assert Position(4, 3) in moves  # Double

def test_pawn_no_double_move_after_first():
    board = Board()
    pawn = Pawn(Position(4, 2), Colour.WHITE)
    pawn.first_move = False
    board.add_piece(pawn)

    strategy = PawnStrategy()
    moves = strategy.get_legal_moves(pawn, board)

    assert Position(4, 3) in moves
    assert Position(4, 4) not in moves  # No double move

def test_pawn_double_move_blocked_by_piece_in_path():
    board = Board()
    pawn = Pawn(Position(4, 1), Colour.WHITE)
    blocker = Pawn(Position(4, 2), Colour.BLACK)  # Blocks path
    board.add_piece(pawn)
    board.add_piece(blocker)

    strategy = PawnStrategy()
    moves = strategy.get_legal_moves(pawn, board)

    assert Position(4, 3) not in moves  # Can't jump over

def test_pawn_double_move_blocked_at_destination():
    board = Board()
    pawn = Pawn(Position(4, 1), Colour.WHITE)
    blocker = Pawn(Position(4, 3), Colour.BLACK)  # Blocks destination
    board.add_piece(pawn)
    board.add_piece(blocker)

    strategy = PawnStrategy()
    moves = strategy.get_legal_moves(pawn, board)

    assert Position(4, 2) in moves     # Can still single move
    assert Position(4, 3) not in moves  # Destination blocked

def test_pawn_diagonal_capture():
    board = Board()
    pawn = Pawn(Position(4, 1), Colour.WHITE)
    capturable_spaces = [
        Position(5,2),
        Position(3,2)
    ]
    capturable_pawns = [Pawn(position, Colour.BLACK) for position in capturable_spaces]
    board.add_piece(pawn)
    for piece in capturable_pawns:
        board.add_piece(piece)
    
    strategy = PawnStrategy()
    moves = strategy.get_legal_moves(pawn, board)
    assert Position(5,2) in moves
    assert Position(3,2) in moves

def test_no_diagonal_capture_if_empty():
    board = Board()
    pawn = Pawn(Position(4, 1), Colour.WHITE)
    board.add_piece(pawn)
    
    strategy = PawnStrategy()
    moves = strategy.get_legal_moves(pawn, board)
    assert Position(5,2) not in moves
    assert Position(3,2) not in moves

def test_no_diagonal_capture_friendly():
    board = Board()
    pawn = Pawn(Position(4, 1), Colour.WHITE)
    capturable_spaces = [
        Position(5,2),
        Position(3,2)
    ]
    capturable_pawns = [Pawn(position, Colour.WHITE) for position in capturable_spaces]
    board.add_piece(pawn)
    for piece in capturable_pawns:
        board.add_piece(piece)
    
    strategy = PawnStrategy()
    moves = strategy.get_legal_moves(pawn, board)
    assert Position(5,2) not in moves
    assert Position(3,2) not in moves