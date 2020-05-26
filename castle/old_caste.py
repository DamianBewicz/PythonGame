from castle.castle import Castle
from merchants.alchemist import Alchemist
from merchants.armourer import Armourer
from merchants.blacksmith import Blacksmith
from merchants.enchanter import Enchanter
from merchants import AmateurArmourer, AmateurBlacksmith, AmateurEnchanter, AmateurAlchemist


class OldCastle(Castle):
    ARMOURER: Armourer = AmateurArmourer()
    BLACKSMITH: Blacksmith = AmateurBlacksmith()
    ENCHANTER: Enchanter = AmateurEnchanter()
    ALCHEMIST: Alchemist = AmateurAlchemist()
    REQUIRED_STORY_LINE: int = 2
