from random import randint


class Enemy:
    def __init__(self) -> None:
        self.name = NotImplemented
        self.max_dmg = NotImplemented
        self.min_dmg = NotImplemented
        self.max_hp = NotImplemented
        self.hp = NotImplemented
        self.gold_loot_range = NotImplemented, NotImplemented
        self.loot = NotImplemented

    def __str__(self) -> str:
        return f"""\n{self.name}
Punkty życia : {self.hp}\n"""

    def attack(self, other_player) -> None:
        other_player.hp -= randint(self.min_dmg, self.max_dmg)

    def is_dead(self) -> bool:
        return self.hp <= 0

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
