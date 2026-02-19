from src.board import Board
from src.core.position import Position
from src.core.colour import Colour
from src.pieces import Piece

def test_board_has_bounds():
    board = Board()
    assert board.bounds == (0, 7)

def test_board_starts_empty():
    board = Board()
    assert board.get_pieces() == []

def test_board_can_add_piece():
    class DummyPiece(Piece):
        def get_legal_moves(self, board: 'Board') -> list[Position]:
            return []
    board = Board()
    board.add_piece(DummyPiece(Position(0, 0), Colour.WHITE))
    assert len(board.get_pieces()) == 1
    assert board.get_pieces()[0].position == Position(0, 0)
    assert board.get_pieces()[0].colour == Colour.WHITE
    assert type(board.get_pieces()[0]) == DummyPiece

def test_board_get_piece_at_position():
    class DummyPiece(Piece):
        def get_legal_moves(self, board: 'Board') -> list[Position]:
            return []
    board = Board()
    piece = DummyPiece(Position(0,1), Colour.WHITE)
    board.add_piece(piece)
    assert board.get_piece_at(Position(0, 1)) == piece
    assert board.get_piece_at(Position(0,0)) is None