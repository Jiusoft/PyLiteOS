import os, sys, time, runpy, signal, psutil

# Set Ctrl+C Output to Nothing
signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

os.system("clear")
os.chdir(os.path.dirname(os.path.abspath(__file__)))

username = str(Path().absolute()).split("/")[-1]
try:
    password = open("password.pwd", "r").read()
except FileNotFoundError:
    pass

battery_percent = None
battery_lock = threading.Lock()

def update_battery():
    global battery_percent
    while True:
        battery = psutil.sensors_battery()
        battery_percent = battery.percent if battery else "Unknown"
        time.sleep(5)  # Update the battery count every 5 seconds

battery_thread = threading.Thread(target=update_battery)
battery_thread.daemon = True
battery_thread.start()

while True:
    os.system("clear")  # Clear the screen before updating the battery count

    with battery_lock:
        current_battery_percent = battery_percent

    print(f"Battery: {current_battery_percent}%\n")
    print("""[1] Browser
[2] Terminal
[3] Files
[4] Calculator
[5] Text Editor
[6] Settings
[exit] Exit
""")
    option = input("[]: ")
    if option == "1":
        #os.system("cls" if os.name == "nt" else "clear")
        os.system("w3m https://html.duckduckgo.com/html")
    elif option == "2":
        runpy.run_path(path_name="terminal.py")
    elif option == "3":
        runpy.run_path(path_name="files.py")
    elif option == "4":
        runpy.run_path(path_name="calculator.py")
    elif option == "5":
        os.system("cls" if os.name == "nt" else "clear")
        os.system("nano")
    elif option == "6":
        runpy.run_path(path_name="settings.py")
    elif option == "exit":
        os.system(su -c "shutdown -h now")
    else:
        print("Invalid Option.")
