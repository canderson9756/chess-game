from src.game.state import PlayingState
from src.game import Game
from src.pieces import Knight, Rook
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

def test_playing_state_transitions_to_check(game_with_validation: 'Game'):
    rook = Rook(Position(4, 0), Colour.WHITE)
    game_with_validation.board.add_piece(rook)

    state = PlayingState()