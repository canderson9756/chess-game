from src.pieces import Piece
from src.core import Position, Colour
from src.board import Board
import pytest
from typing import Callable

_ALL_POSITIONS = [Position(file, rank) for rank in range(8) for file in range(8)]


class DummyPiece(Piece):
    def get_legal_moves(self, board: "Board") -> list["Position"]:
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
