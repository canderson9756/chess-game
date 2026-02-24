from dataclasses import dataclass, field
import time

@dataclass
class GameEvent:
    timestamp: float = field(default_factory=time.time, kw_only=True)