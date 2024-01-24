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
ROOM_INFO is a dictionary of rooms where each value is a tuple containing a nested list and a boolean value. 
Each sublist of the nested list represents a row of tables and each value in the sublist is the number of students the 
row can hold. The boolean value indicates whether a room is standard or irregular.  
"""

ROOM_INFO = {
    "ols009": ([
                   [6, 6],
                   [7,7],
                   [7,8],
                   [8,9],
                   [6,4],
                   [4]
               ], False),
    "ols018": ([
                   [6,6,6,6,6],
                   [6,6,6,6,6],
                   [6,6,6,6,6]
               ], True),
    "ols005": ([
                   [6,6],
                   [6,6],
                   [6,6],
                   [6,6],
                   [6,6],
                   [6,6],
                   [6,6],
                   [6,6],
               ], True),
    "mech215": ([
                    [6,6],
                    [6,6],
                    [6,6],
                    [6,6],
                ], True)
}

REVERSE = False

if len(argv) >= 3 and (argv[2] == "-r" or argv[2] == "--reverse"):
    REVERSE = True

data = roster_parsing.read_csv(SECT_DICT, ROOM_INFO)

ROOM = data[0]
current_room_info = data[1]
students = data[2]

win = tkinter.Tk()
win.title('Lab ' + argv[1])

tables = seating_selection.seating_selection(current_room_info, students)
seating_display.seating_display(current_room_info, tables, win, REVERSE)

win.mainloop()

