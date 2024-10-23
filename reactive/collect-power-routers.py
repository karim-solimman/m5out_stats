import re
import sys
import openpyxl
import os

excel_header = [
    '#', 'routing_algorithm', 'synthetic_traffic',
    '111', '112', '113', '121', '122', '123', '131', '132', '133',
    '211', '212', '213', '221', '222', '223', '231', '232', '233',
    '311', '312', '313', '321', '322', '323', '331', '332', '333',
    'total'
]

def get_value(l : str) -> str: 
    tmp_line = re.split(': |\n', l)
    return tmp_line[1]

if __name__ == '__main__':
    print("collect-power-routers.py - starting....")
    
    buffers_power = []
    power_file = open("/home/soliman/gem5_adaptive/soliman_power.txt")
    all_lines = power_file.readlines()
    for index, line in enumerate(all_lines):
        if "Buffer/Dynamic power" in line:
            value = get_value(line)
            buffers_power.append(value)
    print(sys.argv)
    routing_algorithm = sys.argv[1]
    synthetic_traffic = sys.argv[2]

    # Copy data to excel workbook
    # Check if the excel workbook existed or not
    if(os.path.isfile(f"/home/soliman/m5out_stats/reactive/power_routers_{routing_algorithm}.xlsx")):
        print("File existed")
        wb = openpyxl.load_workbook(f"/home/soliman/m5out_stats/reactive/power_routers_{routing_algorithm}.xlsx")
        ws = wb["Sheet"]
    else:
        print("Create file")
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(excel_header)
    
    excel_data = [1, routing_algorithm, synthetic_traffic] + buffers_power
    ws.append(excel_data)
    wb.save(f"/home/soliman/m5out_stats/reactive/power_routers_{routing_algorithm}.xlsx")
    print("Excel file saved...")
    