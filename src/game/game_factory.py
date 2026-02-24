from src.board.builder import BoardBuilder
from src.game.game import Game
from src.validator.check_validator import CheckValidator
from src.pieces.base.piece import Piece

class GameFactory:
    @staticmethod
    def create_standard_game() -> 'Game':
        return Game(board=BoardBuilder().with_standard_position().build(), validator=CheckValidator())
    
    @staticmethod
    def create_empty_game() -> Game:
        """For testing or custom setups"""
        return Game(validator=CheckValidator())

    @staticmethod
    def create_from_position(pieces: list['Piece']) -> Game:
        """Create game from a list of pieces (puzzles)"""
        builder = BoardBuilder()
        for piece in pieces:
            builder.with_piece(piece)
        return Game(board=builder.build(), validator=CheckValidator())

