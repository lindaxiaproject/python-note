from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Player:
    name: str
    number: int
    postion: str
    age: int
p1 = Player('SXT', 18, 'PG', 26)
print(p1)
