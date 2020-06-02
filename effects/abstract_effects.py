from random import randint

from dmg_object.damage_object import DamageObject


class Effect:
    STATUS_EFFECT = NotImplemented

    def __init__(self, duration: int = None, chance: int = None) -> None:
        self.name: str = NotImplemented
        self._duration: int = duration
        self.chance: int = chance

    def is_activated(self) -> bool:
        return randint(1, 100) in range(1, self.chance + 1)

    def activate(self, character) -> None:
        self._duration -= 1

    def is_finished(self) -> bool:
        return self._duration == 0


class PeriodicDamage(Effect):
    TYPE = NotImplemented
    STATUS_EFFECT: str = "DEBUFF"

    def __init__(self, duration: int, chance: int, dmg: int) -> None:
        super().__init__(duration, chance)
        self.dmg: int = dmg

    def activate(self, character) -> None:
        super().activate(character)
        character.take_dmg(DamageObject(dmg=self.dmg))


class CrowdControl(Effect):
    STATUS_EFFECT: str = "CROWD CONTROL"

    def __init__(self, duration=None, chance=None) -> None:
        super().__init__(duration, chance)
        self.name = NotImplemented
