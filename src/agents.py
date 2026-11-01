from abc import ABC, abstractmethod

from enums import Priority


class SupportAgent(ABC):

    def __init__(
            self,
            agent_id,
            name,
            max_tickets
    ):

        self.agent_id = agent_id
        self.name = name
        self.max_tickets = max_tickets

        self._assigned_tickets = []

    def has_capacity(self):

        return (
                len(self._assigned_tickets)
                < self.max_tickets
        )

    @property
    def assigned_tickets(self):
        return tuple(self._assigned_tickets)

    @abstractmethod
    def can_handle(self, ticket):
        pass


class JuniorAgent(SupportAgent):

    def can_handle(self, ticket):

        return ticket.priority in {
            Priority.LOW,
            Priority.NORMAL
        }


class SeniorAgent(SupportAgent):

    def can_handle(self, ticket):
        return True