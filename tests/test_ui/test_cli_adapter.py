from src.ui import GameAdapter, CLIAdapter
from src.board import BoardBuilder

import pytest

def test_cli_adapter_is_game_advisor():
    adapter = CLIAdapter()
    assert isinstance(adapter, GameAdapter)

def test_cli_adapter_display_board_prints_output(capsys):   #type: ignore
    adapter = CLIAdapter()
    board = BoardBuilder().with_standard_position().build()
    adapter.display_board(board)
    output = capsys.readouterr()    #type: ignore
    assert "♔" in output.out or "K" in output.out  #type: ignore

def test_cli_adapter_show_message_prints(capsys):
    adapter = CLIAdapter()
    adapter.show_message("Test message")
    output = capsys.readouterr()
    assert "Test message" in output.out

def test_cli_adapter_show_error_prints(capsys):
    adapter = CLIAdapter()
    adapter.show_error("Error!")
    output = capsys.readouterr()
    assert "Error" in output.out

