from models.item import Item
from models.room import Room


class Player:
    """pelaajahahmo, sen sijainti ja reppu."""

    def __init__(self, name: str, age: int, location: Room):
        self.name = name
        self.age = age
        self.location = location
        self.items: list[Item] = []
        self.energia: int = 100
        self.x: int = 0
        self.y: int = 0
        self.syvyys: int = 1

    def move(self, destination: Room) -> bool:
        """Siirtää pelaajan uuteen huoneeseen."""
        if destination:
            self.location = destination
            return True
        return False

    def collect_item(self) -> Item | None:
        """Poimii nykyisessä huoneessa olevan esineen reppuun."""
        if self.location.item:
            poimittu = self.location.item
            self.items.append(poimittu)
            self.location.item = None
            return poimittu
        return None

    def has_item(self, item_name: str) -> bool:
        """Tarkistaa, löytyykö repusta tietynniminen esine."""
        return any(item.name.lower() == item_name.lower() for item in self.items)

    def remove_item(self, item_name: str) -> Item | None:
        """Poistaa ja palauttaa esineen repusta nimen perusteella."""
        for index, item in enumerate(self.items):
            if item.name.lower() == item_name.lower():
                return self.items.pop(index)
        return None

    def get_total_weight(self) -> float:
        """Laskee pelaajan kantamien esineiden yhteispainon."""
        return sum(item.weight for item in self.items)