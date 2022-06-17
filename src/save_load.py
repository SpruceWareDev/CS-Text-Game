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
