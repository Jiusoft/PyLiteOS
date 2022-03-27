from cgi import test
import os, time
from pathlib import Path

os.system("clear")
os.chdir(Path(__file__).parent) 

def check():
    if os.path.exists("users"):
        if not any(os.scandir("users")):
            os.system("python3 login.py register")
        else:
            print("""[1] Login
[2] Create new user
            """)
            option = input("[]: ")
            if option=="1":
                os.system("python3 login.py login")
            elif option=="2":
                os.system("python3 login.py register")
            else:
                print("Invalid Option. Please Try again. ")
                time.sleep(1.5)
                check()
    else:
        os.mkdir("users")
        check()

check()