from items.abstract_item import Potion


class ManaPotion(Potion):
    MANA_REGEN: int = NotImplemented

    def __str__(self) -> str:
        return f"{self.NAME}: Regeneruje {self.MANA_REGEN} punktów many"

    def drink(self, player: 'Player') -> None:
        player.gain_mana(self.MANA_REGEN)


class MinorManaPotion(ManaPotion):
    MANA_REGEN: int = 15
    NAME: str = "Mniejsza mikstura many"


class NormalManaPotion(ManaPotion):
    MANA_REGEN: int = 20
    NAME: str = "Mikstura many"


class GreaterManaPotion(ManaPotion):
    MANA_REGEN: int = 30
    NAME: str = "Większa mikstura many"


class ElixirOfMana(ManaPotion):
    MANA_REGEN: int = 50
    NAME: str = "Eliksir many"
