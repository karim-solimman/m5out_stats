import openpyxl
import os


syn_traffics = ["triba27_uniform_random", "triba27_bit_reverse", "triba27_transpose",
                 "triba27_tornado", "triba27_bit_complement", "triba27_shuffle" ]

def get_routing_info(dir_name):
    tmp_name = dir_name.split('0', 1)
    return tmp_name[0][:-1], float('0' + tmp_name[1])


if __name__ == '__main__':
    print("Start reading data...")
    routing_algorithm = "dm4t"
    directory = f"/home/soliman/m5out_stats/reactive/{routing_algorithm}"
    sim_cycles = 12500000
    files_count = 0
    
    # excel sheet
    # check if exists first, otherwise create a new one for collecting the data from the stats files
    ws_header = ["#", "routing algorithm", "synthetic traffic", "injection rate", "sim cycles",
                  "average_flit_latency", "average_flit_network_latency", "flit_queuing_latency",
                    "average_flit_vnet_latency", "average_hops", "average_packet_latency", "average_packet_network_latency",
                    "average_packet_queueing_latency", "average_packet_vnet_latency", "average_link_utilization",
                    "average_vc_load", "ext_in_link_utilization", "ext_out_link_utilization",
                    "Flits_inject", "Flits_received", "int_link_utilization", "Pkt_inject", "Pkt_received", 
                    "Flits_delivery_perc", "Pkt_delivery_perc", "throughput", "receiption_rate",]
    if(os.path.isfile(f"./{routing_algorithm}.xlsx")):
        print("Excel existed...")
        wb = openpyxl.load_workbook(f"./{routing_algorithm}.xlsx")
        ws = wb.active
    else:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(ws_header)
    
    for index, file in enumerate(os.listdir(directory)):
        synthetic_traffic, injection_rate = get_routing_info(file)
        stats_path = f"{directory}/{file}/stats.txt"
        data = [index + 1, routing_algorithm, synthetic_traffic, injection_rate, sim_cycles / 500]
        print(file, stats_path)
        with open(stats_path) as stats_file:
            for line in stats_file:
                # index 5
                if "average_flit_latency" in line:
                    data.append(float(line.split()[1]) / 500)
                # index 6
                if "average_flit_network_latency" in line:
                    data.append(float(line.split()[1]) / 500)
                # index 7
                if "average_flit_queueing_latency" in line:
                    data.append(float(line.split()[1]) / 500)
                # index 8
                if "average_flit_vnet_latency" in line:
                    indexes = []
                    for i in range(len(line)):
                        if line[i] == '|':
                            indexes.append(i)
                    indexes.append(line.index('('))
                    v1 = line[indexes[0] + 1:indexes[1] - 1]
                    v2 = line[indexes[1] + 1:indexes[2] - 1]
                    v3 = line[indexes[2] + 1:indexes[3] - 1]
                    v1, v2, v3 = v1.strip(), v2.strip(), v3.strip()
                    avg = (float(v1) + float(v2) + float(v3)) / 3.0
                    data.append(avg / 500)
                # index 9
                if "average_packet_latency" in line:
                    data.append(float(line.split()[1]) / 500)
                # index 10
                if "average_packet_network_latency" in line:
                    data.append(float(line.split()[1]) / 500)
                # index 11
                if "average_packet_queueing_latency" in line:
                    data.append(float(line.split()[1]) / 500)
                # index 12
                if "average_packet_vnet_latency" in line:
                    indexes = []
                    for i in range(len(line)):
                        if line[i] == '|':
                            indexes.append(i)
                    indexes.append(line.index('('))
                    v1 = line[indexes[0] + 1:indexes[1] - 1]
                    v2 = line[indexes[1] + 1:indexes[2] - 1]
                    v3 = line[indexes[2] + 1:indexes[3] - 1]
                    v1, v2, v3 = v1.strip(), v2.strip(), v3.strip()
                    avg = (float(v1) + float(v2) + float(v3)) / 3.0
                    data.append(avg / 500)
                # index 13
                if "system.ruby.network.packets_injected::total" in line:
                    data.append(int(line.split()[1]))
                # index 14
                if "system.ruby.network.packets_received::total" in line:
                    data.append(int(line.split()[1]))
                # index 15
                if "system.ruby.network.flits_injected::total" in line:
                    data.append(int(line.split()[1]))
                # index 16
                if "system.ruby.network.flits_received::total" in line:
                    data.append(int(line.split()[1]))
                # index 17
                if "system.ruby.network.ext_in_link_utilization" in line:
                    data.append(int(line.split()[1]))
                # index 18
                if "system.ruby.network.ext_out_link_utilization" in line:
                    data.append(int(line.split()[1]))
                # index 19
                if "system.ruby.network.int_link_utilization" in line:
                    data.append(int(line.split()[1]))
                # index 20
                if "system.ruby.network.average_hops" in line:
                    data.append(float(line.split()[1]))
                # index 21
                if "system.ruby.network.avg_link_utilization" in line:
                    data.append(float(line.split()[1]))
                # index 22
                if "system.ruby.network.avg_vc_load::total" in line:
                    data.append(float(line.split()[1]))
            # print(len(data), data)
            # calculate flits dlivery percentage
            data.append(data[19] / data[18])
            # claculate packets delivery percentage
            data.append(data[22] / data [21])
            # calculate packet throughput flit/cycle/node
            data.append(data[19]/data[4]/27)
            # calculate packet recieption rate packet/node/cycle
            data.append(data[22]/27/data[4])
        print(index + 1, synthetic_traffic, injection_rate, "... Done")
        # store the file count
        files_count = index + 1
        ws.append(data)
    print(files_count, " .. Done saving data")
    wb.save(f"{routing_algorithm}.xlsx")


