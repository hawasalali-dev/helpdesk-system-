from helpdesk import HelpdeskSystem
from agents import JuniorAgent, SeniorAgent

from ticket import (
    HardwareTicket,
    SoftwareTicket,
    NetworkTicket
)

from enums import (
    Priority,
    TicketStatus
)

from exceptions import HelpdeskError


def main():

    helpdesk = HelpdeskSystem()

    junior = JuniorAgent(
        "A001",
        "Max",
        2
    )

    senior = SeniorAgent(
        "A002",
        "Sara",
        5
    )

    helpdesk.register_agent(junior)
    helpdesk.register_agent(senior)

    hardware_ticket = HardwareTicket(
        "HD-1001",
        "Drucker defekt",
        "Druckt nicht",
        Priority.HIGH,
        "Mustermann",
        "Printer",
        "INV-777"
    )

    software_ticket = SoftwareTicket(
        "SW-1002",
        "Excel Problem",
        "Excel startet nicht",
        Priority.NORMAL,
        "Schmidt",
        "Excel",
        "365"
    )

    network_ticket = NetworkTicket(
        "NW-1003",
        "Netzwerk langsam",
        "Hohe Latenz",
        Priority.CRITICAL,
        "Meier",
        "192.168.1.10",
        "Office-LAN"
    )

    helpdesk.add_ticket(hardware_ticket)
    helpdesk.add_ticket(software_ticket)
    helpdesk.add_ticket(network_ticket)

    try:

        helpdesk.assign_ticket(
            "SW-1002",
            "A001"
        )

        helpdesk.assign_ticket(
            "NW-1003",
            "A002"
        )

        helpdesk.change_status(
            "SW-1002",
            TicketStatus.IN_PROGRESS
        )

        helpdesk.change_status(
            "SW-1002",
            TicketStatus.RESOLVED
        )

        helpdesk.change_status(
            "SW-1002",
            TicketStatus.CLOSED
        )

    except HelpdeskError as error:
        print(error)

    print("\nTickets:")

    for ticket in helpdesk.list_tickets():
        print(ticket)

    print("\nHistorie:")

    for entry in software_ticket.history:
        print(entry)


if __name__ == "__main__":
    main()