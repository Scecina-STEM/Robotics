# This is Basics, a bunch of functions that I use a lot.
# These are open for anynoe to use, and modify.
# I do not garentee that user modifications will work.
# Enjoy!

### Imports ###
# Global #
import sys
# Local #

### Main Class ###
class Basics:

    ### Terminal Functions ###
    class Terminal:

        class Arguments:
            def __init__(self, *, removeDashInit:bool=False) -> None:
                self.arguments:dict = self.getArguments(removeDash=removeDashInit)

            def getArguments(self, *, removeDash:bool=False) -> dict:
                """Get the arguments and turn them into a key-pair dict. This will take double dash flags and assign them as keys, and the value immediatly after will be its value. Example:
                
                python main.py --foo bar --file ../file_location
                
                return: {"--foo": "bar", "--file": "../file_location"}

                Args:
                    removeDash:bool = remove the two hyphens before the key name
                """
                arguments:list = sys.argv
                arguments.pop(0)
                argu_pairs = [(arguments[i], arguments[i+1]) for i in range(0, len(arguments), 2)]
                to_return:dict = {}
                for pair in argu_pairs:
                    if removeDash:
                        to_return[pair[0].replace("-", "")] = pair[1]
                    else:
                        to_return[pair[0]] = pair[1]
                return to_return
            
            def find(self, index:str) -> str|None:
                """This function will find the value for a key, returning None if the value is not found.
                
                Args:
                    index:str = the name of the key to look for
                """
                for key in list(self.arguments.keys()):
                    if key == index:
                        return self.arguments[key]
                return None
            
            def run(self, index:str, function) -> None:
                """This function will look for an index, then if found, run a function with it.

                Args:
                    index:str = the name of the keus to look for
                    function = a function to run. Should only have 1 input, that will be the index's value.

                Returns:
                    None: function does not have output
                    Any: the output of the function
                """
                if self.find(index) != None:
                    try:
                        return function(self.find(index))
                    except TypeError:
                        raise TypeError("Function input is not callable! (try removing parenthesis)")
                else:
                    raise self.ArgumentNotFound(f"Argument not found for \"{index}\"")

            class ArgumentNotFound(Exception):
                "Raised when an argument cannot be found"
                pass