from .user import User
from .address_book import AddressBook
from .record import Record
from .phone import Phone

ADDRESS_BOOK = AddressBook()

__all__ = [
    "User",
    "AddressBook",
    "Record",
    "ADDRESS_BOOK",
    "Phone"
]
