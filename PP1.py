# Name: Aidan Latham
# Email: aidan.latham@slu.edu
# Currrent Date: Janurary 22nd
# Course Information: CSCI 1300-01
# Instructor: Judy Etchison
#
# This is the source code for the "fishbowl" scene, including animation.

# Import the cs1graphics library.
from cs1graphics import *

# Import the sleep command from time library.
from time import sleep

# Canvas to be used.
screen = Canvas(1000,650,title = 'Fish Bowl Scene')

# Table
table = Rectangle(900,30,Point(500,600))
table.setFillColor('chocolate4')
table.setDepth(49)
screen.add(table)

# Table legs
tableLeg1 = Rectangle(30,35,Point(150,631.5))
tableLeg1.setFillColor('chocolate4')
tableLeg2 = tableLeg1.clone()
tableLeg2.moveTo(850,631.5)
screen.add(tableLeg1)
screen.add(tableLeg2)

# Fishbowl
fishbowl = Circle(325,Point(500,325))
fishbowl.setFillColor('skyblue')
fishbowl.setDepth(50)
screen.add(fishbowl)

# Fishbowl bottom
bottom = Rectangle(500,33,Point(500,632))
bottom.setFillColor('white')
bottom.setBorderWidth(0)
bottom.setDepth(49)
screen.add(bottom)

# Fishbowl top
top = Rectangle(800,100,Point(500,20))
top.setFillColor('white')
top.setBorderWidth(0)
top.setDepth(49)
screen.add(top)

# Fish
fish = Layer()
body = Circle(35,Point(35,0))
body.setFillColor('darkorange')
tail = Polygon(Point(-50,20),Point(0,0),Point(-50,-20))
tail.setFillColor('darkorange')
eye = Circle(5,Point(45,-12))
eye.setFillColor('black')
mouth = Path(Point(45,10),Point(50,20),Point(62,22.27))
mouth.setDepth(0)
fish.add(mouth)
fish.add(body)
fish.add(tail)
fish.add(eye)
screen.add(fish)
fish.moveTo(500,300)

# Seaweed
seaweed1 = Polygon(Point(325,585),Point(300,525),Point(310,495),
                   Point(300,465),Point(350,415),Point(375,465),
                   Point(360,495),Point(375,535),Point(350,585))
seaweed1.setFillColor('darkgreen')
seaweed2 = seaweed1.clone()
seaweed2.flip()
seaweed2.moveTo(450,585)
screen.add(seaweed1)
screen.add(seaweed2)

# Start prompt
startPrompt = Text('Click anywhere to start the animation!',20)
startPrompt.moveTo(500,200)
screen.add(startPrompt)
screen.wait()
screen.remove(startPrompt)

# Fish animation
sleep(1.5)
time = 0
for time in range(0,35):
    fish.move(5,5)
    sleep(.05)
    time = time + .1
sleep(.75)
fish.flip()
sleep(.75)
for time in range(0,15):
    fish.move(-5,-10)
    sleep(.05)
    time = time + .1
sleep(.25)
for time in range(0,15):
    fish.move(-15,-2)
    sleep(.05)
    time = time + .1
sleep(.75)
fish.flip()
sleep(1)

# Exit prompt
exitPrompt = Text('Click anywhere to exit!! Thanks for watching!',20)
exitPrompt.moveTo(500,200)
screen.add(exitPrompt)
screen.wait()
screen.close()
    
