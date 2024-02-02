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
\\usepackage{fancyhdr}

\\usepackage{fontspec}
\\setmainfont{QTChanceryType}

% Set up fancy headers
\\pagestyle{fancy}
\\fancyhf{}
\\renewcommand{\\headrulewidth}{0pt}

% Define a command to create a card with question, answer, and additional text
\\newcommand{\\mycard}[3]{
    \\fbox{%
        \\begin{minipage}[t][3.5in][t]{2.5in}
            \\vfill
            \\centering{\\fontsize{15}{17}\\selectfont #1}
            \\vfill
            \\centering{\\fontsize{15}{17}\\selectfont #2}
            \\vfill
            \\centering\\textbf{#3}
        \\end{minipage}
    }
    \\vspace{0.5in}
}

% Define a command to create a card with only an image
\\newcommand{\\imagecard}[1]{
    \\fbox{%
        \\begin{minipage}[t][3.5in][t]{2.5in}
            \\vspace*{\\fill}
            \\centering\\includegraphics[width=2in, height=2in, keepaspectratio]{#1}
            \\vspace*{\\fill}
        \\end{minipage}
    }
    \\vspace{0.5in}
}

\\begin{document}\\centering
"""

# Use the mycard and imagecard commands for each set of six cards
data = data[1:]
for i in range(0, len(data), 4):
    cards = data[i:i+4]

    # Odd page with text
    latex_content += "\\newpage\n"
    latex_content += "\\vfill\n"  # Center the cards vertically
    for card in cards:
        question = card[0]
        answer = card[1]
        static_text = "Chess: Civil War Addition"
        latex_content += f"\\mycard{{{question}}}{{{answer}}}{{{static_text}}}\n"
    latex_content += "\\vfill\n"

    # Even page with image (replace 'path/to/image' with the actual path to your image file)
    latex_content += "\\newpage\n"
    latex_content += "\\vfill\n"  # Center the cards vertically
    for _ in range(4):
        image_path = 'images/ccwalogo.png'  # Replace with the path to your image file
        latex_content += f"\\imagecard{{{image_path}}}\n"
    latex_content += "\\vfill\n"

latex_content += "\\end{document}"

# Save LaTeX content to a .tex file
with open('output.tex', 'w') as texfile:
    texfile.write(latex_content)

print("LaTeX file generated: output.tex")
