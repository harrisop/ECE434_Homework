# ECE434 Homework 2
## GPIO Speed
## Sophia Harrison 

## Buttons and LEDS
The python file LEDButtonTest.py reads switches and lights a corresponding LED, as well as tests that the LEDs and push buttons are functioning properly.

## Measuring a GPIO Pin on an Oscilloscope
### GPIO with Bash
1. The min voltage = 3.75 mV and the max voltage is 3.0 V
2. The period is 252 ms and the freq. is 3.97 Hz
3. The period is a little over double 100 ms.
4. They differ because other processes make the period slower than intended by the code. The file has to be opened and closed, along with other processes that contribute the periods being different.
5. Around 4% of the CPU is being used.
6. The shortest period I could get is

| Sleep Time | Period (ms) | Processor Usage % |
| ---- | --------- | -------- |
| 0.1 | 252 |  4 |
| 0.01 | 65 | 14 |
|  0.001 | 60 | 17 |
| 0.0001 | 40 | 18 |

7. The period is not very stable when using a sleep time of 0.0001. The is a standard deviation of 28m.
8. The period remained relatively unstable with the standard deviaiton in the period being about 14m.
9. After cleaning up some of the unneeded lines, the period became slightly more stable with the standard deviation of the period being about 11m.
10. After using sh instead, the period did get shorter and came out to about 30 ms.
11. The shortest period I got was 30 ms, which I got after doing question 10.

### GPIO with Python
See fastLEDToggle.py file for code
Results:
1. The period was 177.8 microseconds and the freq. was 5.625kHz.
2. About 90% of the processor was being used.

### GPIO with C
See togglegpio.c file for code.
Results:
1. The period was 300.7 microseconds and the freq. was 3.325 kHz.
2. About 28% of the processor was being used.

### Summary Table for GPIO
>Table of Results:
| Method | Period (seconds) |
| ---- | --------- |
| bash | 30 milli |
| python | 178 micro |
| C | 300.7 micro |


## GPIOD
Using the toggle examples, I measured how fast I could toggle one gpio bit using c then python. This was then repeated using two bits. Results are recorded in the table below.


### Summary Table for GPIOD
>Table of Results:
> I ran each of the files below and measured the frequency of the LED using gpio60.
| File | Frequency (Hz) |
| ---- | --------- |
| toggle1.c | 4.978 |
| toggle1.py | 4.975 |
| toggle2.c | 4.976 |
| toggle2.py | 4.979 |

## Security
I changed the ssh port number form 22 to 2022 and followed the rest of the instructions for this section. After doing so I ran into some issues with ssh-ing into my bone and so I then changed the port back so that my bone wouldn't be giving me issues.

## getSetEvent.py and Etch-a-Sketch pt. 2
I modified the file getsetEvent.py so that it could read four push buttons and turn on the corresponding LED.

The etchasketch.py file is the second iteration where the direction of the pen that draws on the etch-a-sketch is controlled by the push buttons.
I have 5 pushbuttons for the etch-a-sketch: one to go left, right, up, and down on the board and one extra button to clear the board. The board is still printed to the terminal.
