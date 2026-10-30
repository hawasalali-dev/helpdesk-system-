class HelpdeskError(Exception):
    """Basisklasse aller Helpdesk-Fehler."""
    pass


class TicketNotFoundError(HelpdeskError):
    pass


class InvalidStatusTransitionError(HelpdeskError):
    pass


class AssignmentError(HelpdeskError):
    pass


class CapacityExceededError(AssignmentError):
    pass


class ValidationError(HelpdeskError):
    pass