from src.game.state import CheckState, PlayingState, CheckmateState
from src.game import Game
from src.pieces import Rook, Queen
from src.core import Position, Colour

def test_check_state_not_game_over():
    state = CheckState()
    assert state.is_game_over() == False

def test_check_state_status():
    state = CheckState()
    assert state.get_status() == "Check"

def test_check_state_rejects_moves_not_out_of_check(game_with_validation: 'Game'):
    rook = Rook(Position(4, 3), Colour.BLACK)   # Enemy rook checking white king
    game_with_validation.board.add_piece(rook)

    state = CheckState()
    result = state.handle_move(game_with_validation, Position(4, 0), Position(4, 1))

    assert result == False

def test_check_state_allows_move_out_of_check(game_with_validation: 'Game'):
    rook = Rook(Position(4, 3), Colour.BLACK)   # Enemy rook checking white king
    game_with_validation.board.add_piece(rook)

    state = CheckState()

    result = state.handle_move(game_with_validation, Position(4, 0), Position(3, 0))
    assert result == True

def test_check_state_transitions_to_playing_after_escape_move(game_with_validation: 'Game'):
    rook = Rook(Position(4, 3), Colour.BLACK)   # Enemy rook checking white king
    game_with_validation.board.add_piece(rook)

    game_with_validation.set_state(CheckState())
    game_with_validation.make_move(Position(4,0), Position(3, 0))
    
    assert isinstance(game_with_validation.state, PlayingState)

def test_check_state_stays_with_counter_check(game_with_validation: 'Game'):
    rook = Rook(Position(4, 3), Colour.BLACK)   # Enemy rook checking white king
    friendly_rook = Rook(Position(7, 3), Colour.WHITE)
    game_with_validation.board.add_piece(rook)
    game_with_validation.board.add_piece(friendly_rook)
    game_with_validation.set_state(CheckState())

    game_with_validation.make_move(Position(7, 3), Position(4, 3))
    
    assert isinstance(game_with_validation.state, CheckState)

def test_check_state_transitions_to_checkmante(game_with_validation: 'Game'):
    rook = Rook(Position(4, 3), Colour.BLACK)   # Enemy rook checking white king
    friendly_rook = Rook(Position(7, 3), Colour.WHITE)
    queen1 = Queen(Position(2, 6), Colour.WHITE)
    queen2 = Queen(Position(6, 6), Colour.WHITE)
    game_with_validation.board.add_piece(rook)
    game_with_validation.board.add_piece(friendly_rook)
    game_with_validation.board.add_piece(queen1)
    game_with_validation.board.add_piece(queen2)
    game_with_validation.set_state(CheckState())

    game_with_validation.make_move(Position(7, 3), Position(4, 3))
    
    assert isinstance(game_with_validation.state, CheckmateState)