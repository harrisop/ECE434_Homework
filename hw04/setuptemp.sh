#
# run this to be able to run tempReadDriver.sh
# sets up permissions and the devices
#
cd /sys/class/i2c-adapter/i2c-2/
sudo chown debian:debian *
echo tmp101 0x48 > new_device
echo tmp101 0x4a > new_device