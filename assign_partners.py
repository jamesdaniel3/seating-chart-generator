from sys import argv
import tkinter
import seating_selection
import seating_display
import roster_parsing


"""
SECT_DICT is a dictionary where each key is a section number and each value is the room that the section's lab is held in.
"""

SECT_DICT = {100: "ols018", 101: "ols018", 102: "ols018", 103: "ols018", 104: "ols009", 105: "ols018"}


"""
STANDARD_ROOMS_INFO is a dictionary of rooms where each value is a tuple of the following format: 
(columns of tables, number of tables, (table width, table height), max student per table)
"""

STANDARD_ROOMS_INFO = {"ols018": [[6,6,6,6,6], [6,6,6,6,6], [6,6,6,6,6]],
              "ols005": (2, 8, (400, 200), 6),
              "mech215": (4, 4, (200, 500), 6)}

"""
IRREGULAR_ROOMS_INFO is a dictionary of rooms where each value is a nested list. Each sublist is a row of tables 
and each value in the sublist is the number of students the row can hold 
"""
IRREGULAR_ROOMS_INFO = {"ols009": [[6, 6], [7,7], [7,8], [8,9], [6,4], [4] ] }

REVERSE = False

if len(argv) >= 3 and (argv[2] == "-r" or argv[2] == "--reverse"):
    REVERSE = True

data = roster_parsing.read_csv(SECT_DICT, STANDARD_ROOMS_INFO, IRREGULAR_ROOMS_INFO)

ROOM = data[0]
ROOM_INFO = data[1]
students = data[2]

win = tkinter.Tk()
win.title('Lab ' + argv[1])

tables = seating_selection.irregular_seating_selection(ROOM_INFO, students)

if ROOM in IRREGULAR_ROOMS_INFO:
    seating_display.irregular_seating_display(ROOM_INFO, tables, win, REVERSE)

else:
    seating_display.irregular_seating_display(ROOM_INFO, tables, win, REVERSE)

win.mainloop()
