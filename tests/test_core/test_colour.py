from src.core.colour import Colour

def test_colour_has_white_and_black():
    assert Colour.WHITE
    assert Colour.BLACK

def test_colour_has_opposite():
    assert Colour.WHITE.opposite() == Colour.BLACK
    assert Colour.BLACK.opposite() == Colour.WHITE

def test_colour_moves_correctly():
    assert Colour.WHITE.direction() == 1
    assert Colour.BLACK.direction() == -1