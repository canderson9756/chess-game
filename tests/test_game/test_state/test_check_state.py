from src.game.state import CheckState
from src.game import Game
from src.pieces import Rook
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
