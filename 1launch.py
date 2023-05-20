from tkinter import *
import os, psutil, time

def update_battery_label():
    battery = psutil.sensors_battery()
    if battery is not None:
        hours = battery.secsleft // 3600
        minutes = battery.secsleft // 60 - hours * 60
        seconds = battery.secsleft - (hours * 3600 + minutes * 60)
        battlabel1.config(text=f"Battery: {battery.percent}%")
        battlabel2.config(text="Estimated Battery Time Left: " + f"{hours}h {minutes}m {seconds}s" if not(battery.secsleft == -2 or battery.secsleft == 4294967295) else "Estimated Battery Time Left: Unlimited (Charging)")
        battlabel3.config(text=f"State: " + "Charging" if battery.power_plugged else "State: Not Charging")
    else:
        battlabel1.config(text="Battery: Battery information not available.")
        battlabel2.config(text="State: Battery information not available.")

    # Schedule the next update after 0.1 second
    battlabel1.after(1000, update_battery_label)

root = Tk()
root.configure(background='#ffffff')
root.attributes('-fullscreen', True)
battlabel1 = Label(root, text="Battery: ", bg='#ffffff')
battlabel2 = Label(root, text="Estimated Battery Time Left: ", bg='#ffffff')
battlabel3 = Label(root, text="State: ", bg='#ffffff')
termf = Frame(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight()-battlabel1.winfo_height(), bg='#ffffff')

battlabel1.grid(row=0, column=0, sticky=NW)
battlabel2.grid(row=0, column=1)
battlabel3.grid(row=0, column=2, sticky=NE)

termf.grid(row=1, column=0, columnspan=3, sticky=S)
#os.system(f'xterm -into {termf.winfo_id()} -geometry {termf.winfo_width()}x{termf.winfo_height()} +sb -bg rgb:ffffff -e python3 2bootloader.py &')
update_battery_label()

root.mainloop()
