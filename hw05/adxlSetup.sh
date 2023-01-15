#
# run this to be able to run accelometer code
# sets up permissions and the device
#
cd /sys/class/i2c-adapter/i2c-2/
#sudo chown debian:debian *
echo adxl345 0x53 > new_device
