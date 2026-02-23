from src.game.state import CheckmateState
from src.game import Game
from src.core import Position

import pytest


def test_checkmate_state_is_game_over():
    state = CheckmateState()
    assert state.is_game_over() == True


def test_checkmate_state_status():
    state = CheckmateState()
    assert state.get_status() == "Checkmate"


def test_checkmate_state_rejects_all_moves(game_with_validation: 'Game'):
    state = CheckmateState()
    result = state.handle_move(game_with_validation, Position(4, 0), Position(4, 1))
    assert result == False
