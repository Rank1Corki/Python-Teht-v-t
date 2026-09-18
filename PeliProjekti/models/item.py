class Item:
    """pelin esine."""

    def __init__(self, name: str, weight: float, category: str = "materiaali"):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        return f"{self.name} ({self.weight:.1f} kg)"