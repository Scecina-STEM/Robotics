# Global Imports
import re
import json
# Local Imports

#^{(.+)}\n([\w\W]+){end}$
#^\[([a-z0-9]*)\](.+)\n([\w\W]+?)---$
#^ +\[(\w+).(\w+)\](.*)$

def log(msg:any) -> None:
    if True:
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
        se_pattern = r"^\[([a-z0-9]*)\](.+)\n([\w\W]+?)---$"
        sections = re.finditer(se_pattern, body, re.MULTILINE)
        log(sections)
        contents = {}
        for matchNum, match in enumerate(sections, start=1):
            log(matchNum)
            log(match)
            se_parts = match
            line_id = se_parts.group(1)
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
                    "type": "",
                    "goto": op.group(2)
                }
                match op.group(1):
                    case 'd': option['type'] = "dialog"
                    case 'a': option['type'] = "action"
                line['options'].append(option)

            contents[line_id] = line
        tore = {
            "name": "",
            "contents": contents
        }
        print(json.dumps(tore))
        return tore