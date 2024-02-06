import tkinter

HEADER = ('Arial', '16', 'bold', 'underline')
BODY = ('Arial', '12')
IMAGE_HEIGHT = 800
IMAGE_WIDTH = 1200

def seating_display(room_info, tables, window, reverse):
    """
    This function takes in the information needed to form a regular and irregular seating chart and then calls the
    appropriate function.

    :param room_info: a tuple containing a given rooms information where the first value is a nested list where each
                        sublist represents a row in the room and each value contains the number of students that can
                        fit at a table and the second value is a boolean value that indicates whether the room is standard
    :param tables: a nested list of tables where each table is a list of student names
    :param window: the window object created by tkinter
    :param reverse: if this parameter is True, the rows in the image will be reversed
    """
    standard_room = room_info[1]
    print(room_info)
    if standard_room:
        standard_seating_display(room_info, tables, window, reverse)
    else:
        irregular_seating_display(room_info, tables, window, reverse)



def standard_seating_display(room_info, tables, window, reverse):
    """
    This function puts together and displays the image for a standard lab's seating chart

    :param room_info: a tuple containing a given rooms information where the first value is a nested list where each
                        sublist represents a row in the room and each value contains the number of students that can
                        fit at a table and the second value is a boolean value that indicates whether the room is standard
    :param tables: a nested list of tables where each table is a list of student names
    :param window: the window object created by tkinter
    :param reverse: if this parameter is True, the rows in the image will be reversed
    """
    rows_of_desks = room_info[0]
    if reverse:
        tables.reverse()
        rows_of_desks.reverse()

    num_rows = len(rows_of_desks)
    desk_count = 0

    for i in range(num_rows):
        row = tkinter.Frame(window)
        num_desks = len(rows_of_desks[i])

        for j in range(num_desks):
            desk_count += 1
            canvas_width = IMAGE_WIDTH / num_desks
            canvas_height = IMAGE_HEIGHT / num_rows
            can = tkinter.Canvas(row, bg='white', width=canvas_width, height=canvas_height, highlightbackground='black')
            can.create_text(canvas_width/2, 25, fill='black', text='Table ' + str(desk_count), font=HEADER)
            next_y = 50
            names_at_table = ""

            for pair in tables[desk_count - 1]:
                for each in pair:
                    can.create_text(10, next_y, fill='black', text=each, font=BODY, anchor='w')
                    next_y += 18
                next_y += 30

            can.create_text(10, next_y, fill='black', text=names_at_table.replace('_', ' '), font=BODY, anchor='w')
            can.pack(side=tkinter.LEFT)
        row.pack()


def irregular_seating_display(room_info, tables, window, reverse):
    """
    This function puts together and displays the image for an irregular lab's seating chart

    :param room_info: a tuple containing a given rooms information where the first value is a nested list where each
                        sublist represents a row in the room and each value contains the number of students that can
                        fit at a table and the second value is a boolean value that indicates whether the room is standard
    :param tables: a nested list of tables where each table is a list of student names
    :param window: the window object created by tkinter
    :param reverse: if this parameter is True, the rows in the image will be reversed
    """

    rows_of_desks = room_info[0]
    if reverse:
        tables.reverse()
        rows_of_desks.reverse()

    num_rows = len(rows_of_desks)
    desk_count = 0

    for i in range(num_rows):
        row = tkinter.Frame(window)
        num_desks = len(rows_of_desks[i])

        for j in range(num_desks):
            desk_count += 1
            canvas_width = IMAGE_WIDTH / num_desks
            canvas_height = IMAGE_HEIGHT / num_rows
            can = tkinter.Canvas(row, bg='white', width=canvas_width, height=canvas_height, highlightbackground='black')
            can.create_text(canvas_width/2, 25, fill='black', text='Table ' + str(desk_count), font=HEADER)
            next_y = 50
            names_at_table = ""
            student_groups = []

            maximum_text_length = canvas_width / 2

            for person in tables[desk_count - 1]:
                temp_stu = person.split(" ")
                student = temp_stu[1] + " " + temp_stu[0] + "      "
                if get_text_size(names_at_table + student, BODY) < maximum_text_length:
                    names_at_table += student
                else:
                    student_groups.append(names_at_table)
                    names_at_table = student

            if len(student_groups) != 0:
                group_spacing = canvas_height / len(student_groups) *.4
                if group_spacing > 50:
                    group_spacing = 50
                for each in student_groups:
                    can.create_text(10, next_y, fill='black', text=each, font=BODY, anchor='w')
                    next_y += group_spacing
            can.create_text(10, next_y, fill='black', text=names_at_table.replace('_', ' '), font=BODY, anchor='w')
            can.pack(side=tkinter.LEFT)
        row.pack()


def get_text_size(text, font_info):
    """
    This function takes in piece text and returns the length of it in pixels, given a font type and size.

    :param text: the text being measured
    :param font_info: a tuple of font info in the form (font name, size)
    :return: the length of the text
    """
    scratch = tkinter.Canvas()
    temp = scratch.create_text((0, 0), text=text, font=font_info)
    size = scratch.bbox(temp)
    length_of_text = abs(size[0])
    return length_of_text