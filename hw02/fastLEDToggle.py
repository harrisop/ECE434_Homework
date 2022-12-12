#!/usr/bin/python
#//////////////////////////////////////
#   Sophia Harrison
#   12/10/22
#   fastLEDToggle.py
#	This code attempts to toggle an LED as fast as it can.
#	Wiring:	
#	Setup:	
#	See:	
#//////////////////////////////////////

import Adafruit_BBIO.GPIO as GPIO
import time

LEDPin = "P9_12"
# Set up LED Pin
GPIO.setup(LEDPin, GPIO.OUT)

while True:
    GPIO.output(LEDPin, 1)
    GPIO.output(LEDPin, 0)
