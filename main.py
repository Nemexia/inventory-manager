import models
import version


class Application:
    def __init__(self):
        self.inventory:models.Inventory|None = None

    def run(self):
        self.main_page()
            

    def main_page(self) -> None:
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
    
    def load_inventory(self) -> None:
        print("Load Inventory")
        print("Enter the name of the inventory:")
        name = input(">> ")
        self.inventory = models.Inventory(name)

    def exit(self):
        print("Exiting...")
        exit()


if __name__ == '__main__':
    app = Application()
    app.run()
