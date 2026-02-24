"""Singleton event bus for publishing and subscribing to game events.

This module provides the EventBus class which implements the Observer pattern
as a central dispatcher for game events.
"""

from .game_event import GameEvent
from .event_listener import EventListener

from collections import defaultdict


class EventBus():
    """Singleton event bus for game event dispatching.

    EventBus allows components to subscribe to specific event types and
    receive notifications when those events are published. Uses the
    Singleton pattern to ensure a single global event bus.

    Example:
        >>> bus = EventBus()
        >>> bus.subscribe(MoveEvent, my_listener)
        >>> bus.publish(MoveEvent(piece, origin, destination))
    """

    _instance: 'EventBus | None' = None
    _listeners: 'defaultdict[type[GameEvent], list[EventListener]]'

    def __new__(cls):
        """Create or return the singleton EventBus instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._listeners = defaultdict(list)
        return cls._instance

    def subscribe(self, event_type: 'type[GameEvent]', listener: 'EventListener') -> 'None':
        """Subscribe a listener to a specific event type.

        Args:
            event_type: The type of event to listen for.
            listener: The listener to notify when the event occurs.
        """
        self._listeners[event_type].append(listener)

    def publish(self, event: 'GameEvent') -> 'None':
        """Publish an event to all subscribed listeners.

        Args:
            event: The event to publish.
        """
        listeners = self._listeners[type(event)]
        for listener in listeners:
            listener.on_event(event)

    def clear(self) -> 'None':
        """Remove all listeners from all event types."""
        self._listeners = defaultdict(list)

    def unsubscribe(self, event_type: 'type[GameEvent]', listener: 'EventListener') -> None:
        """Remove a listener from a specific event type.

        Args:
            event_type: The event type to unsubscribe from.
            listener: The listener to remove.
        """
        type_listeners = self._listeners[event_type]
        for i, type_listener in enumerate(type_listeners):
            if listener is type_listener:
                type_listeners.pop(i)
                break

    @property
    def listeners(self):
        """Get the dictionary of all listeners by event type."""
        return self._listeners