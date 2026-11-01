class HelpdeskError(Exception):
    pass


class TicketNotFoundError(HelpdeskError):
    pass


class AgentNotFoundError(HelpdeskError):
    pass


class InvalidStatusTransitionError(HelpdeskError):
    pass


class AssignmentError(HelpdeskError):
    pass


class CapacityExceededError(AssignmentError):
    pass


class ValidationError(HelpdeskError):
    pass