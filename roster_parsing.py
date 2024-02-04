from sys import argv
import section_and_room_info

ROOM = ""
ROOM_INFO = ()

def read_csv(roster_file):
    """
    This function reads the lab roster csv file stored in the directory and outputs a list containing a lab's room,
    it's information, and a list containing all the students in the lab.

    :param roster_file: a string containing the name of the file that holds all the students
    :return: a list containing a lab's room, it's information, and a list containing all the students in the lab.
    """
    global ROOM, ROOM_INFO
    students = []
    sect_dict = section_and_room_info.SECT_DICT # a dictionary of the form { section number: room }
    rooms_info = section_and_room_info.ROOM_DICT # a dictionary containing the information about all rooms seating and whether each is standard, see ROOM_INFO in assign_partners.py

    if len(argv) < 2:
        print('ERROR: Please enter a section number and room number.')
        quit()

    try:
        with open(roster_file, 'r') as roster:
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

            for line in roster:
                line = line.strip().split(',')
                if line[lab_ind].strip():
                    data = line[lab_ind].strip().split(';')
                    students.append(data[0].replace(' ', '_') + ' ' + data[1].replace(' ', '_'))

    except FileNotFoundError:
        print('ERROR: Lab roster not found.')
        quit()

    return [ROOM, ROOM_INFO, students]

