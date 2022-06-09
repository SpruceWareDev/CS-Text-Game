from player import Player
import login
import random
from utils import typing_effect
import location


def game_menu():
    # Login system
    login.login_menu()

    print("""
    1. Play
    2. Tutorial
    3. Quit
    """)
    choice = input("> ")
    if choice == "1":
        game()
    elif choice == "2":
        tutorial()
    elif choice == "3":
        quit()
    else:
        print("Invalid choice")
        game_menu()


def game():
    playing = True

    typing_effect("Welcome to the game!", 0.05)
    typing_effect("You will start by creating a player.", 0.05)
    player_name = input("Enter a name for your player: ")
    # create the player
    player = Player(player_name)
    typing_effect("You have created a player named {}".format(player.name), 0.05)

    # starts in the forest
    current_location = location.StartForest()
    typing_effect("You have entered the {}".format(current_location.name), 0.05)
    typing_effect("You can move around the map by using the directions north, south, east, and west.", 0.05)
    typing_effect("You can also use the command 'help' to see what commands you can run..", 0.05)

    while playing:
        command = input("> ")
        split_command = command.split(" ")
        # help command prints out all the commands you can use
        if split_command[0] == "help":
            print("""
            You can move around the map by using the move commands followed by [north, east, south, west].
            You can also use the command 'help' to see what commands you can run.
            You can also use the command 'inventory' to see what items you have.
            You can also use the command 'quit' to quit the game.
            """)
        # move command handles moving the player around the current location they are in using compass points
        elif split_command[0] == "move":
            # checks if the player has entered a direction
            if len(split_command) < 2:
                print("Invalid command. You must add a direction to move.")
            else:
                current_location.move_player(split_command[1])
        # inventory command prints out all the items the player has
        elif split_command[0] == "inventory":
            print("You have the following items:")
            for item in player.get_inventory():
                print(item)
        # quit command quits the game
        elif split_command[0] == "quit":
            playing = False
        else:
            print("Invalid command")


def tutorial():
    typing_effect("Welcome to the tutorial!", 0.05)


game_menu()
