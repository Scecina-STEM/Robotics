# Built in python 3.11, check for incapatibility
# TODO look for python version

# Global Imports

# Local Imports
from RunGame import *

options:str = """Welcome to Python Sequence of Adventure!
Choose your path:
[1] Start Game
[2] Resume Game
[3] Installed Maps"""
print(options)
choice:str = input("> ")
match choice:
    case '1':
        print("So you have chosen...\nSelect a map to use")
        #SetupGame
        with open("mapdata/games") as file:
            for game in file.read().split('\n'):
                print(f"    {game}")
        chosen_game = input("> ")
        SetupGame(chosen_game)
    case '2':
        print("So you have chosen...\nSelect a save to load")
        for save in os.scandir("./savedata/"):
            print(f"    {save.name}")
        chosen_save = input("> ")
        StartGame(chosen_save)
    case '3':
        print()