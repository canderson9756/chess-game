from src import Game
from src.board import Board
from src.core import Colour, Position
from src.moves import MoveHistory
from src.pieces import Queen, Rook, Knight    # Using the queen as a test piece as it has the most flexibility

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

def test_game_changes_player_turn(make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]):
    origin, destination = Position(0,0), Position(1, 5)
    piece = make_dummy_piece(origin, Colour.WHITE)
    game = Game()
    game.board.add_piece(piece)
    game.make_move(origin, destination)
    assert game.player_turn == Colour.BLACK

def test_game_make_move_can_be_undone(make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]):
    game = Game()
    piece = make_dummy_piece(Position(1, 0), Colour.WHITE)
    game.board.add_piece(piece)

    game.make_move(Position(1, 0), Position(2, 2))

    assert game.player_turn == Colour.BLACK

    # This only works if a Move was pushed to history
    game.undo()

    assert piece.position == Position(1, 0)  # Back to original
    assert game.player_turn == Colour.WHITE     # Bak to original player

def test_game_make_capture_move():
    game = Game()
    piece = Queen(Position(0, 3), Colour.WHITE)
    enemy = Queen(Position(3, 3), Colour.BLACK)
    game.board.add_piece(piece)
    game.board.add_piece(enemy)

    result = game.make_move(Position(0, 3), Position(3, 3))

    assert result == True
    assert piece.position == Position(3,3)
    assert enemy not in game.board.get_pieces()

def test_game_cannot_move_wrong_colour(make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]):
    game = Game()
    piece = make_dummy_piece(Position(1, 0), Colour.BLACK)
    game.board.add_piece(piece)

    result = game.make_move(Position(1, 0), Position(2, 2))

    assert result == False
    assert piece.position == Position(1, 0)

def test_game_rejects_illegal_move():
    game = Game()
    piece = Queen(Position(0, 3), Colour.WHITE)
    game.board.add_piece(piece)

    result = game.make_move(Position(0, 3), Position(1, 0))     # Illeagal Queen move

    assert result == False
    assert piece.position == Position(0, 3)

def test_game_redo(make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]):

    game = Game()
    piece = make_dummy_piece(Position(1, 0), Colour.WHITE)
    game.board.add_piece(piece)

    game.make_move(Position(1, 0), Position(2, 2))

    assert game.player_turn == Colour.BLACK

    # This only works if a Move was pushed to history
    game.undo()

    assert piece.position == Position(1, 0)  # Back to original
    assert game.player_turn == Colour.WHITE     # Bak to original player

    game.redo()

    assert piece.position == Position(2, 2)
    assert game.player_turn == Colour.BLACK

def test_game_rejects_move_that_leaves_king_in_check(game_with_validation: 'Game'):
    game = game_with_validation
    rook = Rook(Position(4, 7), Colour.BLACK)  # Attacks king's file
    blocker = Knight(Position(4, 1), Colour.WHITE)  # Blocking
    game.board.add_piece(rook)
    game.board.add_piece(blocker)

    # Try to move blocker away (would expose king)
    result = game.make_move(Position(4, 1), Position(2, 2))

    assert result == False
    assert blocker.position == Position(4, 1)  # Didn't move
