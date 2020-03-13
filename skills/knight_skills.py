from random import randint
from effects.bleed import Bleed


class Berserker:
    def __init__(self):
        self.mana_cost = 15
        self.skill_type = "physical"

    def __str__(self):
        return "Berserker"

    def cast(self, player, enemy) -> bool:
        can_cast = self.has_mana(player)
        if can_cast:
            player.mana -= self.mana_cost
            enemy.hp -= randint(player.min_dmg, player.max_dmg) * 2
            return can_cast
        print("\nBrakuje many!\n")
        return can_cast

    def has_mana(self, player) -> bool:
        return player.mana >= self.mana_cost


class BloodySlice:
    def __init__(self):
        self.mana_cost = 10
        self.skill_type = "physical"

    def __str__(self):
        return "Krwawe cięcie"

    def cast(self, player, enemy) -> bool:
        if self.has_mana(player):
            can_cast = self.has_mana(player)
            if can_cast:
                player.mana -= self.mana_cost
                bleed = Bleed(100)
                enemy.hp -= randint(player.min_dmg, player.max_dmg)
                bleed.add_effect(enemy)
                return can_cast
            print("Brakuje many")
            return can_cast

    def has_mana(self, player):
        return player.mana >= self.mana_cost


class BattleShout:
    def __init__(self):
        self.min_dmg_buff = 5
        self.max_dmg_buff = 5
        self.mana_cost = 10
        self.duration_time = 3
        self.skill_type = "buff"

    def __str__(self):
        return "Okrzyk bojowy"

    def cast(self, player) -> bool:
        can_cast = self.has_mana(player)
        if can_cast:
            player.mana -= self.mana_cost
            player.effects.append()
        print("\nBrakuje many!\n")
        return can_cast

    def has_mana(self, player):
        return player.mana >= self.mana_cost

