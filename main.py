from characters import Paladin, Mage, Knight, Goblin, Orc, Shaman, Warlock
from termcolor import colored
from os import system


class Game:
    AVAIBLE_CLASSES = {
        "1": Knight,
        "2": Paladin,
        "3": Mage,
    }

    ENEMIES = {
        1: Goblin(),
        2: Orc(),
        3: Warlock(),
        4: Shaman()
    }

    LAST_PART = len(ENEMIES)

    def __init__(self) -> None:
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

    def create_character(self) -> None:
        chosen_name = self.choose_name()
        while True:
            try:
                print()
                self.introduce_classes()
                chosen_character = input("\nWybierz klasę swojej postaci\n")
                self.player = self.AVAIBLE_CLASSES[chosen_character](chosen_name)
                break
            except KeyError:
                print("\nPodana wartość jest nieprawidłowa\n")

    def has_someone_died(self) -> None:
        return self.player.is_dead() or self.enemy.is_dead()

    def start_fight(self) -> None:
        while True:
            print(self.player)
            print(self.player.effects)
            print(self.enemy)
            print(self.enemy.effects)
            self.player.perform_action(self.enemy)
            self.player.activate_effects()
            if self.has_someone_died():
                break
            self.enemy.perform_action(self.player)
            self.enemy.activate_effects()
            if self.has_someone_died():
                break
            system("clear")

    def add_part(self) -> None:
        self.part += 1

    def change_enemy(self) -> None:
        self.enemy = Game.ENEMIES[self.part]


def main() -> None:
    game = Game()
    game.create_character()
    system("clear")
    while True:
        game.change_enemy()
        game.start_fight()
        if game.player.is_dead():
            print(colored("\nPrzegrałeś, powodzenia następnym razem\n", "white"))
            break
        elif game.part == game.LAST_PART:
            print(colored("\nBrawo, pokonałeś wszystkich wrogów, moje gratulacje :D\n", "blue"))
            break
        game.player.reset()
        game.add_part()


if __name__ == "__main__":
    main()


