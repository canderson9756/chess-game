from src.game.state import GameState
import pytest

def test_game_state_is_abstract():
    with pytest.raises(TypeError):
        GameState() # type: ignore

