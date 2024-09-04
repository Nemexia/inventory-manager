import models
import version
import pickle
import os



class Application:
    def __init__(self):
        self.inventory: models.Inventory | None = None

    def run(self):
        self.main_page()

    def main_page(self) -> None:
        while True:
            print(f"Nemexia's Inventory Manager v{version.version}")
            print("")
            print("1: New Inventory")
            print("2: Load Inventory")
            print("0: Exit")
            choice = input(">> ")

            if choice == "1":
                self.new_inventory()
            elif choice == "2":
                self.load_inventory()
            elif choice == "0":
                self.exit()
            else:
                print("Invalid input.")

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
        try:
            with open('saves/'+name+'.isf', 'rb') as save_file:
                self.inventory = pickle.load(save_file)
        except FileNotFoundError:
            print("Inventory not found.")
            return
        self.inventory_page()

    def inventory_page(self) -> None:
        while True:
            print(f"Inventory {self.inventory.name}")
            print("1: Add Item")
            print("2: Remove Item")
            print("3: Print Inventory")
            print("4: Save Inventory")
            print("5: Delete Inventory")
            print("0: Exit Inventory")
            choice = input(">> ")

            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.remove_item()
            elif choice == "3":
                self.print_inventory()
            elif choice == "4":
                self.save_inventory()
            elif choice == "5":
                self.delete_inventory()
            elif choice == "0":
                break
            else:
                print("Invalid input.")

    def add_item(self) -> None:
        print("Add Item")
        print("Enter the name of the item:")
        name = input(">> ")
        print("Enter the amount of the item:")
        amount = float(input(">> "))
        print("Enter the unit of the amount:")
        unit = input(">> ")
        print("Enter the threshold of the item:")
        threshold = float(input(">> "))
        print("Enter the category of the item:")
        category = input(">> ")
        print("Enter the unit cost of the item:")
        unit_cost = float(input(">> "))
        item = models.InventoryItem(name, amount, unit, threshold, category, unit_cost)
        self.inventory.add_item(item)

    def remove_item(self) -> None:
        print("Remove Item")
        print("Enter the name of the item:")
        name = input(">> ")
        self.inventory.remove_item(name)

    def print_inventory(self) -> None:
        self.inventory.print_inventory()

    def save_inventory(self) -> None:
        try:    
            with open('saves/'+self.inventory.name+'.isf', 'wb') as save_file:
                pickle.dump(self.inventory, save_file)
        except FileNotFoundError:
            print("No 'saves' folder found. Creating one now...")
            os.makedirs('saves')
            print("Save folder created. Please Save Inventory again.")
            return

    def delete_inventory(self) -> None:
        pass


    def exit(self) -> None:
        print("Exiting...")
        exit()


if __name__ == '__main__':
    app = Application()
    app.run()
