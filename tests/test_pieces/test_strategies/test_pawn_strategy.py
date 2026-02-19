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
