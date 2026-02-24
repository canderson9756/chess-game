from src.events import GameEvent

def test_game_event_has_timestamp():
    event = GameEvent()
    assert event.timestamp is not None