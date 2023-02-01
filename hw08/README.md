# ECE434 Homework 8
## Programmable Realtime Unit (PRU)
### Sophia Harrison 

## 2.6 BLinking an LED
See hello.pru0.c for the code for this part. To start the PRU code you type in the command line "make start" and similarly, to stop you type in "make stop" and this will stop the PRU code execution. The pin toggles pretty fast, with a frequency of about 12.5MHz. There appears to be some jitter but for the most part it seems stable. <br>
<img src=./scope_captures/part1.png width="500">

## 5.3 PWM Generator
See pwm1.pru0.c for the code for this part. Make sure to run pwm_setup.sh to set up the beagle pins for this code. I did a scope capture with the delays of 2000 cycles added to make the waveform symmetric and at around 50MHz. <br>
Waveform Stability -> much more stable than the last. <br>
Std Dev -> about 150 mV <br>
Jitter? -> no real visible jitter <br>
<img src=./scope_captures/part2.png width="500">

## 5.4 Controlling the PWM Frequency
See pwm4.pru0.c and pwm-test.c for the code for this part. The output pins P9_31, P9_29, P9_30, and P9_28 are being driven. The highest frequency I could get with four channels is about 327 kHz. <br>
<img src=./scope_captures/part3.png width="500">

## 5.9 Reading an Input at Regular Intervals
See input.pru0.c for the code and run the input_setup.sh bash file to set up the beagle to run this code. <br>
How fast the code can transfer the input to the ouput? -> Using a function generator and a scope I found the fastest it could go is about 500 ns, seen in the capture below. <br>
<img src=./scope_captures/part4.png width="500">
