from src.moves import MoveHistory, StandardMove
from src.core import Colour, Position
from src.board import Board

import pytest  # type: ignore

from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from ..conftest import *


def test_move_history_push_and_undo(
    make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]
):
    origin = Position(0, 0)
    destination = Position(0, 4)
    board = Board()
    history = MoveHistory()

    piece = make_dummy_piece(origin, Colour.WHITE)
    enemy = make_dummy_piece(destination, Colour.BLACK)

    board.add_piece(piece)
    board.add_piece(enemy)

    move = StandardMove(piece, origin, destination)

    move.execute(board)
    history.push(move)

    assert piece.position == destination

    history.undo(board)

    assert piece.position == origin


def test_move_history_redo(
    make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]
):
    origin = Position(0, 0)
    destination = Position(0, 4)
    board = Board()
    history = MoveHistory()

    piece = make_dummy_piece(origin, Colour.WHITE)
    enemy = make_dummy_piece(destination, Colour.BLACK)

    board.add_piece(piece)
    board.add_piece(enemy)

    move = StandardMove(piece, origin, destination)

    move.execute(board)
    history.push(move)
    history.undo(board)

    history.redo(board)

    assert piece.position == destination


def test_move_history_redo_cleared_on_new_move(
    make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]
):
    origin = Position(0, 0)
    destination1 = Position(0, 4)
    destination2 = Position(0, 5)
    board = Board()
    history = MoveHistory()

    piece = make_dummy_piece(origin, Colour.WHITE)
    enemy = make_dummy_piece(destination1, Colour.BLACK)

    board.add_piece(piece)
    board.add_piece(enemy)

    move1 = StandardMove(piece, origin, destination1)
    move1.execute(board)
    history.push(move1)

    history.undo(board)

    move2 = StandardMove(piece, origin, destination2)
    move2.execute(board)
    history.push(move2)

    history.push(move2)

    assert not history.can_redo()
