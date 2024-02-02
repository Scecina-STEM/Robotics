import csv

# Read data from CSV file
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# Create LaTeX file
latex_content = """
\\documentclass[letterpaper]{article}
\\usepackage[margin=0.5in]{geometry}
\\usepackage{graphicx}

\\usepackage{fontspec}
\\setmainfont{QTChanceryType}

\\begin{document}
"""

latex_content += "\\pagestyle{empty}\n"

# Define a command to create a card with question, answer, and additional text, with a black outline
latex_content += """
\\newcommand{\\mycard}[3]{
    \\fbox{%
        \\begin{minipage}[t][3.5in][t]{2.5in}
            \\centering{\\fontsize{15}{17}\\selectfont #1}
            \\vfill
            \\centering{\\fontsize{15}{17}\\selectfont #2}
            \\vfill
            \\centering\\textbf{Chess: Civil War Addition (#3)}
        \\end{minipage}
    }
    \\vspace{0.5in}
}
"""

# Use the mycard command for each row in the CSV
index:int = 1
card_version:str = 'A'
for row in data[1:]:  # Skip header row
    question = row[0]
    answer = row[1]
    ca = f"{card_version}{index}"
    latex_content += f"\\mycard{{{question}}}{{{answer}}}{{{ca}}}\n"
    index = index+1

latex_content += "\\end{document}"

# Save LaTeX content to a .tex file
with open('output.tex', 'w') as texfile:
    texfile.write(latex_content)

print("LaTeX file generated: output.tex")
