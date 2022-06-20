from player import Player
import login
import random
from utils import typing_effect
import location
import save_load


def game_menu():
    # Login system
    login.login_menu()

    print("""
    1. Play
    2. Load Previous Game
    3. Tutorial
    4. Quit
    """)
    choice = input("> ")
    if choice == "1":
        game()
    elif choice == "2":
        load_previous_game()
    elif choice == "3":
        tutorial()
    elif choice == "4":
        quit()
    else:
        print("Invalid choice")
        game_menu()


def game():
    typing_effect("Welcome to the game!", 0.05)
    typing_effect("You will start by creating a player.", 0.05)
    player_name = input("Enter a name for your player: ")
    # create the player
    player = Player(player_name)
    typing_effect("You have created a player named {}".format(player.name), 0.05)

    # starts in the forest
    current_location = location.StartForest(player)
    current_location.set_chest_data(current_location.max_chests)
    typing_effect("You have entered the {}".format(current_location.name), 0.05)
    typing_effect(f"The location you have entered is {current_location.sizeX} by {current_location.sizeY}.", 0.05)
    typing_effect("You can use the command 'help' to see what commands you can run..", 0.05)

    # run the main game loop
    game_loop(player, current_location)


def game_loop(player, current_location):
    playing = True
    # command system for the game
    # controls basically everything in the game
    # might improve this later with classes or something
    while playing:
        command = input("> ")
        split_command = command.split(" ")
        # help command prints out all the commands you can use
        if split_command[0] == "help":
            print("""
                You can use the following commands:
                You can use the 'location' command to do all location actions. For help type 'location help'.
                You can also use the command 'help' to see what commands you can run.
                You can also use the command 'inventory' to see what items you have.
                You can also use the command 'quit' to quit the game.
                """)
        # location command handles location commands like movement and help
        elif split_command[0] == "location":
            # checks if the player has entered a command
            if len(split_command) < 2:
                print("Invalid command. You must add a location command. If not sure type 'location help'.")
            else:
                current_location.handle_location_command(split_command[1], split_command[2:])
        # inventory command prints out all the items the player has
        elif split_command[0] == "inventory":
            print("You have the following items:")
            for item in player.get_inventory():
                print(f"- {item.name} - {item.description}")
        # quit command quits the game
        elif split_command[0] == "quit":
            # test save functionality
            save_load.save_game_data(player, current_location)
            playing = False
        else:
            print("Invalid command")


def tutorial():
    # tutorial but its not done bc i want a game first XD
    typing_effect("Welcome to the tutorial!", 0.05)


def load_previous_game():
    # loads previous game data from game files
    player, location = save_load.load_game_data()

    # print to notify the user
    print(f"You have loaded {player.name} from the previous game.")
    print(f"You have loaded into {location.name}.")

    # passes loaded data to the game loop
    game_loop(player, location)


game_menu()
