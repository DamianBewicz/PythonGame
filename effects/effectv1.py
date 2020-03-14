from random import randint


class Effect:
    def __init__(self, duration=None, chance=None):
        self.type = NotImplemented
        self._duration = duration
        self.chance = chance

    def is_activated(self):
        return randint(1, 100) in range(1, self.chance + 1)

    def activate(self, character):
        self._duration -= 1

    def is_finished(self):
        return self._duration == 0


class BleedEffect(Effect):
    TYPE = "DEBUFF STATS"

    def __init__(self, duration=3, dmg=4, chance=100):
        super().__init__(duration, chance)
        self.dmg = dmg

    def activate(self, character):
        super().activate(character)
        character.take_dmg(self)


class BattleShoutEffect(Effect):
    TYPE = "BUFF STATS"

    def __init__(self, duration=3, chance=100):
        super().__init__(duration, chance)
        self.min_dmg = 5
        self.max_dmg = 5


class HolyShieldEffect(Effect):
    TYPE = "BUFF"

    def __init__(self, duration=3, chance=100):
        super().__init__(duration, chance)
        self.hp = 4

    def activate(self, character):
        super().activate(character)
        character.heal(self)



