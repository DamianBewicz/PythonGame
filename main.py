from castle import OldCastle
from termcolor import colored
from os import system
from castle.new_castle import NewCastle
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
        Shaman,
        Warlock
    ]
    LAST_PART = len(ENEMIES)

    def __init__(self) -> None:
        self.player = None
        self.part: int = 0
        self.game_over: bool = False
        self.locations = []

    def create_character(self) -> None:
        chosen_name = input("\nWybierz imię swojej postaci\n")
        while True:
            try:
                print()
                classes_names = [cls.CLASS_NAME.value.capitalize() for cls in self.AVAIBLE_CLASSES]
                introduce_from_list(classes_names)
                chosen_character = input("\nWybierz klasę swojej postaci\n")
                self.player = self.AVAIBLE_CLASSES[int(chosen_character) - 1](chosen_name)
                self.add_locations(self.player)
                return
            except KeyError:
                print("\nPodana wartość jest nieprawidłowa\n")

    def add_locations(self, player) -> None:
        castles = [
            OldCastle(player),
            NewCastle(player)
        ]
        self.locations.extend(castles)

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
        self.start_fight()
        self.part += 1
        if self.part == self.LAST_PART:
            raise GameHasFinished(colored("\nBrawo, pokonałeś wszystkich wrogów, moje gratulacje :D\n", "blue"))
        self.player.reset()
        self.player.level_up()

    def choose_main_actions(self) -> None:
        main_actions_names = (
            "Kontynuuj historię",
            "Idź do zamku",
            "Ekwipunek",
            "Zagraj w Blackjack'a",
        )
        main_actions = (
            self.continue_story,
            self.choose_castle,
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

    def choose_castle(self) -> None:
        question = "\nWybierz lokacje\n"
        main_actions_names = (
            "Idź do starego zamku",
            "Idź do nowego zamku",
        )
        main_actions = (
            self.locations[0].visit_merchant,
            self.locations[1].visit_merchant
        )

        while True:
            try:
                introduce_from_list(main_actions_names)
                chosen_action = choose_item(main_actions, question)
                if chosen_action is not None:
                    chosen_action()
                else:
                    break
            except IndexError:
                print("\nPodana wartość jest nieprawidłowa!\n")


def main() -> None:
    game = Game()
    game.create_character()
    system("clear")
    game.choose_main_actions()


if __name__ == "__main__":
    main()
