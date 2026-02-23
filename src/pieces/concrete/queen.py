"""Queen piece implementation.

This module provides the Queen class representing the queen chess piece
which combines rook and bishop movement.
"""

from src.core.position import Position
from src.pieces.base.piece import Piece
from src.core.colour import Colour
from src.pieces.strategies.queen_strategy import QueenStrategy
from src.board.board import Board


class Queen(Piece):
    """A queen chess piece.

    Queens can move any number of squares horizontally, vertically, or
    diagonally. They combine the movement of rooks and bishops but
    cannot jump over other pieces.
    """

    def __init__(self, position: "Position", colour: "Colour"):
        """Initialize a queen at the given position.

        Args:
            position: The starting position.
            colour: The queen's colour.
        """
        super().__init__(position, colour)
        self._strategy = QueenStrategy()

    def get_legal_moves(self, board: "Board") -> list[Position]:
        """Get all legal moves for this queen.

        Args:
            board: The current board state.

        Returns:
            List of valid positions the queen can move to.
        """
        return self._strategy.get_legal_moves(self, board)

    def get_attack_moves(self, board: Board) -> list[Position]:
        return self._strategy.get_attack_moves(self, board)