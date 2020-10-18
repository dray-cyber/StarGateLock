import tkinter as tk
import os
root = tk.Tk()
apple = 0

if apple != 2:
    worked = False
    apple = 2
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
if worked == False:
    if screen_height == 720 and screen_width == 1280:
        os.system('cmd /c pythonw.exe 1280x720.py')
        worked = True
    if screen_height == 1080 and screen_width == 1920:
        os.system('cmd /c pythonw.exe 1920x1080.py')
        worked = True
    if screen_height == 768 and screen_width == 1366:
        os.system('cmd /c pythonw.exe 1366x768.py')
        worked = True
    if screen_height == 768 and screen_width == 1280:
        os.system('cmd /c pythonw.exe 1280x768.py')
        worked = True
else:
    os.system('cmd /c pythonw.exe stargate.py')
    worked = True