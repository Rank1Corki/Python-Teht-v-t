from models.item import Item
from models.room import Room

class Player:
    def __init__(self, name: str, location: Room):
        self.name = name
        self.location = location
        self.items: list[Item] = []
        self.energia: int = 100
        self.x: int = 0
        self.y: int = 0
        self.syvyys: int = 1

    def move(self, destination: Room) -> bool:
        if destination:
            self.location = destination
            return True
        return False

    def collect_item(self) -> Item | None:
        if self.location.item:
            poimittu = self.location.item
            self.items.append(poimittu)
            self.location.item = None
            return poimittu
        return None

    def get_total_weight(self) -> float:
        return sum(item.weight for item in self.items)