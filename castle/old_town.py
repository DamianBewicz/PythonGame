from characters.npcs.alchemist import Alchemist
from characters.player.player import Player
from professions.wood_cutter import WoodCutter


class OldTown:
    def __init__(self, player: Player) -> None:
        self.player = player
        self.npcs = [Alchemist()]
        self.professions = [WoodCutter()]
        self.interactions = [
            ("Idź na rynek", self.avaible_npcs),
            ("Idź do pracy", self.avaible_jobs),
        ]

    def __str__(self) -> str:
        return "Znajdujesz się w starej twierdzy. Niektórzy handlarze nadal znajdują tutaj swoje źródło dochodu"

    def introduce_interactions(self) -> None:
        while True:
            print("\nWybierz akcję, jeśli chcesz wyjść naciśnij enter.\n")
            for number, interaction in enumerate(self.interactions):
                print(number + 1, interaction[0])
            choice = input()
            if choice == "":
                break
            self.interactions[int(choice) - 1][1]()

    def avaible_npcs(self) -> None:
        print("\nWybierz handlarza\n")
        for number, npc in enumerate(self.npcs):
            print(number + 1, npc)
        choice = int(input())
        self.npcs[choice - 1].choose_action(self.player)

    def avaible_jobs(self) -> None:
        print("\nWybierz zawód\n")
        for number, profession in enumerate(self.professions):
            print(number + 1, profession)
        choice = int(input())
        self.professions[choice - 1].get_pay(self.player)
