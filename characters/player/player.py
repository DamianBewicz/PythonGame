from math import floor
from characters.character import Character
from enums import EquipmentSections, AttackType
from eq import Equipment
from settings import MAX_DEFENSE
from termcolor import colored


class NoManaException(Exception):
    pass


class HasMovedException(Exception):
    pass


class Player(Character):
    CLASS_NAME = NotImplemented

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.rest_hp = NotImplemented
        self.rest_mana = NotImplemented
        self.skills = NotImplemented
        self.equipment = Equipment(self.CLASS_NAME)
        self.actions = (
            "Zwykły atak",
            "Umiejętność",
            "Odpoczynek",
            "Plecak",
        )

    def take_dmg(self, dmg_object) -> None:
        try:
            resistance_from_items = self.equipment.magic_resistance.get_value(dmg_object.source) / 200
            magic_source_resistance = 1
            self.hp -= floor(dmg_object.dmg * (magic_source_resistance - resistance_from_items))
        except (KeyError, AttributeError):
            physical_dmg_resistance = 1
            total_armor = self.equipment.defense.amount
            total_dmg_resistance = physical_dmg_resistance - total_armor / MAX_DEFENSE / 2
            try:
                shield = self.equipment.personal_items.get_item(EquipmentSections.SHIELD.value)
                if shield.has_blocked():
                    print(colored("\nAtak został zablokowany!\n", "green"))
                else:
                    self.hp -= floor(dmg_object.dmg * total_dmg_resistance)
            except AttributeError:
                self.hp -= floor(dmg_object.dmg * total_dmg_resistance)

    def rest(self) -> None:
        self.hp += self.rest_hp
        self.mana += self.rest_mana
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        if self.mana > self.max_mana:
            self.mana = self.max_mana
        raise HasMovedException

    def introduce_actions(self) -> None:
        for number, action in enumerate(self.actions, start=1):
            print(number, action)

    def perform_action(self, character) -> None:
        if not self.cant_move():
            while True:
                actions = {
                    "1": self.attack.perform,
                    "2": self.perform_skill,
                    "3": self.rest,
                    "4": self.equipment.backpack.use_item_during_combat
                }
                self.introduce_actions()
                try:
                    choice = input("\nWybierz akcję\n")
                    print()
                    action = actions[choice]
                    if choice == "1":
                        action(character)
                        raise HasMovedException
                    elif choice == "2":
                        action(character)
                    elif choice == "3":
                        action()
                    else:
                        action(self)
                except HasMovedException:
                    break
                except KeyError:
                    print("\nPodana wartość jest nieprawidłowa\n")
                except NoManaException:
                    print("\nBrakuje many\n")

    def perform_skill(self, character) -> None:
        while True:
            chosen_skill = self.skills.choose()
            if chosen_skill is None:
                break
            else:
                if self.has_mana(chosen_skill):
                    self.lose_mana(chosen_skill.mana_cost)
                    if chosen_skill.TYPE in (AttackType.BUFF, AttackType.HEAL):
                        chosen_skill.perform(self)
                    else:
                        chosen_skill.perform(character)
                    raise HasMovedException
                raise NoManaException

    def reset(self) -> None:
        self.hp = self.max_hp
        self.mana = self.max_mana
        self.effects.clear()
