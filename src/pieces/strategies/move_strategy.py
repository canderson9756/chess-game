from abc import ABC, abstractmethod
from src.board.board import Board
from src.pieces.base.piece import Piece
from src.core.position import Position

class MoveStrategy(ABC):
    @abstractmethod
    def get_legal_moves(self, piece: 'Piece', board: 'Board') -> list['Position']:
        pass