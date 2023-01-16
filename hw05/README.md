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
The files for this part of the assignment can be found in hello, ebbchar, gpio_test, and led. 

## ADXL345 Accelerometer
Run the adxlSetup.sh file to ensure the device is properly set up for use. adxlViaKernel.sh tests that the device data can be read. The data read from the accelerometer is used to drive the etchasketch python file. I got a library off of the internet called adxl345.py in order to be able to more easily drive my etch-a-sketch with the accelerometer.