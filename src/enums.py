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


ALLOWED_TRANSITIONS = {
    TicketStatus.OPEN: {
        TicketStatus.IN_PROGRESS
    },

    TicketStatus.IN_PROGRESS: {
        TicketStatus.WAITING,
        TicketStatus.RESOLVED
    },

    TicketStatus.WAITING: {
        TicketStatus.IN_PROGRESS,
        TicketStatus.RESOLVED
    },

    TicketStatus.RESOLVED: {
        TicketStatus.CLOSED
    },

    TicketStatus.CLOSED: set()
}
