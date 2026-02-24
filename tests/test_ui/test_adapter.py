from src.ui import GameAdapter

import pytest


def test_game_adapter_is_abstract():
    with pytest.raises(TypeError):
        GameAdapter()   # type: ignore
