from random import randint


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
            print(effect._duration)
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
                if chosen_attack.type == "BUFF" or chosen_attack.type == "HEAL":
                    return chosen_attack.perform(self)
                return chosen_attack.perform(character)
            print("Brakuje many")