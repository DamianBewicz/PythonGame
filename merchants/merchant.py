from math import floor
from characters.player.player import Player
from items.abstract_item import Item
from utils import get_classes_from_keys, choose_item, classes_to_items, introduce_from_list


class Merchant:
    ITEMS_PRICES: dict = NotImplemented
    MARGIN: float = NotImplemented

    def __init__(self):
        self.interactions: tuple = NotImplemented

    def introduce_items(self, margin: float = 1) -> None:
        print()
        for number, (item, price) in enumerate(self.ITEMS_PRICES.items(), start=1):
            print(
                "{number}{item}\n"
                "Koszt: {price} złota\n".format(
                    number=str(number) + " " if margin != self.MARGIN else "",
                    item=item(),
                    price=floor(margin*price),
                ))

    def has_money(self, player: Player, item: Item) -> bool:
        return player.equipment.gold.ammount >= self.get_price(item)

    def get_price(self, item) -> int:
        return self.ITEMS_PRICES[type(item)]

    def can_sell(self, item) -> bool:
        return type(item) in get_classes_from_keys(self.ITEMS_PRICES)

    def buy_items(self, player) -> None:
        while True:
            self.introduce_items()
            print(player.equipment.gold)
            list_of_items = classes_to_items(get_classes_from_keys(self.ITEMS_PRICES))
            question = "\nPodaj numer przedmiotu, lub naciśnij enter aby wyjść\n"
            chosen_item = choose_item(list_of_items, question)
            if chosen_item is not None:
                if self.has_money(player, chosen_item):
                    price = self.get_price(chosen_item)
                    player.equipment.gold.subtract(price)
                    player.equipment.backpack.append(chosen_item)
                else:
                    print("\nNie masz hajsu na ten szajs\n")
            else:
                break

    def sell_items(self, player) -> None:
        while True:
            self.introduce_items(margin=self.MARGIN)
            players_backpack_items = player.equipment.backpack.items
            introduce_from_list(players_backpack_items)
            print(player.equipment.gold)
            question = "\nWybierz przedmiot który chcesz sprzedać, lub naciśnij enter aby wyjść\n"
            chosen_item = choose_item(players_backpack_items, question)
            if chosen_item is not None:
                if self.can_sell(chosen_item):
                    players_backpack_items.remove(chosen_item)
                    gold_from_item = floor(self.MARGIN * self.get_price(chosen_item))
                    player.equipment.gold.add(gold_from_item)
                else:
                    print("\nNie handluje tym szajsem\n")
            else:
                break

    def choose_interaction(self) -> None:
        return NotImplemented
