from pets.pet import Pet
from skills.attack_skill import Attack
from skills.mage_skills import Fireball


class Imp(Pet):
    def __init__(self, name: str = "Imp", mana: int = 20):
        super().__init__(name, mana)
        self.attack = Attack(5, 10)
        self.skill = Fireball()

    def perform(self, character) -> None:
        if self.has_mana():
            self.skill.perform(character)
        else:
            self.attack.perform(character)

    def has_mana(self) -> bool:
        return self.mana >= self.skill.mana_cost
