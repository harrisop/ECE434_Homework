# 
#   This code reads the x and y from the accelerometer.
#   make sure to run adxlSetup.sh first
#

cd /sys/class/i2c-adapter/i2c-2/2-0053/iio:device1
# read x and y
x=$(cat in_accel_x_raw)
y=$(cat in_accel_y_raw)

printf "x: $x \ny: $y \n"