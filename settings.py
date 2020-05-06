from items.defensive_items import PlateBoots, IronShield, PlateGloves, PlateTrousers, PlateHelmet, PlateArmor

MOST_VALUABLE_ITEMS = [PlateArmor(), PlateHelmet(), PlateTrousers(), PlateGloves(), PlateBoots(), IronShield()]
MAX_DEFENSE = sum([item.defense for item in MOST_VALUABLE_ITEMS])
MAX_RESISTANCE_VALUE = 200
