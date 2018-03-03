'''
Name: Aidan Latham
Email: aidan.latham@slu.edu
Current Date: Feb 15th
Course Information: CSCI 1300-01
Instructor: Judy Etchison
Description: Source code for "Mastermind" code game. Includes user defined
             functions and loop structures.
'''


''' Import packages '''
# Import cs1graphics package to use for extra credit
from cs1graphics import *

# Import function to generate code
from random import randint


''' Establish Canvas to be used '''
# Create Canvas
screen = Canvas(1000,800,'brown')


''' Define necessary functions '''
# define function to check validity of input
def valid_check(num_str):
    if(not num_str.isdigit()):
        return "ERROR: contains non-numbers, try again"
    if(len(num_str) != 4):
        return "ERROR: enter 4 digits, try again"
    for i in range(4):
        if(int(num_str[i]) > 5 or int(num_str[i]) < 1):
            return "ERROR: guess must be comprised of digits 1-5, try again"
    return ''

# define function to check user input code vs. generated code
def check_code(code,user_num_str):
    num_exist = 0
    num_right_position = 0
    exclude_pos_code = []
    exclude_pos_str = []
    for i in range(4):
        if(user_num_str[i] == code[i]):
            num_right_position += 1
            exclude_pos_str.append(i)
            exclude_pos_code.append(i)
    for i in range(4):
        for j in range(4):
            if(user_num_str[i] == code[j] and not (i in exclude_pos_str)
                                          and not (j in exclude_pos_code)):
               num_exist += 1
               exclude_pos_str.append(i)
               exclude_pos_code.append(j)
    return [num_exist,num_right_position]

# define function to print out circles
def display_circles(code,ycod):
    colors = ['yellow','purple','green','blue','red']
    master_xcod = 160    
    for i in range(4):
        temp_circ = Circle(20,Point(master_xcod,ycod))
        temp_circ.setFillColor(colors[int(code[i])-1])
        screen.add(temp_circ)
        master_xcod += 80

# define function to display right/wrong count
def display_pegs(results_list,ycod):
    exist_text = Text(str(results_list[0]),24,Point(500,ycod))
    exist_text.setFontColor('white')
    right_pos_text = Text(str(results_list[1]),24,Point(540,ycod))
    right_pos_text.setFontColor('red')
    screen.add(exist_text)
    screen.add(right_pos_text)


''' main body '''
# First, generate code and print start, and display
# opening text on canvas
master_code = ''
for i in range(4):
    master_code += str(randint(1,5))
print "Ready to play Mastermind!!"
print "\n\n"
screen.add(Text("Ready to play Mastermind!!",24,Point(800,40)))
screen.add(Text("White means num present, but not right position",12,Point(800,80)))
screen.add(Text("Red means num present AND right position",12,Point(800,100)))
screen.add(Text("Input guess using command prompt",12,Point(800,120)))

# Display code in the form of circles at bottom of Canvas,
# and hide them with a black rectangle until completion
master_ycod = 740
display_circles(master_code,master_ycod)
cover = Rectangle(280,40,Point(280,master_ycod))
cover.setFillColor('black')
screen.add(cover)
                       
# Prompt user for input
answer_list = [0,0]
num_guess = 0
circ_ycod = 40
while(True):
    guess = raw_input("Guess?: ")
    if("ERROR" in valid_check(guess)):
        print valid_check(guess)
    else:
        display_circles(guess,circ_ycod)
        num_guess += 1
        answer_list = check_code(master_code,guess)
        display_pegs(answer_list,circ_ycod)
        if(answer_list[1] == 4 or num_guess == 10):
            break
        print answer_list[0],"exist but are not in the right position,",answer_list[1],
        print "are in the right position."
        circ_ycod += 60

# Display results/remove master code cover
print "\n\n"
if(guess == master_code):
    screen.add(Text("You cracked the code!",24,Point(800,700)))
    print "You guessed the key:",master_code,
    print "It took you",num_guess,"guesses.\n\n\n"
else:
    screen.add(Text("Oof, wrong!",24,Point(800,700)))
    print "Sorry, you lost. The code was",master_code,"Try again next time.\n\n\n"
screen.remove(cover)

