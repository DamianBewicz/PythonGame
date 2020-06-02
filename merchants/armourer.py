from items import (
    RustyArmor, RustyTrousers, RustyShield, RustyBoots, RustyGloves, RustyHelmet, PlateArmor,
    ArchmageRobe, PlateBoots, PlateGloves, MysticalGloves, PlateHelmet, ArchmageHeadpiece,
    BurnishedShield, IronShield, PlateTrousers, PhoenixTrousers, SorcererBoots,
)
from merchants.merchant import Merchant
from utils import introduce_from_list, choose_item


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
            chosen_action = choose_item(actions, question)
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


class ExpieriencedArmourer(Armourer):
    ITEMS_PRICES: dict = {
        PlateArmor: 300,
        ArchmageRobe: 300,
        PlateBoots: 150,
        SorcererBoots: 150,
        PlateGloves: 150,
        MysticalGloves: 150,
        PlateHelmet: 200,
        ArchmageHeadpiece: 200,
        BurnishedShield: 250,
        IronShield: 250,
        PlateTrousers: 150,
        PhoenixTrousers: 150,
    }
    MARGIN: float = 0.6
