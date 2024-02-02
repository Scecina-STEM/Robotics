### Imports ###
## Global ##
import csv
import urllib.request
import re
## Local ##

# card: 28mm x 49 mm

latex = """
\\documentclass[letterpaper]{article}
\\usepackage[margin=0.5in]{geometry}
\\usepackage{graphicx}

\\newcommand{\\mycard}[2]{
    \\fbox{
        \\begin{minipage}[t][49mm][t]{28mm}
            \\centering{\\fontsize{15}{17}\\selectfont #1}
            \\vspace*{\\fill}
            \centering\includegraphics[width=28mm, height=49mm, keepaspectratio]{#2}
            \\vspace*{\\fill}
        \\end{minipage}
    }
    \\vspace{0.5in}
}

\\begin{document}\\centering
"""

### CODE ###
with open("organs.csv", "r") as f:
    reader = csv.reader(f)
    csvS = list(reader)[1:]

for line in csvS:
    print(line)
    # get the file type
    hd_link:str
    try:
        match = re.search(r"\.([a-zA-z]+)$", line[2])
        print(match.group(1))
        hd_link = './images/' + line[0] + '.' + match.group(1)
        urllib.request.urlretrieve(line[2], hd_link)
    except:
        print(f"Can't download {hd_link}")
    latex += f"\\mycard{{{line[1]}}}{{{hd_link}}}\n"

latex += "\\end{document}"

with open("output.tex", "w") as f:
    f.write(latex)