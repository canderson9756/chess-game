from .move_strategy import MoveStrategy
from src.core.direction import Direction
from src.core.position import Position
from src.pieces.base.piece import Piece
from src.board.board import Board

KNIGHT_MOVES = [
    Direction(1, 2), Direction(2, 1),
    Direction(-1, 2), Direction(-2, 1),
    Direction(1, -2), Direction(2, -1),
    Direction(-1, -2), Direction(-2, -1),
]

class KnightStrategy(MoveStrategy):
    def get_legal_moves(self, piece: 'Piece', board: 'Board') -> list['Position']:
        moves: list['Position'] = []
        for move in KNIGHT_MOVES:
            target = piece.position + move
            if target.is_valid():
                if board.has_friendly_piece(target, piece.colour):
                    continue
                moves.append(target)
        return moves