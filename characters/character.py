from effects import EffectSet, Blind
from effects.abstract_effects import CrowdControl


class Character:
    def __init__(self, name: str) -> None:
        self.name = name
        self.max_hp = NotImplemented
        self.max_mana = NotImplemented
        self.hp = NotImplemented
        self.mana = NotImplemented
        self.effects = EffectSet()

    def __str__(self) -> str:
        return f'{self.name}\n' \
               f'Punkty życia: {self.hp}\n' \
               f'Punkty many: {self.mana}\n'

    @property
    def attack(self):
        return NotImplemented

    def take_dmg(self, dmg: int) -> None:
        return NotImplemented

    def is_dead(self) -> None:
        return self.hp <= 0

    def perform_action(self, character) -> None:
        self.attack.perform(character)

    def cant_move(self) -> bool:
        return self.effects.contains(Blind) or self.effects.contains(CrowdControl)

    def activate_effects(self) -> None:
        self.effects.activate(self)

    def heal(self, heal: int) -> None:
        self.hp += heal
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def gain_mana(self, mana: int) -> None:
        self.mana += mana
        if self.mana > self.max_mana:
            self.mana = self.max_mana

    def lose_mana(self, mana: int) -> None:
        self.mana -= mana
        if self.mana < 0:
            self.mana = 0

    def has_mana(self, skill):
        return self.mana >= skill.mana_cost