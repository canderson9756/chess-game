"""Game state machine implementation using the State pattern.

This package provides game states that handle moves differently based on
the current game situation (normal play, check, checkmate, stalemate).

Classes:
    GameState: Abstract base class for game states.
    PlayingState: Normal gameplay state.
    CheckState: State when king is in check.
    CheckmateState: Game over state - checkmate.
    StalemateState: Game over state - stalemate.
"""

from .game_state import GameState
from .playing_state import PlayingState
from .checkmate_state import CheckmateState
from .stalemate_state import StalemateState
from .check_state import CheckState

__all__ = ['GameState', 'PlayingState', 'CheckmateState', 'StalemateState', 'CheckState']