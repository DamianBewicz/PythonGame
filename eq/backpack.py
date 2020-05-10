from enums import ItemType
from items.abstract_item import Item
from utils import introduce_from_list, choose_item


class Backpack:

    def __init__(self) -> None:
        self.items: list = []

    def filter(self, type: ItemType, sorted: bool = True) -> list:
        list_of_items = [x for x in filter(lambda x: x.TYPE.value == type.value, self.items)]
        if sorted:
            list_of_items.sort(key=lambda object: str(object))
        return list_of_items

    def append(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, item: Item):
        self.items.remove(item)

    def use_item_during_combat(self, player: 'Player'):
        while True:
            potion_items = self.filter(ItemType.POTION)
            introduce_from_list(potion_items)
            question = "\nWybierz miskturę do użycia, lub naciśnij enter aby wyjść\n"
            choosen_item = choose_item(potion_items, question)
            if choosen_item is None:
                break
            self.remove_item(choosen_item)
            choosen_item.drink(player)
