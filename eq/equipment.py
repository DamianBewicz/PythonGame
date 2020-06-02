from enums import PlayerClasses, ItemType
from eq.defense import MagicResistance, Defense
from items.abstract_item import EquipableItem
from utils import introduce_from_list, choose_item
from .backpack import Backpack
from .gold import Gold
from .personalitems import PersonalItems
from termcolor import colored


class Equipment:
    def __init__(self, player_class_type) -> None:
        self.backpack: Backpack = Backpack()
        self.personal_items: PersonalItems = PersonalItems()
        self.player_class_type: PlayerClasses = player_class_type
        self.magic_resistance: MagicResistance = MagicResistance()
        self.defense: Defense = Defense()
        self.gold: Gold = Gold()

    def choose_main_action(self) -> None:
        actions_names = (
            "Załóż przedmiot",
            "Zdejmij przedmiot",
            "Pokaż statystyki",
        )
        actions = (
            self._choose_item_to_wear,
            self._choose_item_to_take_off,
            self._show_defense,
        )
        while True:
            introduce_from_list(actions_names)
            question = "\nWybierz akcje, lub naciśnij enter aby wyjść\n"
            chosen_action = choose_item(actions, question)
            if chosen_action is None:
                break
            chosen_action()

    def _choose_item_to_wear(self) -> None:
        while True:
            try:
                print()
                print(self.personal_items)
                equipable_items = self.backpack.filter(ItemType.EQUIPPABLE)
                introduce_from_list(equipable_items, space=True)
                question = "\nPodaj numer przedmiotu, który chcesz użyć, lub naciśnij enter aby wyjść.\n"
                item = choose_item(equipable_items, question)
                if item is None:
                    break
                if item.can_wear(self.player_class_type):
                    self.backpack.remove_item(item)
                    self._wear_item(item)
                else:
                    print(colored("\nNie można założyć przedmiotu!\n"), "red")
            except IndexError:
                print(colored("\nPodany numer jest nieprawidłowy\n"), "red")

    def _choose_item_to_take_off(self) -> None:
        while True:
            print(self.personal_items)
            items_names = [slot_name.capitalize() for slot_name in self.personal_items.items.keys()]
            introduce_from_list(items_names)
            print()
            question = "\nWybierz przedmiot który chcesz zdjąć, lub naciśnij enter aby wyjść\n"
            chosen_item_type = choose_item(list(self.personal_items.items.keys()), question)
            if chosen_item_type is None:
                break
            self._take_off(chosen_item_type)

    def _take_off(self, item_type) -> None:
        item = self.personal_items.pop(item_type)
        if item is not None:
            try:
                self.defense -= item.defense
                self.magic_resistance -= item.magic_resistance
            except AttributeError:
                pass
            self.backpack.append(item)
        else:
            print(colored("\nWybrany slot jest pusty!\n", "red"))

    def _wear_item(self, item) -> None:
        if self.personal_items.is_in_slot(item):
            item_type = EquipableItem.get_item_section(item)
            item_from_eq = self.personal_items.pop(item_type)
            self.backpack.append(item_from_eq)
            try:
                self.defense -= item_from_eq.defense
            except AttributeError:
                pass
        try:
            self.defense += item.defense
        except AttributeError:
            pass
        self.personal_items.set(item)

    def _show_defense(self) -> None:
        print()
        print(self.defense)
        print(self.magic_resistance)
