from items.abstract_item import Potion


class HealthPotion(Potion):
    HP_REGEN: int = NotImplemented

    def __str__(self) -> str:
        return f"{self.NAME}: Regeneruje {self.HP_REGEN} punktów życia"

    def drink(self, player: 'Player') -> None:
        player.heal(self.HP_REGEN)


class MinorHealthPotion(HealthPotion):
    HP_REGEN: int = 30
    NAME: str = "Mniejsza mikstura zdrowia"


class NormalHealthPotion(HealthPotion):
    HP_REGEN: int = 40
    NAME: str = "Mikstura zdrowia"


class GreaterHealthPotion(HealthPotion):
    HP_REGEN: int = 60
    NAME: str = "Większa mikstura zdrowia"


class ElixirOfLife(HealthPotion):
    HP_REGEN: int = 100
    NAME: str = "Eliksir życia"
