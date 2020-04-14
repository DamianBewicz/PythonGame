from items.defensive_items.abstract_items import Helmet


class RustedHelmet(Helmet):
    NAME = "Zardzewiały hełm"

    def __init__(self) -> None:
        super().__init__()
        self.defense = 5

