#!/usr/bin/env python3
#   
#   readW1Temp.py
#   Sophia Harrison
#   Reads the MAX31820 temperature sensors
#   From: https://pypi.org/project/w1thermsensor/
#

import time
from w1thermsensor import W1ThermSensor


for sensor in W1ThermSensor.get_available_sensors():
    # goes through each sensor active and prints temp
    print("Sensor %s has temperature %.2f C \n" % (sensor.id, sensor.get_temperature()))