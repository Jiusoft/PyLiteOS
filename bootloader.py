import os

os.chdir("/".join(__file__.split("/")[:-1]))

def check():
    if os.path.exists("users"):
        if not any(os.scandir("users")):
            os.system("python3 login.py register")
        else:
            os.system("python3 login.py login")
    else:
        os.mkdir("users")
        check()

check()