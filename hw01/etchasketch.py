#!/usr/bin/python
#//////////////////////////////////////
#   Sophia Harrison
#   12/8/22
#   etchasketch.py
#	This is an etch-a-sketch in the terminal.
#	Wiring:	
#	Setup:	
#	See:	
#//////////////////////////////////////

import sys

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

# Loop to Check Terminal Input for Grid
while True:
    inp = input('Direction> ')
    grid[y,x] = '*'
    if inp == 'Exit':
        sys.stdout.write("Goodbye!\n")
        sys.exit()
    elif inp == 'Clear':
        sys.stdout.write("Cleared!\n")
        x = 0
        y = 0
        clearBoard()
    elif inp == 'u':
        sys.stdout.write("up!\n")
        y = y - 1
        if y < 0:
            y = grid_size - 1
    elif inp == 'd':
        sys.stdout.write("down!\n")
        y = y + 1
        if y >= grid_size:
            y = 0
    elif inp == 'l':
        sys.stdout.write("left!\n")
        x = x - 1
        if x < 0:
            x = grid_size - 1
    elif inp == 'r':
        sys.stdout.write("right!\n")
        x = x + 1
        if x >= grid_size:
            x = 0
    else:
        sys.stdout.write("I don't understand, say that again\n")
    grid[y,x] = '+'
    printGrid(grid)  