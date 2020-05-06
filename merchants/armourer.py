from items.defensive_items import RustyArmor, RustyTrousers, RustyBoots, RustyGloves, RustyHelmet, RustyShield
from merchants.merchant import Merchant
from utils import introduce_from_list, choose_action


class Armourer(Merchant):

    def choose_interaction(self, player) -> None:
        actions = (
            self._buy_items,
            self._sell_items,
        )
        interactions_names = (
            "Kup przedmiot",
            "Sprzedaj przedmiot",
        )
        question = "\nWybierz interakcje, lub naciśnij enter, aby wyjść\n"
        while True:
            introduce_from_list(interactions_names)
            chosen_action = choose_action(actions, question)
            if chosen_action is not None:
                chosen_action(player)
            else:
                break


class AmateurArmourer(Armourer):
    ITEMS_PRICES: dict = {
        RustyArmor: 100,
        RustyTrousers: 75,
        RustyShield: 75,
        RustyBoots: 50,
        RustyGloves: 50,
        RustyHelmet: 50,
    }
    MARGIN: float = 0.5
