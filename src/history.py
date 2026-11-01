from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class HistoryEntry:
    timestamp: datetime
    action: str
    actor: str
    description: str