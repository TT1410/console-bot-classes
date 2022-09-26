from .field import Field


class Name(Field):
    def __init__(self, value: str) -> None:
        self.value = value
