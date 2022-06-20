import random


class Item:
    def __init__(self, name, description, stack_size):
        self.name = name
        self.description = description
        self.stack_size = stack_size
        self.amount = 1

    def __str__(self):
        return self.name

    def is_stackable(self):
        return self.stack_size > 1


###########
# weapons #
###########

class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description, 1)
        self.damage = damage

    def attack(self):
        return self.damage


class Stick(Weapon):
    def __init__(self):
        super().__init__("Stick", "A simple stick.", 1)

    def special_attack(self):
        return self.damage * 2


class SpunkStick(Weapon):
    def __init__(self):
        super().__init__("SpunkStick", "A simple spunky stick (murder harry fenton).", 1)

    def special_attack(self):
        return self.damage * 10


class WoodenSword(Weapon):
    def __init__(self):
        super().__init__("Wooden Sword", "A basic wooden sword.", 10)

    def special_attack(self):
        return self.damage * 3


class StoneSword(Weapon):
    def __init__(self):
        super().__init__("Stone Sword", "A basic stone sword.", 12)

    def special_attack(self):
        return self.damage * 3


###############
# Other items #
###############
class Potion:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def effect(self):
        pass


class HealthPotion(Potion):
    def __init__(self, player):
        super(HealthPotion, self).__init__("Health Potion", "A potion that heals you when used.")
        self.player = player

    def effect(self):
        self.player.health = 100
        print("You have been healed to full health!")


###################
# Loot Generation #
###################

class LootSet:
    def __init__(self, chest_type):
        self.chest_type = chest_type

    def generate_loot(self):
        pass


class CrapLoot(LootSet):
    def __init__(self, player):
        super(CrapLoot, self).__init__("Crap Chest")
        self.player = player

    def generate_loot(self):
        loot_array = []
        for i in range(3):
            num = random.randint(1, 3)
            if num == 1:
                loot_array.append(Stick())
            elif num == 2:
                loot_array.append(WoodenSword())
            else:
                loot_array.append(HealthPotion(self.player))

        return loot_array


item_list = {"Stick": Stick, "Wooden Sword": WoodenSword, "Stone Sword": StoneSword, "SpunkStick": SpunkStick,
         "Health Potion": HealthPotion}
