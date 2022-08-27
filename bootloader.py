import os, time, sys
from pathlib import Path

def main():
    os.system("cls" if os.name=="nt" else "clear")
    os.chdir(Path(__file__).parent) 

    def check(noprint=None):
        if os.path.exists("users"):
            if not any(os.scandir("users")):
                os.system("python3 login.py register")
            else:
                if not noprint == True:
                    print("""[1] Login
[2] Create new user
[exit] Exit
                """)
                else:
                    print("\n", end="")
                option = input("[]: ")
                if option=="exit":
                    sys.exit()
                elif option=="1":
                    os.system("python3 login.py login")
                elif option=="2":
                    os.system("python3 login.py register")
                else:
                    print("Invalid Option.")
                    time.sleep(1.5)
                    check(noprint=True)
        else:
            os.mkdir("users")
            check()

    check()

if __name__ == '__main__':
    main()