# Global Imports
import re
import json
# Local Imports

#^{(.+)}\n([\w\W]+){end}$
#^\[([a-z0-9]*)\](.+)\n([\w\W]+?)---$
#^ +\[(\w+).(\w+)\](.*)$

def log(msg:any) -> None:
<<<<<<< HEAD
    if False:
=======
    if True:
>>>>>>> 1653635 (Anthony (#8))
        print(msg)

# Classes
class soal:
    def loads(input:str) -> dict:
        log(f"Using the following:\n{input}")
        #break into header and body
        hb_pattern = r"{(.+)}\n([\w\W]+){end}"
        head_body = re.search(hb_pattern, input)
        #TODO parse the header
        body = head_body.group(2)
<<<<<<< HEAD
        se_pattern = r"^\[([a-z0-9]*).([\w]+).([\w ]*)\](.+)\n([\w\W]+?)---$"
=======
        se_pattern = r"^\[([a-z0-9]*)\](.+)\n([\w\W]+?)---$"
>>>>>>> 1653635 (Anthony (#8))
        sections = re.finditer(se_pattern, body, re.MULTILINE)
        log(sections)
        contents = {}
        for matchNum, match in enumerate(sections, start=1):
            log(matchNum)
            log(match)
            se_parts = match
            line_id = se_parts.group(1)
<<<<<<< HEAD
            line_text = se_parts.group(4)

            line = {
                "text": line_text.strip(),
                "speaker": match.group(3),
                "type": "",
                "options": [ ]
            }
            match match.group(2):
                case 'd': line['type'] = "dialog"
                case 'a': line['type'] = "action"

            options_text = se_parts.group(5)
            op_pattern = r"^ +\[(\w+).(\w+)\](.*)$"
            for matchNum, op in enumerate(re.finditer(op_pattern, options_text, re.MULTILINE), start=1):
                option = {
                    "text": (op.group(3)).strip(),
=======
            line_text = se_parts.group(2)

            line = {
                "text": line_text,
                "options": [ ]
            }

            options_text = se_parts.group(3)
            op_pattern = r"^ +\[(\w+).(\w+)\](.*)$"
            for matchNum, op in enumerate(re.finditer(op_pattern, options_text, re.MULTILINE), start=1):
                option = {
                    "text": op.group(3),
>>>>>>> 1653635 (Anthony (#8))
                    "type": "",
                    "goto": op.group(2)
                }
                match op.group(1):
                    case 'd': option['type'] = "dialog"
                    case 'a': option['type'] = "action"
<<<<<<< HEAD
                    case 'c': line['type'] = "continue"
                    case 'n': line['type'] = "next"
=======
>>>>>>> 1653635 (Anthony (#8))
                line['options'].append(option)

            contents[line_id] = line
        tore = {
            "name": "",
            "contents": contents
        }
<<<<<<< HEAD
        log(json.dumps(tore))
=======
        print(json.dumps(tore))
>>>>>>> 1653635 (Anthony (#8))
        return tore