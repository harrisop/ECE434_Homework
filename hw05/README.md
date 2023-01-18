# ECE434 Homework 5
## Kernel
### Sophia Harrison 

## Make
The answers below relate to this command: bone$ gcc -g -c app.c -o app.o
1. Target = app.o
2. Dependency = app.c
3. Command = gcc (gnu c compiler)
The -c option tells the complier to put the file to an object file.
The makefile created for this part of the assignment is "Makefile" and it includes the path.mak file. This makefile compiles the app.c file. 

## Installing the Kernel Source
For this part of the assignment I followed the instructions and installed the kernel 5.10.145-ti-r55 and switched to this kernel but then switched back to the 5.10.140 version I had before.

## Kernel Modules
The files for this part of the assignment can be found in hello, ebbchar, gpio_test, and led. <br>
gpio_test: takes two button inputs and has two led outputs. The buttons trigger on both falling and rising edges. The buttons are on pins P9_11 and P9_13 and the LEDs are on pins P8_11 and P8_12. Need to set up buttons with the bash file in order for them to work properly. <br>
led: blinks two leds at different rates, 1000 ms and 200 ms. The led pins are P8_11 and P8_12.

## ADXL345 Accelerometer
Run the adxlSetup.sh file to ensure the device is properly set up for use. adxlViaKernel.sh tests that the device data can be read. The data read from the accelerometer is used to drive the etchasketch python file. I got a library off of the internet called adxl345.py in order to be able to more easily drive my etch-a-sketch with the accelerometer.

# hw05 grading

| Points      | Description |
| ----------- | ----------- |
|  0/0 | Project 
|  2/2 | Makefile
|  6/6 | Kernel Source
|  4/4 | Etch-a-Sketch
|  8/8 | Kernel Modules: hello, ebbchar, gpio_test, led
|  4/4 | Extras - Blink at different rates
| 24/20 | **Total**

*My comments are in italics. --may*

*Well done.  Very complete.*