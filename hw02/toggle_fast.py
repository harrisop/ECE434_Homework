#!/usr/bin/python
#//////////////////////////////////////
#   Sophia Harrison
#   12/10/22
#   toggle_fast.py
#	This code toggles leds.
#	Wiring:	Button pins = GPIO_{30, 31, 48, 5, 3}
#           LED pins = GPIO_{49, 117, 115, 121}
#	Setup:	
#	See:	
#//////////////////////////////////////

import time
import os
import Adafruit_BBIO.GPIO as GPIO


# Define buttons
GPIO.setup("P9_11", GPIO.IN)
GPIO.setup("P9_13", GPIO.IN)
GPIO.setup("P9_15", GPIO.IN)
GPIO.setup("P9_17", GPIO.IN)
GPIO.setup("P9_21", GPIO.IN)

# Define LEDs
GPIO.setup("P9_23", GPIO.OUT)
GPIO.setup("P9_25", GPIO.OUT)
GPIO.setup("P9_27", GPIO.OUT)
GPIO.setup("P9_29", GPIO.OUT)

while True:
    if GPIO.input("P9_11"):
        print("High")
    else:
        print("LOW")
    
GPIO.cleanup()