from src.core import Colour
from src.events import EventBus, MoveEvent, CaptureEvent, TurnEvent, GameOverEvent

import pytest

class MockListener(EventListener):
    def __init__(self):
        self.received_event: 'GameEvent | None' = None
        self.call_count: 'int' = 0

    def on_event(self, event: GameEvent) -> None:
        self.received_event = event
        self.call_count += 1

def test_game_publishes_move_event(game_with_validation):
    listener = MockListener()
    EventBus().clear()
    EventBus().subscribe(MoveEvent, listener)

    knight = Knight(Position(1, 0), Colour.WHITE)
    game_with_validation.board.add_piece(knight)
    game_with_validation.make_move(Position(1, 0), Position(2, 2))

    assert isinstance(listener.received_event, MoveEvent)
    assert listener.received_event.piece == knight

def test_game_publishes_capture_event(game_with_validation):
    listener = MockListener()
    EventBus().clear()
    EventBus().subscribe(CaptureEvent, listener)

    rook = Rook(Position(0, 0), Colour.WHITE)
    enemy = Pawn(Position(0, 6), Colour.BLACK)
    game_with_validation.board.add_piece(rook)
    game_with_validation.board.add_piece(enemy)
    game_with_validation.make_move(Position(0, 0), Position(0, 6))

    assert isinstance(listener.received_event, CaptureEvent)

def test_game_publishes_turn_event(game_with_validation):
    listener = MockListener()
    EventBus().clear()
    EventBus().subscribe(TurnEvent, listener)

    # Make a move...
    assert listener.received_event.colour == Colour.BLACK  # After white moves

def test_game_publishes_check_event(game_with_validation):
    # Setup position where move gives check
    listener = MockListener()
    EventBus().subscribe(CheckEvent, listener)
    # Make move that gives check...
    assert listener.received_event.colour_in_check == Colour.BLACK
