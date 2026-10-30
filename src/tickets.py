from abc import ABC, abstractmethod
from datetime import datetime

from src.enums import Priority, TicketStatus
from src.exceptions import ValidationError
from src.history import HistoryEntry