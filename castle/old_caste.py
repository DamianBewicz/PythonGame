from castle import Castle
from merchants import Armourer, Blacksmith, Enchanter, AmateurArmourer, AmateurBlacksmith, AmateurEnchanter


class OldCastle(Castle):
    ARMOURER: Armourer = AmateurArmourer()
    BLACKSMITH: Blacksmith = AmateurBlacksmith()
    ENCHANTER: Enchanter = AmateurEnchanter()
    REQUIRED_STORY_LINE: int = 1
