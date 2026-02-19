from src import Game
from src.board import Board
from src.core import Colour


def test_game_has_board():
    game = Game()
    assert isinstance(game.board, Board)


def tets_game_starts_with_white():
    game = Game()
    assert game.player_turn == Colour.WHITE
