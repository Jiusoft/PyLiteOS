import os, shutil, time
from glob import glob
from pathlib import Path
os.system("cls" if os.name=="nt" else "clear")
username = os.path.basename(os.getcwd())

os.chdir("../../disk/"+username)
def dispfiles():
    if not any(Path('.').iterdir()):
        print("<No Files Found>")
    for i in glob("*"):
        if not os.path.isfile(i):
            print(i.split("/")[-1]+"/")

    for i in glob("*"):
        if os.path.isfile(i):
            print(i.split("/")[-1])

dispfiles()
def dispoptions():
    print("""\n[1] New File
[2] New Folder
[3] Delete File
[4] Delete Folder
[5] Open File (Text Based Files Only)
[6] Change Directory
[7] Move (Rename) File
[8] Move (Rename) Folder
[9] Copy File
[10] Copy Folder
[11] Paste
[exit] Exit
""")
dispoptions()

while True:
    option = input("[]: ")
    if option == "exit":
        os.chdir(f"../../users/{username}")
        os.system("python3 desktop.py")
    elif option == "1":
        newfilename = input("Enter name of new file: ")
        if not os.path.isfile(newfilename):
            tmp = open(newfilename, 'w')
            tmp.close()
        else:
            print("\033[91mERROR: File Exists\033[0m")
            time.sleep(2)
        os.system("cls" if os.name=="nt" else "clear")
        dispfiles()
        dispoptions()
    elif option == "2":
        newfoldername =  input("Enter name of new folder: ")
        if not os.path.isdir(newfoldername):
            os.makedirs(newfoldername)
        else:
            print("\033[91mERROR: Folder Exists\033[0m")
            time.sleep(2)
        os.system("cls" if os.name=="nt" else "clear")
        dispfiles()
        dispoptions()
    elif option == "3":
        delfilename = input("Enter name of the file you want to delete: ")
        try:
            os.remove(delfilename)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
            time.sleep(2)
        os.system("cls" if os.name=="nt" else "clear")
        dispfiles()
        dispoptions()
    elif option == "4":
        delfoldername = input("Enter name of the folder you want to delete: ")
        try:
            shutil.rmtree(delfoldername)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
            time.sleep(2)
        os.system("cls" if os.name=="nt" else "clear")
        dispfiles()
        dispoptions()
    elif option == "5":
        openfilename = input("Enter name of file to open: ")
        if os.path.isfile(openfilename):
            os.sytem("vim %s" % openfilename)
        else:
            print("\033[91mERROR: File Doesn't Exist\033[0m")
            time.sleep(2)
        os.system("cls" if os.name=="nt" else "clear")
        dispfiles()
        dispoptions()
    elif option == "6":
        cdname = input("Enter name of directory to change to (.. for parent directory): ")
        if os.path.isdir(cdname) and "/".join("bruh/test/hi/".strip("/").split("/")[-2:]) == f"/disk/{username}" and not cdname == "..":
            os.chdir(cdname)
        elif os.path.isdir(cdname) and "/".join("bruh/test/hi/".strip("/").split("/")[-2:]) == f"/disk/{username}":
            os.chdir(cdname)
        else:
            print("\033[91mERROR: Folder Doesn't Exist\033[0m")
        os.system("cls" if os.name=="nt" else "clear")
        dispfiles()
        dispoptions()