from src.pieces import Piece
from src.core import Position
import pytest
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from src.board import Board
    from src.core import Colour


class DummyPiece(Piece):
    def get_legal_moves(self, board: "Board") -> list["Position"]:
        return []


@pytest.fixture()
def make_dummy_piece() -> Callable[["Position", "Colour"], "DummyPiece"]:
    def _make(position: "Position", colour: "Colour") -> "DummyPiece":
        return DummyPiece(position, colour)

    return _make
