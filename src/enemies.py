import player


class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack_player(self, player):
        player.health -= self.damage

    