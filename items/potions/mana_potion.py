from characters.player.player import Player
from items.item import Item


class ManaPotion(Item):
    mana = NotImplemented
    cost = NotImplemented

    def __str__(self) -> str:
        return "NotImplemented"

    def use_item(self, player: Player) -> False:
        # Return false, use items makes no round loss
        if player.mana > player.max_mana:
            print("\nMasz pełną manę!\n")
        else:
            player.mana += self.mana
            if player.mana > player.max_mana:
                player.mana = player.max_mana
        return False


class MinorManaPotion(ManaPotion):
    mana = 15
    cost = 40

    def __str__(self) -> str:
        return "Mniejsza mikstura many"


class NormalManaPotion(ManaPotion):
    mana = 20
    cost = 65

    def __str__(self) -> str:
        return "Mikstura many"


class GreaterManaPotion(ManaPotion):
    mana = 30
    cost = 100

    def __str__(self) -> str:
        return "Większa mikstura many"
