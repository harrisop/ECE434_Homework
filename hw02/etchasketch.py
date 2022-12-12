#!/usr/bin/python
#//////////////////////////////////////
#   Sophia Harrison
#   12/8/22
#   etchasketch.py
#	This is an etch-a-sketch in the terminal. This version interfaces with buttons.
#	Wiring:	
#	Setup:	
#	See:	
#//////////////////////////////////////

import sys
import Adafruit_BBIO.GPIO as GPIO
import time

# Define buttons, left to right
BUT1 = "P9_11"
BUT2 = "P9_13"
BUT3 = "P9_19"
BUT4 = "P9_17"
BUT5 = "P9_21"
GPIO.setup("P9_11", GPIO.IN) # left
GPIO.setup("P9_13", GPIO.IN) # 2
GPIO.setup("P9_19", GPIO.IN) # 3
GPIO.setup("P9_17", GPIO.IN) # 4
GPIO.setup("P9_21", GPIO.IN) # 5

# Print Instructions
sys.stdout.write("Welcome! Here are the instructions for this etch-a-sketch:\n")
sys.stdout.write("Type Clear to clear the board\n")
sys.stdout.write("Type Exit to exit the game\n")
sys.stdout.write("Type u to go up the board\n")
sys.stdout.write("Type d to go down the board\n")
sys.stdout.write("Type l to go left on the board\n")
sys.stdout.write("Type r to go right on the board\n")

# get etch size form user
grid_size = int( input('How big do you want your etch-a-sketch? \n') )
xMax = grid_size
yMax = grid_size

# current position
x = 0
y = 0

# initialize grid
grid = { (i,j):' ' for i in range(0,xMax) for j in range(0,yMax) }

# clear board function
def clearBoard():
    for i in range(0, grid_size):
        for j in range(0, grid_size):
            grid[i,j] = ' '

# + at current location
grid[x,y] = '+'

# Print grid
def printGrid(gridtoPrint):
    sys.stdout.write('     ')
    for i in range(0, grid_size ):
        sys.stdout.write('{:} '.format(i))
    sys.stdout.write('\n')
    for i in range(0, grid_size ):
        sys.stdout.write('{:>3}: '.format(i))
        for j in range(0, grid_size):
            sys.stdout.write('{:} '.format(gridtoPrint[i,j]))
        sys.stdout.write("\n")

printGrid(grid)

def update_sketch(channel):
    global y
    global x
    global grid_size
    global grid
    
    grid[y,x] = '*'
    if channel == BUT1:
        sys.stdout.write("Cleared!\n")
        x = 0
        y = 0
        clearBoard()
    elif channel == BUT2:
        sys.stdout.write("up!\n")
        y = y - 1
        if y < 0:
            y = grid_size - 1
    elif channel == BUT3:
        sys.stdout.write("down!\n")
        y = y + 1
        if y >= grid_size:
            y = 0
    elif channel == BUT4:
        sys.stdout.write("left!\n")
        x = x - 1
        if x < 0:
            x = grid_size - 1
    elif channel == BUT5:
        sys.stdout.write("right!\n")
        x = x + 1
        if x >= grid_size:
            x = 0
    grid[y,x] = '+'
    printGrid(grid)

def direction_pressed(channel):
    print('Edge detected on channel %s'%channel)
    update_sketch(channel)

# Set Up Events
GPIO.remove_event_detect(BUT1)
GPIO.add_event_detect(BUT1, GPIO.BOTH, callback=direction_pressed) 
GPIO.remove_event_detect(BUT2)
GPIO.add_event_detect(BUT2, GPIO.BOTH, callback=direction_pressed) 
GPIO.remove_event_detect(BUT3)
GPIO.add_event_detect(BUT3, GPIO.BOTH, callback=direction_pressed) 
GPIO.remove_event_detect(BUT4)
GPIO.add_event_detect(BUT4, GPIO.BOTH, callback=direction_pressed) 
GPIO.remove_event_detect(BUT5)
GPIO.add_event_detect(BUT5, GPIO.BOTH, callback=direction_pressed) 

# Sleep While waiting for button press
while True:
    time.sleep(100)
