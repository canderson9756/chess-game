from src.board.board import Board
from src.core.colour import Colour
from src.core.position import Position

from .adapter import GameAdapter
from .constants import PIECE_SYMBOLS

class CLIAdapter(GameAdapter):
    def display_board(self, board: Board) -> None:
        print(self._render_board(board))
    
    def get_move_input(self) -> tuple['Position', 'Position']:
        origin = Position.from_algebraic(input("From: "))
        dest = Position.from_algebraic(input("To: "))
        return origin, dest

    def show_message(self, message: str) -> None:
        print(message)

    def show_error(self, error: str) -> None:
        print(f"Error: {error}")

    def show_game_over(self, result: str, winner: 'Colour | None') -> None:
        if winner:
            print(f"Game Over: {result} - {winner.name} wins!")
        else:
            print(f"Game Over: {result}")

    def _render_board(self, board: 'Board') -> 'str':
        lines: 'list[str]' = []
        for rank in range(7, -1, -1):  # 8 down to 1
            row = f"{rank + 1} "
            for file in range(8):
                piece = board.get_piece_at(Position(file, rank))
                if piece:
                    symbol = PIECE_SYMBOLS.get(
                        (type(piece).__name__, piece.colour.name),
                        "?"
                    )
                    row += symbol + " "
                else:
                    row += ". "
            lines.append(row)
        lines.append("  a b c d e f g h")
        return "\n".join(lines)
