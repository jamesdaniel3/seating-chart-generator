import random
import math


def standard_seating_selection(students_list, room_info):
    """
    This function will return a twice-nested list of tables where each table is a list of student pairs and
    each student pair is a list of two students for students in rooms with standard setups (ex. OLS018)

    :param students_list: a list of the names of students in the lab
    :param room_info: a tuple containing of the following format:
                        (columns of tables, number of tables, (table width, table height), max student per table)
    :return: a twice-nested list of tables where each table is a list of student pairs and each student pair
                        is a list of two students
    """
    pairings = []  # list of partners. i.e. [[partner 1, partner 2], ...]
    num_tables = room_info[1]
    seats_per_table = room_info[3]
    num_students = len(students_list)
    total_seats = num_tables * seats_per_table

    while len(students_list) > 1:
        first = random.randrange(0, len(students_list))
        pairings.append([students_list[first]])
        students_list = students_list[:first] + students_list[first + 1:]
        second = random.randrange(0, len(students_list))
        pairings[-1].append(students_list[second])
        students_list = students_list[:second] + students_list[second + 1:]


    # find out how many tables are needed to house all students
    while True:
        if total_seats - seats_per_table > num_students:
            total_seats -= seats_per_table
        else:
            break

    tables_needed = math.ceil(total_seats/seats_per_table)

    # evenly distribute student pairs across needed tables
    resulting_tables = [[] for _ in range(room_info[1])]
    current_table = 0
    while len(pairings) > 0:
        if current_table < tables_needed:
            resulting_tables[current_table].append(pairings[0])
            pairings.pop(0)
            current_table += 1
        else:
            current_table = 0

    # account for odd number of students
    for table in resulting_tables:
        student_count = 0
        for pair in table:
            student_count += len(pair)
        if student_count < seats_per_table and student_count != 0:
            if len(students_list):
                table[0].append(students_list[0])


    resulting_tables = center_student_seating(resulting_tables, room_info)
    return resulting_tables


def irregular_seating_selection(num_students_by_row, students_list):
    """


    :param num_students_by_row:
    :param students_list: a list of the names of students in the lab
    :return: a nested list of tables where each element is a list of students
    """
    resulting_tables = []
    for row in num_students_by_row:
        for desk in row:
            choices = []
            for y in range(desk):
                if len(students_list) == 0:
                    break
                student_num = random.randrange(0, len(students_list))
                choices.append(students_list[student_num])
                del students_list[student_num]

            resulting_tables.append(choices)

    resulting_tables = ensure_a_pair(resulting_tables)

    return resulting_tables


def ensure_a_pair(student_groups):
    """
    This function is only intended to be used with irregular rooms.
    This function checks that no tables have 1 student, and will move a student to a table that has 1 student if found.

    :param student_groups: a nested list of tables where each element is a list of students at the table
    :return: the length of a given string in pixels
    """
    for x in range(len(student_groups) - 1, -1, -1):
        if len(student_groups[x]) == 1:
            student_to_be_moved = student_groups[x - 1].pop()
            student_groups[x].append(student_to_be_moved)
            return student_groups
    return student_groups

def center_student_seating(seating_dict, room_info):
    """
    This function is only intended to be used with standard rooms.
    This function takes in a seating arrangement for students and centers them in the room. If there is an imbalance in
    columns, there will always be 1 more empty column on the right of the room than the left. If there is only one row
    of students, the students will be placed in the second row of the room.

    :param seating_dict: a twice-nested list of tables where each table is a list of student pairs and each student pair
                        is a list of two students
    :param room_info: a tuple containing of the following format:
                        (columns of tables, number of tables, (table width, table height), max student per table)
    :return: a twice-nested list of tables where each table is a list of student pairs and each student pair
                        is a list of two students
    """

    num_tables = room_info[1]
    tables_per_row = room_info[0]
    tables_with_students = [i for i in seating_dict if i != []]

    # Center last row of students
    num_full_rows = math.floor(len(tables_with_students) / tables_per_row)
    seating_without_full_rows = seating_dict[(num_full_rows * tables_per_row)::]
    last_row_of_students = [i for i in seating_without_full_rows if i != []]
    empty_tables_in_row = tables_per_row - len(last_row_of_students)
    last_row = [[] for _ in range(math.floor(empty_tables_in_row / 2))]
    last_row.extend(last_row_of_students)
    extra_tables_last_row = tables_per_row - len(last_row)
    for x in range(extra_tables_last_row):
        last_row.append([])

    full_rows = seating_dict[0: (num_full_rows * tables_per_row)]
    full_rows.extend(last_row)

    # if there is less than a full row of students, place all students in the second row
    if len(tables_with_students) < tables_per_row:
        empty_row = [[] for _ in range(tables_per_row)]
        empty_row.extend(full_rows)
        full_rows = empty_row

    # fill in the rest of the tables as empty
    while len(full_rows) < num_tables:
        full_rows.append([])

    return full_rows


