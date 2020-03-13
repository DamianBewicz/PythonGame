from random import randint
from skills.abstract_skills import Spell


class Fireball(Spell):
    def __init__(self, mana_cost=20, dmg=30):
        super().__init__(mana_cost, dmg)

    def has_mana(self, player):
        return player.mana >= self.mana_cost

    def cast(self, player, enemy):
        if self.has_mana(player):
            enemy.hp -= self.dmg
        return self.has_mana(player)


class FireShield:
    def __init__(self):
        self.mana_cost = 15
        self.dmg = 15
        self.skill_type = "magic"

    def has_mana(self, player):
        return player.mana >= self.mana_cost

    def cast(self, player):
        can_cast = self.has_mana(player)
        if self.has_mana(player):
            player.mana -= self.mana_cost
            player.effects.append(FireShield(100))
            return can_cast
        print("\nBrakuje many!\n")
        return can_cast
