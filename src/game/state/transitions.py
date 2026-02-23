from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.game.game import Game
    from src.game.state import GameState

def determine_next_state(game: 'Game') -> 'GameState':
    from src.game.state.playing_state import PlayingState
    from src.game.state.check_state import CheckState
    from src.game.state.checkmate_state import CheckmateState
    from src.game.state.stalemate_state import StalemateState
    if game.is_in_check(game.player_turn) and not game.has_legal_moves(game.player_turn):
        return CheckmateState()
    elif game.is_in_check(game.player_turn) and game.has_legal_moves(game.player_turn):
        return CheckState()
    elif not game.is_in_check(game.player_turn) and not game.has_legal_moves(game.player_turn):
        return StalemateState()
    else:
        return PlayingState()