from src.board.board import Board
from src.core.position import Position
from src.pieces.base.piece import Piece
from .move_strategy import MoveStrategy
from src.core.direction import Direction

KING_MOVES = [
    Direction(0,1),
    Direction(1,1),
    Direction(1,0),
    Direction(1,-1),
    Direction(0,-1),
    Direction(-1,-1),
    Direction(-1, 0),
    Direction(-1,1)
]

class KingStrategy(MoveStrategy):
    def get_legal_moves(self, piece: Piece, board: 'Board') -> list[Position]:
        moves: list[Position] = []
        for move in KING_MOVES:
            target = piece.position + move
            if target.is_valid():
                if board.has_friendly_piece(target, piece.colour):
                    continue
                moves.append(target)
        return moves