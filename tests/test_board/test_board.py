from src.board import Board
from src.core.position import Position
from src.core.colour import Colour

import pytest  # type: ignore
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ..conftest import *


def test_board_has_bounds():
    board = Board()
    assert board.bounds == (0, 7)


def test_board_starts_empty():
    board = Board()
    assert board.get_pieces() == []


def test_board_can_add_piece(
    make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]
):
    board = Board()
    board.add_piece(make_dummy_piece(Position(0, 0), Colour.WHITE))
    assert len(board.get_pieces()) == 1
    assert board.get_pieces()[0].position == Position(0, 0)
    assert board.get_pieces()[0].colour == Colour.WHITE
    # assert type(board.get_pieces()[0]) == Piece


def test_board_get_piece_at_position(
    make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]
):
    board = Board()
    piece = make_dummy_piece(Position(0, 1), Colour.WHITE)
    board.add_piece(piece)
    assert board.get_piece_at(Position(0, 1)) == piece
    assert board.get_piece_at(Position(0, 0)) is None


def test_board_is_occupied(
    make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]
):
    board = Board()
    piece = make_dummy_piece(Position(0, 1), Colour.WHITE)
    board.add_piece(piece)
    assert board.is_occupied(Position(0, 1))
    assert not board.is_occupied(Position(0, 0))


def test_board_has_friendly_piece(
    make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]
):
    board = Board()
    piece = make_dummy_piece(Position(0, 1), Colour.WHITE)
    board.add_piece(piece)
    assert board.has_friendly_piece(Position(0, 1), Colour.WHITE)
    assert not board.has_friendly_piece(Position(0, 1), Colour.BLACK)
    assert not board.has_friendly_piece(Position(5, 5), Colour.WHITE)
    assert not board.has_friendly_piece(Position(5, 5), Colour.BLACK)


def test_board_has_enemy_piece(
    make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]
):
    board = Board()
    piece = make_dummy_piece(Position(0, 1), Colour.BLACK)
    board.add_piece(piece)
    assert board.has_enemy_piece(Position(0, 1), Colour.WHITE)
    assert not board.has_enemy_piece(Position(0, 1), Colour.BLACK)
    assert not board.has_enemy_piece(Position(5, 5), Colour.WHITE)
    assert not board.has_enemy_piece(Position(5, 5), Colour.BLACK)


def test_board_get_pieces_by_colour(
    make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]
):
    white_piece = make_dummy_piece(Position(0, 0), Colour.WHITE)
    black_piece = make_dummy_piece(Position(0, 0), Colour.BLACK)
    board = Board()
    board.add_piece(white_piece)
    board.add_piece(black_piece)
    assert board.get_pieces(Colour.WHITE) == [white_piece]
    assert board.get_pieces(Colour.BLACK) == [black_piece]


def test_board_move_piece(
    make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]
):
    board = Board()
    piece = make_dummy_piece(Position(0, 4), Colour.WHITE)
    board.add_piece(piece)

    board.move_piece(Position(0, 4), Position(0, 7))

    assert board.get_piece_at(Position(0, 4)) == None
    assert board.get_piece_at(Position(0, 7)) == piece


def test_board_remove_piece(
    make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]
):
    board = Board()
    piece = make_dummy_piece(Position(0, 4), Colour.WHITE)
    board.add_piece(piece)

    board.remove_piece(Position(0, 4))

    assert board.get_piece_at(Position(0, 4)) == None
