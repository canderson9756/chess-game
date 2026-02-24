from src.events import MoveEvent
from src.core import Colour, Position
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ..conftest import *

def test_move_event_stores_origin_destination(make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]):
    origin = Position(0, 0)
    destination = Position(3, 6)
    piece = make_dummy_piece(origin, Colour.WHITE)
    move_event = MoveEvent(piece, origin, destination)
    assert move_event.piece == piece
    assert move_event.origin ==origin
    assert move_event.destination == destination
    assert move_event.timestamp is not None