from enums import AttackType, MagicNature


class DamageObject:
    def __init__(self, dmg: int, attack_type: AttackType = None, source: MagicNature = None) -> None:
        self.dmg = dmg
        self.attack_type = attack_type
        self.source = source
