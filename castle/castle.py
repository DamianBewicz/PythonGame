from merchants.alchemist import Alchemist
from merchants.armourer import Armourer
from merchants.blacksmith import Blacksmith
from merchants.enchanter import Enchanter
from utils import introduce_from_list, choose_action


class Castle:
    ARMOURER: Armourer = NotImplemented
    BLACKSMITH: Blacksmith = NotImplemented
    ENCHANTER: Enchanter = NotImplemented
    ALCHEMIST: Alchemist = NotImplemented
    REQUIRED_STORY_LINE: int = NotImplemented

    def __init__(self, game_story_part, player):
        self.required_part = game_story_part
        self.player = player

    def can_enter(self):
        pass

    def visit_merchant(self):
        actions: list = [
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
            question = "\nWybierz, do kogo chcesz się wybrać, lub naciśnij enter, aby wyjść\n"
            introduce_from_list(merchant_actions_names)
            chosen_merchant = choose_action(actions, question)
            if chosen_merchant is not None:
                chosen_merchant.choose_interaction(self.player)
            else:
                break
