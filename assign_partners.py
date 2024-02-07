from sys import argv
import tkinter
import seating_selection
import seating_display
import roster_parsing
import platform
import pyautogui
import subprocess

roster_file = 'testing_roster.csv'
REVERSE = False
DOWNLOAD = False
SYSTEM_PLATFORM = platform.system()

if len(argv) >= 3:
    for argument in argv:
        if "-r" in argument or "--reverse" in argument:
            REVERSE = True
        if "-d" in argument or "--download" in argument:
            DOWNLOAD = True


data = roster_parsing.read_csv(roster_file)

ROOM = data[0]
current_room_info = data[1]
students = data[2]

win = tkinter.Tk()
win.title('Lab ' + argv[1])

tables = seating_selection.seating_selection(current_room_info, students)
seating_display.seating_display(current_room_info, tables, win, REVERSE)


win.update()
x = win.winfo_rootx() + win.winfo_x()
y = win.winfo_rooty() + win.winfo_y()
width = x + win.winfo_width()
height = y + win.winfo_height()

if SYSTEM_PLATFORM == 'Windows':
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save("seating_chart.png")
elif SYSTEM_PLATFORM == 'Darwin':  # macOS
    subprocess.run(["screencapture", "-R", f"{x},{y},{width},{height}", "seating_chart.png"])
elif SYSTEM_PLATFORM == 'Linux':
    subprocess.run(["scrot", "-u", "-o", "seating_chart.png", "-s"])
else:
    print("Unsupported operating system for downloads")


win.mainloop()

