from tkinter import *
import os

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
termf = Frame(root, height=screen_height, width=screen_width)

termf.pack()
os.system(f'xterm -into {termf.winfo_id()} -geometry {screen_width}x{screen_height} +sb -e python3 2.py&')

root.mainloop()
