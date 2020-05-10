from items import MinorHealthPotion, NormalHealthPotion, MinorManaPotion, NormalManaPotion
from merchants.merchant import Merchant
from utils import introduce_from_list, choose_action


class Alchemist(Merchant):
    pass

    "Going to make method only avaible in alchemist, left for later"

    def choose_interaction(self, player):
        actions = (
            self._buy_items,
            self._sell_items,
        )

        interactions_names = (
            "Kup przedmiot",
            "Sprzedaj przedmiot",
        )

        question = "\nWybierz interakcje\n"
        while True:
            introduce_from_list(interactions_names)
            chosen_action = choose_action(actions, question)
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
