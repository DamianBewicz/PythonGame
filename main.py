from typing import Type
from castle.old_town import OldTown
from characters import Knight, Mage, Paladin, Blacksmith, Villager, Player
from effects.effect import Effect
from story_line import *


class Game:

    def __init__(self) -> None:
        self.player = Game.create_character()
        self.act = 0
        self.castles = OldTown(self.player)
        self.enemies = [Villager, Blacksmith]

    STORY_LINE = {
        0: part1,
        1: part2,
    }

    def start_story(self) -> None:
        Game.make_acion(self)

    @staticmethod
    def create_character() -> Player:
        classes = (
            Knight,
            Mage,
            Paladin,
        )

        character_name = input("Podaj nazwę gracza\n")
        while True:
            try:
                print()
                for number, cls in enumerate(classes):
                    print(f"{number + 1} {cls.NAME}")
                choice = int(input("\n\nWybierz klasę swojej postaci\n"))
                return classes[choice - 1](character_name)
            except IndexError:
                print("Nieprawidłowy number!")
            except ValueError:
                print("Potrzebna cyfra!")

    def make_acion(self) -> None:
        main_actions = (
            ("Idź do zamku", self.castles.introduce_interactions),
            ("Kontynuuj przygodę", self.continue_story),
        )
        while True:
            print("\nDokonaj wyboru\n")
            for number, action in enumerate(main_actions):
                print(number + 1, action[0])
            choice = int(input())
            main_actions[choice - 1][1]()
            if Game.is_finished(self):
                break

    @staticmethod
    def create_enemy(part):
        enemies = [Villager, Blacksmith]
        return enemies[part]()

    @staticmethod
    def fight_boss(player, enemy) -> None:
        while True:
            print(player)
            Effect.effects_action(player)
            player.perform_action(enemy)
            print(player.max_dmg)
            if player.is_dead():
                player.lose_item()
                break
            print(enemy)
            Effect.effects_action(enemy)
            if enemy.is_dead():
                enemy.drop_loot(player)
                player.reset()
                break
            enemy.attack(player)

    def continue_story(self) -> None:
        print(Game.STORY_LINE[self.act])
        created_enemy = Game.create_enemy(self.act)
        Game.fight_boss(self.player, created_enemy)
        self.act += 1

    def is_finished(self) -> bool:
        return self.act == len(Game.STORY_LINE)


game1 = Game()
game1.start_story()
