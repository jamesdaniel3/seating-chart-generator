import random
import math

def seating_selection(room_info, students_list):
    """
    This function takes in a nested list where each sublist is a row of tables and each value in the sublist is the
    number of students the row can hold and a list of students in a lab and returns a random seating arrangement for the
    students.

    :param room_info: a tuple containing a given rooms information where the first value is a nested list where each
                        sublist represents a row in the room and each value contains the number of students that can
                        fit at a table and the second value is a boolean value that indicates whether the room is standard
    :param students_list: a list of the names of students in the lab
    :return: a nested list of tables where each element is a list of students
    """
    standard_room = room_info[1]
    resulting_tables = []
    num_students_by_row = room_info[0]
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


    if standard_room:
        resulting_tables = split_last_two_tables(resulting_tables)
        resulting_tables = center_student_seating(resulting_tables, num_students_by_row)

    return resulting_tables


def split_last_two_tables(student_groups, ):
    """
    This function splits the students in the last two tables that have students evenly between the two. Currently, has
    no ability to check that it is not overloading a table which is a concern for irregular rooms. Also, the spacing comes
    out weird in standard rooms.

    :param student_groups: a nested list of tables where each element is a list of students at the table
    :return: the length of a given string in pixels
    """
    students = []
    for x in range(len(student_groups) - 1, 0, -1):
        if len(student_groups[x]) > 0 and len(student_groups[x-1]) > 0:
            students.extend(student_groups[x])
            students.extend(student_groups[x-1])

            student_groups[x] = students[0: len(students) // 2]
            student_groups[x - 1] = students[len(students) // 2:]

            return student_groups

    return student_groups

def center_student_seating(seating_dict, room_info):
    """
    This function is only intended to be used with standard rooms.
    This function takes in a seating arrangement for students and centers them in the room. If there is an imbalance in
    columns, there will always be 1 more empty column on the right of the room than the left. If there is only one row
    of students, the students will be placed in the second row of the room.

    :param seating_dict: a nested list of tables where each element is a list of students
    :param room_info: a tuple containing a given rooms information where the first value is a nested list where each
                        sublist represents a row in the room and each value contains the number of students that can
                        fit at a table and the second value is a boolean value that indicates whether the room is standard
    :return: a nested list of tables where each element is a list of students, but the last row of tables that contains
                        students has been centered
    """

    num_tables = len(room_info) * len(room_info[0]) # assumes that there will be at least one desk
    tables_per_row = len(room_info[0])
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


