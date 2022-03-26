import os, sys, time

args = sys.argv[1:]

def register():
    print("Welcome New User, let's create a new account for PySubOS. ")
    username = input("Username for New User: ")
    password = input("Password for New User: ")
    if os.path.exists("users"):
        os.chdir("users")
    else:
        os.mkdir("users")
        os.chdir("users")
    try:
        os.mkdir(username)
        os.chdir(username)
        print("Thank you for the information, setting up new user. ")
    except FileExistsError:
        print("User Exists. ")
        time.sleep(1)
        os.system("clear")
        register()
    with open("password.pwd", "w") as pwd:
        pwd.write(password)
    os.chdir("../../")
    time.sleep(2)
    os.system("clear")
    login()

def login():
    if not os.path.exists("users") or not any(os.scandir("users")):
        register()
    else:
        for user in next(os.walk('users'))[1]:
            print(f"[{next(os.walk('users'))[1].index(user)+1}] {user}")
        input("\n[?]: ")

if args[0]=="register":
    register()
elif args[0]=="login":
    login()
else:
    print("error")
