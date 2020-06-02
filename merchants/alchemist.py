from items import MinorHealthPotion, NormalHealthPotion, MinorManaPotion, NormalManaPotion, GreaterManaPotion, \
    ElixirOfLife, GreaterHealthPotion, ElixirOfMana
from merchants.merchant import Merchant
from utils import introduce_from_list, choose_item


class Alchemist(Merchant):
    # TODO: Going to make method only avaible in alchemist, left for later

    def choose_interaction(self, player):
        actions = (
            self._buy_items,
            self._sell_items,
        )

        interactions_names = (
            "Kup przedmiot",
            "Sprzedaj przedmiot",
        )

        while True:
            introduce_from_list(interactions_names)
            chosen_action = choose_item(actions, "\nWybierz interakcje\n")
            if chosen_action is not None:
                chosen_action(player)
            else:
                break


class AmateurAlchemist(Alchemist):
    ITEMS_PRICES: dict = {
        MinorHealthPotion: 50,
        NormalHealthPotion: 55,
        MinorManaPotion: 60,
        NormalManaPotion: 80,
    }
    MARGIN: float = 0.5


class ExperiencedAlchemist(Alchemist):
    ITEMS_PRICES: dict = {
        GreaterHealthPotion: 70,
        ElixirOfLife: 100,
        GreaterManaPotion: 70,
        ElixirOfMana: 100,
    }
    MARGIN: float = 0.6
