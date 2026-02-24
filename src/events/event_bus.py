from .game_event import GameEvent
from .event_listener import EventListener

from collections import defaultdict

class EventBus():
    _instance: 'EventBus | None' = None
    _listeners: 'defaultdict[type[GameEvent], list[EventListener]]'

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._listeners = defaultdict(list)
        return cls._instance
    
    def subscribe(self, event_type: 'type[GameEvent]', listener: 'EventListener') -> 'None':
        self._listeners[event_type].append(listener)
    
    def publish(self, event: 'GameEvent') -> 'None':
        listeners = self._listeners[type(event)]
        for listener in listeners:
            listener.on_event(event)

    def clear(self) -> 'None':
        self._listeners = defaultdict(list)

    def unsubscribe(self, event_type: 'type[GameEvent]', listener: 'EventListener'):
        type_listeners = self._listeners[event_type]
        for i, type_listener in enumerate(type_listeners):
            if listener is type_listener:
                type_listeners.pop(i)
                break

    @property
    def listeners(self):
        return self._listeners