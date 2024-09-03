import models
import version


class Application:
    def __init__(self):
        self.inventory:models.Inventory|None = None

    def run(self):
        while True:
            choice = self.main_page()
            if choice == "1":
                self.new_inventory()
            if choice == "2":
                self.load_inventory()
            if choice == "3":
                self.exit()

    def main_page(self) -> str:
        print(f"Nemexia's Inventory Manager v{version.version}")
        print("")
        print("choose option:")
        print("1: New Inventory")
        print("2: Load Inventory")
        print("3: Exit")
        choice = input(">> ")
        return choice
    
    def new_inventory(self):
        print("New Inventory")
        print("Enter the name of the inventory:")
        name = input(">> ")
        self.inventory = models.Inventory(name)
    
    def load_inventory(self):
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
