class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.health > 0

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def get_inventory(self):
        return self.inventory
