from src.core.position import Position
from ..base.piece import Piece

class Knight(Piece):
    def get_legal_moves(self) -> list[Position]:
        return []