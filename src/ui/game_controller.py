from src.game.game import Game
from src.ui.adapter import GameAdapter
from src.core.colour import Colour

class GameController:
    def __init__(self, game: 'Game', adapter: 'GameAdapter'):
        self._game = game
        self._adapter = adapter

    def run(self) -> None:
        while not self._game.is_game_over():
            self._adapter.display_board(self._game.board)
            self._adapter.show_message(f"{self._game.player_turn}'s turn")

            try:
                origin, destination = self._adapter.get_move_input()
                if not self._game.make_move(origin, destination):
                    self._adapter.show_error(f"Invalid move: {origin} -> {destination}. Try again.")
            except ValueError as e:
                self._adapter.show_error(str(e))
        self._adapter.show_game_over(
            self._game.get_status(),
            self._get_winner()
        )

    def _get_winner(self) -> 'Colour | None':
        if self._game.get_status() == "Checkmate":
            return self._game.player_turn.opposite()
        return None