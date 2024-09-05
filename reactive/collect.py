import os
import openpyxl

ws_header = ["#", "routing algorithm", "synthetic traffic", "injection rate", "sim cycles",
                  "average_flit_latency", "average_flit_network_latency", "flit_queuing_latency",
                    "average_flit_vnet_latency", "average_hops", "average_packet_latency", "average_packet_network_latency",
                    "average_packet_queueing_latency", "average_packet_vnet_latency", "average_link_utilization",
                    "average_vc_load", "ext_in_link_utilization", "ext_out_link_utilization",
                    "Flits_inject", "Flits_received", "int_link_utilization", "Pkt_inject", "Pkt_received", 
                    "Flits_delivery_perc", "Pkt_delivery_perc", "throughput", "receiption_rate",]


syn_traffics = ["triba27_uniform_random", "triba27_bit_reverse", "triba27_transpose",
                 "triba27_tornado", "triba27_bit_complement", "triba27_shuffle"]


if __name__ == '__main__':
    print("Reading XLSX files...")

    # data extraction
    extension = '.xlsx'
    extracted_data = "average_packet_latency"
    
    # select xlsx files [not throughput files]
    all_files = os.listdir("./")
    xlsx_files = []
    for file in all_files:
        if file.endswith(extension) and not "throughput" in file:
            xlsx_files.append(file)
    xlsx_files.sort()

    # the output xlsx file
    if(os.path.isfile(f"./{extracted_data}.xlsx")):
        print("Excel existed...")
        wb = openpyxl.load_workbook(f"./{extracted_data}.xlsx")
        ws = wb.active
    else:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(ws_header)
    
    for file in xlsx_files:
        routing_algorithm = file.split('.')[0]
        tmp_wb = openpyxl.load_workbook(file)
        tmp_wc = tmp_wb['Sheet']
        print(file, tmp_wc.cell(row=2,column=5).value)
        tmp_wb.close()