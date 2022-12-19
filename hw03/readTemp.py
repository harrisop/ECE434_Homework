#!/usr/bin/python
#//////////////////////////////////////
#   Sophia Harrison
#   12/16/22
#   readTemp.py
#	Reads two TMP101 sensors and prints to the terminal.
#   Pin Configuration:
#   ALERT2 = P9_42, ALERT1 = 41
#   SCL = P9_18, SDA = P9_20
#   AD1 = P9_12, AD2 = P8_11
#	
#//////////////////////////////////////

import smbus
import time

bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x4a

while True:
    temp1 = bus.read_byte_data(address1, 0)
    temp1 = (temp1* 9/5) + 32

    temp2 =  bus.read_byte_data(address2, 0)
    temp2 = (temp2 * 9/5) + 32

    #print (temp, end="\r")
    
    print("Temp1 Reading: ", temp1, "\n")
    print("Temp2 Reading: ", temp2, "\n")
    time.sleep(1)