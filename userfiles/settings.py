import os, socket, time
from pathlib import Path
global username
from getpass import getpass
username = os.path.basename(os.getcwd())
os.system("cls" if os.name=="nt" else "clear")

def settings(password):
    print(f"""Info:
    Host Name: {socket.gethostname()}
    Host IP Address: {socket.gethostbyname(socket.gethostname())}
    Username: {os.path.basename(os.getcwd())}
    Password: {password}

Changable:
    [1] Username
    [2] Password
    [exit] Exit
""")
    while True:
        option = input("[]: ")
        if option == "exit":
            os.system("python3 desktop.py")

        elif option == "1":
            os.chdir("..")
            newusername = input("Enter New Username: ")
            os.rename(username, newusername)
            os.chdir(newusername)
            input("Press Enter to Restart...")
            os.system("python3 desktop.py")

        elif option == "2":
            newpassword = input("Enter New Password: ")
            with open("password.pwd", "w") as f:
                f.write(newpassword)
            input("Press Enter to Restart...")
            os.system("python3 verification.py")

        else:
            print("Invalid option. Please Try Again.")


def logintobios():
    login = getpass(f"Please Enter the Password for {username}: ")
    password = open("password.pwd", 'r').read()
    if login == password:
        settings(password=password)
    else:
        print("Invalid Password. Please try again.")
        time.sleep(1.5)
        print(login)
        print(password)
        print(os.getcwd())
        logintobios()

logintobios()