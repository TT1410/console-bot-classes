from .name import Name
from .phone import Phone


class Record:
    def __init__(self, name: str, phone: str = None) -> None:
        self.name: Name = Name(name)
        self.phones: list[Phone] = [Phone(phone)] if phone else []

    def add_phone(self, phone: str) -> Phone:
        phone = Phone(phone)

        if any((phone.value == x.value) for x in self.phones):
            raise ValueError(f"Number '{phone.value}' was already added earlier")

        self.phones.append(phone)

        return phone

    def replace_phone(self, index: int, phone: str) -> tuple[Phone, Phone]:
        old_phone = self.phones.pop(index - 1)
        new_phone = self.add_phone(phone)

        return old_phone, new_phone

    def remove_phone(self, index: int) -> Phone:
        return self.phones.pop(index - 1)
