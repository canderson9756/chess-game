from src.core import Position, Colour
from src.pieces import Piece, King
from src.board import Board
from src.game import Game
from src.validator import CheckValidator
from src.events import EventListener, GameEvent
import pytest
from typing import Callable

_ALL_POSITIONS = [Position(file, rank) for rank in range(8) for file in range(8)]


class DummyPiece(Piece):
    def get_legal_moves(self, board: "Board") -> list["Position"]:
        return _ALL_POSITIONS
    def get_attack_moves(self, board: Board) -> list[Position]:
        return _ALL_POSITIONS


@pytest.fixture()
def make_dummy_piece() -> Callable[["Position", "Colour"], "DummyPiece"]:
    def _make(position: "Position", colour: "Colour") -> "DummyPiece":
        return DummyPiece(position, colour)
    return _make


@pytest.fixture()
def all_positions() -> list[Position]:
    """All 64 valid board positions, ordered rank by rank (a1..h1, a2..h2, ...)."""
    return list(_ALL_POSITIONS)


@pytest.fixture(params=_ALL_POSITIONS, ids=lambda p: p.to_algebraic())
def position(request: pytest.FixtureRequest) -> Position:
    """Parametrized fixture — runs the test once for every square on the board."""
    return request.param

@pytest.fixture
def game_with_kings():
    game = Game()
    game.board.add_piece(King(Position(4, 0), Colour.WHITE))
    game.board.add_piece(King(Position(4, 7), Colour.BLACK))
    return game

@pytest.fixture
def game_with_validation():
    """Integration test fixture - full validation with kings"""
    game = Game(validator=CheckValidator())
    game.board.add_piece(King(Position(4, 0), Colour.WHITE))
    game.board.add_piece(King(Position(4, 7), Colour.BLACK))
    return game

@pytest.fixture
def board_with_kings():
    """Board with both kings for integration tests"""
    board = Board()
    board.add_piece(King(Position(4, 0), Colour.WHITE))
    board.add_piece(King(Position(4, 7), Colour.BLACK))
    return board

class MockListener(EventListener):
    def __init__(self):
        self.received_event: 'GameEvent | None' = None
        self.call_count: 'int' = 0

    def on_event(self, event: GameEvent) -> None:
        self.received_event = event
        self.call_count += 1

@pytest.fixture
def mock_listener() -> 'EventListener':
    return MockListener()

