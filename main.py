from character_class import Knight, Mage, Paladin
from characters.blacksmith import Blacksmith
from characters.villager import Villager
from story_line import *


class Game:

    STORY_LINE = {
        1: part1,
        2: part2,
    }

    CHARACTER_CLASSES = (
        ("Rycerz", Knight),
        ("Mag", Mage),
        ("Palladyn", Paladin),
    )

    @staticmethod
    def create_character():
        character_name = input("Podaj nazwę gracza\n")
        while True:
            try:
                print()
                for number, class_name in enumerate(Game.CHARACTER_CLASSES):
                    print(f"{number + 1} {class_name[0]}")
                selected_class = int(input("\n\nWybierz klasę swojej postaci\n"))
                return Game.CHARACTER_CLASSES[selected_class - 1][1](character_name)
            except IndexError:
                print("Nieprawidłowy number!")
            except ValueError:
                print("Potrzebna cyfra!")

    @staticmethod
    def tell_story(part):
        return Game.STORY_LINE[part]

    @staticmethod
    def create_enemy(part):
        enemies = [Villager, Blacksmith]
        return enemies[part - 1]()

    @staticmethod
    def fight_boss(player, enemy):
        while True:
            print(player)
            player.perform_action(enemy)
            if player.is_dead():
                player.lose_item()
                break
            print(enemy)
            if enemy.is_dead():
                enemy.drop_loot(player)
                player.reset()
                break
            enemy.attack(player)

    @staticmethod
    def start_story():
        created_player = Game.create_character()
        act = 1
        while True:
            print(Game.tell_story(act))
            created_enemy = Game.create_enemy(act)
            Game.fight_boss(created_player, created_enemy)
            if act == len(Game.STORY_LINE):
                break
            else:
                act += 1


Game.start_story()
