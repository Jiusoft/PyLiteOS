import os, sys

os.system("cls" if os.name=="nt" else "clear")
print("PySubOS Terminal")

while True:
    cmd = input("\n>>> ").strip()
    if cmd == 'exit':
        os.system("python3 desktop.py")
        sys.exit()
    else:
        os.system(cmd)