import unittest

from ticket import SoftwareTicket
from enums import Priority, TicketStatus
from exceptions import InvalidStatusTransitionError


class TestTicket(unittest.TestCase):

    def setUp(self):
        self.ticket = SoftwareTicket(
            ticket_id="SW-1001",
            title="Excel Fehler",
            description="Excel startet nicht",
            priority=Priority.NORMAL,
            created_by="Max",
            software_name="Excel",
            version="365"
        )

    def test_creation(self):
        self.assertEqual(
            self.ticket.ticket_id,
            "SW-1001"
        )

    def test_category(self):
        self.assertEqual(
            self.ticket.get_category(),
            "Software"
        )

    def test_valid_status_change(self):
        self.ticket.change_status(
            TicketStatus.IN_PROGRESS
        )

        self.assertEqual(
            self.ticket.status,
            TicketStatus.IN_PROGRESS
        )

    def test_invalid_status_change(self):
        with self.assertRaises(
            InvalidStatusTransitionError
        ):
            self.ticket.change_status(
                TicketStatus.CLOSED
            )


if __name__ == "__main__":
    unittest.main()