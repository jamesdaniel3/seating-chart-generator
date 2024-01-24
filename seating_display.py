from math import ceil
import tkinter

HEADER = ('Arial', '16', 'bold', 'underline')
BODY = ('Arial', '12')
IMAGE_HEIGHT = 800
IMAGE_WIDTH = 1200


def standard_seating_display(room_info, tables, window, reverse):
    """
    This function puts together the image for a standard lab's seating chart.

    :param room_info: a tuple containing of the following format:
                        (columns of tables, number of tables, (table width, table height), max student per table)
    :param tables: a twice-nested list of tables where each table is a list of student pairs and each student pair
                        is a list of two students
    :param window: the window object created by tkinter
    :param reverse: if this parameter is True, the rows in the image will be reversed
    """
    # specs for current room
    room_width = room_info[0]
    num_tables = room_info[1]
    canvas_width = room_info[2][0]
    canvas_height = room_info[2][1]

    if reverse:
        tables.reverse()

    for i in range(ceil(num_tables / room_width)):
        row = tkinter.Frame(window)
        for j in range(room_width):
            can = tkinter.Canvas(row, bg='white', width=canvas_width, height=canvas_height, highlightbackground='black')
            can.create_text(canvas_width/2, 25, fill='black', text='Table ' + str(i * room_width + j + 1), font=HEADER)
            next_y = 50
            for pair in tables[i * room_width + j]:
                for student in pair:
                    temp_stu = student.split(" ")
                    student = temp_stu[1] + " " + temp_stu[0]
                    can.create_text(10, next_y, fill='black', text=student.replace('_', ' '), font=BODY, anchor='w')
                    next_y += 18
                next_y += 18
            can.pack(side=tkinter.LEFT)
        row.pack()


def irregular_seating_display(room_info, tables, window, reverse):
    """
    This function puts together the image for an irregular lab's seating chart

    :param room_info: a tuple containing of the following format:
                        (number of columns, a list containing the TOTAL number of students per row)
    :param tables: a nested list of tables where each table is a list of student names
    :param window: the window object created by tkinter
    :param reverse: if this parameter is True, the rows in the image will be reversed
    """

    if reverse:
        tables.reverse()

    num_rows = len(room_info)
    desk_count = 0

    for i in range(num_rows):
        row = tkinter.Frame(window)
        num_desks = len(room_info[i])
        for j in range(num_desks):
            desk_count += 1
            canvas_width = IMAGE_WIDTH / num_desks
            canvas_height = IMAGE_HEIGHT / num_rows
            can = tkinter.Canvas(row, bg='white', width=canvas_width, height=canvas_height, highlightbackground='black')
            can.create_text(canvas_width/2, 25, fill='black', text='Table ' + str(desk_count), font=HEADER)
            next_y = 50
            names_at_table = ""
            for pair in tables[desk_count - 1]:
                temp_stu = pair.split(" ")
                student = temp_stu[1] + " " + temp_stu[0] + "      "
                if get_text_size(names_at_table + student, BODY) < canvas_width - 100:
                    names_at_table += student
                else:
                    can.create_text(10, next_y, fill='black', text=names_at_table.replace('_', ' '), font=BODY, anchor='w')
                    names_at_table = student
                    next_y += 18
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