from sys import argv
import tkinter
import seating_selection
import seating_display
import roster_parsing

roster_file = 'generated_students.csv'

REVERSE = len(argv) >= 3 and (argv[2] == "-r" or argv[2] == "--reverse")

data = roster_parsing.read_csv(roster_file)

ROOM = data[0]
current_room_info = data[1]
students = data[2]

win = tkinter.Tk()
win.title('Lab ' + argv[1])

tables = seating_selection.seating_selection(current_room_info, students)
seating_display.seating_display(current_room_info, tables, win, REVERSE)

win.mainloop()

