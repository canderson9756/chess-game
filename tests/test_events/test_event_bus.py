from src.events import EventBus, GameEvent, EventListener

import pytest

class MockListener(EventListener):
    def __init__(self):
        self.received_event: 'GameEvent | None' = None
        self.call_count: 'int' = 0

    def on_event(self, event: GameEvent) -> None:
        self.received_event = event
        self.call_count += 1

def test_event_bus_is_singleton():
    bus1 = EventBus()
    bus2 = EventBus()
    assert bus1 is bus2

def test_subscribe_adds_listener(mock_listener: 'EventListener'):
    bus = EventBus()
    bus.subscribe(GameEvent, mock_listener)
    assert mock_listener in bus.listeners[GameEvent]

def test_subscribe_adds_multiple_listeners(mock_listener: 'EventListener'):
    bus = EventBus()
    listener2 = MockListener()
    bus.subscribe(GameEvent, mock_listener)
    bus.subscribe(GameEvent, listener2)
    assert mock_listener in bus.listeners[GameEvent]
    assert listener2 in bus.listeners[GameEvent]
    
def test_publish_notifies_event_listener(mock_listener: 'MockListener'):
    bus = EventBus()
    bus.subscribe(GameEvent, mock_listener)
    event = GameEvent()
    bus.publish(event)
    assert mock_listener.received_event == event
    assert mock_listener.call_count == 1

def test_unsubscribe_removes_listener(mock_listener: 'EventListener'):
    bus = EventBus()
    bus.clear()
    bus.subscribe(GameEvent, mock_listener)
    bus.unsubscribe(GameEvent, mock_listener)
    assert mock_listener not in bus.listeners[GameEvent]

def test_unsubscribe_stops_notifications(mock_listener: 'MockListener'):
    bus = EventBus()
    bus.clear()
    bus.subscribe(GameEvent, mock_listener)
    bus.unsubscribe(GameEvent, mock_listener)
    bus.publish(GameEvent())
    assert mock_listener.received_event is None

