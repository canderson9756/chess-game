"""Abstract event listener interface.

This module provides the EventListener abstract class that defines
the interface for event handlers.
"""

from abc import ABC, abstractmethod
from .game_event import GameEvent


class EventListener(ABC):
    """Abstract base class for event listeners.

    Implement this interface to receive notifications from the EventBus
    when subscribed events occur.

    Example:
        >>> class MoveLogger(EventListener):
        ...     def on_event(self, event):
        ...         print(f"Move made: {event}")
    """

    @abstractmethod
    def on_event(self, event: 'GameEvent') -> 'None':
        """Handle an event notification.

        Args:
            event: The event that occurred.
        """
        pass