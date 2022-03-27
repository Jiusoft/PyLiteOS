import os, sys, time

def verify():
    os.system("clear")
    password = open("password.pwd", "r").read()
    pwdinput = input("Please Enter Password: ")
    if pwdinput == password:
        os.system("python3 desktop.py")
    else:
        print("Wrong Password. Please Try again!")
        time.sleep(1.5)
        verify()

verify()