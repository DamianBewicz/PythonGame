from enums import PlayerClasses
from items import Backpack
from items.abstract_item import EquipableItem, ItemType
from items.defense.defense import Defense
from items.defense.magic_resist import MagicResistance
from items.gold import Gold
from items.personalitems import PersonalItems
from utils import introduce_from_list, choose_item


class Equipment:
    def __init__(self, player_class_type) -> None:
        self.backpack: Backpack = Backpack()
        self.personal_items: PersonalItems = PersonalItems()
        self.player_class_type: PlayerClasses = player_class_type
        self.magic_resistance: MagicResistance = MagicResistance()
        self.defense: Defense = Defense()
        self.gold: Gold = Gold()

    def choose_item_to_wear(self) -> None:
        while True:
            try:
                print(self.personal_items)
                equipable_items = self.backpack.filter(ItemType.EQUIPPABLE)
                introduce_from_list(equipable_items)
                question = "\nPodaj numer przedmiotu, który chcesz użyć, lub naciśnij enter aby wyjść.\n"
                item = choose_item(equipable_items, question)
                if item is None:
                    break
                if item.can_wear(self.player_class_type):
                    self.backpack.remove_item(item)
                    self._wear_item(item)
                else:
                    print("\nNie można założyć przedmiotu!\n")
            except IndexError:
                print("\nPodany numer jest nieprawidłowy\n")

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
        print(self.defense)
