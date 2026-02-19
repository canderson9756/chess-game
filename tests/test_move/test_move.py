from src.moves import Move
from src.core import Position, Colour
from typing import TYPE_CHECKING, Callable
import pytest

if TYPE_CHECKING:
    from ..conftest import *


def test_move_is_abstract(
    make_dummy_piece: Callable[["Position", "Colour"], "DummyPiece"]
):
    with pytest.raises(TypeError):
        origin = Position(0, 0)
        Move(make_dummy_piece(origin, Colour.WHITE), origin, Position(3, 3))  # type: ignore[abstract]
