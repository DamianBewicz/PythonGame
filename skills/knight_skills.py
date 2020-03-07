from random import randint


class Berserker:
    def __init__(self):
        self.mana_cost = 15

    def __str__(self):
        return "Berserker"

    def cast(self, player, enemy) -> None:
        player.mana -= self.mana_cost
        enemy.hp -= randint(player.min_dmg, player.max_dmg) * 2

    def has_mana(self, player) -> bool:
        return self.mana_cost < player.mana


def main():
    player = None
    skill = Berserker()
    if skill.available_for(player):
        skill.cast(enemy)
