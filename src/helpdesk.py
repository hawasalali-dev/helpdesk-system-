from exceptions import (
    TicketNotFoundError,
    AgentNotFoundError,
    AssignmentError,
    CapacityExceededError
)


class HelpdeskSystem:

    def __init__(self):

        self._tickets = {}
        self._agents = {}

    def add_ticket(self, ticket):

        self._tickets[ticket.ticket_id] = ticket

    def register_agent(self, agent):

        self._agents[agent.agent_id] = agent

    def get_ticket(self, ticket_id):

        if ticket_id not in self._tickets:
            raise TicketNotFoundError(ticket_id)

        return self._tickets[ticket_id]

    def get_agent(self, agent_id):

        if agent_id not in self._agents:
            raise AgentNotFoundError(agent_id)

        return self._agents[agent_id]

    def assign_ticket(
            self,
            ticket_id,
            agent_id
    ):

        ticket = self.get_ticket(ticket_id)
        agent = self.get_agent(agent_id)

        if ticket.assigned_to is not None:
            raise AssignmentError(
                "Ticket bereits zugewiesen."
            )

        if not agent.has_capacity():
            raise CapacityExceededError(
                "Agent hat keine freie Kapazität."
            )

        if not agent.can_handle(ticket):
            raise AssignmentError(
                f"{agent.name} "
                f"darf dieses Ticket nicht bearbeiten."
            )

        ticket.assigned_to = agent
        agent._assigned_tickets.append(ticket)

        ticket.add_history(
            "ASSIGNED",
            agent.name,
            "Ticket zugewiesen"
        )

    def change_status(
            self,
            ticket_id,
            new_status,
            actor="System"
    ):

        ticket = self.get_ticket(ticket_id)

        ticket.change_status(
            new_status,
            actor
        )

    def list_tickets(
            self,
            status=None,
            priority=None
    ):

        tickets = list(self._tickets.values())

        if status:
            tickets = [
                t for t in tickets
                if t.status == status
            ]

        if priority:
            tickets = [
                t for t in tickets
                if t.priority == priority
            ]

        return tickets

    def __len__(self):
        return len(self._tickets)