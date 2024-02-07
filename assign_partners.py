from sys import argv
import tkinter
import seating_selection
import seating_display
import roster_parsing
import save_image
import platform


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


if DOWNLOAD:
    save_image.take_screenshot(win, SYSTEM_PLATFORM)

win.mainloop()
