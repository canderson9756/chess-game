from src.core.colour import Colour

def test_colour_has_white_and_black():
    assert Colour.WHITE
    assert Colour.BLACK

def test_colour_has_oposite():
    assert Colour.WHITE.oposite() == Colour.BLACK
    assert Colour.BLACK.oposite() == Colour.WHITE

def test_colour_moves_correctly():
    assert Colour.WHITE.direction() == 1
    assert Colour.BLACK.direction() == -1