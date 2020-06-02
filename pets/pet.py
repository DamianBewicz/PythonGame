from skills import Attack
from skills.abstract_skills import Skill


class Pet:
    def __init__(self, name: str = None, mana: int = None) -> None:
        self.name: str = name
        self.mana: int = mana
        self.attack: Attack = NotImplemented
        self.skill: Skill = NotImplemented

    def perform(self, character):
        return NotImplemented
