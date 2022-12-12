# ECE434 Homework 2
## GPIO Speed
## Sophia Harrison 

## Buttons and LEDS
The python file LEDButtonTest.py reads switches and lights a corresponding LED, as well as tests that the LEDs and push buttons are functioning properly.

## Measuring a GPIO Pin on an Oscilloscope
### GPIO with Bash
1. voltage
2. period and freq.
3. 
4. 
5. 
6. The shortest period I could get is

| Sleep Time | Period | Processor Usage |
| ---- | --------- | -------- |
| bash| | |
| python | | |
| C | | |

7. 
8. 
9. 
10. 
11. 

### GPIO with Python
See fastLEDToggle.py file for code
Results:
1. period and freq.
2. how much processor being used

### GPIO with C
See togglegpio.c file for code.
Results:
1. period and freq.
2. how much processor being used

### Summary Table for GPIO
>Table of Results:
| Method | Frequency |
| ---- | --------- |
| bash| |
| python | |
| C | |


## GPIOD
Using the toggle examples, I measured how fast I could toggle one gpio bit using c then python. This was then repeated using two bits. Results are recorded in the table below.


### Summary Table for GPIOD
>Table of Results:
| File | Frequency |
| ---- | --------- |
| toggle1.c | |
| toggle1.py | |
| toggle2.c | |
| toggle2.py | |


## getSetEvent.py and Etch-a-Sketch pt. 2
I modified the file getsetEvent.py so that it could read four push buttons and turn on the corresponding LED.
The etchasketch.py file is the second iteration where the direction of the pen that draws on the etch-a-sketch is controlled by the push buttons.