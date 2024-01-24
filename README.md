# seating-chart-generator
This is the code to generate random seating charts for all of the labs in one of the classes that I TA.

Unfortunately, I did not think to put this code on github from its inception, so most of the process
of making it is undocumented. I uploaded it now and will begin to add comments where needed.

In the future, I will likely have additions to make to this code that I will be able to document.

# To Run:
This program only runs from the command line. In order to run it, cd to the directory
that this script is in, make sure the generated_students.csv file is in the same directory,
and type the following command.

> python3 assign_partners.py 1xx < --reverse or -r >

NOTE: Replace 1xx with your lab section, valid lab sections are 100-105. 

This command should bring up an image of the seating chart, based on the room your lab section
is in. The optional reverse flag reverses the rows that appear in the seating chart to allow for the 
seating chart to be displayed in different areas of the room and still make sense.

Random names were generated here: http://random-name-generator.info/index.php?n=100&g=1&st=2
