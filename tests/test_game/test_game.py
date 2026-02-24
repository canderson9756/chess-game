from src import Game
from src.board import Board,BoardBuilder
from src.core import Colour, Position
from src.moves import MoveHistory
from src.pieces import Queen, Rook, Knight, King
from src.game.state import PlayingState

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

def test_game_starts_in_playing_state():
    game = Game()
    assert isinstance(game.state, PlayingState)

def test_game_is_in_check(game_with_validation: 'Game'):
    rook = Rook(Position(4, 3), Colour.BLACK)
    game_with_validation.board.add_piece(rook)
    assert game_with_validation.is_in_check(Colour.WHITE)

def test_game_not_in_check(game_with_validation: 'Game'):
    rook = Rook(Position(5, 3), Colour.BLACK)
    game_with_validation.board.add_piece(rook)
    assert not game_with_validation.is_in_check(Colour.WHITE)

def test_game_has_legal_moves(game_with_validation: 'Game'):
    rook = Rook(Position(5, 3), Colour.BLACK)
    game_with_validation.board.add_piece(rook)
    assert game_with_validation.has_legal_moves(Colour.WHITE)
    assert game_with_validation.has_legal_moves(Colour.BLACK)

def test_game_not_has_legal_moves(game_with_validation: 'Game'):
    # Set up rooks to put king in stalemate
    rook1 = Rook(Position(5, 1), Colour.BLACK)
    rook2 = Rook(Position(3, 1), Colour.BLACK)

    game_with_validation.board.add_piece(rook1)
    game_with_validation.board.add_piece(rook2)

    assert not game_with_validation.has_legal_moves(Colour.WHITE)

def test_game_make_move(game_with_kings: 'Game', make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]):
    origin, destination = Position(0,0), Position(1, 5)
    piece = make_dummy_piece(origin, Colour.WHITE)

    game_with_kings.board.add_piece(piece)
    result = game_with_kings.make_move(origin, destination)
    assert result == True
    assert piece.position == destination

def test_game_changes_player_turn(game_with_kings: 'Game',make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]):
    origin, destination = Position(0,0), Position(1, 5)
    piece = make_dummy_piece(origin, Colour.WHITE)
    game_with_kings.board.add_piece(piece)
    game_with_kings.make_move(origin, destination)
    assert game_with_kings.player_turn == Colour.BLACK

def test_game_make_move_can_be_undone(game_with_kings: 'Game', make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]):
    piece = make_dummy_piece(Position(1, 0), Colour.WHITE)
    game_with_kings.board.add_piece(piece)

    game_with_kings.make_move(Position(1, 0), Position(2, 2))

    assert game_with_kings.player_turn == Colour.BLACK

    # This only works if a Move was pushed to history
    game_with_kings.undo()

    assert piece.position == Position(1, 0)  # Back to original
    assert game_with_kings.player_turn == Colour.WHITE     # Bak to original player

def test_game_make_capture_move(game_with_kings: 'Game'):
    piece = Queen(Position(0, 3), Colour.WHITE)
    enemy = Queen(Position(3, 3), Colour.BLACK)
    game_with_kings.board.add_piece(piece)
    game_with_kings.board.add_piece(enemy)

    result = game_with_kings.make_move(Position(0, 3), Position(3, 3))

    assert result == True
    assert piece.position == Position(3,3)
    assert enemy not in game_with_kings.board.get_pieces()

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

def test_game_redo(game_with_kings: 'Game', make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]):
    piece = make_dummy_piece(Position(1, 0), Colour.WHITE)
    game_with_kings.board.add_piece(piece)

    game_with_kings.make_move(Position(1, 0), Position(2, 2))

    assert game_with_kings.player_turn == Colour.BLACK

    # This only works if a Move was pushed to history
    game_with_kings.undo()

    assert piece.position == Position(1, 0)  # Back to original
    assert game_with_kings.player_turn == Colour.WHITE     # Bak to original player

    game_with_kings.redo()

    assert piece.position == Position(2, 2)
    assert game_with_kings.player_turn == Colour.BLACK

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

def test_game_accepts_board_parameter():
    board = BoardBuilder().with_piece(King(Position(4, 0), Colour.WHITE)).build()
    game = Game(board=board)
    assert game.board.get_piece_at(Position(4, 0)) is not None

def test_game_defaults_to_empty_board():
    game = Game()
    assert len(game.board.get_pieces()) == 0
