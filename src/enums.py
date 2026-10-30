from enum import Enum, auto


class TicketStatus(Enum):
    OPEN = auto()
    IN_PROGRESS = auto()
    WAITING = auto()
    RESOLVED = auto()
    CLOSED = auto()


class Priority(Enum):
    LOW = auto()
    NORMAL = auto()
    HIGH = auto()
    CRITICAL = auto()