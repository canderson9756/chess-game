"""Event system implementing the Observer pattern.

This package provides an event-driven architecture for game notifications.
Components can subscribe to specific event types and receive notifications
when those events occur.

Classes:
    GameEvent: Base class for all game events.
    EventListener: Abstract listener interface.
    EventBus: Singleton event dispatcher.
    MoveEvent: Event fired when a piece moves.
    CaptureEvent: Event fired when a piece is captured.
    CheckEvent: Event fired when a king is in check.
    TurnEvent: Event fired when the turn changes.
    GameOverEvent: Event fired when the game ends.
"""

from .game_event import GameEvent
from .event_listener import EventListener
from .event_bus import EventBus
from .move_event import MoveEvent
from .capture_event import CaptureEvent
from .game_over_event import GameOverEvent
from .turn_event import TurnEvent
from .check_event import CheckEvent

__all__ = ['GameEvent', 'EventListener', 'EventBus', 'MoveEvent', 'CaptureEvent', 'GameOverEvent', 'CheckEvent', 'TurnEvent']
