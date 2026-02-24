from src.board import BoardBuilder
from src.pieces import *
from src.core import Position, Colour

def test_builder_builds_empty_board():
    builder = BoardBuilder()
    board = builder.build()
    assert board is not None
    assert len(board.get_pieces()) == 0

def test_board_builder_returns_self_for_chaining():
    builder = BoardBuilder()
    result = builder.with_piece(King(Position(4, 0), Colour.WHITE))
    assert result is builder

def test_with_piece_adds_piece():
    board = BoardBuilder() \
        .with_piece(King(Position(4, 0), Colour.WHITE)) \
        .build()

    assert board.get_piece_at(Position(4, 0)) is not None

def test_with_piece_multiple_pieces():
    board = BoardBuilder() \
        .with_piece(King(Position(4, 0), Colour.WHITE)) \
        .with_piece(King(Position(4, 7), Colour.BLACK)) \
        .build()

    assert len(board.get_pieces()) == 2

def test_with_standard_position_has_32_pieces():
    board = BoardBuilder().with_standard_position().build()
    assert len(board.get_pieces()) == 32

def test_with_standard_position_has_16_white_pieces():
    board = BoardBuilder().with_standard_position().build()
    white_pieces = board.get_pieces(Colour.WHITE)
    assert len(white_pieces) == 16

def test_with_standard_position_has_16_black_pieces():
    board = BoardBuilder().with_standard_position().build()
    black_pieces = board.get_pieces(Colour.BLACK)
    assert len(black_pieces) == 16

def test_with_standard_position_kings_in_correct_position():
    board = BoardBuilder().with_standard_position().build()
    white_king = board.get_piece_at(Position(4, 0))
    black_king = board.get_piece_at(Position(4, 7))
    assert isinstance(white_king, King)
    assert isinstance(black_king, King)

def test_with_standard_position_white_pawns_on_rank_2():
    board = BoardBuilder().with_standard_position().build()
    for file in range(8):
        piece = board.get_piece_at(Position(file, 1))
        assert isinstance(piece, Pawn)
        assert piece.colour == Colour.WHITE
