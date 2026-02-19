"""Capture move implementation for chess pieces.

This module provides the CaptureMove class which handles chess moves where
a piece captures an opponent's piece. It implements the Command pattern,
allowing moves to be executed and undone, restoring the captured piece on undo.
"""

from src.board.board import Board
from .move import Move
from src.pieces.base.piece import Piece
from src.core.position import Position


class CaptureMove(Move):
    """A chess move where the moving piece captures an opponent's piece.

    Removes the enemy piece at the destination before moving the attacking
    piece into that square. The captured piece is stored so the move can
    be fully reversed.

    Example:
        >>> move = CaptureMove(knight, Position(2, 1), Position(3, 3))
        >>> move.execute(board)  # Captures enemy at (3, 3) and moves knight there
        >>> move.undo(board)     # Returns knight to (2, 1) and restores captured piece
    """

    def __init__(self, piece: "Piece", origin: "Position", destination: "Position"):
        super().__init__(piece, origin, destination)
        self._captured_piece: "Piece"

    def execute(self, board: "Board") -> None:
        """Capture the enemy piece at the destination and move the piece there.

        Stores the captured piece, removes it from the board, then moves
        the attacking piece from origin to destination.

        Args:
            board: The board to update.
        """
        self._captured_piece = board.get_piece_at(self.destination)  # type: ignore
        board.remove_piece(self.destination)
        board.move_piece(self.origin, self.destination)

    def undo(self, board: "Board") -> None:
        """Reverse the capture by returning both pieces to their original positions.

        Moves the attacking piece back to origin and restores the captured
        piece to the destination square.

        Args:
            board: The board to revert.
        """
        board.move_piece(self.destination, self.origin)
        board.add_piece(self._captured_piece)
