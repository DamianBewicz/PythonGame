from random import randint
from characters.enemies import Enemy
from items.backpack import Backpack


class Player:
    NAME = NotImplemented

    def __init__(self, name: str) -> None:
        self.name = name
        self.max_dmg = NotImplemented
        self.min_dmg = NotImplemented
        self.max_hp = NotImplemented
        self.max_mana = NotImplemented
        self.hp = NotImplemented
        self.mana = NotImplemented
        self.rest_hp_rate = NotImplemented
        self.rest_mana_rate = NotImplemented
        self.backpack = Backpack()
        self.money = 100
        self.skills = NotImplemented
        self.effects = []
        self.actions = [
            ("Zwykły atak", self.attack),
            ("Atak specjalny", self.choose_skill),
            ("Odpoczynek", self.rest),
            ("Plecak", self.use),
        ]

    def __str__(self) -> str:
        return f"\n{self.name}\n" \
               f"Życie postaci : {self.hp}\n" \
               f"Mana postaci : {self.mana}\n"

    def attack(self, enemy: Enemy) -> True:
        enemy.hp -= randint(self.min_dmg, self.max_dmg)
        return True

    def perform_action(self, enemy: Enemy) -> None:
        while True:
            for number, action in enumerate(self.actions):
                print(number + 1, action[0])
            choice = int(input("\nWybierz akcje\n"))
            result = True
            if choice == 1 or choice == 2:
                result = self.actions[choice - 1][1](enemy)
            if choice == 3 or choice == 4:
                result = self.actions[choice - 1][1]()
            if result is True:
                break

    def choose_skill(self, enemy: Enemy) -> bool:
        for number, skill in enumerate(self.skills):
            print(f"{number + 1} {skill[0]}")
        choice = int(input("\nWybierz atak\n")) - 1
        return self.skills[choice][1](enemy)

    def use(self) -> bool:
        # Returns True if item was corectly used,otherwise returns False.
        if not self.backpack.is_empty():
            self.backpack.print_available_items()
            choice = int(input("\nWybierz przedmiot\n"))
            if self.backpack.items[choice - 1].use_item(self):
                self.backpack.items.pop(choice - 1)
                return True
            return False
        print("\nPlecak jest pusty!\n")
        return False

    def is_dead(self) -> bool:
        return self.hp <= 0

    def lose_item(self) -> None:
        self.money = int(0.1 * self.money)
        self.backpack.items.clear()

    def rest(self) -> True:
        self.hp += self.rest_hp_rate
        if self.hp > self.max_hp:
            self.hp = self.max_hp

        self.mana += self.rest_mana_rate
        if self.mana > self.max_mana:
            self.mana = self.max_mana
        return True

    def reset(self) -> None:
        self.hp = self.max_hp
        self.mana = self.max_mana
        self.effects = []

    def go_oldtown(self) -> None:
        pass

