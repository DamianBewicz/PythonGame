from typing import Type
from random import randint
from effects.bleed import Bleed
from ..enemies import Enemy
from .player import Player
from skills.knight_skills import Berserker, BloodySlice, BattleShout

T_PHYSICAL = 'PHYSICAL'


class Atak:
    def __init__(self, attacker: Player, dmg: int, type_: 'str' = T_PHYSICAL):
        self.attacker = attacker
        self.dmg = dmg
        self.type = type_


class Knight(Player):
    NAME = "Rycerz"

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.name = name
        self._max_dmg = 15
        self._min_dmg = 10
        self._max_hp = 80
        self._max_mana = 20
        self._hp = 80
        self._mana = 20
        self.rest_hp_rate = 20
        self.rest_mana_rate = 5
        self.skills = [
            (Berserker()),
            (BloodySlice()),
            (BattleShout()),
        ]

    # def zadaj_obrazenia(self, atak: Atak):
    #     if atak.type_ == T_PHYSICAL and self.has_fire_shied():
    #         atak.attacker.zadaj_obrazenia(Atak(attacker=self, dmg=atak.dmg*0.5))
    #     self.__hp -= atak.dmg


k = Knight('asdf')
k.__hp = 40

