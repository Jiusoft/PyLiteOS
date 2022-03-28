import os, sys, time
from pathlib import Path

os.system("clear")
print("""██████╗ ██╗   ██╗███████╗██╗   ██╗██████╗  ██████╗ ███████╗
██╔══██╗╚██╗ ██╔╝██╔════╝██║   ██║██╔══██╗██╔═══██╗██╔════╝
██████╔╝ ╚████╔╝ ███████╗██║   ██║██████╔╝██║   ██║███████╗
██╔═══╝   ╚██╔╝  ╚════██║██║   ██║██╔══██╗██║   ██║╚════██║
██║        ██║   ███████║╚██████╔╝██████╔╝╚██████╔╝███████║
╚═╝        ╚═╝   ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
""")

os.chdir(Path(__file__).parent)

username = str(Path().absolute()).split("/")[-1]
try:
    password = open("password.pwd", "r").read()
except FileNotFoundError:
    pass

print("""
[1] Browser
[2] Terminal
[3] Calculator
[4] Text Editor
[5] Settings
""")
while True:
    option = int(input("[]: "))
    if option==1:
        pass
    elif option==2:
        pass
    elif option==3:
        os.system("python3 calculator.py")
    elif option==4:
        os.system("vim")