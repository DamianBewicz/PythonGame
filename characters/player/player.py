from effects.effects import Blind
from effects.effects_set import EffectSet
from skills.abstract_skills import Type


class NoManaException(Exception):
    pass


class Character:
    def __init__(self, name: str) -> None:
        self.name = name
        self.max_hp = NotImplemented
        self.max_mana = NotImplemented
        self.hp = NotImplemented
        self.mana = NotImplemented
        self.attack = NotImplemented
        self.effects = EffectSet()

    def __str__(self):
        return f'{self.name}\n' \
               f'Punkty życia: {self.hp}\n' \
               f'Punkty many: {self.mana}\n'

    def take_dmg(self, attack) -> None:
        self.hp -= attack.dmg

    def is_dead(self) -> None:
        return self.hp <= 0

    def perform_action(self, character):
        self.attack.perform(character)

    def cant_move(self):
        return self.effects.contains(Blind)

    def activate_effects(self):
        self.effects.activate(self)

    def heal(self, effect) -> None:
        self.hp += effect.hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp


class Player(Character):
    CLASS_NAME = NotImplemented

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.rest_hp = NotImplemented
        self.rest_mana = NotImplemented
        self.skills = NotImplemented
        self.actions = (
            "Zwykły atak",
            "Umiejętność",
            "Odpoczynek",
        )

    def rest(self) -> None:
        self.hp += self.rest_hp
        self.mana += self.rest_mana
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        if self.mana > self.max_mana:
            self.mana = self.max_mana

    def introduce_actions(self) -> None:
        for number, action in enumerate(self.actions, start=1):
            print(number, action)

    def perform_action(self, character) -> None:
        while True:
            actions = {
                "1": self.attack.perform,
                "2": self.perform_skill,
                "3": self.rest
            }
            self.introduce_actions()
            try:
                choice = input("\nWybierz akcję\n")
                action = actions[choice]
                if choice in ("1", "2"):
                    action(character)
                else:
                    action()
                return
            except KeyError:
                print("\nPodana wartość jest nieprawidłowa\n")
            except NoManaException:
                print("Brakuje many")

    def has_mana(self, choosen_attack) -> bool:
        return self.mana >= choosen_attack.mana_cost

    def perform_skill(self, character) -> None:
        while True:
            chosen_attack = self.skills.choose()
            if chosen_attack is None:
                break
            elif self.has_mana(chosen_attack):
                self.mana -= chosen_attack.mana_cost
                if chosen_attack.type in (Type.BUFF, Type.HEAL):
                    return chosen_attack.perform(self)
                return chosen_attack.perform(character)
            raise NoManaException

    def reset(self):
        self.hp = self.max_hp
        self.mana = self.max_mana
        self.effects.clear()
