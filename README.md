# seating-chart-generator
This is the code to generate random seating charts for all of the labs in one of the classes that I TA.

Unfortunately, I did not think to put this code on github from its inception, so the initial refactor
is undocumented. 


# To Run:
This program only runs from the command line. In order to run it, cd to the directory
that this script is in, make sure the generated_students.csv file is in the same directory,
and type the following command.

> python3 assign_partners.py 1xx < --reverse or -r > <--download or -d>

NOTE: Replace 1xx with your lab section, valid lab sections are 100-105. 

This command should bring up an image of the seating chart, based on the room your lab section
is in. The optional reverse flag reverses the order of the rows (top row becomes bottom) that appear in the seating chart to allow for the 
seating chart to be displayed in different areas of the room and still make sense. The optional download 
flag will install the necessary packages and then download the seating chart to the current directory as 
a png. I have plans to allow the user to choose the download location in the future. 

Random names were generated here: http://random-name-generator.info/index.php?n=100&g=1&st=2
