from items.defensive_items.abstract_items import Gloves


class RustedGloves(Gloves):
    NAME = "Zardzewiałe rękawice"

    def __init__(self) -> None:
        super().__init__()
        self.defense = 5
