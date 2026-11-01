import unittest

from agents import JuniorAgent, SeniorAgent
from ticket import SoftwareTicket
from enums import Priority


class TestAgent(unittest.TestCase):

    def setUp(self):

        self.junior = JuniorAgent(
            "A001",
            "Max",
            2
        )

        self.senior = SeniorAgent(
            "A002",
            "Sara",
            5
        )

    def test_junior_can_handle_normal(self):

        ticket = SoftwareTicket(
            "T1",
            "Excel",
            "Startet nicht",
            Priority.NORMAL,
            "User",
            "Excel",
            "365"
        )

        self.assertTrue(
            self.junior.can_handle(ticket)
        )

    def test_junior_cannot_handle_critical(self):

        ticket = SoftwareTicket(
            "T2",
            "Serverfehler",
            "Kritisch",
            Priority.CRITICAL,
            "User",
            "Windows",
            "2022"
        )

        self.assertFalse(
            self.junior.can_handle(ticket)
        )

    def test_senior_can_handle_all(self):

        ticket = SoftwareTicket(
            "T3",
            "Serverfehler",
            "Kritisch",
            Priority.CRITICAL,
            "User",
            "Windows",
            "2022"
        )

        self.assertTrue(
            self.senior.can_handle(ticket)
        )

    def test_agent_has_capacity(self):

        self.assertTrue(
            self.junior.has_capacity()
        )


if __name__ == "__main__":
    unittest.main()