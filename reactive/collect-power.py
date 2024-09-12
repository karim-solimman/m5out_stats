import re

data = {
    "routers_buffer_dynamic" : "",
    "routers_buffet_leakage" : "",
    "routers_crossbar_dynamic": "",
    "routers_crossbar_leakage": "",
    "routers_sw_dynamic": "",
    "routers_sw_leakage": "",
    "routers_clock_dynamic": "",
    "routers_clock_leakage": "",
    "routers_dynamic": "",
    "routers_leakage": "",
    "routers_buffer_area": "",
    "routers_crossbar_area": "",
    "routers_sw_area": "",
    "routers_others" : "",
    "routers_all_area": "",
    "int_links_dynamic" : "",
    "int_links_leakage" : "",
    "ext_links_dynamic" : "",
    "ext_links_leakage" : "",
    "all_links_dynamic" : "",
    "all_links_leakage" : "",
    "all_routers_links_dynamic": "",
    "all_routers_links_leakage": ""
}

def get_value(l : str) -> str: 
    tmp_line = re.split(': |\n', l)
    return tmp_line[1]


if __name__ == "__main__":
    print("Hello from collect-power.py")
    power_file = open("/home/soliman/gem5_adaptive/soliman_power.txt")
    buffers_dynamic_power = []
    all_lines = power_file.readlines()
    for index, line in enumerate(all_lines):
        if "Sum totals for all routers Buffer/Leakage power" in line:
            value = get_value(line)
            print(index, line.split(), value)
            data["routers_buffet_leakage"] = value
        if "Sum totals for all routers Crossbar/Dynamic power:" in line:
            value = get_value(line)
            print(index, line.split(), value)
            data["routers_crossbar_dynamic"] = value
        if "Sum totals for all routers Crossbar/Leakage power:" in line:
            value = get_value(line)
            print(index, line.split(), value)
            data["routers_crossbar_leakage"] = value
        if "Sum totals for all routers Switch allocator/Dynamic power:" in line:
            value = get_value(line)
            print(index, line.split(), value)
            data["routers_sw_dynamic"] = value
        if "Sum totals for all routers Switch allocator/Leakage power:" in line:
            value = get_value(line)
            print(index, line.split(), value)
            data["routers_sw_leakage"] = value
        if "Sum totals for all routers Clock/Dynamic power:" in line:
            value = get_value(line)
            print(index, line.split(), value)
        if "Sum totals for all routers Clock/Leakage power:" in line:
            value = get_value(line)
            print(index, line.split(), value)
        if "Sum totals for all routers Total/Dynamic power:" in line:
            value = get_value(line)
            print(index, line.split(), value)
        if "Sum totals for all routers Total/Leakage power:" in line:
            value = get_value(line)
            print(index, line.split(), value)
        if "Sum totals for all routers Area/Buffer:" in line:
            value = get_value(line)
            print(index, line.split(), value)
        if "Sum totals for all routers Area/Crossbar:" in line:
            value = get_value(line)
            print(index, line.split(), value)
        if "Sum totals for all routers Area/Switch allocator" in line:
            value = get_value(line)
            print(index, line.split(), value)
        if "Sum totals for all routers Area/Other" in line:
            value = get_value(line)
            print(index, line.split(), value)
        if "Sum totals for all routers Area/Total" in line:
            value = get_value(line)
            print(index, line.split(), value)
        if "Buffer/Dynamic power:" in line:
            value = get_value(line)
            buffers_dynamic_power.append(value)
            if len(buffers_dynamic_power) == 28:
                print(index, line.split(), buffers_dynamic_power[-1])
        if "Total power for all int_links:" in line:
            value_dynamic = get_value(all_lines[index+1])
            value_leakage = get_value(all_lines[index+2])
            print(index, line.split(), value_dynamic, value_leakage)
        if "Total power for all ext_links:" in line:
            value_dynamic = get_value(all_lines[index+1])
            value_leakage = get_value(all_lines[index+2])
            print(index, line.split(), value_dynamic, value_leakage)
        if "Total power for all links:" in line:
            value_dynamic = get_value(all_lines[index+1])
            value_leakage = get_value(all_lines[index+2])
            print(index, line.split(), value_dynamic, value_leakage)
        if "Sum power for all routers + links:" in line:
            value_dynamic = get_value(all_lines[index+1])
            value_leakage = get_value(all_lines[index+2])
            print(index, line.split(), value_dynamic, value_leakage)
        
            
        
        