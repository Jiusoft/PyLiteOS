import os, sys, time, shutil
from getpass import getpass

args = sys.argv[1:]
os.system("cls" if os.name=="nt" else "clear")

def register():
    print("Welcome New User, let's create a new account for PySubOS. ")
    username = input("Username for New User: ")
    password = getpass("Password for New User: ")
    if not os.path.exists("users"):
        os.mkdir("users")
    if not os.path.exists("disk"):
        os.mkdir("disk")
    try:
        os.chdir("users")
        os.mkdir(username)
        os.chdir("../disk")
        os.mkdir(username)
        shutil.copytree("../userfiles", "../users/"+username, dirs_exist_ok=True)
        os.chdir("../users/"+username)
        print("Thank you for the information, setting up new user. ")
    except FileExistsError:
        print("User Exists. ")
        time.sleep(3)
        os.system("cls" if os.name=="nt" else "clear")
        register()
    with open("password.pwd", "w") as pwd:
        pwd.write(password)
    os.chdir("../../")
    time.sleep(2)
    os.system("cls" if os.name=="nt" else "clear")
    login()

def login():
    if not os.path.exists("users") or not any(os.scandir("users")):
        register()
    else:
        for user in next(os.walk('users'))[1]:
            print(f"[{next(os.walk('users'))[1].index(user)+1}] {user}")
        user = input("\n[]: ")
        os.chdir("./users/" + next(os.walk('users'))[1][int(user)-1])
        os.system("python3 verification.py")

if args[0]=="register":
    register()
elif args[0]=="login":
    login()
else:
    print("error")
