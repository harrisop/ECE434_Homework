#!/usr/bin/env python3
# 
#   using pins: P8_11 and P8_12 for the left (eQEP2)
#               P8_33 and P8_35 for the right (eQEP1)
#   need to run setup
#
#

import time

eQEP = '1'
COUNTERPATH = '/sys/bus/counter/devices/counter'+eQEP+'/count0'
COUNTERPATH2 = '/sys/bus/counter/devices/counter2/count0'


ms = 100
maxCount = '1000000'

f = open(COUNTERPATH+'/ceiling', 'w')
f.write(maxCount)
f.close()
f = open(COUNTERPATH2+'/ceiling', 'w')
f.write(maxCount)
f.close()

f = open(COUNTERPATH+'/enable', 'w')
f.write('1')
f.close()
f = open(COUNTERPATH2+'/enable', 'w')
f.write('1')
f.close()

f = open(COUNTERPATH+'/count', 'r')
f2 = open(COUNTERPATH2+'/count', 'r')


olddata = -1
olddata2 = -1
while True:
    f.seek(0)
    f2.seek(0)
    data = f.read()[:-1]
    data2 = f2.read()[:-1]
    if data !=olddata:
        olddata = data
        print("data = " + data)
    if data2 != olddata2:
        olddata2 = data2
        print("data2 = " + data2)
    time.sleep(ms/1000)
    