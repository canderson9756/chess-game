"""UI adapter module for different presentation layers.

This package provides the GameAdapter interface for implementing
different user interfaces (CLI, GUI, Web) using the Adapter pattern.

Classes:
    GameAdapter: Abstract interface for UI implementations.
"""

from .adapter import GameAdapter

__all__ = ['GameAdapter']