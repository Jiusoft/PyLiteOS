import os, sys, time
from getpass import getpass

if "skipver" in sys.argv:
    os.system("python3 desktop.py")

def verify():
    os.system("cls" if os.name=="nt" else "clear")
    password = open("password.pwd", "r").read()
    pwdinput = getpass("Please Enter Password: ")
    if pwdinput == password:
        os.system("python3 desktop.py")
    else:
        print("Wrong Password. Please Try again!")
        time.sleep(1.5)
        verify()

verify()
