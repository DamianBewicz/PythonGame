from enums import MagicNature


class DamageObject:
    def __init__(self, dmg: int, attack_type: str = None, source: MagicNature = None) -> None:
        self.dmg: int = dmg
        self.attack_type: str = attack_type
        self.source: str = source
