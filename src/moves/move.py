from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.position import Position
    from src.pieces.base.piece import Piece

class Move(ABC):
    def __init__(self, piece: 'Piece', origin: 'Position', destination: 'Position'):
        self.piece = piece
        self.origin = origin
        self.destination = destination

    @abstractmethod
    def excecute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass