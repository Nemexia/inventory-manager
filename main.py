import models
import version


class Application:
    def __init__(self):
        self.inventory:models.Inventory|None = None

    def run(self):
        self.main_page()
            

    def main_page(self) -> None:
        while True:
            print(f"Nemexia's Inventory Manager v{version.version}")
            print("")
            print("1: New Inventory")
            print("2: Load Inventory")
            print("3: Exit")
            choice = input(">> ")

            if choice == "1":
                self.new_inventory()
            elif choice == "2":
                self.load_inventory()
            elif choice == "3":
                self.exit()
    
    def new_inventory(self) -> None:
        print("New Inventory")
        print("Enter the name of the inventory:")
        name = input(">> ")
        self.inventory = models.Inventory(name)
        self.inventory_page()
    
    def load_inventory(self) -> None:
        print("Load Inventory")
        print("Enter the name of the inventory:")
        name = input(">> ")
        self.inventory = models.Inventory(name)
        self.inventory_page()

    def inventory_page(self) -> None:
        while True:
            print(f"Inventory {self.inventory.name}")
            print("1: Add Item")
            print("2: Remove Item")
            print("3: Print Inventory")
            print("4: Exit Inventory")
            choice = input(">> ")
            
            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.remove_item()
            elif choice == "3":
                self.print_inventory()
            elif choice == "4":
                break

    def add_amount(self) -> models.Amount:
        print("Enter the value:")
        value = input(">> ")
        print("Enter the unit of the amount:")
        unit = input(">> ")
        return models.Amount(value, unit)

    def add_item(self) -> None:
        print("Add Item")
        print("Enter the name of the item:")
        name = input(">> ")
        print("Enter the amount of the item:")
        amount = self.add_amount()
        print("Enter the threshold of the item:")
        threshold = self.add_amount()
        print("Enter the category of the item:")
        category = input(">> ")
        print("Enter the unit cost of the item:")
        unit_cost = float(input(">> "))
        item = models.InventoryItem(name, amount, threshold, category, unit_cost)
        self.inventory.add_item(item)
        self.inventory_page()
    
    def remove_item(self) -> None:
        print("Remove Item")
        print("Enter the name of the item:")
        name = input(">> ")
        self.inventory.remove_item(name)
        self.inventory_page()
    

    def exit(self) -> None:
        print("Exiting...")
        exit()


if __name__ == '__main__':
    app = Application()
    app.run()
