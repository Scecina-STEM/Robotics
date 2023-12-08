# Global Imports
import tomllib
import json
# Local Imports
import _Runtime
from Items import Item

#classes
class SaveData:
    def __init__(self, save_name) -> None:
        with open(f"./savedata/{save_name}/save.json", 'r') as file:
            sd = json.loads(file.read())
        self.path = sd['Path']
        self.level = sd['Level']
        self.character_name = sd['CharacterName']
        self.health = sd['SaveState']['Health']
        self.armour_class = sd['SaveState']['ArmourClass']
        self.requirements = sd['SaveState']['Requirements']
        self.inventory = []
        for item in sd['SaveState']['Inventory']:
            it = Item(item['id'], item['name'], item['type'], item['meta'])
            self.inventory.append(it)
        pass

    def pushToRuntime(self) -> None:
        _Runtime.GamePath = self.path
        _Runtime.Level = self.level
        _Runtime.CharacterName = self.character_name
        _Runtime.Health = self.health
        _Runtime.ArmourClass = self.armour_class
        _Runtime.Requirements = self.requirements
        _Runtime.Inventory = self.inventory

class SaveDataFuncts:
    def save():
        save_data:dict = {
            "Path": _Runtime.GamePath,
            "Level":_Runtime.Level,
            "CharacterName": _Runtime.CharacterName,
            "SaveState": {
                "Health": _Runtime.Health,
                "ArmourClass": _Runtime.ArmourClass,
                "Inventory": [],
                "Requirements": _Runtime.Requirements
            }
        }
        for item in _Runtime.Inventory:
            save_data['SaveState']['Inventory'].append(dict(item))
        
        with open(f"{save_data['Path']}save.json", 'w') as file:
            file.write(json.dumps(save_data, indent=4))
        pass

class MapData:
    def __init__(self, map_name:str) -> None:
        # GET map config
        with open(f"mapdata/{map_name}/config.toml") as file:
            map_data = tomllib.loads(file.read())
        self.map_name = map_data['map_name']
        self.map_key = map_data['map_key']
        self.map_version = map_data['map_version']
        # GET default character
        with open(f"mapdata/{map_name}/character.json") as file:
            char_data = json.loads(file.read())
        self.d_health = char_data['Stats']['Health']
        self.d_armour_class = char_data['Stats']['ArmourClass']
        self.d_inventory = char_data['Level0']['Inventory']
        self.d_requirements = char_data['Level0']['Requirements']
        pass