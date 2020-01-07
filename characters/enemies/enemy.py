from random import randint
from math import floor


class Enemy:
    def __init__(self) -> None:
        self.name = NotImplemented
        self.max_dmg = NotImplemented
        self.min_dmg = NotImplemented
        self.max_hp = NotImplemented
        self.max_mana = NotImplemented
        self.hp = NotImplemented
        self.mana = NotImplemented
        self.gold_loot_range = NotImplemented, NotImplemented
        self.loot = NotImplemented
        self.effects = []
        self.skills = [
            self.attack,
            self.rest,
        ]

    def __str__(self) -> str:
        return f"""\n{self.name}
`Punkty życia : {self.hp}\n"""

    def attack(self, other_player) -> None:
        other_player.hp -= randint(self.min_dmg, self.max_dmg)

    def is_dead(self) -> bool:
        return self.hp <= 0

    def rest(self, player) -> None:
        self.hp += floor(0.05 * self.max_hp)
        self.mana += floor(0.05 * self.max_mana)

    def drop_loot(self, other_player) -> None:
        other_player.money += randint(*self.gold_loot_range)
        for item in self.loot:
            if not other_player.backpack.is_full():
                other_player.backpack.items.append(item)
            else:
                choice = input(f"Otrzymano {item}, lecz plecak jest pełny.\n"
                               "Czy chcesz wyrzucić przedmiot z plecaka?\n1 Tak\n2 Nie\n")
                if choice == '1' and other_player.backpack.remove_item():
                    other_player.backpack.items.append(item)

    def make_move(self, player) -> None:
        if self.mana < self.max_mana:
            random_skill = randint(0, 1)
            self.skills[random_skill](player)
        else:
            random_skill = randint(0, len(self.skills) - 1)
            self.skills[random_skill](player)
