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

    for index, file in enumerate(os.listdir(benchmark_directory)):
        extracted_data = []
        stats_file = f"{benchmark_directory}/{file}/stats.txt"
        print(index + 1, file, stats_file)

        with open(stats_file) as f:
            # index
            extracted_data.append(index + 1)
            # routing algorithm
            extracted_data.append(file)
            for index, line in enumerate(f):
                #sim cycles
                if "simTicks" in line:
                    extracted_data.append(int(line.split()[1]) / 500)
                    print(f"simCycles {int(line.split()[1]) / 500}")
                # sim time
                # average flit latency
                # average flit network latency
                # average flit queueing latency
                # average flit vnet latency
                # average hops
                # average packet latency
                # average packet network latency
                # average packet queuing latency
                # average packet vnet latency
                # average link utilization
                # average vc load
                # ext in link utilization
                # ext out link utilization
                # flits injected
                # flits received
                # int link utilization
                # packets injected
                # packets received
                # flits delivery percentage
                # packets delivery percentage
                # throughput
                # receiption rate
        
    # wb.save("Test.xlsx")

    print("Generate sucessfully...")