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

    def handle_location_command(self, command, args):
        if command == "help":
            print("""
            You can use the following location commands:
            You can use the 'move' command followed by 'north', 'east', 'south' or 'west' to move around.
            You can also use the command 'help' to see what commands you can run (this menu).
            """)
        elif command == "move":
            if len(args) < 1:
                print("Invalid command. You must add a direction to move. If not sure type 'location help'.")
            else:
                self.move_player(args[0])
        else:
            print("Invalid command")


class StartForest(Location):
    def __init__(self):
        super().__init__("Start Forest", "A small forest that you start in.", 5, 5)
        self.playerX = 0
        self.playerY = 0
