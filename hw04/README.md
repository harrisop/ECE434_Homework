# ECE434 Homework 4
## MMAP & LCD
### Sophia Harrison 

## Memory Map

## GPIO Via MMAP
1. See LEDBUTtoggle.py for the code that reads two switches and controls two LEDs using mmap
2. See LEDtoggle.py for the code that toggles a GPIO port as fast as it can. The measurements for the different sleep times and without the sleep is shown in the table below.

| Sleep Time | Speed |
| ----------- | ---------|
| 0.5 | x |
| 0.1 | x |
| 0.01 | x |
| 0 | x |

## I2C Via the Kernel
See tempReadDriver.sh for the code. 
I read the TMP101 sensors using the kernel driver and then converted the measurement to degrees farenheit, printing them to the command line. 

## Etch-A-Sketch Part 4 (using Flask)
I modified my etch-a-sketch to take input from a web browser using flask. The etchasketch.py file is the file to run and it uses the html file etchasketch.html which can be found in the tmeplates folder. Using the buttons on the local web browser, you can now control where the cursor goes. Instructions for the game can be found on the web browser when you run the python file.

## LCD Display
