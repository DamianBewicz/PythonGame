from characters import Enemy, Paladin, Mage, Knight


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
        for number, classes in enumerate(self.AVAIBLE_CLASSES.values(), start=1):
            print(number, classes)

    def create_character(self):
        while True:
            try:
                chosen_character = input("\nWybierz klasę swojej postaci\n")
                self.introduce_classes()
                self.player = self.AVAIBLE_CLASSES[chosen_character]()
                break
            except KeyError:
                print("\nPodana wartość jest nieprawidłowa\n")


game = Game()
Game.choose_name()


player = Mage("Bebikowy")
enemy = Enemy("Adaś")

while True:
    print(player.effects)
    player.activate_effect()
    player.perform_action(enemy)
    print(enemy.hp)
    if enemy.is_dead():
        break
    enemy.perform_action(player)
    print(player.hp)
    print(enemy.effects)
    enemy.activate_effect()
    if player.is_dead():
        break
