import unittest

from helpdesk import HelpdeskSystem
from agents import JuniorAgent
from ticket import SoftwareTicket
from enums import Priority, TicketStatus
from exceptions import InvalidStatusTransitionError


class HelpdeskTest(unittest.TestCase):

    def setUp(self):

        self.system = HelpdeskSystem()

        self.agent = JuniorAgent(
            "A1",
            "Max",
            2
        )

        self.system.register_agent(
            self.agent
        )

        self.ticket = SoftwareTicket(
            "T1",
            "Excel Fehler",
            "Startet nicht",
            Priority.NORMAL,
            "User",
            "Excel",
            "365"
        )

        self.system.add_ticket(
            self.ticket
        )

    def test_assign_ticket(self):

        self.system.assign_ticket(
            "T1",
            "A1"
        )

        self.assertEqual(
            self.ticket.assigned_to,
            self.agent
        )

    def test_invalid_status_transition(self):

        with self.assertRaises(
                InvalidStatusTransitionError):

            self.ticket.change_status(
                TicketStatus.CLOSED
            )


if __name__ == "__main__":
    unittest.main()