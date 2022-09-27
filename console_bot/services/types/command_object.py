from dataclasses import dataclass


@dataclass
class Command:
    username: str
    value: str
