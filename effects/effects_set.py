from termcolor import colored

from effects.abstract_effects import Effect


class EffectSet:
    def __init__(self):
        self.__effects = []

    def __str__(self):
        buffs = ""
        debuffs = ""
        for effect in self.__effects:
            if effect.TYPE == "BUFF" or effect.TYPE == "BUFF STATS":
                buffs += effect.name + " "
            else:
                debuffs += effect.name + " "
        return f"Efekty: {colored(buffs,'green')}{colored(debuffs,'red')}\n"

    def append(self, effect) -> None:
        for e in self.__effects:
            if type(e) == type(effect):
                self.remove(e)
                break
        self.__effects.append(effect)

    def remove(self, effect) -> None:
        self.__effects.remove(effect)

    def activate(self, character) -> None:
        for effect in self.__effects:
            effect.activate(character)
            if effect.is_finished():
                self.remove(effect)

    def contains(self, cls) -> bool:
        return any(isinstance(effect, cls) for effect in self.__effects)

    def clear(self) -> None:
        for effect in self.__effects:
            self.__effects.remove(effect)

    def get_effect(self, effect) -> Effect:
        return next(filter(lambda x: type(x) == effect,  self.__effects))

    def stats_effects(self) -> iter:
        return filter(lambda effect: effect.TYPE in ("BUFF STATS", "DEBUFF STATS"), self.__effects)

    def contains_stats_effect(self) -> bool:
        return any((effect.TYPE in ("BUFF STATS", "DEBUFF STATS") for effect in self.__effects))