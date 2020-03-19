from characters import Enemy, Paladin, Mage, Knight
from characters.enemies.villager import Goblin


class Game:
    AVAIBLE_CLASSES = {
        "1": Knight,
        "2": Paladin,
        "3": Mage,
    }

    def __init__(self, ):
        self.player = NotImplemented
        self.enemy = Enemy("Adaś")
        self.part = 1

    @staticmethod
    def choose_name() -> str:
        chosen_name = input("\nWybierz imię swojej postaci\n")
        return chosen_name

    def introduce_classes(self) -> None:
        for number, cls in enumerate(self.AVAIBLE_CLASSES.values(), start=1):
            print(number, cls.NAME)

    def create_character(self):
        chosen_name = self.choose_name()
        while True:
            try:
                self.introduce_classes()
                chosen_character = input("\nWybierz klasę swojej postaci\n")
                self.player = self.AVAIBLE_CLASSES[chosen_character](chosen_name)
                break
            except KeyError:
                print("\nPodana wartość jest nieprawidłowa\n")


player = Knight("Bebikowy")
enemy = Goblin()

while True:
    print(player.effects)
    print(player)
    player.activate_effect()
    player.perform_action(enemy)
    print(enemy.hp)
    if enemy.is_dead():
        break
    enemy.perform_action(player)
    print(player.hp)
    print(enemy)
    print(enemy.effects)
    enemy.activate_effect()
    if player.is_dead():
        break
