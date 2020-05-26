from merchants.alchemist import Alchemist
from merchants.armourer import Armourer
from merchants.blacksmith import Blacksmith
from merchants.enchanter import Enchanter
from utils import introduce_from_list, choose_item


class Castle:
    ARMOURER: Armourer = NotImplemented
    BLACKSMITH: Blacksmith = NotImplemented
    ENCHANTER: Enchanter = NotImplemented
    ALCHEMIST: Alchemist = NotImplemented
    REQUIRED_STORY_LINE: int = NotImplemented

    def __init__(self, player):
        self.player = player

    def can_enter(self, game_part) -> bool:
        return game_part >= self.REQUIRED_STORY_LINE

    def visit_merchant(self) -> None:
        merchants: list = [
            self.ARMOURER,
            self.BLACKSMITH,
            self.ENCHANTER,
            self.ALCHEMIST
        ]

        merchant_actions_names: list = [
            "Idź do płatnerz",
            "Idź do kowala",
            "Idź do zaklinacza",
            "Idź do alchemika"
        ]
        while True:
            introduce_from_list(merchant_actions_names)
            question = "\nWybierz, do kogo chcesz się wybrać, lub naciśnij enter, aby wyjść\n"
            chosen_merchant = choose_item(merchants, question)
            if chosen_merchant is not None:
                chosen_merchant.choose_interaction(self.player)
            else:
                return
