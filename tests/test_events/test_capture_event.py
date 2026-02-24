from src.events import CaptureEvent
from src.core import Colour, Position
from src.pieces import Queen

def test_capture_event_stores_both_pieces():
    captured = Queen(Position(2, 2), Colour.BLACK)
    capturing = Queen(Position(1, 0), Colour.WHITE)
    event = CaptureEvent(captured, capturing)
    assert event.captured_piece == captured
    assert event.capturing_piece == capturing
