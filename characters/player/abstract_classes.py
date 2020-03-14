from enum import Enum
from random import randint

from effects.effectv1 import BleedEffect, BattleShoutEffect, HolyShieldEffect


class Attack:
    def __init__(self, min_dmg=None, max_dmg=None, type="PHYSICAL"):
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.type = type

    @property
    def dmg(self):
        return randint(self.min_dmg, self.max_dmg)

    def perform(self, character):
        character.take_dmg(self)
        return True

    def add(self, effect):
        self.min_dmg += effect.min_dmg
        self.max_dmg += effect.max_dmg

    def sub(self, effect):
        self.min_dmg -= effect.min_dmg
        self.max_dmg -= effect.max_dmg


class SkillSet:
    def __init__(self, skills=None):
        self.skills = skills

    def introduce(self):
        for number, skill in self.skills.items():
            print(number, skill)

    def choose(self):
        while True:
            self.introduce()
            choice = input("\nWybierz umiejętność, jeśli chcesz wyjść naciśnij enter\n")
            try:
                if choice == "":
                    break
                return self.skills[choice]
            except KeyError:
                print("\nPodana wartość jest nieprawidłowa, proszę podać cyfrę!\n")


class Type(Enum):
    HEAL = "HEAL"
    BUFF = "BUFF"
    PHYSICAL = "PHYSICAL"
    MAGIC = "MAGIC"


class Skill:
    def __init__(self, mana_cost=None):
        self.mana_cost = mana_cost
        self.type = NotImplemented


class Berserker(Skill):
    def __init__(self, mana_cost=15, min_dmg=20, max_dmg=30):
        super().__init__(mana_cost)
        self.type = Type.PHYSICAL
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    def __str__(self):
        return "Berserker"

    @property
    def dmg(self):
        return randint(self.min_dmg, self.max_dmg)

    def perform(self, character):
        character.take_dmg(self)
        return True


class BloodySlice(Skill):
    def __init__(self, mana_cost=10, min_dmg=10, max_dmg=15):
        super().__init__(mana_cost)
        self.type = Type.PHYSICAL
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    def __str__(self):
        return "Krawe Cięcie"

    @property
    def dmg(self):
        return randint(self.min_dmg, self.max_dmg)

    @property
    def debuff(self):
        return BleedEffect()

    def perform(self, character):
        if self.debuff.is_activated():
            character.add_effect(self.debuff)
        character.take_dmg(self)
        return True


class BattleShout(Skill):
    def __init__(self, mana_cost=10):
        super().__init__(mana_cost)
        self.type = Type.BUFF

    def __str__(self):
        return "Okrzyk Bojowy"

    @property
    def effect(self):
        return BattleShoutEffect()

    def perform(self, character):
        if self.effect.is_activated():
            character.attack.add(self.effect)
            character.add_effect(self.effect)
        return True


class Knight(Player):
    def __init__(self, name=None):
        super().__init__(name)
        self.name = name
        self.max_hp = 60
        self.max_mana = 25
        self.hp = 60
        self.mana = 25
        self.attack = Attack(10, 20)
        self.rest_hp = 15
        self.rest_mana = 5
        self.effects = []
        self.skills = SkillSet({
            "1": Berserker(),
            "2": BloodySlice(),
            "3": BattleShout(),
        })

    def remove_effect(self, effect):
        if effect.type == "DEBUFF STATS":
            self.attack.add(effect)
        if effect.type == "BUFF STATS":
            self.attack.sub(effect)
        self.effects.remove(effect)


class Paladin(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.max_hp = 50
        self.max_mana = 35
        self.hp = 50
        self.mana = 35
        self.attack = Attack(5, 15)
        self.rest_hp = 10
        self.rest_mana = 15
        self.effects = []
        self.skills = SkillSet({
            "1": HammerTime(),
            "2": HolyLight(),
            "3": HolyShield(),
        })

    def heal(self, effect):
        self.hp += effect.hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp


class HolyLight(Skill):
    def __init__(self, mana_cost=20):
        super().__init__(mana_cost)
        self.hp = 30
        self.type = Type.HEAL

    def __str__(self):
        return "Święty Blask"

    def perform(self, character):
        character.heal(self)
        return True


class HammerTime(Skill):
    def __init__(self, mana_cost=15):
        super().__init__(mana_cost)
        self.type = Type.MAGIC
        self.min_dmg = 10
        self.max_dmg = 25

    def __str__(self):
        return "Czas Młota!"

    @property
    def dmg(self):
        return randint(self.min_dmg, self.max_dmg)

    def perform(self, character):
        character.take_dmg(self)
        return True


class HolyShield(Skill):
    def __init__(self, mana_cost=20):
        super().__init__(mana_cost)
        self.type = Type.BUFF

    def __str__(self):
        return "Święta Tarcza"

    @property
    def buff(self):
        return HolyShieldEffect()

    def perform(self, character):
        if self.buff.is_activated():
            character.add_effect(self.buff)
        return True


player = Paladin("Bebikowy")
enemy = Enemy("Adaś")


while True:
    player.activate_effect()
    player.perform_action(enemy)
    print(enemy.hp)
    if enemy.is_dead():
        break
    enemy.attack.perform(player)
    print(player.hp)
    enemy.activate_effect()
    if player.is_dead():
        break
