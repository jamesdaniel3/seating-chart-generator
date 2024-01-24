from sys import argv

ROOM = ""
ROOM_INFO = ()

def read_csv(sect_dict, rooms_info):
    """
    This function reads the lab roster csv file stored in the directory and outputs a list containing a lab's room,
    it's information, and a list containing all the students in the lab.

    :param sect_dict: a dictionary of the form { section number: room }
    :param rooms_info: a dictionary of the form
                    { room: (columns of tables, number of tables, (table width, table height), max student per table) }
    :param irregular_rooms_info: a dictionary of the form {room : (columns or tables, array of TOTAL students per row) }
    :return: a list containing a lab's room, it's information, and a list containing all the students in the lab.
    """
    global ROOM, ROOM_INFO
    students = []

    if len(argv) < 2:
        print('ERROR: Please enter a section number and room number.')
        quit()

    try:
        with open('generated_students.csv', 'r') as roster:
            lab_nums = roster.readline().strip().split(',')
            lab_ind = 0
            while lab_ind < len(lab_nums) and argv[1] not in lab_nums[lab_ind]:
                lab_ind += 1
            if int(argv[1]) not in sect_dict.keys():
                print('ERROR: Lab number', argv[1], 'not found.')
                quit()
            else:
                ROOM = sect_dict[int(argv[1])]
                ROOM_INFO = rooms_info[ROOM]
                # if ROOM in irregular_rooms_info:
                #     ROOM_INFO = irregular_rooms_info[ROOM]
                # else:
                #     ROOM_INFO = rooms_info[ROOM]

            for line in roster:
                line = line.strip().split(',')
                if line[lab_ind].strip():
                    data = line[lab_ind].strip().split(';')
                    students.append(data[0].replace(' ', '_') + ' ' + data[1].replace(' ', '_'))

    except FileNotFoundError:
        print('ERROR: Lab roster not found.')
        quit()

    return [ROOM, ROOM_INFO, students]

