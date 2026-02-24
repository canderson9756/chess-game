from src.events import TurnEvent
from src.core import Colour

def test_turn_event_stores_colour():
    event = TurnEvent(Colour.WHITE)
    assert event.colour == Colour.WHITE 