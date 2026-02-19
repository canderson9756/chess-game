from src.pieces.strategies import SlidingStrategy
import pytest


def test_sliding_strategy_is_abstract():
    with pytest.raises(TypeError):
        SlidingStrategy()  # type: ignore[abstract]
