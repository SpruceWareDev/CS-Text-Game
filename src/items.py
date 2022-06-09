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


##########
# weapons#
##########

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
