from src.ui import GameController, GameAdapter
from src.game import GameFactory

def test_controller_calls_display_board(mocker):
    game = GameFactory.create_standard_game()
    adapter = mocker.Mock(spec=GameAdapter)
    adapter.get_move_input.side_effect = [KeyboardInterrupt]  # Exit loop

    controller = GameController(game, adapter)
    try:
        controller.run()
    except KeyboardInterrupt:
        pass

    adapter.display_board.assert_called()
