'''
Name: Aidan Latham
Email: aidan.latham@slu.edu
Current Date: February 7th
Course Information: CSCI 1300-01
Instructor: Judy Etchison

Source code for checkerboard program, including generation subroutine and number valid check subroutine
'''
# Import the cs1graphics library
from cs1graphics import *


# Subroutine to check whether input numbers are valid. Bounds determined by
# program instructions (num no less than 2, no greater than 6. Can be changed)
def num_valid_check(string):
    if (not string.isdigit()):
        return False
    if(int(string) < 2 or int(string) > 6):
        return False
    return True
# This subroutine isn't necessary, but I felt it was good practice


# Prompt user for variables. While loops for invalid input as stated
# in the program instructions.

# Number of Checkerboards
numOfBoards = raw_input("How many checkerboards? (From 2 to 6): ")
while (not num_valid_check(numOfBoards)):
    print "Not a valid integer. Try again."
    numOfBoards = raw_input("How many checkerboards?: ")
numOfBoards = int(numOfBoards)

# Number of rows
rows = raw_input("How many rows? (From 2 to 6): ")
while (not num_valid_check(rows)):
    print "Not a valid integer. Try again."
    rows = raw_input("How many rows? (From 2 to 6): ")
rows = int(rows)

# Number of columns
columns = raw_input("How many columns? (From 2 to 6): ")
while (not num_valid_check(columns)):
    print "Not a valid integer. Try again."
    columns = raw_input("How many columns?: ")
columns = int(columns)

# List of colors. Dependent on number of checkerboards so that
# only the correct amount of colors need to be input
colors = []
for i in range(numOfBoards):
    colors.append(raw_input("Input a color: "))


# Create canvas
screen = Canvas(600,600)


# Initialize variables to be used in the size/position of the checkerboard.
#  Modular, will work even with changes to length
length = 25
xcod = length
ycod = length

# Temporarily assign the xcod to reset to at each row
reset_xcod = length


# Create subroutine to generate checkerboard.
# A LOT of parameters, could use some optimization.
# Line width is modular, can be changed.
def checkerboard_gen(length,rows,columns,color,xcod,ycod,reset_xcod,z):
    for i in range(rows):       
        for j in range(columns):
            shape_temp = Square(length,Point(xcod,ycod))
            if ((j % 2 == i % 2) == (z % 2 == 0)):       # this conditional might seem a little unecessary at first.
                shape_temp.setFillColor(color)           # Its use is so that the checkerboards next to each other have
            shape_temp.setBorderWidth(0)                 # alternating starting blocks.
            screen.add(shape_temp)
            xcod += length
        ycod += length     
        xcod = reset_xcod
# this subroutine is also unecessary, as the code could've just been utilized
# in the upcoming for loop. In fact, I'd say it would have been easier to implement that way.
# However, I felt it would be good practice and a fun challenge to get used to Python's
# implementation of user defined methods.

        
# Create checkerboards
# Utilized subroutine that makes each checkerboard at a time, rather
# then going row by row across entire stretch.
for i in range(numOfBoards):
    checkerboard_gen(length,rows,columns,colors[i],xcod,ycod,reset_xcod,i)
    reset_xcod += length * columns
    xcod = reset_xcod
    if ((i + 1) >= 3):
        ycod = length * (rows + 1)
    else:
        ycod = length
    if ((i + 1) % 3 == 0):
        reset_xcod = length
        xcod = length









        
