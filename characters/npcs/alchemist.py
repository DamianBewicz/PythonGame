from items.potions.health_potion import MinorHealthPotion, HealthPotion, NormalHealthPotion
from items.potions.mana_potion import MinorManaPotion, ManaPotion, NormalManaPotion
from characters.npcs.merchant import Merchant


class Alchemist(Merchant):
    def __init__(self) -> None:
        super().__init__()
        self.items = [
            MinorHealthPotion(),
            NormalHealthPotion(),
            MinorManaPotion(),
            NormalManaPotion(),
        ]

    def __str__(self) -> str:
        return "Alchemik"
