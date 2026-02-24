"""Main game controller for chess.

This module provides the Game class which orchestrates the entire chess game,
handling moves, turn management, validation, and game state transitions.
"""

from src.board.board import Board
from src.core.colour import Colour
from src.pieces.base.piece import Piece
from src.moves.move import Move
from src.moves.standard_move import StandardMove
from src.moves.capture_move import CaptureMove
from src.moves.move_history import MoveHistory
from src.validator.validator import Validator
from src.events import EventBus, MoveEvent, CaptureEvent, CheckEvent, GameEvent, TurnEvent

from src.game.state.playing_state import PlayingState

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.position import Position
    from src.game.state.game_state import GameState


class Game:
    """Main chess game controller.

    Game manages the chess game flow including move execution, turn management,
    validation, state transitions, and event publishing. It uses the State pattern
    for game phases and Observer pattern for event notifications.

    Attributes:
        board: The game board.
        player_turn: The colour of the player to move.
        move_history: History of moves for undo/redo.
        state: Current game state (Playing, Check, Checkmate, Stalemate).

    Example:
        >>> game = GameFactory.create_standard_game()
        >>> game.make_move(Position.from_algebraic("e2"), Position.from_algebraic("e4"))
        True
        >>> game.player_turn
        Colour.BLACK
    """
    def __init__(self, board: 'Board | None' = None, validator: 'Validator | None' = None):
        """Initialize a new game.

        Args:
            board: Optional pre-configured board. Creates empty board if None.
            validator: Optional move validator chain. No validation if None.
        """
        self._board = board if board else Board()
        self._player_turn = Colour.WHITE
        self._move_history = MoveHistory()
        self._validator = validator
        self._state: 'GameState' = PlayingState()
        self._event_bus: 'EventBus' = EventBus()

    def make_move(self, origin: 'Position', destination: 'Position') -> bool:
        """Attempt to make a move, delegating to current game state.

        Args:
            origin: Starting position of the piece.
            destination: Target position for the move.

        Returns:
            True if the move was successful, False otherwise.
        """
        return self._state.handle_move(self, origin, destination)

    def execute_move(self, origin: 'Position', destination: 'Position') -> 'bool':
        """Execute a move after validation.

        Validates the move, executes it, publishes events, and updates
        the game state. This is called by game states after their own checks.

        Args:
            origin: Starting position of the piece.
            destination: Target position for the move.

        Returns:
            True if the move was executed, False if invalid.
        """
        piece = self._board.get_piece_at(origin)
        if piece is None:
            return False
        if piece.colour != self._player_turn:
            return False
        legal_moves = piece.get_legal_moves(self._board)
        if destination not in legal_moves:
            return False
        
        move = self._create_move(piece, origin, destination)

        if self._validator and not self._validator.validate(move, self._board):
            return False

        move.execute(self._board)
        self._event_bus.publish(MoveEvent(piece, origin, destination))
        if isinstance(move, CaptureMove):
            self._event_bus.publish(CaptureEvent(move._captured_piece, piece)) #type: ignore
            
        self._move_history.push(move)
        self._change_player_turn()

        if self.is_in_check(self._player_turn):
            self._event_bus.publish(CheckEvent(self._player_turn))

        return True
    
    def _create_move(self, piece: 'Piece', origin: 'Position', destination: 'Position') -> 'Move':
        """Create the appropriate move type based on the destination.

        Args:
            piece: The piece being moved.
            origin: Starting position.
            destination: Target position.

        Returns:
            CaptureMove if destination has enemy piece, StandardMove otherwise.
        """
        if self._board.has_enemy_piece(destination, piece.colour):
            return CaptureMove(piece, origin, destination)
        return StandardMove(piece, origin, destination)

    def _change_player_turn(self) -> None:
        """Switch to the other player's turn and publish turn event."""
        self._player_turn = self._player_turn.opposite()
        self._event_bus.publish(TurnEvent(self._player_turn))

    def undo(self) -> None:
        """Undo the last move and switch turns back."""
        self._move_history.undo(self._board)
        self._change_player_turn()

    def redo(self) -> None:
        """Redo the last undone move and switch turns."""
        self._move_history.redo(self._board)
        self._change_player_turn()

    def set_state(self, state: 'GameState') -> 'None':
        """Set the current game state.

        Args:
            state: The new game state.
        """
        self._state = state

    def get_status(self) -> 'str':
        """Get the current game status string.

        Returns:
            Status string from current state (e.g., "Playing", "Check", "Checkmate").
        """
        return self._state.get_status()

    def is_game_over(self) -> 'bool':
        """Check if the game has ended.

        Returns:
            True if game is over (checkmate or stalemate).
        """
        return self._state.is_game_over()

    def is_in_check(self, colour: 'Colour') -> 'bool':
        """Check if the specified colour's king is in check.

        Args:
            colour: The colour to check.

        Returns:
            True if that colour's king is under attack.
        """
        king = self._board.find_king(colour)
        return self._board.is_square_attacked(king.position, colour.opposite())

    def has_legal_moves(self, colour: 'Colour') -> 'bool':
        """Check if the specified colour has any legal moves.

        Args:
            colour: The colour to check.

        Returns:
            True if at least one legal move exists.
        """
        for piece in self._board.get_pieces(colour):
            for dest in piece.get_legal_moves(self._board):
                move = self._create_move(piece, piece.position, dest)
                if self._validator is None or self._validator.validate(move, self._board):
                    return True
        return False

    @property
    def board(self) -> 'Board':
        """Get the game board."""
        return self._board

    @property
    def player_turn(self) -> 'Colour':
        """Get the colour of the player to move."""
        return self._player_turn

    @property
    def move_history(self) -> 'MoveHistory':
        """Get the move history manager."""
        return self._move_history

    @property
    def state(self) -> 'GameState':
        """Get the current game state."""
        return self._state
