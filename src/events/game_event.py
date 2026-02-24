"""Base class for all game events.

This module provides the GameEvent base class that all specific events inherit from.
"""

from dataclasses import dataclass, field
import time


@dataclass
class GameEvent:
    """Base class for all game events.

    All events automatically receive a timestamp when created.

    Attributes:
        timestamp: Unix timestamp when the event was created.
    """

    timestamp: float = field(default_factory=time.time, kw_only=True)