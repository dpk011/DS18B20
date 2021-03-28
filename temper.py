"""
Read temperature from one DS18B20 temperature sensor and display 
"""


import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices'
device_folder = glob.glob(base_dir + '/28*')[0]
device_file = device_folder +  r'/temperature'
print device_file


def read_temp_raw():
    f = open(device_file, 'r')
    line = f.readlines()[0]
    f.close()
    return line

def read_temp():
#    lines = read_temp_raw()
    temp_str =  read_temp_raw()
    temp_c = float(temp_str)/1000.0
    temp_f = (temp_c * 9.0 / 5.0) + 32.0
    return temp_c, temp_f

i = 0
while True:
    temp_c, temp_f = read_temp();
    i = i + 1
    print  '{2} Tempearture: {0:2.3f} degC  or  {1:2.3f} F'.format(temp_c, temp_f, i)
    time.sleep(1)
