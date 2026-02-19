from src.board.board import Board
from src.core.colour import Colour

class Game:
    def __init__(self):
        self.board = Board()
        self.player_turn = Colour.WHITE