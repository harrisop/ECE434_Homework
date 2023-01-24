# 
#   Reads the temperatures from the three 1 wire 
#   temperature sensors. 
#   Data pins for the sensors are on P9_14
#

cd /sys/class/hwmon/hwmon0
temp1=$(cat temp1_input)

cd /sys/class/hwmon/hwmon1
temp2=$(cat temp1_input)

cd /sys/class/hwmon/hwmon2
temp3=$(cat temp1_input)

temp1m=$(echo "$temp1/1000" |bc)
temp11=$(echo "$temp1m*1.8" |bc)
temp1f=$(echo "$temp11+32" |bc)

temp2m=$(echo "$temp2/1000" |bc)
temp22=$(echo "$temp2m*1.8" |bc)
temp2f=$(echo "$temp22+32" |bc)

temp3m=$(echo "$temp3/1000" |bc)
temp33=$(echo "$temp3m*1.8" |bc)
temp3f=$(echo "$temp33+32" |bc)

printf "Temp1: $temp1f \nTemp2: $temp2f \nTemp3: $temp3f\n"