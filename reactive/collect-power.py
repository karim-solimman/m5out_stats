import re

def get_value(l : str) -> str: 
    tmp_line = re.split(': |\n', l)
    return tmp_line[1]


if __name__ == "__main__":
    print("Hello from collect-power.py")
    power_file = open("/home/soliman/gem5_adaptive/soliman_power.txt")
    for line in power_file:
        if "Sum totals for all routers Buffer/Leakage power" in line:
            value = get_value(line)
            print(line, value)
        if "Sum totals for all routers Crossbar/Dynamic power:" in line:
            value = get_value(line)
            print(line, value)
        if "Sum totals for all routers Crossbar/Dynamic power:" in line:
            value = get_value(line)
            print(line, value)
        if "Sum totals for all routers Crossbar/Leakage power:" in line:
            value = get_value(line)
            print(line, value)
        if "Sum totals for all routers Switch allocator/Dynamic power:" in line:
            value = get_value(line)
            print(line, value)
        if "Sum totals for all routers Switch allocator/Leakage power:" in line:
            value = get_value(line)
            print(line, value)
        if "Sum totals for all routers Clock/Dynamic power:" in line:
            value = get_value(line)
            print(line, value)
        if "Sum totals for all routers Clock/Leakage power:" in line:
            value = get_value(line)
            print(line, value)
        if "Sum totals for all routers Total/Dynamic power:" in line:
            value = get_value(line)
            print(line, value)
            
        