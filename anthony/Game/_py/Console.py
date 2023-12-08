# Global Imports

# Local Imports

# Colors

# Reset
Color_Off='\033[0m'       # Text Reset

# Regular Colors
Black='\033[0;30m'        # Black
Red='\033[0;31m'          # Red
Green='\033[0;32m'        # Green
Yellow='\033[0;33m'       # Yellow
Blue='\033[0;34m'         # Blue
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan
White='\033[0;37m'        # White

# Special Colors

Dark_Gray='\033[1;30m'     # Dark Gray
# Classes

def say(msg:str, indent:int=0, type:int=0) -> None:
    to:str
    match type:
        case 0: to = (msg) # Normal
        case 1: to = (f"{Green}{msg}{Color_Off}") # Added item
        case 2: to = (f"{Red}{Color_Off}{Color_Off}") # Took item
    indent_s:str=""
    for i in range(indent):
        indent_s = indent_s + "   "
    print(f"{indent_s}{to}")