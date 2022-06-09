class Location:
    def __init__(self, name, description, sizeX, sizeY):
        self.name = name
        self.description = description
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.playerX = 0
        self.playerY = 0

    def __str__(self):
        return self.name

    def move_player(self, direction):
        if direction == "north":
            if self.playerY > 0:
                self.playerY -= 1
        elif direction == "south":
            if self.playerY < self.sizeY:
                self.playerY += 1
        elif direction == "east":
            if self.playerX < self.sizeX - 1:
                self.playerX += 1
        elif direction == "west":
            if self.playerX > 0:
                self.playerX -= 1
        else:
            print("Invalid direction")

        print("You have moved {}".format(direction))
        print(f"You are now at {self.playerX}, {self.playerY}")


class StartForest(Location):
    def __init__(self):
        super().__init__("Start Forest", "A small forest that you start in.", 5, 5)
        self.playerX = 0
        self.playerY = 0
