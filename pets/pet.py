class Pet:
    def __init__(self, name: str = None, mana: int = None) -> None:
        self.name = name
        self.mana = mana
        self.attack = NotImplemented
        self.skill = NotImplemented

    def perform(self, character):
        return NotImplemented
