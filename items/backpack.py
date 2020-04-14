from items.abstract_item import ItemType
from items.defensive_items.armors import LeatherArmor


class Backpack:

    def __init__(self) -> None:
        self.items = [LeatherArmor()]

    def filter(self, type: ItemType, sorted: bool = True) -> list:
        list_of_items = [x for x in filter(lambda x: x.TYPE.value == type.value, self.items)]
        if sorted:
            list_of_items.sort(key=lambda x: x.__str__())
        return list_of_items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
