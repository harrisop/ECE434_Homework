#!/usr/bin/python
#//////////////////////////////////////
#   Sophia Harrison
#   12/16/22
#   tempAlert.py
#	Reads two TMP101 sensors and prints to the terminal.
#   Pin Configuration:
#   ALERT2 = P9_42, ALERT1 = 41
#   SCL = P9_18, SDA = P9_20
#   AD1 = P9_12, AD2 = P8_11
#	
#//////////////////////////////////////

import smbus
import time
import Adafruit_BBIO.GPIO as GPIO

bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x4a

# set up alert pins
GPIO.setup("P9_41", GPIO.IN)
GPIO.setup("P9_42", GPIO.IN)

GPIO.cleanup()
t_high = 0x15
t_low = 0x0F

# set high and low temp for first TMP101
bus.write_byte_data(0x48, 0x01, 0x60)
bus.write_byte_data(0x48, 0x02, t_low)
bus.write_byte_data(0x48, 0x03, t_high)

# set high and low temp for second TMP101
bus.write_byte_data(0x4a, 0x01, 0x60)
bus.write_byte_data(0x4a, 0x02, t_low)
bus.write_byte_data(0x4a, 0x03, t_high)

while True:
    if GPIO.input("P9_41") == 0:
        # Alert
        temp1 = bus.read_byte_data(address1, 0)
        temp1 = (temp1* 9/5) + 32
        print("Temp1 Reading: ", temp1, "F \n")
    if GPIO.input("P9_42") == 0:
        # Alert 2
        temp2 =  bus.read_byte_data(address2, 0)
        temp2 = (temp2 * 9/5) + 32
        print("Temp2 Reading: ", temp2, "F \n")
    
    time.sleep(1)