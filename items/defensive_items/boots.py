from items.defensive_items.abstract_items import Boots


class RustedBoots(Boots):
    NAME = "Zardzewiałe buty"

    def __init__(self) -> None:
        super().__init__()
        self.defense = 5

    def __str__(self) -> str:
        return "Zardzewiałe buty"
