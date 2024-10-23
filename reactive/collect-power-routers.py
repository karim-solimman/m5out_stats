import re
import sys
import openpyxl
import os

def get_value(l : str) -> str: 
    tmp_line = re.split(': |\n', l)
    return tmp_line[1]

if __name__ == '__main__':
    print("collect-power-routers.py - starting....")
    power_file = open("/home/soliman/gem5_adaptive/soliman_power.txt")
    buffers_dynamic_power = []
    all_lines = power_file.readlines()
    for index, line in enumerate(all_lines):
        if "Buffer/Dynamic power" in line:
            value = get_value(line)
            print(value)
   