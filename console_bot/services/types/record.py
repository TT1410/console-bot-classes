from .name import Name
from .phone import Phone


class Record:
    def __init__(self, name: str, phone: str = None) -> None:
        self.name: Name = Name(name)
        self.phones: list[Phone] = [Phone(phone)] if phone else []

    def add_phone(self, phone: str) -> None:
        phone = Phone(phone)

        if phone not in self.phones:
            self.phones.append(phone)
