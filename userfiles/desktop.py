import os, sys, time, runpy, signal, psutil, readline
readline
import psutil
from pathlib import Path
readline.set_history_length(256)

# Set Ctrl+C Output to Nothing
signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

os.system("clear")
print("""██████╗ ██╗   ██╗██╗     ██╗████████╗███████╗ ██████╗ ███████╗
██╔══██╗╚██╗ ██╔╝██║     ██║╚══██╔══╝██╔════╝██╔═══██╗██╔════╝
██████╔╝ ╚████╔╝ ██║     ██║   ██║   █████╗  ██║   ██║███████╗
██╔═══╝   ╚██╔╝  ██║     ██║   ██║   ██╔══╝  ██║   ██║╚════██║
██║        ██║   ███████╗██║   ██║   ███████╗╚██████╔╝███████║
╚═╝        ╚═╝   ╚══════╝╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚══════╝
""")                                                              
os.chdir(os.path.dirname(os.path.abspath(__file__)))

username = str(Path().absolute()).split("/")[-1]
try:
    password = open("password.pwd", "r").read()
except FileNotFoundError:
    pass

while True:
    print("""[1] Browser
[2] Terminal
[3] Files
[4] Calculator
[5] Text Editor
[6] Settings
[exit] Exit
""")
    option = input("[]: ")
    if option == "1":
        #os.system("cls" if os.name == "nt" else "clear")
        os.system("w3m https://html.duckduckgo.com/html")
    elif option == "2":
        runpy.run_path(path_name="terminal.py")
    elif option == "3":
        runpy.run_path(path_name="files.py")
    elif option == "4":
        runpy.run_path(path_name="calculator.py")
    elif option == "5":
        os.system("cls" if os.name == "nt" else "clear")
        os.system("nano")
    elif option == "6":
        runpy.run_path(path_name="settings.py")
    elif option == "exit":
        os.system("su -c \"shutdown -h now\"")
    else:
        print("Invalid Option.")

