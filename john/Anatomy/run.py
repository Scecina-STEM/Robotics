import os

os.system("rm -rf images/")
os.mkdir("./images/")

os.system("python latexgen.py")

if input("latex gen?(y/n)") == "y":
    os.system("lualatex output.tex")
    os.system("rm output.aux | rm output.log")