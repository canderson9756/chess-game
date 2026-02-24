from abc import ABC, abstractmethod
from .game_event import GameEvent

class EventListener(ABC):
    @abstractmethod
    def on_event(self, event: 'GameEvent') -> 'None':
        pass