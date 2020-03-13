from random import randint
from collections import namedtuple

chance = namedtuple("chance", ("start", "end"))


class Effect:
    def __init__(self) -> None:
        self.type = NotImplemented
        self.duration = NotImplemented
        self.effect_chance_range = chance(1, 100)
        self.effect_chance = NotImplemented

    def __str__(self) -> str:
        return NotImplemented

    def perform_action(self, character):
        return NotImplemented

    def add_effect(self, character) -> None:
        if self.is_triggered():
            if self.__class__ not in [effect.__class__ for effect in character.effects]:
                created_object = self
                character.effects.append(created_object)
                if created_object.type == "Static":
                    created_object.perform_action(character)
            else:
                self.remove_effect(character)
                character.effects.append(self)

    def remove_effect(self, character):
        effect_classes = [obj.__class__ for obj in character.effects]
        index = effect_classes.index(self.__class__)
        if character.effects[index].type == "Static":
            character.effects[index].remove_buff(character)
        character.effects.pop(index)

    def is_triggered(self) -> bool:
        chance_number = randint(self.effect_chance_range.start, self.effect_chance_range.end)
        if chance_number in range(1, self.effect_chance + 1):
            return True
        return False

    def is_finished(self) -> bool:
        return self.duration == 0

    def effect_countdown(self, character) -> None:
        if not self.is_finished():
            self.duration -= 1
            if self.type != "Static":
                self.perform_action(character)
            if self.is_finished():
                self.remove_effect(character)

    @staticmethod
    def effects_action(character) -> None:
        if len(character.effects) != 0:
            for effect in character.effects:
                effect.effect_countdown(character)
        return None
