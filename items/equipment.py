from items import Backpack
from items.abstract_item import EquipableItem, ItemType
from items.defensive_items import RustedArmor
from items.personalitems import PersonalItems
from utils import introduce_from_list, choose_item


class Equipment:
    def __init__(self):
        self.backpack = Backpack()
        self.personal_items = PersonalItems()

    def choose_item_to_wear(self):
        while True:
            try:
                print(self.personal_items)
                equipable_items = self.backpack.filter(ItemType.EQUIPABLE)
                introduce_from_list(equipable_items)
                question = "\nPodaj numer przedmiotu, który chcesz użyć, lub naciśnij enter aby wyjść.\n"
                item = choose_item(equipable_items, question)
                if item is None:
                    break
                self.backpack.remove_item(item)
                self.wear_item(item)
            except IndexError:
                print("\nPodany numer jest nieprawidłowy\n")

    def wear_item(self, item):
        if self.personal_items.is_in_slot(item):
            item_type = EquipableItem.get_item_section(item)
            item_from_eq = self.personal_items.pop(item_type)
            self.backpack.add_item(item_from_eq)
        self.personal_items.set(item)


if __name__ == "__main__":
    a = Equipment()
    a.personal_items.set(RustedArmor())
    a.choose_item_to_wear()
