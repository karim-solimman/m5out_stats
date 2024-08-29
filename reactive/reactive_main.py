import openpyxl
import os

syn_traffics = ["triba27_uniform_random", "triba27_bit_reverse", "triba27_transpose",
                 "triba27_tornado", "triba27_bit_complement", "triba27_shuffle" ]

def get_routing_info(dir_name):
    tmp_name = dir_name.split('0', 1)
    return tmp_name[0][:-1], '0' + tmp_name[1]


if __name__ == '__main__':
    print("Start reading data...")
    directory = "/home/soliman/m5out_stats/reactive/ddra"
    routing_algorithm = "ddra"
    sim_cycles = 25000
    
    # create the excel sheet for collecting the data from the stats files
    wb = openpyxl.Workbook()
    ws = wb.active
    ws_header = ["#", "routing algorithm", "synthetic traffic", "injection rate", "sim cycles",
                  "average_flit_latency", "average_flit_network_latency", "flit_queuing_latency",
                    "average_flit_vnet_latency", "average_packet_latency", "average_packet_network_latency",
                    "average_packet_queueing_latency", "average_packet_vnet_latency", "Flits_inject",
                    "Flits_received", "Pkt_inject", "Pkt_received", "Flits_delivery_perc", "Pkt_delivery_perc",
                    "throughput", "receiption_rate", "ext_in_link_utilization", "ext_out_link_utilization",
                    "int_link_utilization", "average_hops", "average_link_utilization", "average_vc_load"]
    ws.append(ws_header)
   
    for index, file in enumerate(os.listdir(directory)):
        synthetic_traffic, injection_rate = get_routing_info(file)
        stats_path = f"{directory}/{file}/stats.txt"
        data = [index + 1, routing_algorithm, synthetic_traffic, injection_rate, sim_cycles]
        with open(stats_path) as stats_file:
            for line in stats_file:
                if "average_flit_latency" in line:
                    data.append(float(line.split()[1]))
                if "average_flit_network_latency" in line:
                    data.append(float(line.split()[1]))
                if "average_flit_queueing_latency" in line:
                    data.append(float(line.split()[1]))
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
                    print(v1, v2, v3)
                    avg = (float(v1) + float(v2) + float(v3)) / 3.0
                    data.append(avg)
                if "average_packet_latency" in line:
                    print(line.split())
                    data.append(float(line.split()[1]))
                if "average_packet_network_latency" in line:
                    print(line.split())
                    data.append(float(line.split()[1]))
                if "average_packet_queueing_latency" in line:
                    print(line.split())
                    data.append(float(line.split()[1]))
                if "average_packet_vnet_latency" in line:
                    print(line.split())
                    indexes = []
                    for i in range(len(line)):
                        if line[i] == '|':
                            indexes.append(i)
                    indexes.append(line.index('('))
                    v1 = line[indexes[0] + 1:indexes[1] - 1]
                    v2 = line[indexes[1] + 1:indexes[2] - 1]
                    v3 = line[indexes[2] + 1:indexes[3] - 1]
                    v1, v2, v3 = v1.strip(), v2.strip(), v3.strip()
                    print(v1, v2, v3)
                    avg = (float(v1) + float(v2) + float(v3)) / 3.0
                    data.append(avg)
                if "system.ruby.network.packets_injected::total" in line:
                    print(line.split())
                    data.append(float(line.split()[1]))
                if "system.ruby.network.packets_received::total" in line:
                    print(line.split())
                    data.append(float(line.split()[1]))
                if "system.ruby.network.flits_injected::total" in line:
                    print(line.split())
                    data.append(float(line.split()[1]))
                if "system.ruby.network.flits_received::total" in line:
                    print(line.split())
                    data.append(float(line.split()[1]))
        print(index, synthetic_traffic, injection_rate, "Done")
    
    print(len(next(os.walk(directory))[1]), "Done saving data")
    wb.save(f"{routing_algorithm}.xlsx")


