from src.events import CheckEvent
from src.core import Colour

def test_turn_event_stores_colour():
    event = CheckEvent(Colour.WHITE)
    assert event.colour_in_check == Colour.WHITE 