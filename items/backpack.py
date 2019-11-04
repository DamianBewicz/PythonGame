from items.health_potion import HealthPotion


class Backpack:

    def __init__(self):
        self.items = []
        self.avaible_slots = 10

    def __str__(self):
        return f"""\nMiejsce w ekwipunku - {self.avaible_slots}"""

    def print_available_items(self):
        for slot, item in enumerate(self.items):
            print(f"{slot} {item}")

    def is_empty(self):
        return len(self.items) == 0

    # def choose_method(self):
    #     backpack_methods = [("Użyj przedmiotu", self.add_item), ("Wyrzuć przedmot", self.remove_item)]
    #     print()
    #     for number, name in enumerate(backpack_methods):
    #         print(f"{number + 1} {name[0]}")
    #     choice = int(input("\nWybierz akcje\n"))
    #     return backpack_methods[choice - 1][1]()

    # def add_item(self, item):
    #     if self.avaible_slots < 10:
    #         self.items.append(item)
    #         self.avaible_slots -= 1
    #     else:
    #         print("Plecak jest pełny")
    #         self.choose_method()

    # def remove_item(self):
    #     if not self.is_empty():
    #         self.print_available_items()
    #         choice = int(input("Wybierz przedmiot, który chcesz wyrzucić"))
    #         self.items.pop(choice - 1)
    #     else:
    #         print("\nPlecak jest pusty")
    #         self.choose_method()

    # def add_starting_items(self):
    #     self.items.append(HealthPotion())
    #     self.avaible_slots -= 1
