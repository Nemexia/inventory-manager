import dataclasses


@dataclasses.dataclass
class InventoryItem:
    name: str
    amount: float
    unit: str
    threshold: float
    category: str
    unit_cost: float

    def __str__(self) -> str:
        return f"{self.name} has {self.amount} {self.unit} and is in category {self.category}"

    def total_cost(self) -> float:
        return self.amount * self.unit_cost


class Inventory:
    def __init__(self, name: str):
        self.name = name
        self.items: list[InventoryItem] = []

    def add_item(self, item: InventoryItem) -> None:
        self.items.append(item)

    def remove_item(self, item: InventoryItem) -> None:
        self.items.remove(item)

    def print_inventory(self) -> None:
        print(f"Inventory has {len(self.items)} items:")
        for position, item in enumerate(self.items):
            print(f"{position}: {item}")

    def __str__(self) -> str:
        return f"Inventory {self.name} with {len(self.items)} items"
