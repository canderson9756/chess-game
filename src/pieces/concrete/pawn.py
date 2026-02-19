from src.core.position import Position
from src.pieces.base.piece import Piece
from src.core.colour import Colour
from src.pieces.strategies.pawn_strategy import PawnStrategy
from src.board.board import Board

class Pawn(Piece):
    def __init__(self, position: 'Position', colour: 'Colour'):
        super().__init__(position, colour)
        self._strategy = PawnStrategy()

    def get_legal_moves(self, board: 'Board') -> list[Position]:
        return self._strategy.get_legal_moves(self, board)