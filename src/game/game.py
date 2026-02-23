from src.board.board import Board
from src.core.colour import Colour
from src.pieces.base.piece import Piece
from src.moves.move import Move
from src.moves.standard_move import StandardMove
from src.moves.capture_move import CaptureMove
from src.moves.move_history import MoveHistory
from src.validator.validator import Validator

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.position import Position


class Game:
    def __init__(self, validator: 'Validator | None' = None):
        self._board = Board()
        self._player_turn = Colour.WHITE
        self._move_history = MoveHistory()
        self._validator = validator

    def make_move(self, origin: 'Position', destination: 'Position') -> bool:
        piece = self._board.get_piece_at(origin)
        if piece is None:
            return False
        if piece.colour != self._player_turn:
            return False
        legal_moves = piece.get_legal_moves(self._board)
        if destination not in legal_moves:
            return False
        
        move = self._create_move(piece, origin, destination)

        if self._validator and not self._validator.validate(move, self._board):
            return False

        move.execute(self._board)
        self._move_history.push(move)
        self._change_player_turn()
        return True
    
    def _create_move(self, piece: 'Piece', origin: 'Position', destination: 'Position') -> 'Move':
        if self._board.has_enemy_piece(destination, piece.colour):
            return CaptureMove(piece, origin, destination)
        return StandardMove(piece, origin, destination)
    
    def _change_player_turn(self) -> None:
        self._player_turn = self._player_turn.opposite()

    def undo(self) -> None:
        self._move_history.undo(self._board)
        self._change_player_turn()

    def redo(self) -> None:
        self._move_history.redo(self._board)
        self._change_player_turn()

    @property
    def board(self) -> 'Board':
        return self._board
    
    @property
    def player_turn(self) -> 'Colour':
        return self._player_turn
    
    @property
    def move_history(self) -> 'MoveHistory':
        return self._move_history
    
