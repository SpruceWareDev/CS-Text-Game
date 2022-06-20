import os
from player import Player
import location
import items

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
    location_file.write(f"{location.name},{location.playerX},{location.playerY},")
    for chest in location.chest_locations:
        location_file.write(f"{chest[0]}/{chest[1]},")
    location_file.close()


def load_game_data():
    if not os.path.isdir("gamedata"):
        return None

    # load inventory
    inventory_file = open(f"gamedata/inventory{FILE_EXTENSION}", "r")
    inventory_data = inventory_file.read()
    inventory_file.close()
    inventory_data = inventory_data.split(",")
    inventory_data.pop()
    inventory = []
    for item in inventory_data:
        inventory.append(get_item(item))

    # load player info
    player_file = open(f"gamedata/player{FILE_EXTENSION}", "r")
    player_data = player_file.read()
    player_file.close()
    player_data = player_data.split(",")
    player = Player(player_data[0])
    player.health = int(player_data[1])
    player.inventory = inventory

    # load location data
    location_file = open(f"gamedata/location{FILE_EXTENSION}", "r")
    location_data = location_file.read()
    location_file.close()
    location_data = location_data.split(",")
    location = get_location(player, location_data[0])
    location.set_player_position(int(location_data[1]), int(location_data[2]))
    location_data.pop()
    for i in range(3, len(location_data)):
        location.chest_locations.append([int(location_data[i].split("/")[0]), int(location_data[i].split("/")[1])])

    # return statement (player, location)
    return player, location


locations = {"Start Forest": location.StartForest}


def get_location(player, location_name):
    return locations[location_name](player)


def get_item(item_name):
    return items.item_list[item_name]()
