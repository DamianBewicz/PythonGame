class HealthPotion:
    hp = NotImplemented
    cost = NotImplemented

    def __repr__(self) -> str:
        return "NotImplemented"

    def use_item(self, player) -> False:
        # Return false, use items makes no round loss
        if player.hp >= player.max_hp:
            print("\nMasz pełne życie!\n")
        else:
            player.hp += self.hp
            if player.hp > player.max_hp:
                player.hp = player.max_hp
        return False


class MinorHealthPotion(HealthPotion):
    hp = 20
    cost = 40

    def __str__(self) -> str:
        return "Mniejsza mikstura zdrowia"


class NormalHealthPotion(HealthPotion):
    hp = 25
    cost = 65

    def __str__(self) -> str:
        return "Mikstura zdrowia"


class GreaterHealthPotion(HealthPotion):
    hp = 35
    cost = 100

    def __str__(self) -> str:
        return "Większa mikstura zdrowia"
