import os
import openpyxl

ws_header = ["#", "routing algorithm", "sim cycles", "sim time"
                  "average_flit_latency", "average_flit_network_latency", "flit_queuing_latency",
                    "average_flit_vnet_latency", "average_hops", "average_packet_latency", "average_packet_network_latency",
                    "average_packet_queueing_latency", "average_packet_vnet_latency", "average_link_utilization",
                    "average_vc_load", "ext_in_link_utilization", "ext_out_link_utilization",
                    "Flits_inject", "Flits_received", "int_link_utilization", "Pkt_inject", "Pkt_received", 
                    "Flits_delivery_perc", "Pkt_delivery_perc", "throughput", "receiption_rate",]

if __name__ == '__main__':
    print("Starting...")


    # data extraction
    extension = '.xlsx'
    benchmark = "blackscholes"
    benchmark_directory = f"_full-system-{benchmark}"

    print(f"Benchmark | {benchmark}")

    print("Creating xlsx workbook...")
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(ws_header)

    for file_index, file in enumerate(os.listdir(benchmark_directory)):
        extracted_data = []
        stats_file = f"{benchmark_directory}/{file}/stats.txt"
        print(file_index + 1, file, stats_file)

        with open(stats_file) as f:
            # index
            extracted_data.append(file_index + 1)
            # routing algorithm
            extracted_data.append(file)

            for line_index, line in enumerate(f):
                # print(line_index, line)
                # sim cycles
                if "simTicks" in line:
                    extracted_data.append(int(line.split()[1]) )
                # sim time
                if "hostSeconds" in line:
                    extracted_data.append(float(line.split()[1]))
                # average flit latency - index 4
                if "average_flit_latency" in line:
                    extracted_data.append(float(line.split()[1]) / 500)
                # average flit network latency - index 5
                if "average_flit_network_latency" in line:
                    extracted_data.append(float(line.split()[1]) / 500)
                # average flit queueing latency - index 6
                if "average_flit_queueing_latency" in line:
                    extracted_data.append(float(line.split()[1]) / 500)
                # average flit vnet latency - index 7
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
                    extracted_data.append(avg / 500)
                # average packet latency - index 8
                if "average_packet_latency" in line:
                    extracted_data.append(float(line.split()[1]) / 500)
                # average packet network latency - index 9
                if "average_packet_network_latency" in line:
                    extracted_data.append(float(line.split()[1]) / 500)
                # average packet queuing latency - index 10
                if "average_packet_queueing_latency" in line:
                    extracted_data.append(float(line.split()[1]) / 500)
                # average packet vnet latency - index 11
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
                    extracted_data.append(avg / 500)
                # packets injected - index 12
                if "system.ruby.network.packets_injected::total" in line:
                    extracted_data.append(int(line.split()[1]))
                # packets received - index 13
                if "system.ruby.network.packets_received::total" in line:
                    extracted_data.append(int(line.split()[1]))
                # flits injected - index 14
                if "system.ruby.network.flits_injected::total" in line:
                    extracted_data.append(int(line.split()[1]))
                # flits received - index 15
                if "system.ruby.network.flits_received::total" in line:
                    extracted_data.append(int(line.split()[1]))
                # ext in link utilization - index 16
                if "system.ruby.network.ext_in_link_utilization" in line:
                    extracted_data.append(int(line.split()[1]))
                # ext out link utilization - index 17
                if "system.ruby.network.ext_out_link_utilization" in line:
                    extracted_data.append(int(line.split()[1]))
                # int link utilization - index 18
                if "system.ruby.network.int_link_utilization" in line:
                    extracted_data.append(int(line.split()[1]))
                # average hops - index 19
                if "system.ruby.network.average_hops" in line:
                    extracted_data.append(float(line.split()[1]))
                # average link utilization - index 20
                if "system.ruby.network.avg_link_utilization" in line:
                    extracted_data.append(float(line.split()[1]))
                # average vc load - index 21
                if "system.ruby.network.avg_vc_load::total" in line:
                    extracted_data.append(float(line.split()[1]))
                
            # flits delivery percentage
            extracted_data.append(extracted_data[15] / extracted_data[14])
            # packets delivery percentage
            extracted_data.append(extracted_data[13] / extracted_data [12])
            # throughput flit/cycle/node
            extracted_data.append(extracted_data[15]/extracted_data[2]/27)
            # receiption rate packet/node/cycle
            extracted_data.append(extracted_data[13]/27/extracted_data[2])

            ws.append(extracted_data)

    wb.save(f"_full-system-{benchmark}.xlsx")
    print("Generate sucessfully...")