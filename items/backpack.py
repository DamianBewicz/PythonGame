from items.item import Item
from typing import Union


class Backpack:

    def __init__(self) -> None:
        self.items = []
        self.avaible_slots = 10

    def __str__(self) -> str:
        return f"""\nMiejsce w ekwipunku - {self.avaible_slots}"""

    def print_available_items(self):
        for slot, item in enumerate(self.items):
            print(f"{slot + 1} {item}")

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def is_full(self) -> bool:
        return len(self.items) >= self.avaible_slots

    def remove_item(self,  item_index: int, is_player_choosing: bool = True) -> Union[bool, ]:
        if not self.is_empty() and is_player_choosing:
            self.print_available_items()
            choice = input("\nWybierz przedmiot, który chcesz wyrzucić."
                           "\nNaciśnij enter jeśli chcesz wyjść.\n")
            if choice == "":
                return False
            self.items.pop(item_index)
            return True
        if not is_player_choosing:
            return self.items.pop(item_index)
        print("\nPlecak jest pusty")
        return False

    def add(self, item: Item) -> None:
        if self.is_full():
            print("\nPlecak jest pełny")
            return
        self.items.append(item)
        self.avaible_slots -= 1

    # def choose_method(self):
    #     backpack_methods = [("Użyj przedmiotu", self.add_item), ("Wyrzuć przedmot", self.remove_item)]
    #     print()
    #     for number, name in enumerate(backpack_methods):
    #         print(f"{number + 1} {name[0]}")
    #     choice = int(input("\nWybierz akcje\n"))
    #     return backpack_methods[choice - 1][1]()

    # def add_starting_items(self):
    #     self.items.append(HealthPotion())
    #     self.avaible_slots -= 1
