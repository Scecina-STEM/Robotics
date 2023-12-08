# Global imports
import os
import re
# Local imports
from SaveData import *
from Items import Item
from Level import Level
import _Runtime

def SetupGame(map_name:str) -> None:
    print("lol")
    map_data = MapData(map_name)
    # Create a new save directory
    while True:
        print("Save name (alphanumerical only):")
        save_name:str = input("> ")
        save_dir:str = f"./savedata/{map_data.map_key}-{save_name}/"
        if os.path.isdir(save_dir):
            print("Warning: cannot override existing save")
        else:
            print("Creating save location")
            os.mkdir(save_dir)
            break
    # Setup the save data
    print("Setting up save...\nCharacter name:")
    character_name:str = input("> ")
    save_data:dict = {
        "Path": save_dir,
        "Level": 0,
        "CharacterName": character_name,
        "SaveState": {
            "Health": map_data.d_health,
            "ArmourClass": map_data.d_armour_class,
            "Inventory": [],
            "Requirements": map_data.d_requirements
        }
    }
    # Fill inventory
    with open(f"./mapdata/{map_name}/items.json", "r") as file:
        items:dict = json.loads(file.read())
        for item in map_data.d_inventory:
            item_frame = items[item['ItemID']]
            item_obj = Item(item['ItemID'], item['Name'], item_frame['Type'], item_frame['Meta'])
            for i in range(0, item['Count']):
                save_data['SaveState']['Inventory'].append(item_obj)
    # Settup RAM data
    _Runtime.GamePath = save_dir
    _Runtime.Level = 0
    _Runtime.CharacterName = character_name
    _Runtime.Health = save_data['SaveState']['Health']
    _Runtime.ArmourClass = save_data['SaveState']['ArmourClass']
    _Runtime.Requirements = save_data['SaveState']['Requirements']
    _Runtime.Inventory = save_data['SaveState']['Inventory']
    # Run Save
    SaveDataFuncts.save()
    #TODO: move onto playnig the game
    input("Press 'enter' to continue...")
    StartGame(f"{map_data.map_key}-{save_name}")

def StartGame(save_name) -> None:
    print("Lol")
    save_re = re.search(r"([\w]*)-([\w]*)", save_name)
    map_data = MapData(save_re.group(1))
    save_data = SaveData(save_name)
    save_data.pushToRuntime()
    # Loop levels
    lvl_i = 1
    while True:
        lvl:Level = Level(lvl_i)
        next:int = lvl.runLevel()
        lvl_i = next
        pass