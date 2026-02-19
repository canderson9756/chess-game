from src.pieces.base.piece import Piece
from src.core.position import Position
from src.core.colour import Colour

import pytest
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from ...conftest import *


def test_piece_is_abstract():
    with pytest.raises(TypeError):
        Piece(Position(0,0), Colour.WHITE) # type: ignore[abstract]

def test_piece_has_position_and_colour(make_dummy_piece: Callable[['Position', 'Colour'], 'DummyPiece']):
    piece = make_dummy_piece(Position(0, 0), Colour.WHITE) # type: ignore[abstract]
    assert piece.position == Position(0, 0)
    assert piece.colour == Colour.WHITE

def test_piece_can_move(make_dummy_piece: Callable[['Position', 'Colour'], 'DummyPiece']):
    piece = make_dummy_piece(Position(0, 0), Colour.WHITE) # type: ignore[abstract]
    piece.move_to(Position(5, 2))
    assert piece.position == Position(5, 2)

def test_piece_identifies_enemy_colour(make_dummy_piece: Callable[['Position', 'Colour'], 'DummyPiece']):
    white_piece = make_dummy_piece(Position(0, 0), Colour.WHITE) # type: ignore[abstract]
    assert white_piece.is_enemy(Colour.BLACK)
    assert not white_piece.is_enemy(Colour.WHITE)

def test_piece_has_abstract_legal_moves():
    class DummyPieceNoLegalMoves(Piece):
        pass
    with pytest.raises(TypeError):
        DummyPieceNoLegalMoves(Position(0, 0), Colour.WHITE) # type: ignore[abstract]