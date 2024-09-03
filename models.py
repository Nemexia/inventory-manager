import dataclasses

@dataclasses.dataclass
class Amount:
    value: float | int
    unit: str

@dataclasses.dataclass
class InventoryItem:
    name: str
    count: Amount
    threshold: Amount
    category: str


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
