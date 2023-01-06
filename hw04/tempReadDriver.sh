# 
# Reading TMP101 sensors uing kernel driver
# Pin Configuration:
# ALERT2 = P9_42, ALERT1 = 41
# SCL = P9_18, SDA = P9_20
# AD1 = P9_12, AD2 = P8_11
#


cd /sys/class/i2c-adapter/i2c-2/2-0048/hwmon/hwmon0
temp1=$(cat temp1_input)

cd /sys/class/i2c-adapter/i2c-2/2-004a/hwmon/hwmon1
temp2=$(cat temp1_input)

temp1m=$(echo "$temp1/1000" |bc)
temp11=$(echo "$temp1m*1.8" |bc)
temp1f=$(echo "$temp11+32" |bc)

temp2m=$(echo "$temp2/1000" |bc)
temp22=$(echo "$temp2m*1.8" |bc)
temp2f=$(echo "$temp22+32" |bc)

printf "Temp1: $temp1f \nTemp2: $temp2f \n"