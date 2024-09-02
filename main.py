import version
import models


class Application:
    def __init__(self):
        self.inventory = models.Inventory()

    def run(self):
        self.main_page()

    def main_page(self):
        print(f"Nemexia's Inventory Manager v{version.version}")
        print("choose option:")
        print("1: New Inventory")
        print("2: Load Inventory")


if __name__ == '__main__':
    app = Application()
    app.run()
