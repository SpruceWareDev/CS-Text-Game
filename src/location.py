import random
import items


class Location:
    def __init__(self, player, name, description, sizeX, sizeY):
        self.name = name
        self.description = description
        self.player = player
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
            You can also use the command 'search' to search the location you are currently in.
            """)
        elif command == "move":
            if len(args) < 1:
                print("Invalid command. You must add a direction to move. If not sure type 'location help'.")
            else:
                self.move_player(args[0])
        elif command == "search":
            self.search_location()
        else:
            print("Invalid command")

    def search_location(self):
        print("Nothing to search here.")


class StartForest(Location):
    def __init__(self, player):
        super().__init__(player, "Start Forest", "A small forest that you start in.", 10, 10)
        self.playerX = 0
        self.playerY = 0

    def search_location(self):
        print("You are searching the current area.")
        num = random.randint(1, 10)
        if num == 1:
            found_item = items.Stick()
            print(f"You have found a {found_item.name}!")
            self.player.add_item(found_item)
        elif num == 2:
            found_item = items.WoodenSword()
            print(f"You have found a {found_item.name}!")
            self.player.add_item(found_item)
        else:
            print("You found nothing.")
