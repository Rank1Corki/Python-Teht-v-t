from models.item import Item

class Room:
    def __init__(self, name: str, item: Item | None = None):
        self.name = name
        self.item = item
        self.exits = {}

    def add_exit(self, direction: str, destination: "Room"):
        self.exits[direction.lower()] = destination

    def get_map_view(self) -> str:
        n = "  [▲]  " if "pohjoinen" in self.exits else "  [ ]  "
        s = "  [▼]  " if "etela" in self.exits else "  [ ]  "
        w = "[◄]" if "lansi" in self.exits else "[ ]"
        e = "[►]" if "ita" in self.exits else "[ ]"
        d = " [ALAS]" if "alas" in self.exits else ""
        core = " ★ " if self.item else " · "

        return (
            f"        +-------+\n"
            f"        {n}\n"
            f"        {w} {core} {e}{d}\n"
            f"        {s}\n"
            f"        +-------+\n"
            f"        (★ = Hohtava esine maassa, · = Tyhjä käytävä)"
        )