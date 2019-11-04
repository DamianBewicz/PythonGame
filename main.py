from character_class import Knight, Mage, Paladin
from characters.blacksmith import Blacksmith
from characters.villager import Villager


class Game:

    @staticmethod
    def create_name() -> str:
        player_name = input("Podaj nazwę gracza\n")
        return player_name

    @staticmethod
    def choose_class() -> int:
        classes_names = ["Rycerz", "Mag", "Palladyn"]
        print()
        for number, character_name in enumerate(classes_names):
            print(f"{number + 1} {character_name}")
        selected_class = int(input("\n\nWybierz klasę swojej postaci\n"))
        return selected_class

    @staticmethod
    def create_character():
        character_name = Game.create_name()
        character_classes = [Knight(character_name), Mage(character_name), Paladin(character_name)]
        return character_classes[Game.choose_class() - 1]

    @staticmethod
    def story(part):
        story_line = {1: """\nZwykły śmiertelnik wyrusza w poszukiwaniu przygód, pierwszym przeciwinikiem na jego 
drodze jest niejaki Władysław. Jego widły jako jedne z nielicznych w wiosce są w stanie do czegokolwiek
się przysłużyć.\n""",
                      2: """\nPojedynek ten nie sprawił przyjemności naszemu poszukiwaczowi przygód. Uważał on, że
poradzi sobie bez problemu z kimś dużo silniejszym. Następnym jego przeciwnikiem był niejaki kowal Zygmunt.
Jego biceps przyćmiły nawet samego Mariusza Pudzianowskiego.\n"""}
        return story_line[part]

    @staticmethod
    def create_enemy(part):
        enemies = [Villager, Blacksmith, ]
        return enemies[part - 1]()


player = Game.create_character()
act = 1

while True:
    print(Game.story(act))
    enemy = Game.create_enemy(act)
    while True:
        print(player)
        player.choose_action(enemy)
        if player.is_dead():
            player.lose_item()
            break
        print(enemy)
        if enemy.is_dead():
            enemy.drop(player)
            player.reset()
            break
        enemy.attack(player)
    act += 1
