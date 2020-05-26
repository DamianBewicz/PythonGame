from castle import OldCastle
from termcolor import colored
from os import system
from characters.enemies import Goblin, Orc, Warlock, Shaman
from characters.player import Knight, Paladin, Mage
from minigames.blackjack import Blackjack
from utils import introduce_from_list, choose_item


class GameHasFinished(Exception):
    pass


class Game:
    AVAIBLE_CLASSES: list = [
        Knight,
        Paladin,
        Mage,
    ]
    ENEMIES: list = [
        Goblin,
        Orc,
        Warlock,
        Shaman
    ]
    LAST_PART = len(ENEMIES)

    def __init__(self) -> None:
        self.player = None
        self.part: int = 0
        self.game_over: bool = False
        self.old_castle = None

    def create_character(self) -> None:
        chosen_name = input("\nWybierz imię swojej postaci\n")
        while True:
            try:
                print()
                classes_names = [cls.CLASS_NAME.value.capitalize() for cls in self.AVAIBLE_CLASSES]
                introduce_from_list(classes_names)
                chosen_character = input("\nWybierz klasę swojej postaci\n")
                self.player = self.AVAIBLE_CLASSES[int(chosen_character)](chosen_name)
                self.old_castle = OldCastle(self.player)  # TODO: self.part
                return
            except KeyError:
                print("\nPodana wartość jest nieprawidłowa\n")

    def start_fight(self) -> None:
        enemy = Game.ENEMIES[self.part]()
        while True:
            print(self.player)
            print(self.player.effects)
            print(enemy)
            print(enemy.effects)

            self.player.perform_action(enemy)
            self.player.activate_effects()
            if self.player.is_dead():
                raise GameHasFinished(colored("\nPrzegrałeś, powodzenia następnym razem\n", "white"))
            if enemy.is_dead():
                return

            enemy.perform_action(self.player)
            enemy.activate_effects()
            if self.player.is_dead():
                raise GameHasFinished(colored("\nPrzegrałeś, powodzenia następnym razem\n", "white"))
            if enemy.is_dead():
                return

            system("clear")

    def continue_story(self) -> None:
        self.part += 1
        self.start_fight()
        if self.part == self.LAST_PART:
            raise GameHasFinished(colored("\nBrawo, pokonałeś wszystkich wrogów, moje gratulacje :D\n", "blue"))
        self.player.reset()

    def choose_main_actions(self) -> None:
        main_actions_names = (
            "Kontynuuj historię",
            "Idź do starego zamku",
            "Ekwipunek",
            "Zagraj w Blackjack'a",
        )
        main_actions = (
            self.continue_story,
            self.old_castle.visit_merchant,
            self.player.equipment.choose_main_action,
            Blackjack.main
        )
        question = "\nWybierz interakcje\n"
        while True:
            try:
                introduce_from_list(main_actions_names)
                chosen_action = choose_item(main_actions, question)
                if chosen_action is not None:
                    try:
                        chosen_action()
                    except TypeError:
                        chosen_action(self.player)
                else:
                    print("\nPodana wartość jest nieprawidłowa!\n")
            except GameHasFinished as reason:
                print(reason)
                return None


def main() -> None:
    game = Game()
    game.create_character()
    system("clear")
    game.choose_main_actions()


if __name__ == "__main__":
    main()
