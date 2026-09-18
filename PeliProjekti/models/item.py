class Item: 
    def __init__(self, name: str, weight: float, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        return f"{self.name} ({self.weight:.1f} kg)"