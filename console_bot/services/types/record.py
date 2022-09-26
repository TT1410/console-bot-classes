from .name import Name
from .phone import Phone


class Record:
    def __init__(self, name: str, phone: str = None) -> None:
        self.name: Name = Name(name)
        self.phones: list[Phone] = [Phone(phone)] if phone else []
