from skills.abstract_skills import Skill
from .pet import Pet
from skills import Attack, Fireball


class Imp(Pet):
    def __init__(self, name: str = "Imp", mana: int = 20):
        super().__init__(name, mana)
        self.attack: Attack = Attack(5, 10)
        self.skill: Skill = Fireball()

    def perform(self, character) -> None:
        print(self.mana)
        if self.has_mana():
            self.skill.perform(character)
        else:
            self.attack.perform(character)

    def has_mana(self) -> bool:
        return self.mana >= self.skill.mana_cost
