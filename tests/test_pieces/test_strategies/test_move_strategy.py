from src.pieces.strategies import MoveStrategy
import pytest


def test_move_strategy_is_abstract():
    with pytest.raises(TypeError):
        MoveStrategy()  # type: ignore[abstract]
