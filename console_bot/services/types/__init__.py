from .command_object import Command
from .address_book import AddressBook
from .record import Record
from .phone import Phone

ADDRESS_BOOK = AddressBook()

__all__ = [
    "Command",
    "AddressBook",
    "Record",
    "ADDRESS_BOOK",
    "Phone"
]
