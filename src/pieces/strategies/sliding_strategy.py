"""Base strategy for sliding pieces (Rook, Bishop, Queen).

This module provides the SlidingStrategy abstract class that handles
movement logic for pieces that slide along directions until blocked.
"""

from src.pieces.strategies.move_strategy import MoveStrategy
from src.pieces.base.piece import Piece
from src.board.board import Board
from src.core.direction import Direction
from src.core.position import Position
from abc import abstractmethod


class SlidingStrategy(MoveStrategy):
    """Base strategy for pieces that slide along directions.

    Sliding pieces (Rook, Bishop, Queen) move any number of squares
    in their allowed directions until they reach the board edge,
    a friendly piece (blocked), or an enemy piece (capture).

    Subclasses must implement the `directions` property to define
    which directions the piece can move.
    """

    @property
    @abstractmethod
    def directions(self) -> list['Direction']:
        """Get the directions this piece can move.

        Returns:
            A list of Direction objects representing valid movement vectors.
        """
        pass

    def get_legal_moves(self, piece: 'Piece', board: 'Board') -> list['Position']:
        """Calculate all legal moves by extending in each direction.

        Args:
            piece: The piece to calculate moves for.
            board: The current board state.

        Returns:
            A list of valid destination positions.
        """
        moves: list['Position'] = []
        for direction in self.directions:
            moves.extend(self._get_moves_in_direction(piece, board, direction))
        return moves

    def _get_moves_in_direction(self, piece: 'Piece', board: 'Board | None', direction: 'Direction') -> list['Position']:
        """Get all moves in a single direction.

        Extends from the piece's position in the given direction until
        hitting a board edge, friendly piece, or enemy piece.

        Args:
            piece: The piece to calculate moves for.
            board: The current board state (None to ignore collisions).
            direction: The direction to extend moves.

        Returns:
            A list of valid positions in this direction.
        """
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