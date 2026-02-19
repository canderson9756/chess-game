from src.core.position import Position
from src.pieces.base.piece import Piece
from src.core.colour import Colour
from src.pieces.strategies.king_strategy import KingStrategy
from src.board.board import Board

class King(Piece):
    def __init__(self, position: 'Position', colour: 'Colour'):
        super().__init__(position, colour)
        self._strategy = KingStrategy()

    def get_legal_moves(self, board: 'Board') -> list[Position]:
        return self._strategy.get_legal_moves(self, board)