"""Tests for the CaptureMove class.

This module contains unit tests for the CaptureMove implementation,
verifying that capture moves correctly remove the enemy piece, place the
attacking piece at the destination, and fully restore board state on undo.
"""

from src.moves import CaptureMove
from src.board import Board
from src.core import Position, Colour
from typing import TYPE_CHECKING, Callable
import pytest

if TYPE_CHECKING:
    from ..conftest import *

def test_capture_move_makes_move(make_dummy_piece: Callable[['Position', 'Colour'], 'DummyPiece']):
    origin = Position(0, 0)
    destination = Position(0, 4)
    board = Board()

    piece = make_dummy_piece(origin, Colour.WHITE)
    enemy = make_dummy_piece(destination, Colour.BLACK)

    board.add_piece(piece)
    board.add_piece(enemy)

    move = CaptureMove(piece, origin, destination)

    move.execute(board)

    assert piece.position == destination
    assert board.get_piece_at(origin) == None
    assert board.get_piece_at(destination) == piece
    assert enemy not in board.get_pieces()

def test_capture_move_undos_move(make_dummy_piece: Callable[['Position', 'Colour'], 'DummyPiece']):
    origin = Position(0, 0)
    destination = Position(0, 4)
    board = Board()

    piece = make_dummy_piece(origin, Colour.WHITE)
    enemy = make_dummy_piece(destination, Colour.BLACK)

    board.add_piece(piece)
    board.add_piece(enemy)

    move = CaptureMove(piece, origin, destination)

    move.execute(board)
    move.undo(board)

    assert piece.position == origin
    assert board.get_piece_at(origin) == piece
    assert board.get_piece_at(destination) == enemy
    assert enemy in board.get_pieces()

