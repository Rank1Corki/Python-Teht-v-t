from models.item import Item


class Room:
    """kaivoskammio tai luolan tila."""

    def __init__(self, name: str, description: str = "", item: Item | None = None):
        self.name = name
        self.description = description
        self.item = item
        self.exits: dict[str, "Room"] = {}

    def add_exit(self, direction: str, destination: "Room") -> None:
        """Lisää huoneeseen poistumissuunnan toiseen huoneeseen."""
        self.exits[direction.lower()] = destination

    def get_map_view(self) -> str:
        """Palauttaa huoneen ilmansuunnat ja tilan tekstigrafiikkana."""
        n = "  [▲]  " if "pohjoinen" in self.exits else "  [ ]  "
        s = "  [▼]  " if "etela" in self.exits else "  [ ]  "
        w = "[◄]" if "lansi" in self.exits else "[ ]"
        e = "[►]" if "ita" in self.exits else "[ ]"
        d = " [ALAS]" if "alas" in self.exits else ""
        y = " [YLÖS]" if "ylos" in self.exits else ""
        core = " ★ " if self.item else " · "

        return (
            f"        +-------+\n"
            f"        {n}\n"
            f"        {w} {core} {e}{d}{y}\n"
            f"        {s}\n"
            f"        +-------+\n"
            f"        (★ = Kohde tai esine huoneessa, · = Tyhjä käytävä)"
        )