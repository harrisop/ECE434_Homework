# ECE434 Homework 4
## MMAP & LCD
### Sophia Harrison 

## Memory Map
Here is the memory map I created for the beagle, referencing the memory map tables in the AM335x TRM.<br>
<img src="https://user-images.githubusercontent.com/56809512/211339552-1ff70a0e-bb65-4c29-a8cd-d72cb8dffde4.png" width="100">

## GPIO Via MMAP
1. See LEDBUTtoggle.py for the code that reads two switches and controls two LEDs using mmap
2. See LEDtoggle.py for the code that toggles a GPIO port as fast as it can. As the sleep time decreased, the speed of toggling increased but the increase started to level out as the sleep time 
approached zero and when the usleep was removed. To the nake eye it just appeared as if the led remained on towards the end of this test. 

## I2C Via the Kernel
See tempReadDriver.sh for the code. Run setuptemp.sh before runnign tempReadDriver.sh to set everything up.
I read the TMP101 sensors using the kernel driver and then converted the measurement to degrees farenheit, printing them to the command line. 

## Etch-A-Sketch Part 4 (using Flask)
I modified my etch-a-sketch to take input from a web browser using flask. The etchasketch.py file is the file to run and it uses the html file etchasketch.html which can be found in the tmeplates folder. Using the buttons on the local web browser, you can now control where the cursor goes. Instructions for the game can be found on the web browser when you run the python file.

## LCD Display
See playMedia.sh for the code that tests the LCD display. When you run the bash file, an image is displayed then rotated and displayed again, then text is added to the image and displayed. Finally there is a video that is displayed. 
