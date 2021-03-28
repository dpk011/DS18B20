# -*- coding: utf-8 -*-

"""
Read and display temperatures from multiple DS18B20 sensors
"""

from __future__ import print_function

import os
import glob
import time
import datetime

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices'
device_folders = glob.glob(base_dir + '/28*')
device_files = [folder +  r'/temperature' for folder in device_folders]
# print(device_folders)


def read_temp_raw(device_file):
    f = open(device_file, 'r')
    line = f.readlines()[0]
    f.close()
    return line

def read_temp(device):
    temp_str =  read_temp_raw(device)
    temp_c = float(temp_str)/1000.0
    temp_f = (temp_c * 9.0 / 5.0) + 32.0
    return temp_c, temp_f

i = 0
print("Time", end=",")

for i in range(len(device_files)):
    print("{0}_id,{0}_degC,{0}_F".format(i),end=",")

print()

while True:
    print("{0}".format(datetime.datetime.now().time()), end=",")
    for i in range(len(device_files)):
        temp_c, temp_f = read_temp(device_files[i])
        print("{0},{1:2.3f},{2:2.3f}".format(device_folders[i][-12:], temp_c, temp_f), end=",")

    print()
