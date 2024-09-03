import models
import version


class Application:
    def __init__(self):
        self.inventory = models.Inventory()

    def run(self):
        while True:
            choice = self.main_page()
            if choice == "1":
                pass
            if choice == "2":
                pass
            if choice == "3":
                exit()

    def main_page(self) -> str:
        print(f"Nemexia's Inventory Manager v{version.version}")
        print("")
        print("choose option:")
        print("1: New Inventory")
        print("2: Load Inventory")
        print("3: Exit")
        choice = input(">> ")
        return choice


if __name__ == '__main__':
    app = Application()
    app.run()
