from effects.abstract_effects import PeriodicDamage, Effect, CrowdControl


class BleedEffect(PeriodicDamage):

    def __init__(self, duration=3, dmg=4, chance=100):
        super().__init__(duration, dmg=dmg, chance=chance)
        self.name = "Krwawienie"


class BurnEffect(PeriodicDamage):

    def __init__(self, duration=3, dmg=4, chance=30):
        super().__init__(duration, dmg=dmg, chance=chance)
        self.name = "Podpalenie"


class BattleShoutEffect(Effect):
    TYPE = "BUFF STATS"

    def __init__(self, duration=3, chance=100):
        super().__init__(duration, chance)
        self.name = "Okrzyk bojowy"
        self.min_dmg = 5
        self.max_dmg = 5


class HolyShieldEffect(Effect):
    TYPE = "BUFF"

    def __init__(self, duration=3, chance=100):
        super().__init__(duration, chance)
        self.name = "Święta tarcza"
        self.hp = 4

    def activate(self, character):
        super().activate(character)
        character.heal(self)


class FireShieldEffect(Effect):
    TYPE = "BUFF"
    DMG_RED = 0.6

    def __init__(self, duration=3, chance=100):
        super().__init__(duration, chance)
        self.name = "Płomienna Tarcza"


class Blind(CrowdControl):

    def __init__(self, duration=2, chance=50) -> None:
        super().__init__(duration, chance)
        self.name = "Oślepienie"


class EarthQuakeEffect(CrowdControl):

    def __init__(self, duration=2, chance=100) -> None:
        super().__init__(duration, chance)
        self.name = "Ogłuszenie"


class FuryEffect(Effect):
    TYPE = "BUFF"

    def __init__(self, duration=2, chance=50):
        super().__init__(duration, chance)
        self.name = "Szał"


class CurseEffect(Effect):
    TYPE = "DEBUFF"

    def __init__(self, duration=2, chance=100, percent_damage_reduction=40) -> None:
        super().__init__(duration, chance)
        self.name = "Klątwa"
        self.percent_damage_reduction = percent_damage_reduction

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
