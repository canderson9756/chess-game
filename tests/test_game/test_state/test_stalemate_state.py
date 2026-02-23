from src.game.state import StalemateState
from src.game import Game
from src.core import Position

import pytest


def test_stalemate_state_is_game_over():
    state = StalemateState()
    assert state.is_game_over() == True


def test_stalemate_state_status():
    state = StalemateState()
    assert state.get_status() == "Stalemate"


def test_stalemate_state_rejects_all_moves(game_with_validation: 'Game'):
    state = StalemateState()
    result = state.handle_move(game_with_validation, Position(4, 0), Position(4, 1))
    assert result == False
