from math import floor
from items.abstract_item import Item
from utils import get_classes_from_keys, choose_item, classes_to_items, introduce_from_list, choose_action


class Merchant:
    ITEMS_PRICES: dict = NotImplemented
    MARGIN: float = NotImplemented

    def _introduce_items(self, margin: float = 1) -> None:
        print()
        for number, (item, price) in enumerate(self.ITEMS_PRICES.items(), start=1):
            print(
                "{number}{item}\n"
                "Koszt: {price} złota\n".format(
                    number=str(number) + " " if margin != self.MARGIN else "",
                    item=item(),
                    price=floor(margin*price),
                ))

    def _has_money(self, player: 'Player', item: Item) -> bool:
        return player.equipment.gold.amount >= self._get_price(item)

    def _get_price(self, item: Item) -> int:
        return self.ITEMS_PRICES[type(item)]

    def _can_sell(self, item: Item) -> bool:
        return type(item) in get_classes_from_keys(self.ITEMS_PRICES)

    def _buy_items(self, player: 'Player') -> None:
        while True:
            self._introduce_items()
            print(player.equipment.gold)
            list_of_items = classes_to_items(get_classes_from_keys(self.ITEMS_PRICES))
            question = "\nPodaj numer przedmiotu, lub naciśnij enter aby wyjść\n"
            chosen_item = choose_item(list_of_items, question)
            if chosen_item is not None:
                if self._has_money(player, chosen_item):
                    price = self._get_price(chosen_item)
                    player.equipment.gold.subtract(price)
                    player.equipment.backpack.append(chosen_item)
                else:
                    print("\nNie masz hajsu na ten szajs\n")
            else:
                break

    def _sell_items(self, player: 'Player') -> None:
        while True:
            self._introduce_items(margin=self.MARGIN)
            players_backpack_items = player.equipment.backpack.items
            introduce_from_list(players_backpack_items, space=True)
            print(player.equipment.gold)
            question = "\nWybierz przedmiot który chcesz sprzedać, lub naciśnij enter aby wyjść\n"
            chosen_item = choose_item(players_backpack_items, question)
            if chosen_item is not None:
                if self._can_sell(chosen_item):
                    players_backpack_items.remove(chosen_item)
                    gold_from_item = floor(self.MARGIN * self._get_price(chosen_item))
                    player.equipment.gold.add(gold_from_item)
                else:
                    print("\nNie handluje tym szajsem\n")
            else:
                break

    def choose_interaction(self, player) -> None:
        return NotImplemented


class WeaponImprover(Merchant):
    IMPROVE_PRICE: int = NotImplemented
    WEAPON_FOR_IMPROVING = NotImplemented

    def _has_money_for_improve(self, player) -> bool:
        return player.equipment.gold.amount >= self.IMPROVE_PRICE

    def _can_improve(self, player, item) -> bool:
        return self._has_money_for_improve(player) and isinstance(item, self.WEAPON_FOR_IMPROVING) and not item.is_improved

    def _improve_weapon(self, player) -> None:
        while True:
            players_backpack_items = player.equipment.backpack.items
            introduce_from_list(players_backpack_items, space=True)
            print("\nKoszt ulepszenia broni " + str(self.IMPROVE_PRICE) + "\n")
            question = "\nPodaj numer przedmiotu, który chcesz naostrzyć, lub naciśnij enter aby wyjść\n"
            chosen_item = choose_item(players_backpack_items, question)
            if chosen_item is not None:
                if self._can_improve(player, chosen_item):
                    player.equipment.gold.subtract(self.IMPROVE_PRICE)
                    chosen_item.improve()
                else:
                    print("\nNie można naostrzyć broni\n")
            else:
                break

    def choose_interaction(self, player) -> None:
        actions = (
            self._buy_items,
            self._sell_items,
            self._improve_weapon
        )

        interactions_names: tuple = (
            "Kup przedmiot",
            "Sprzedaj przedmiot",
            "Ulepsz przedmiot"
        )

        interaction_question = "\nWybierz interakcje, jeśli chcesz wyjść naciśnij enter\n"
        while True:
            introduce_from_list(interactions_names)
            chosen_action = choose_action(actions, interaction_question)
            if chosen_action is not None:
                chosen_action(player)
            else:
                break
