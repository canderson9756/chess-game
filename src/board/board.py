from src.pieces.base.piece import Piece
from src.core.position import Position
from src.core.colour import Colour

class Board:
    def __init__(self):
        self._pieces: list['Piece'] = []
    
    @property
    def bounds(self) -> tuple[int, int]:
        return (0,7)
        
    def add_piece(self, piece: 'Piece') -> None:
        self._pieces.append(piece)

    def get_piece_at(self, position: 'Position') -> Piece | None:
        for piece in self._pieces:
            if piece.position == position:
                return piece
        return None
    
    def is_occupied(self, position: 'Position') -> bool:
        piece = self.get_piece_at(position)
        return True if piece else False
    
    def has_friendly_piece(self, position: 'Position', colour: 'Colour') -> bool:
        piece = self.get_piece_at(position)
        if piece:
            return True if piece.colour == colour else False
        return False
    
    def has_enemy_piece(self, position: 'Position', colour: 'Colour') -> bool:
        piece = self.get_piece_at(position)
        if piece:
            return True if piece.colour != colour else False
        return False

    def get_pieces(self, colour: Colour | None = None) -> list['Piece']:
        if colour is None:
            return self._pieces
        return [p for p in self._pieces if p.colour == colour]