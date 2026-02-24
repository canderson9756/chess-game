from src.events import EventListener
import pytest

def test_event_listener_is_abstract():
    with pytest.raises(TypeError):
        EventListener() #type: ignore