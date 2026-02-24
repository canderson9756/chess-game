"""Factory for creating chess games with different configurations.

This module provides the GameFactory class with static methods for creating
games with standard setups, empty boards, or custom positions.
"""

from src.board.builder import BoardBuilder
from src.game.game import Game
from src.validator.check_validator import CheckValidator
from src.pieces.base.piece import Piece


class GameFactory:
    """Factory for creating chess games with various configurations.

    Provides static methods to create games with standard starting positions,
    empty boards for custom setups, or from specific piece arrangements.

    Example:
        >>> game = GameFactory.create_standard_game()
        >>> empty = GameFactory.create_empty_game()
        >>> puzzle = GameFactory.create_from_position([white_king, black_king, white_rook])
    """

    @staticmethod
    def create_standard_game() -> 'Game':
        """Create a new game with standard starting position.

        Returns:
            A Game with all 32 pieces in starting positions and check validation.
        """
        return Game(board=BoardBuilder().with_standard_position().build(), validator=CheckValidator())

    @staticmethod
    def create_empty_game() -> Game:
        """Create a new game with an empty board.

        Useful for testing or custom setups where pieces are added manually.

        Returns:
            A Game with an empty board and check validation.
        """
        return Game(validator=CheckValidator())

    @staticmethod
    def create_from_position(pieces: list['Piece']) -> Game:
        """Create a game from a list of pieces.

        Useful for setting up chess puzzles or specific positions.

        Args:
            pieces: List of pieces to place on the board.

        Returns:
            A Game with the specified pieces and check validation.
        """
        builder = BoardBuilder()
        for piece in pieces:
            builder.with_piece(piece)
        return Game(board=builder.build(), validator=CheckValidator())

