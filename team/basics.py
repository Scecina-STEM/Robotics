# This is Basics, a bunch of functions that I use a lot.
# These are open for anynoe to use, and modify.
# I do not garentee that user modifications will work.
# Enjoy!

### Imports ###
# Global #
import sys
import re
# Local #

### Main Class ###
class Basics:

    ### Terminal Functions ###
    class Terminal:

        class Arguments:
            def __init__(self, *, removeDashInit:bool=False, specInterp:bool=False) -> None:
                self.arguments:dict = self.getArgumentsSpec()

            def getArguments(self, *, removeDash:bool=False) -> dict:
                """*Do not use. Use getArgumentsSpec() instead*

                Get the arguments and turn them into a key-pair dict. 
                This will take double dash flags and assign them as keys, 
                and the value immediatly after will be its value.

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
            
            def getArgumentsSpec(self) -> dict:
                """Returns a dictionary of double dashed terminal arguments with their value after. 
                Supports single flags, as well as multiple arguments as list for a flag.
                
                Args:
                    [removeDash:bool] = remove the two hyphens before the key name

                Returns:
                    A dictionary containg the args and their values.
                """
                sys_arguments:list = sys.argv; sys_arguments.pop(0)

                arg_list:str = ""
                for arg in sys_arguments:
                    if re.match(r"^--", arg) != None:
                        arg_list += f'\n{arg}'
                    else:
                        arg_list += f' {arg}'

                args:dict = {}
                for line in arg_list.split('\n'):
                    if line == '': continue
                    items:list = line.split(' ')
                    match len(items):
                        case 1:
                            args[items[0]] = None
                        case 2:
                            args[items[0]] = items[1]
                        case _:
                            args[items[0]] = items[1:]
                return args
            
            def find(self, index:str) -> str|list|bool|None:
                """This function will find the value for a key, returning None if the value is not found.
                Single flag arguments will return True.
                
                Args:
                    index:str = the name of the key to look for
                """
                for key in list(self.arguments.keys()):
                    if key == index:
                        if self.arguments[key] != None:
                            return self.arguments[key]
                        else:
                            return True
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