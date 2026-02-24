"""State transition logic for the game state machine.

This module provides the function to determine the next game state
based on check and legal move conditions.
"""

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.game.game import Game
    from src.game.state import GameState


def determine_next_state(game: 'Game') -> 'GameState':
    """Determine the next game state based on current conditions.

    Evaluates whether the current player is in check and has legal moves
    to determine the appropriate next state.

    Args:
        game: The game instance to evaluate.

    Returns:
        The appropriate GameState:
        - CheckmateState if in check with no legal moves
        - CheckState if in check with legal moves
        - StalemateState if not in check with no legal moves
        - PlayingState otherwise
    """
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