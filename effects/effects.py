from .abstract_effects import PeriodicDamage, Effect, CrowdControl
from enums import AttackType


class BleedEffect(PeriodicDamage):
    TYPE: AttackType = AttackType.PHYSICAL

    def __init__(self, duration: int = 3, dmg: int = 4, chance: int = 100) -> None:
        super().__init__(duration, dmg=dmg, chance=chance)
        self.name: str = "Krwawienie"


class BurnEffect(PeriodicDamage):
    TYPE: AttackType = AttackType.MAGIC

    def __init__(self, duration: int = 3, dmg: int = 4, chance: int = 30) -> None:
        super().__init__(duration, dmg=dmg, chance=chance)
        self.name: str = "Podpalenie"


class BattleShoutEffect(Effect):
    STATUS_EFFECT: str = "BUFF STATS"

    def __init__(self, duration: int = 3, chance: int = 100) -> None:
        super().__init__(duration, chance)
        self.name: str = "Okrzyk bojowy"
        self.min_dmg: int = 5
        self.max_dmg: int = 5


class HolyShieldEffect(Effect):
    STATUS_EFFECT: str = "BUFF"

    def __init__(self, duration: int = 3, chance: int = 100) -> None:
        super().__init__(duration, chance)
        self.name: str = "Święta tarcza"
        self.hp: int = 4

    def activate(self, character):
        super().activate(character)
        character.heal(self.hp)


class FireShieldEffect(Effect):
    STATUS_EFFECT: str = "BUFF"
    DMG_RED: float = 0.6

    def __init__(self, duration: int = 3, chance: int = 100) -> None:
        super().__init__(duration, chance)
        self.name: str = "Płomienna Tarcza"


class Blind(CrowdControl):

    def __init__(self, duration: int = 2, chance: int = 50) -> None:
        super().__init__(duration, chance)
        self.name: str = "Oślepienie"


class EarthQuakeEffect(CrowdControl):

    def __init__(self, duration: int = 2, chance: int = 100) -> None:
        super().__init__(duration, chance)
        self.name: str = "Ogłuszenie"


class FuryEffect(Effect):
    STATUS_EFFECT: str = "BUFF"

    def __init__(self, duration: int = 2, chance: int = 50) -> None:
        super().__init__(duration, chance)
        self.name: str = "Szał"


class CurseEffect(Effect):
    STATUS_EFFECT: str = "DEBUFF"

    def __init__(self, duration: int = 2, chance: int = 100, percent_damage_reduction: int = 40) -> None:
        super().__init__(duration, chance)
        self.name: str = "Klątwa"
        self.percent_damage_reduction: int = percent_damage_reduction

    def activate(self, character) -> None:
        self._duration -= 1

    def get_damage_reduction(self) -> float:
        return self.percent_damage_reduction/100

    def is_finished(self) -> bool:
        return self._duration == 0


# class RevengeEffect(Effect):
#     def __init__(self, duration=3, chance=100):
#         super().__init__(duration, chance)
#         self.name = "Zemsta"
