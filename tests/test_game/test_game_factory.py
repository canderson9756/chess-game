# tests/test_game/test_game_factory.py
from src.game import GameFactory, Game
from src.core import Colour

def test_game_factory_creates_game():
    game = GameFactory.create_standard_game()
    assert isinstance(game, Game)

def test_standard_game_has_32_pieces():
    game = GameFactory.create_standard_game()
    assert len(game.board.get_pieces()) == 32

def test_standard_game_has_validator():
    game = GameFactory.create_standard_game()
    # Validator should reject moves that leave king in check
    assert game._validator is not None  # type: ignore

def test_standard_game_white_moves_first():
    game = GameFactory.create_standard_game()
    assert game.player_turn == Colour.WHITE
