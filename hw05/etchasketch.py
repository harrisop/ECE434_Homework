#!/usr/bin/python
#//////////////////////////////////////
#   Sophia Harrison
#   1/15/23
#   etchasketch.py
#	This is an etch-a-sketch in the terminal. This version interfaces with accelerometer.
#	Wiring:	
#	Setup:	
#	See:	
#//////////////////////////////////////

import sys
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus
import binascii
import Adafruit_ADXL345

# set up LEDmatrix
bus = smbus.SMBus(2)  # Use i2c bus 2
matrix = 0x70         # Use address 0x70

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

# set up accelerometer
accel = Adafruit_ADXL345.ADXL345(address=0x53, busnum=2)

# Define clear button, leftmost button
BUT1 = "P9_11"
GPIO.setup("P9_11", GPIO.IN) # left

# get etch size form user, fixed at 8 now
# grid_size = int( input('How big do you want your etch-a-sketch? \n') )
grid_size = 8
xMax = grid_size
yMax = grid_size

# current position
x = 0
y = 0
datax = 0
datay = 0

# initialize grid
grid = { (i,j):' ' for i in range(0,xMax) for j in range(0,yMax) }

cleared_grid = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

current_grid = cleared_grid

# clear board function
def clearBoard():
    datax = 0
    datay = 0
    bus.write_i2c_block_data(matrix, 0, cleared_grid)
    for i in range(0, grid_size):
        for j in range(0, grid_size):
            grid[i,j] = ' '

# + at current location
grid[x,y] = '+'

def printonLED(gridtoPrint):
    temp_b = ["","","","","","","",""]
    for i in range(0, 8): # go through each column
        for j in range(0,8): # go through each spot in this col
            if(gridtoPrint[i,j] == '*' ):
                temp_b[j] += "1"
            else:
                temp_b[j] += "0"
    for i in range(8):
        temp_b[i] = int(temp_b[i], 2)
    current_grid = []
    for i in range(0,8):
        current_grid.append(0)
        current_grid.append(temp_b[i])
    bus.write_i2c_block_data(matrix, 0, current_grid)

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
    # Print to the LED matrix
    printonLED(gridtoPrint)

printGrid(grid)

def update_sketch_y(newy):
    global y
    global x
    global grid_size
    global grid
    grid[y,x] = '*'
    newy = int(newy)
    if newy > y:
        sys.stdout.write("up!\n")
        y = y - 1
        if y < 0:
            y = grid_size - 1
    elif newy < y:
        sys.stdout.write("down!\n")
        y = y + 1
        if y >= grid_size:
            y = 0
    grid[y,x] = '+'
    printGrid(grid)

def update_sketch_x(newx):
    global y
    global x
    global grid_size
    global grid
    grid[y,x] = '*'
    newx = int(newx)
    if newx < x:
        sys.stdout.write("left!\n")
        x = x - 1
        if x < 0:
            x = grid_size - 1
    elif newx > x:
        sys.stdout.write("right!\n")
        x = x + 1
        if x >= grid_size:
            x = 0
    grid[y,x] = '+'
    printGrid(grid)

def direction_pressed(channel):
    global x
    global y
    print('Edge detected on channel %s'%channel)
    if channel == BUT1:
        sys.stdout.write("Cleared!\n")
        x = 0
        y = 0
        clearBoard()    

# Set Up Events for buttons
GPIO.remove_event_detect(BUT1)
GPIO.add_event_detect(BUT1, GPIO.FALLING, callback=direction_pressed) 

# Wait for input from accelerometer
#read = [0,0,0]
read = 0
while True:
    #read = accel.acceleration
    #read = bus.read_i2c_block_data(0x53,0)
    x, y, z = accel.read()
    print(x, y, z)
    #datax = read[0]
    #datay = read[1]
    #if datax != olddata:
    #    olddata = datax
    #    update_sketch_x(datax)
    #    print("datax = " + datax)
    #if datay != olddata2:
    #    olddata2 = datay
    #    update_sketch_y(datay)
    #    print("datay = " + datay)
    time.sleep(0.2)