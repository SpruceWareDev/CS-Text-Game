import os

FILE_EXTENSION = ".txt"


def save_game_data(player, location):
    # check if game data folder exists
    if not os.path.isdir("gamedata"):
        os.mkdir("gamedata")

    # save players inventory
    inventory_file = open(f"gamedata/inventory{FILE_EXTENSION}", "w")
    for item in player.inventory:
        inventory_file.write(item.name + ",")
    inventory_file.close()

    # save other player info
    player_file = open(f"gamedata/player{FILE_EXTENSION}", "w")
    player_file.write(f"{player.name},{player.health}")
    player_file.close()

    # save location data
    location_file = open(f"gamedata/location{FILE_EXTENSION}", "w")
    location_file.write(f"{location.name},{location.sizeX},{location.sizeY},{location.playerX},{location.playerY}")
    location_file.close()
