# 
# Reading TMP101 sensors
# Pin Configuration:
# ALERT2 = P9_42, ALERT1 = 41
# SCL = P9_18, SDA = P9_20
# AD1 = P9_12, AD2 = P8_11
#

const=(2)

temp1=$(i2cget -y 2 0x48 0)
temp11=$(($temp1*$const))
temp1f=$(($temp11+32))

temp2=$(i2cget -y 2 0x4a 0)
temp22=$(($temp2*$const))
temp2f=$(($temp22+32))

printf "Temp1: $temp1f \nTemp2: $temp2f \n"