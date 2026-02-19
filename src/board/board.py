from src.core.position import Position
from src.core.colour import Colour
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.pieces.base.piece import Piece
class Board:
    def __init__(self):
        self._pieces: list['Piece'] = []
    
    @property
    def bounds(self) -> tuple[int, int]:
        return (0,7)
        
    def add_piece(self, piece: 'Piece') -> None:
        self._pieces.append(piece)

    def get_piece_at(self, position: 'Position') -> 'Piece | None':
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

    def get_pieces(self, colour: 'Colour | None' = None) -> list['Piece']:
        if colour is None:
            return self._pieces
        return [p for p in self._pieces if p.colour == colour]
    
    def move_piece(self, move_from: 'Position', move_to: 'Position') -> None:
        piece = self.get_piece_at(move_from)
        if piece:
            piece.set_position(move_to)
        else:
            raise LookupError("Move from position not found. Look at other logic")
        
    def remove_piece(self, remove_position: 'Position') -> None:
        piece = self.get_piece_at(remove_position)
        if piece:
            self._pieces.remove(piece)
        else:
            raise TypeError(f"No piece at the given location: {remove_position}")
