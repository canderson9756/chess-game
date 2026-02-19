"""Tests for the StandardMove class.

This module contains unit tests for the StandardMove implementation,
verifying that standard chess moves execute and undo correctly.
"""

from src.moves import StandardMove

from typing import TYPE_CHECKING, Callable
import pytest
from src.core import *
from src.board import Board

if TYPE_CHECKING:
    from ..conftest import *

def test_standard_move_makes_move(make_dummy_piece: Callable[['Position', 'Colour'], 'DummyPiece']):
    origin = Position(0, 0)
    destination = Position(0, 4)
    board = Board()

    piece = make_dummy_piece(origin, Colour.WHITE)
    board.add_piece(piece)

    move = StandardMove(piece, origin, destination)

    move.execute(board)
    assert piece.position == destination
    assert board.get_piece_at(origin) == None
    assert board.get_piece_at(destination) == piece

def test_standard_move_undos_move(make_dummy_piece: Callable[['Position', 'Colour'], 'DummyPiece']):
    origin = Position(0, 0)
    destination = Position(0, 4)
    board = Board()

    piece = make_dummy_piece(origin, Colour.WHITE)
    board.add_piece(piece)

    move = StandardMove(piece, origin, destination)

    move.execute(board)
    move.undo(board)

    assert piece.position == origin
    assert board.get_piece_at(destination) == None
    assert board.get_piece_at(origin) == piece
