from src.game.state.transitions import determine_next_state
from src.game import Game
from src.pieces import Rook
from src.core import Position, Colour
from src.game.state import CheckmateState, CheckState, StalemateState, PlayingState

import pytest

def test_transition_to_checkmate_when_in_check_no_moves(game_with_validation: 'Game'):
    rook1 = Rook(Position(0, 1), Colour.BLACK)
    rook2 = Rook(Position(0, 0), Colour.BLACK)
    game_with_validation.board.add_piece(rook1)
    game_with_validation.board.add_piece(rook2)

    next_state = determine_next_state(game_with_validation)

    assert isinstance(next_state, CheckmateState)

def test_transition_to_stalemate_when_not_in_check_no_moves(game_with_validation: 'Game'):
    rook1 = Rook(Position(3, 1), Colour.BLACK)
    rook2 = Rook(Position(5, 1), Colour.BLACK)
    game_with_validation.board.add_piece(rook1)
    game_with_validation.board.add_piece(rook2)

    next_state = determine_next_state(game_with_validation)

    assert isinstance(next_state, StalemateState)

def test_transition_to_check_when_in_check_with_moves(game_with_validation: 'Game'):
    rook = Rook(Position(0, 0), Colour.BLACK)
    game_with_validation.board.add_piece(rook)

    next_state = determine_next_state(game_with_validation)

    assert isinstance(next_state, CheckState)

def test_transition_to_playing_when_not_in_check_has_moves(game_with_validation: 'Game'):
    next_state = determine_next_state(game_with_validation)
    assert isinstance(next_state, PlayingState)