from src.pieces.strategies.move_strategy import MoveStrategy
from src.pieces.base.piece import Piece
from src.board.board import Board
from src.core.direction import Direction
from src.core.position import Position
from abc import abstractmethod

class SlidingStrategy(MoveStrategy):
    @property
    @abstractmethod
    def directions(self) -> list['Direction']:
        pass

    def get_legal_moves(self, piece: 'Piece', board: 'Board') -> list['Position']:
        moves: list['Position'] = []
        for direction in self.directions:
            moves.extend(self._get_moves_in_direction(piece, board, direction))
        return moves
    
    def _get_moves_in_direction(self, piece: 'Piece', board: 'Board | None', direction: 'Direction') -> list['Position']:
        moves: list['Position'] = []
        current = piece.position + direction
        while current.is_valid():
            if board is None:
                moves.append(current)
            elif board.has_friendly_piece(current, piece.colour):
                break
            elif board.has_enemy_piece(current, piece.colour):
                moves.append(current)
                break
            else:
                moves.append(current)
            current = current + direction
        return moves