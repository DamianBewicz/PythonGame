from characters import Paladin, Mage, Knight, Goblin, Orc


class Game:
    AVAIBLE_CLASSES = {
        "1": Knight,
        "2": Paladin,
        "3": Mage,
    }

    ENEMIES = {
        1: Goblin(),
        2: Orc()
    }

    LAST_PART = 2

    def __init__(self):
        self.player = NotImplemented
        self.enemy = Goblin()
        self.part = 1
        self.game_over = False

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

    def start_fight(self):
        while True:
            print(self.player)
            print(self.player.effects)
            self.player.activate_effects()
            self.player.perform_action(self.enemy)
            if self.enemy.is_dead():
                self.player.reset()
                break
            self.enemy.perform_action(self.player)
            print(self.enemy)
            print(self.enemy.effects)
            self.enemy.activate_effects()
            if self.player.is_dead():
                break

    def add_part(self):
        self.part += 1

    def change_enemy(self):
        self.enemy = Game.ENEMIES[self.part]


def main():
    game = Game()
    game.create_character()
    while True:
        game.change_enemy()
        game.start_fight()
        if game.player.is_dead():
            break
        elif game.part == game.LAST_PART:
            print("\nBrawo, pokonałeś wszystkich wrogów, moje gratulacje :D\n")
            break
        game.add_part()


if __name__ == "__main__":
    main()


