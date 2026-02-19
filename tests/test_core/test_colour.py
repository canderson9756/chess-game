from src.core.colour import Colour

def test_colour_has_white_and_black():
    assert Colour.WHITE
    assert Colour.BLACK

def test_colour_has_oposite():
    assert Colour.WHITE.oposite() == Colour.BLACK
    assert Colour.BLACK.oposite() == Colour.WHITE