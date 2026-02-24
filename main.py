from src.game import GameFactory
from src.ui import CLIAdapter, GameController

def main():
    game = GameFactory.create_standard_game()
    adapter = CLIAdapter()
    controller = GameController(game, adapter)

    print("Welcome to Chess!")
    print("Enter moves in algebraic notation (e.g., e2 for origin, e4 for destination)")
    print("Press Ctrl+C to quit\n")

    try:
        controller.run()
    except KeyboardInterrupt:
        print("\nGame ended.")

if __name__ == "__main__":
    main()
