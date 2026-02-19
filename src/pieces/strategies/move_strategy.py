from abc import ABC, abstractmethod

class MoveStrategy(ABC):
    @abstractmethod
    def get_legal_moves(self, piece: 'Piece', board: 'Board') -> list['Position']:
        pass