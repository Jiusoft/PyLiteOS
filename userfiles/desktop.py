import os, sys, time, runpy, signal
from pathlib import Path
import pyautogui

signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

os.system("clear")
os.chdir(Path(__file__).parent)

username = str(Path().absolute()).split("/")[-1]
try:
    password = open("password.pwd", "r").read()
except FileNotFoundError:
    pass

print("""[1] Browser
[2] Terminal
[3] Files
[4] Calculator
[5] Text Editor
[6] Settings
[exit] Exit
""")
while True:
    option = input("[]: ")
    if option=="1":
        os.system("cls" if os.name=="nt" else "clear")
        os.system("lynx")
        print("""[1] Browser
[2] Terminal
[3] Files
[4] Calculator
[5] Text Editor
[6] Settings
[exit] Exit
""")
    elif option=="2":
        runpy.run_path(path_name="terminal.py")
    elif option=="3":
        runpy.run_path(path_name="files.py")
    elif option=="4":
        runpy.run_path(path_name="calculator.py")
    elif option=="5":
        os.system("cls" if os.name=="nt" else "clear")
        os.system("nano")
        print("""[1] Browser
[2] Terminal
[3] Files
[4] Calculator
[5] Text Editor
[6] Settings
[exit] Exit
""")
    elif option=="6":
        runpy.run_path(path_name="settings.py")
    elif option=="exit":
        pyautogui.press('f11')
        pyautogui.hotkey('ctrl', 'c')
    else:
        print("Invalid Option.")