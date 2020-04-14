from items.defensive_items.abstract_items import Armor


class RustedArmor(Armor):
    NAME = "Zardzewiała zbroja"

    def __init__(self) -> None:
        super().__init__()
        self.defense = 10


class LeatherArmor(Armor):
    NAME = "Skórzana zbroja"

    def __init__(self) -> None:
        super().__init__()
        self.defense = 25
