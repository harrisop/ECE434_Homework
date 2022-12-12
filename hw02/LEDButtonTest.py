#!/usr/bin/python
#//////////////////////////////////////
#   Sophia Harrison
#   12/10/22
#   LEDButtonTest.py
#	This code tests the functionality of 4 LEDS and 5 push buttons.
#	Wiring:	
#	Setup:	
#	See:	
#//////////////////////////////////////

import Adafruit_BBIO.GPIO as GPIO
import time
import os

# Define buttons
GPIO.setup("P9_11", GPIO.IN)
GPIO.setup("P9_13", GPIO.IN)
GPIO.setup("P9_19", GPIO.IN)
GPIO.setup("P9_17", GPIO.IN)
GPIO.setup("P9_21", GPIO.IN)

# Define LEDs
GPIO.setup("P9_23", GPIO.OUT)
GPIO.setup("P9_27", GPIO.OUT)
GPIO.setup('P9_12', GPIO.OUT)
GPIO.setup('P9_41', GPIO.OUT)

GPIO.cleanup()

# set all LOW
GPIO.output("P9_23",GPIO.LOW)
GPIO.output("P9_27",GPIO.LOW)
GPIO.output('P9_41',GPIO.LOW)
GPIO.output('P9_12',GPIO.LOW)

time.sleep(1)

# Test: turn on and off all LEDS
# # LED 1
# GPIO.output("P9_23",GPIO.HIGH)
# time.sleep(1)
# # LED 2
# GPIO.output("P9_41",GPIO.HIGH)
# time.sleep(1)
# # LED 3
# GPIO.output('P9_27',GPIO.HIGH)
# time.sleep(1)
# # LED 4
# GPIO.output('P9_12',GPIO.HIGH)
# time.sleep(1)

# GPIO.output("P9_23",GPIO.LOW)
# GPIO.output('P9_41',GPIO.LOW)
# GPIO.output("P9_27",GPIO.LOW)
# GPIO.output('P9_12',GPIO.LOW)

while True:
    if GPIO.input("P9_11") == 1:
        print("button 1")
        GPIO.output("P9_23",GPIO.HIGH)

    if GPIO.input("P9_13") == 1:
        print("button 2")
        GPIO.output("P9_41",GPIO.HIGH)

    if GPIO.input("P9_19") == 1:
        print("button 3")
        GPIO.output("P9_27",GPIO.HIGH)

    if GPIO.input("P9_17") == 1:
        print("button 4")
        GPIO.output("P9_12",GPIO.HIGH)
    
GPIO.cleanup()