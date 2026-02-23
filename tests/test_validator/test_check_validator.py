from src.validator import CheckValidator
from src.core import Position, Colour
from src.moves import StandardMove
from src.board import Board
from src.pieces import King, Rook, Knight

import pytest
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from ..conftest import *

def test_move_that_leaves_king_in_check_is_invalid(make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]):
    board = Board()
    king = King(Position(0, 4), Colour.WHITE)   # King on starting square
    rook = Rook(Position(7, 4), Colour.BLACK)   # Rook on the same file
    blocker = Knight(Position(4,4), Colour.WHITE)    # Knight in line

    board.add_piece(king)
    board.add_piece(rook)
    board.add_piece(blocker)

    # Attempt to move the knight, exposing the king to check

    move = StandardMove(blocker, Position(4, 4), Position(2, 5))

    validator = CheckValidator()
    result = validator.validate(move, board)

    assert result == False

def test_move_that_escapes_check_is_valid():
    board = Board()
    king = King(Position(4, 0), Colour.WHITE)
    rook = Rook(Position(4, 7), Colour.BLACK)  # King is in check!
    board.add_piece(king)
    board.add_piece(rook)

    # King moves out of check
    move = StandardMove(king, Position(4, 0), Position(3, 0))

    validator = CheckValidator()
    result = validator.validate(move, board)

    assert result == True  # Escaping check is valid

def test_king_in_check():
    board = Board()
    king = King(Position(5, 0), Colour.WHITE)
    rook = Rook(Position(4, 7), Colour.BLACK)  # King is in check!
    board.add_piece(king)
    board.add_piece(rook)

    move = StandardMove(king, Position(5, 0), Position(4, 0))

    validator = CheckValidator()
    result = validator.validate(move, board)
    assert result == False  # King is in check
