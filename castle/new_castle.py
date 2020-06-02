from castle.castle import Castle
from merchants.alchemist import Alchemist
from merchants.armourer import Armourer
from merchants.blacksmith import Blacksmith
from merchants.enchanter import Enchanter
from merchants import ExperiencedAlchemist, ExperiencedBlacksmith, ExpieriencedArmourer, ExperiencedEnchanter


class NewCastle(Castle):
    ARMOURER: Armourer = ExpieriencedArmourer()
    BLACKSMITH: Blacksmith = ExperiencedBlacksmith()
    ENCHANTER: Enchanter = ExperiencedEnchanter()
    ALCHEMIST: Alchemist = ExperiencedAlchemist()
    REQUIRED_LEVEL: int = 3
