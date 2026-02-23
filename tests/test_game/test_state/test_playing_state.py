from src.game.state import PlayingState, CheckState, CheckmateState, StalemateState
from src.game import Game
from src.pieces import Knight, Rook, Queen
from src.core import Position, Colour

import pytest

def test_playing_state_allows_valid_move(game_with_validation: 'Game'):
    knight = Knight(Position(1, 0), Colour.WHITE)
    game_with_validation.board.add_piece(knight)

    state = PlayingState()

    result = state.handle_move(game_with_validation, Position(1,0), Position(2, 2))

    assert result == True
    assert knight.position == Position(2, 2)

def test_playing_state_status():
    state = PlayingState()
    assert state.get_status() == "Playing"
    assert state.is_game_over() == False

def test_playing_state_transitions_to_check_when_give_check(game_with_validation: 'Game'):
    rook = Rook(Position(3, 1), Colour.WHITE)
    game_with_validation.board.add_piece(rook)

    game_with_validation.make_move(Position(3, 1), Position(3, 7))

    assert isinstance(game_with_validation.state, CheckState)

def test_playing_state_stays_when_no_check(game_with_validation: 'Game'):
    game_with_validation.make_move(Position(4,0), Position(4,1))    # Move King
    assert isinstance(game_with_validation.state, PlayingState)

def test_playing_state_transitions_to_checkmate_when_check_no_moves(game_with_validation: 'Game'):
    rook1 = Rook(Position(0, 1), Colour.WHITE)
    rook2 = Rook(Position(2, 6), Colour.WHITE)
    game_with_validation.board.add_piece(rook1)
    game_with_validation.board.add_piece(rook2)

    game_with_validation.make_move(Position(0, 1), Position(0, 7))
    assert isinstance(game_with_validation.state, CheckmateState)

def test_playing_state_transitions_to_stalemate_when_no_check_no_moves(game_with_validation: 'Game'):

    rook = Rook(Position(3, 0), Colour.WHITE)
    queen = Queen(Position(6, 0), Colour.WHITE)
    game_with_validation.board.add_piece(rook)
    game_with_validation.board.add_piece(queen)

    game_with_validation.make_move(Position(6, 0), Position(6, 6))

    assert isinstance(game_with_validation.state, StalemateState)
