#!/usr/bin/python
#//////////////////////////////////////
#	etchasketch.py
#	Is a etch a sketch in the terminal.
#	Wiring:	
#	Setup:	
#	See:	
#//////////////////////////////////////

import sys

# get etch size form user
grid_size = int(input())
xMax = grid_size
yMax = grid_size

# current position
x = 0
y = 0

grid = []
# initialize grid
for i in range(grid_size):
    grid[i] = [xMax]
    for j in range(len(grid)):
        grid[i][j] = ' '

# + at current location
grid[x][y] = '+'

# Print grid
def printGrid(gridtoPrint):
    #stuff
    sys.stdout.write('   0 1 2 3 4 5 6 7\n')
    for i in range(len(gridtoPrint)):
        sys.stdout.write(format("%d: ",i))
        for j in range(len(gridtoPrint[i])):
            sys.stdout.write(format("%s ", gridtoPrint[i][j]))
        sys.stdout.write("\n")

printGrid(grid)


for line in sys.stdin:
    inp = line.rstrip()
    if inp == 'Exit':
        break
    sys.stdout.write("processeing")
sys.stdout.write("Goodbye!")

sys.exit()