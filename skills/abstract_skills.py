class Skill:
    def __init__(self, mana_cost=NotImplemented):
        self.mana_cost = mana_cost

    def has_mana(self, player):
        return player.mana >= self.mana_cost


class Spell(Skill):
    def __init__(self, mana_cost, dmg):
        super().__init__(mana_cost)
        self.dmg = dmg


class SpecialAttack(Skill):
    def __init__(self, mana_cost):
        super().__init__(mana_cost)


class Buff(Skill):
    def __init__(self, mana_cost, buff=NotImplemented):
        super().__init__(mana_cost)
            self.buff = buff


b = Buff(15)
