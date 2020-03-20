from effects.abstract_effects import PeriodicDamage, Effect


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


class Blind(Effect):
    TYPE = "CROWD CONTROL"

    def __init__(self, duration=2, chance=50) -> None:
        super().__init__(duration, chance)
        self.name = "Oślepienie"


class RevengeEffect(Effect):
    def __init__(self, duration=3, chance=100):
        super().__init__(duration, chance)


class FuryEffect(Effect):
    def __init__(self, duration=2, chance=50):
        super().__init__(duration, chance)
