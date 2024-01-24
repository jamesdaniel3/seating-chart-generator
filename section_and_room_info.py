"""
SECT_DICT is a dictionary where each key is a section number and each value is the room that the section's lab is held in.
"""

SECT_DICT = {100: "ols018", 101: "ols018", 102: "ols018", 103: "ols018", 104: "ols009", 105: "ols018"}


"""
ROOM_INFO is a dictionary of rooms where each value is a tuple containing a nested list and a boolean value. 
Each sublist of the nested list represents a row of tables and each value in the sublist is the number of students the 
row can hold. The boolean value indicates whether a room is standard or irregular.  
"""

ROOM_DICT = {
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
