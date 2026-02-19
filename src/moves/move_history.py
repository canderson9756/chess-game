"""Move history management for undo/redo functionality.

This module provides the MoveHistory class for tracking executed moves
and enabling undo/redo operations during gameplay.
"""

from .move import Move
from src.board.board import Board


class MoveHistory:
    """Manages move history with undo and redo capabilities.

    MoveHistory maintains two stacks: one for moves that can be undone,
    and one for moves that have been undone and can be redone. Executing
    a new move clears the redo stack.

    Example:
        >>> history = MoveHistory()
        >>> history.push(move)
        >>> move.execute(board)
        >>> history.can_undo()
        True
        >>> history.undo(board)  # Reverses the move
        >>> history.can_redo()
        True
        >>> history.redo(board)  # Re-applies the move
    """

    def __init__(self):
        """Initialize an empty move history."""
        self._undo_stack: list["Move"] = []
        self._redo_stack: list["Move"] = []

    def push(self, move: "Move") -> None:
        """Record a new move in the history.

        Adds the move to the undo stack and clears the redo stack,
        since new moves invalidate any previously undone moves.

        Args:
            move: The move to record.
        """
        self._undo_stack.append(move)
        self._redo_stack.clear()

    def undo(self, board: "Board") -> None:
        """Undo the most recent move.

        Pops the last move from the undo stack, reverses it on the board,
        and pushes it to the redo stack.

        Args:
            board: The board to revert.

        Raises:
            IndexError: If there are no moves to undo.
        """
        move = self._undo_stack.pop()
        move.undo(board)
        self._redo_stack.append(move)

    def redo(self, board: "Board") -> None:
        """Redo the most recently undone move.

        Pops the last move from the redo stack, re-executes it on the board,
        and pushes it back to the undo stack.

        Args:
            board: The board to update.

        Raises:
            IndexError: If there are no moves to redo.
        """
        move = self._redo_stack.pop()
        move.execute(board)
        self._undo_stack.append(move)

    def can_undo(self) -> bool:
        """Check if there are moves available to undo.

        Returns:
            True if at least one move can be undone.
        """
        return len(self._undo_stack) > 0

    def can_redo(self) -> bool:
        """Check if there are moves available to redo.

        Returns:
            True if at least one undone move can be redone.
        """
        return len(self._redo_stack) > 0
