# 
# Reading TMP101 sensors
# Pin Configuration:
# ALERT2 = P9_42, ALERT1 = 41
# SCL = P9_18, SDA = P9_20
# AD1 = P9_12, AD2 = P8_11

temp= 'i2cget -y 1 0x48'
temp2=$ (($temp *2))