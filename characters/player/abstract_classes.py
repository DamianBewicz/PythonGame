from random import randint

from effects.effectv1 import Bleed


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


class Character:
    def __init__(self, name: str):
        self.name = name
        self.max_hp = NotImplemented
        self.max_mana = NotImplemented
        self.hp = NotImplemented
        self.mana = NotImplemented
        self.attack = NotImplemented
        self.effects = NotImplemented

    def take_dmg(self, attack):
        self.hp -= attack.dmg

    def is_dead(self):
        return self.hp <= 0

    def add_effect(self, effect):
        for e in self.effects:
            if isinstance(e, type(effect)):
                self.remove_effect(e)
                break
        self.effects.append(effect)

    def remove_effect(self, effect):
        self.effects.remove(effect)

    def activate_effect(self):
        for effect in self.effects:
            effect.activate(self)
            if effect.is_finished():
                self.remove_effect(effect)


class Player(Character):
    NAME = None

    def __init__(self, name: str):
        super().__init__(name)
        self.rest_hp = NotImplemented
        self.rest_mana = NotImplemented
        self.skills = NotImplemented
        self.actions = (
            "Zwykły atak",
            "Umiejętność",
            "Odpoczynek",
        )

    def rest(self):
        self.hp += self.rest_hp
        self.mana += self.rest_mana
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        if self.mana > self.max_mana:
            self.mana = self.max_mana
        return True

    def introduce_actions(self):
        for number, action in enumerate(self.actions, start=1):
            print(number, action)

    def perform_action(self, character):
        while True:
            actions = {
                "1": self.attack.perform,
                "2": self.perform_skill,
                "3": self.rest
            }
            self.introduce_actions()
            result = True
            try:
                choice = input("\nWybierz akcje\n")
                if choice == "1" or choice == "2":
                    result = actions[choice](character)
                else:
                    result = actions[choice]()
            except KeyError:
                print("\nPodana wartość jest nieprawidłowa\n")
                continue
            if result:
                break

    def has_mana(self, choosen_attack):
        return self.mana >= choosen_attack.mana_cost

    def perform_skill(self, character):
        while True:
            chosen_attack = self.skills.choose()
            if chosen_attack is None:
                break
            elif self.has_mana(chosen_attack):
                self.mana -= chosen_attack.mana_cost
                return chosen_attack.perform(character)
            print("Brakuje many")


class Enemy(Character):
    def __init__(self, name: str):
        super().__init__(name)


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


class Skill:
    def __init__(self, mana_cost=None):
        self.mana_cost = mana_cost


class Berserker(Skill):
    def __init__(self, mana_cost=15, min_dmg=20, max_dmg=30):
        super().__init__(mana_cost)
        self.type = "PHYSICAL"
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    def __str__(self):
        return "Berserker"

    @property
    def dmg(self):
        return randint(self.min_dmg, self.max_dmg)

    def perform(self, character):
        return character.take_dmg(self)


class BloodySlice(Skill):
    def __init__(self, mana_cost=10, min_dmg=10, max_dmg=15):
        super().__init__(mana_cost)
        self.type = "PHYSICAL"
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    def __str__(self):
        return "Krawe cięcie"

    @property
    def dmg(self):
        return randint(self.min_dmg, self.max_dmg)

    def perform(self, character):
        debuff = Bleed()
        if debuff.is_activated():
            character.add_effect(debuff)
        character.take_dmg(self)
        return True


class Knight(Player):
    def __init__(self, name=None):
        super().__init__(name)
        self.skills = SkillSet({
            "1": Berserker(),
            "2": BloodySlice(),
            # "3": BattleShout()
        }
        )


player = Knight("Bebikowy")
enemy = Enemy("Adaś", 500, 20, 500, 20, Attack(5, 10))

while True:
    player.perform_action(enemy)
    print(enemy.hp)
    if enemy.is_dead():
        break
    enemy.attack.perform(player)
    print(player.hp)
    print(enemy.effects)
    enemy.activate_effect()
    if player.is_dead():
        break
