from collections import UserDict

from .record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record
