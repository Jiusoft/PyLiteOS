import sys

args = sys.argv[1:]

if args[0]=="register":
    print("register")
elif args[0]=="login":
    print("login")
else:
    print("error")