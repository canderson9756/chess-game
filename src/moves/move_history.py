from .move import Move
from src.board.board import Board


class MoveHistory:

    def __init__(self):
        self._undo_stack: list["Move"] = []
        self._redo_stack: list["Move"] = []

    def push(self, move: "Move") -> None:
        self._undo_stack.append(move)
        self._redo_stack.clear()

    def undo(self, board: "Board") -> None:
        move = self._undo_stack.pop()
        move.undo(board)
        self._redo_stack.append(move)

    def redo(self, board: "Board") -> None:
        move = self._redo_stack.pop()
        move.execute(board)
        self._undo_stack.append(move)

    def can_undo(self) -> bool:
        return len(self._undo_stack) > 0

    def can_redo(self) -> bool:
        return len(self._redo_stack) > 0
