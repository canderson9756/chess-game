"""Abstract base validator for the Chain of Responsibility pattern.

This module provides the Validator abstract class that defines the interface
for move validation chains.
"""

from abc import ABC, abstractmethod
from src.moves.move import Move
from src.board.board import Board


class Validator(ABC):
    """Abstract base class for move validators using Chain of Responsibility.

    Validators can be chained together, with each validator checking a specific
    condition. If validation passes, it delegates to the next validator in the chain.

    Example:
        >>> chain = CheckValidator()
        >>> chain.set_next(BoundsValidator())
        >>> is_valid = chain.validate(move, board)
    """

    def __init__(self):
        """Initialize the validator with no next validator in chain."""
        self._next: 'Validator | None' = None

    def set_next(self, next_validator: 'Validator') -> None:
        """Set the next validator in the chain.

        Args:
            next_validator: The validator to call if this validation passes.
        """
        self._next = next_validator

    def validate(self, move: 'Move', board: 'Board') -> 'bool | None | Validator':
        """Validate a move and delegate to the next validator if valid.

        Args:
            move: The move to validate.
            board: The current board state.

        Returns:
            True if the entire chain validates successfully,
            False if any validator rejects the move.
        """
        if not self._do_validate(move, board):
            return False
        if self._next:
            return self._next.validate(move, board)  # type: ignore
        return True

    @abstractmethod
    def _do_validate(self, move: 'Move', board: 'Board') -> 'bool':
        """Perform the specific validation logic for this validator.

        Args:
            move: The move to validate.
            board: The current board state.

        Returns:
            True if validation passes, False otherwise.
        """
        pass