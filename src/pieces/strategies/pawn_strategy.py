from src.board.board import Board
from src.core.position import Position
from src.pieces.base.piece import Piece
from .move_strategy import MoveStrategy
from src.core.direction import Direction

class PawnStrategy(MoveStrategy):
    def get_legal_moves(self, piece: Piece, board: 'Board') -> list[Position]:
        moves: list[Position] = []
        direction = piece.colour.direction()

        forward = piece.position + Direction(0, direction)
        if forward.is_valid() and not board.is_occupied(forward):
            moves.append(forward)
            if piece.first_move: # type: ignore
                forward = forward + Direction(0, direction)
                if forward.is_valid() and not board.is_occupied(forward):
                    moves.append(forward)
        
        dx = [-1, 1]    # Movements for capturing
        for capture_direction in dx:
            diagonal = piece.position + Direction(capture_direction, direction)
            if diagonal.is_valid() and board.has_enemy_piece(diagonal, piece.colour):
                moves.append(diagonal)

        return moves