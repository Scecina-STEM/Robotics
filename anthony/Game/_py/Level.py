# Global Imports
import json
import re
# Local Imports
import _Runtime
from Console import say
from SoaL import soal

# Classes
class Level:
    def __init__(self, number:int) -> None:
        map_name:str = (re.search(r"([\w]*)-([\w]*)", _Runtime.GamePath)).group(1)
        with open(f"./mapdata/{map_name}/levels/{number}.soal", 'r') as file:
            level_data = soal.loads(file.read())
        self.name = level_data['name']
        self.lines = {}
        for line_name in level_data['contents'].keys():
            line_data = level_data['contents'][line_name]
            self.lines[line_name] = Level.Line(line_data)
        pass

    def runLevel(self) -> int:
        line_index:str = "1"
        while True:
            res:str = self.lines[line_index].runLine()
            if res[0] == 'g':
                pass
            else:
                line_index = res
        

    class Line:
        def __init__(self, data:dict) -> None:
            self.text = data['text']
<<<<<<< HEAD
            self.type = data['type']
            self.speaker = data['speaker']
=======
>>>>>>> 1653635 (Anthony (#8))
            self.options = [ ]
            for opt in data['options']:
                self.options.append(Level.Line.Option(opt))
            pass

        def runLine(self) -> str:
<<<<<<< HEAD
            if self.type == "dialog":
                say(f"{self.speaker}: \"{self.text}\"")
            else:
                say(self.text)

            i = 1
            cont = False
            for opt in self.options:
                if opt.type == "continue":
                    cont = True
                    break
                else:
                    say(f"[{i}] {opt.text}", 1)
                i=i+1
            if not cont:
                togo:str = int(input("> "))
                return self.options[togo-1].goto
            else:
                return self.options[0].goto
=======
            say(self.text)
            i = 1
            for opt in self.options:
                say(f"[{i}] {opt.text}", 1)
                i=i+1
            togo:str = int(input("> "))
            return self.options[togo-1].goto
>>>>>>> 1653635 (Anthony (#8))

        class Option:
            def __init__(self, data) -> None:
                if data['type'] == 'dialog':
                    self.text = f"\"{data['text']}\""
<<<<<<< HEAD
                elif data['type'] == 'action':
                    self.text = data['text']
                else:
                    self.text = ""
=======
                else:
                    self.text = data['text']
>>>>>>> 1653635 (Anthony (#8))
                self.type = data['type']
                self.goto = data['goto']
                pass