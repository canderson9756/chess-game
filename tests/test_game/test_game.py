from src import Game
from src.board import Board
from src.core import Colour, Position
from src.moves import MoveHistory

import pytest
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from ..conftest import *


def test_game_has_board():
    game = Game()
    assert isinstance(game.board, Board)


def tets_game_starts_with_white():
    game = Game()
    assert game.player_turn == Colour.WHITE

def test_game_has_move_history():
    game = Game()
    assert isinstance(game.move_history, MoveHistory)
    assert not game.move_history.can_undo()

def test_game_make_move(make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]):
    origin, destination = Position(0,0), Position(1, 5)
    piece = make_dummy_piece(origin, Colour.WHITE)
    game = Game()
    game.board.add_piece(piece)
    result = game.make_move(origin, destination)
    assert result == True
    assert piece.position == destination
    assert game.player_turn == Colour.BLACK

def test_game_make_move_can_be_undone(make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]):
    game = Game()
    piece = make_dummy_piece(Position(1, 0), Colour.WHITE)
    game.board.add_piece(piece)

    game.make_move(Position(1, 0), Position(2, 2))

    # This only works if a Move was pushed to history
    game.undo()

    assert piece.position == Position(1, 0)  # Back to original
