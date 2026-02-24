from .board import Board
from src.core.colour import Colour
from src.core.position import Position
from src.pieces.base.piece import Piece
from src.pieces.concrete.bishop import Bishop
from src.pieces.concrete.king import King
from src.pieces.concrete.knight import Knight
from src.pieces.concrete.pawn import Pawn
from src.pieces.concrete.queen import Queen
from src.pieces.concrete.rook import Rook

class BoardBuilder:

    def __init__(self):
        self._board = Board()

    def build(self) -> 'Board':
        return self._board
    
    def with_piece(self, piece: 'Piece') -> 'BoardBuilder':
        self._board.add_piece(piece)
        return self
    
    def with_standard_position(self) -> 'BoardBuilder':
        self._board.add_piece(Rook(Position(0, 0), Colour.WHITE))
        self._board.add_piece(Knight(Position(1, 0), Colour.WHITE))
        self._board.add_piece(Bishop(Position(2, 0), Colour.WHITE))
        self._board.add_piece(Queen(Position(3, 0), Colour.WHITE))
        self._board.add_piece(King(Position(4, 0), Colour.WHITE))
        self._board.add_piece(Bishop(Position(5, 0), Colour.WHITE))
        self._board.add_piece(Knight(Position(6, 0), Colour.WHITE))
        self._board.add_piece(Rook(Position(7, 0), Colour.WHITE))

        for file in range(8):
            self._board.add_piece(Pawn(Position(file, 1), Colour.WHITE))

        self._board.add_piece(Rook(Position(0, 7), Colour.BLACK))
        self._board.add_piece(Knight(Position(1, 7), Colour.BLACK))
        self._board.add_piece(Bishop(Position(2, 7), Colour.BLACK))
        self._board.add_piece(Queen(Position(3, 7), Colour.BLACK))
        self._board.add_piece(King(Position(4, 7), Colour.BLACK))
        self._board.add_piece(Bishop(Position(5, 7), Colour.BLACK))
        self._board.add_piece(Knight(Position(6, 7), Colour.BLACK))
        self._board.add_piece(Rook(Position(7, 7), Colour.BLACK))

        for file in range(8):
            self._board.add_piece(Pawn(Position(file, 6), Colour.BLACK))

        return self