import os, sys

args = sys.argv[1:]

def register():
    print("Welcome New User, let's create a new account for PySubOS. ")
    username = input("Username for New User: ")
    password = input("Password for New User: ")
    print("Thank you for the information, setting up new user. ")
    if os.path.exists("users"):
        os.chdir("users")
    else:
        os.mkdir("users")
        os.chdir("users")
    os.mkdir(username)
    os.chdir(username)
    with open("password.pwd", "w") as pwd:
        pwd.write(password)
    

if args[0]=="register":
    register()
elif args[0]=="login":
    print("login")
else:
    print("error")
