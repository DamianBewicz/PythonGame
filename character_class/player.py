from random import randint
from items.backpack import Backpack


class Player:
    def __init__(self, name):
        self.name = name
        self.type = None
        self.max_dmg = None
        self.min_dmg = None
        self.max_hp = None
        self.max_mana = None
        self.hp = None
        self.mana = None
        self.backpack = Backpack()
        self.money = 100
        self.skills = []
        self.effects = []
        self.actions = [("Zwykły atak", self.attack), ("Atak specjalny", self.choose_skill), ("Odpoczynek", self.rest),
                        ("Plecak", self.use), ]

    def __str__(self):
        return f"\n{self.name}\n" \
               f"Życie postaci : {self.hp}\n" \
               f"Mana postaci : {self.mana}\n"

    def attack(self, other_player):
        other_player.hp -= randint(self.min_dmg, self.max_dmg)

    def choose_action(self, other_player):
        for number, action in enumerate(self.actions):
            print(number + 1, action[0])
        choice = int(input("\nWybierz akcje\n"))
        if choice == 1 or choice == 2:
            return self.actions[choice - 1][1](other_player)
        if choice == 3 or choice == 4:
            return self.actions[choice - 1][1]()

    def choose_skill(self, other_player):
        for number, skill in enumerate(self.skills):
            print(f"{number + 1} {skill[0]}")
        choice = int(input("\nWybierz atak\n")) - 1
        return self.skills[choice][1](other_player)

    def use(self, other_player):
        if not self.backpack.is_empty():
            self.backpack.print_available_items()
            choice = int(input("\nWybierz przedmiot\n"))
            self.backpack.items[choice - 1].use_item(self)
            self.backpack.items.pop(choice - 1)
        else:
            print("\nPlecak jest pusty!\n")
            return self.choose_action(other_player)

    def is_dead(self):
        return self.hp <= 0

    def lose_item(self):
        self.money = int(0.1 * self.money)
        self.backpack.items.clear()

    def rest(self):
        raise NotImplemented

    def reset(self):
        self.hp = self.max_hp
        self.mana = self.max_mana
