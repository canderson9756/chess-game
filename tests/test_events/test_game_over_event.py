from src.events import GameOverEvent
from src.core import Colour

def test_checkmate_stores_result_and_winner():
    event = GameOverEvent("Checkmate", Colour.WHITE)
    assert event.result == "Checkmate"
    assert event.winner == Colour.WHITE

def test_stalemate_stores_result_and_no_winner():
    event = GameOverEvent("Stalemate", None)
    assert event.winner == None