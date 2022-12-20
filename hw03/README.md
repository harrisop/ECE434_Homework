# ECE434 Homework 3
## GPIO USING I2C
### Sophia Harrison 

## TMP101 - Temperature Sensors
The three possible i2c addresses for the TMP101, according to the datasheet, are the following:
- 1001000
- 1001001
- 1001010
1. I wired and set up the two temperature sensors.
2. I first created a bash file called readTemp.sh which reads the temperature and prints the measurements to the terminal.
3. I then wrote a python script that also reads the two temperature. See readTemp.py
4. I ran the i2cset command to test this command works for my sensors.
5. Finally I created a python script that waits for an interrupt from the Alert pins for each of the sensors.

## Etch-A-Sketch Part 3
I wired up the LED matrix to the same bus as the temperature sensors, bus 2, and then implemented the LED matrix and the rotary encoders into the etch-a-sketch python script. The instructions for the game were updated and are printed out when the script is run.

## Rotary Encoders
For setting up the rotary encoders, I created and ran rotarySetup.sh so that they can be used in the etch-a-sketch script.