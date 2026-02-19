from src.core.position import Position
from src.pieces.base.piece import Piece
from src.core.colour import Colour
from src.pieces.strategies.queen_strategy import QueenStrategy
from src.board.board import Board

class Queen(Piece):
    def __init__(self, position: 'Position', colour: 'Colour'):
        super().__init__(position, colour)
        self._strategy = QueenStrategy()

    def get_legal_moves(self, board: 'Board') -> list[Position]:
        return self._strategy.get_legal_moves(self, board)