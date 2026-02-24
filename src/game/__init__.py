"""Game management module.

This package provides the main Game class for managing chess game flow,
along with factory methods for creating games with different configurations.

Classes:
    Game: Main game controller handling moves, turns, and game state.
    GameFactory: Factory for creating games with standard or custom setups.
"""

from .game import Game
from .game_factory import GameFactory

__all__ = ['Game', 'GameFactory']