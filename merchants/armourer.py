from items.defensive_items import RustyArmor, RustyTrousers, RustyBoots, RustyGloves, RustyHelmet, RustyShield
from merchants.merchant import Merchant


class AmateurArmourer(Merchant):
    ITEMS_PRICES: dict = {
        RustyArmor: 100,
        RustyTrousers: 75,
        RustyShield: 75,
        RustyBoots: 50,
        RustyGloves: 50,
        RustyHelmet: 50,
    }
    MARGIN: float = 0.5
    SHARPEN_PRICE: int = 30
