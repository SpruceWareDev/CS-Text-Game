from player import Player
import login
import random
from utils import typing_effect

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
    typing_effect("Welcome to the game!", 0.05)


def tutorial():
    typing_effect("Welcome to the tutorial!", 0.05)


game_menu()
