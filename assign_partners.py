from sys import argv
import tkinter
import seating_selection
import seating_display
import roster_parsing


# sect_dict : {section number : room, ...}
SECT_DICT = {100: "ols018", 101: "ols018", 102: "ols018", 103: "ols018", 104: "ols009", 105: "ols018"}

# room_info : {room : (columns of tables, number of tables, (table width, table height), max student per table), ...},
STANDARD_ROOMS_INFO = {"ols018": (5, 15, (200, 200), 6),
              "ols005": (2, 8, (400, 200), 6),
              "mech215": (4, 4, (200, 500), 6)}

# irregular_rooms_info : {room : (columns or tables, array of TOTAL students per row), ... },
IRREGULAR_ROOMS_INFO = {"ols009": [[6, 6], [7,7], [7,8], [8,9], [6,4], [4]]}

REVERSE = False

if len(argv) >= 3 and (argv[2] == "-r" or argv[2] == "--reverse"):
    REVERSE = True

data = roster_parsing.read_csv(SECT_DICT, STANDARD_ROOMS_INFO, IRREGULAR_ROOMS_INFO)

ROOM = data[0]
ROOM_INFO = data[1]
students = data[2]

win = tkinter.Tk()
win.title('Lab ' + argv[1])

if ROOM in IRREGULAR_ROOMS_INFO:
    tables = seating_selection.irregular_seating_selection(ROOM_INFO, students)
    seating_display.irregular_seating_display(ROOM_INFO, tables, win, REVERSE)

else:
    tables = seating_selection.standard_seating_selection(students, ROOM_INFO)
    seating_display.standard_seating_display(ROOM_INFO, tables, win, REVERSE)

win.mainloop()


# to document:
    # functionality of reverse