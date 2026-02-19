"""Abstract base class for movement strategies.

This module defines the MoveStrategy interface that all concrete
movement strategies must implement.
"""

from abc import ABC, abstractmethod
from src.board.board import Board
from src.pieces.base.piece import Piece
from src.core.position import Position


class MoveStrategy(ABC):
    """Abstract base class for piece movement strategies.

    MoveStrategy defines the interface for calculating legal moves.
    Each piece type has a corresponding strategy that implements
    its unique movement rules.
    """

    @abstractmethod
    def get_legal_moves(self, piece: "Piece", board: "Board") -> list["Position"]:
        """Calculate all legal moves for a piece.

        Args:
            piece: The piece to calculate moves for.
            board: The current board state for collision detection.

        Returns:
            A list of valid destination positions.
        """
