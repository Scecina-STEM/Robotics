#imports
import tomllib

#class
class SaveData:
    def __init__(self, save_name:str) -> None:
        self.map_name = ""
        
        pass

class MapData:
    def __init__(self, map_name:str) -> None:
        with open(f"mapdata/{map_name}/config.toml") as file:
            map_data = tomllib.loads(file.read())
        print(map_data)
        self.map_name = map_data['map_name']
        self.map_key = map_data['map_key']
        self.map_version = map_data['map_version']
        pass