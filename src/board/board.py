from src.pieces.base.piece import Piece
from src.core.position import Position

class Board:
    def __init__(self):
        self._pieces: list['Piece'] = []
    
    @property
    def bounds(self) -> tuple[int, int]:
        return (0,7)
    
    def get_pieces(self) -> list['Piece']:
        return self._pieces
    
    def add_piece(self, piece: 'Piece') -> None:
        self._pieces.append(piece)

    def get_piece_at(self, position: 'Position') -> Piece | None:
        for piece in self._pieces:
            if piece.position == position:
                return piece
        return None