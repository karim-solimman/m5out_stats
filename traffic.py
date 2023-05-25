import openpyxl
import argparse
import os
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Program to collect the output data from gem5 output file and combine it into excel file")
    parser.add_argument("--injectionrate",
                        help="Provide injectionrate", default=0.02)
    parser.add_argument(
        "--synthetic", help="Provide synthetic traffic because the different out format file", default="triba27_uniform_random")
    parser.add_argument(
        "--sim_cycles", help="Provide simulation clock cycles for simulation", default="5000000")
    args = parser.parse_args()

    assert (args.synthetic == "triba27_uniform_random" or args.synthetic ==
            "triba27_bit_reverse" or args.synthetic == "triba27_transpose" or args.synthetic == "triba27_tornado")

    # open Excel file to save the data from m5out stats text file generated from gem5 simulator
    work_book = openpyxl.load_workbook(
        "/home/soliman/m5out_stats/m5out_stats_traffic.xlsx")
    work_sheet = work_book["Sheet1"]

    # data list that will store the output values from gem5 simulator
    # begin the list with the injection rate
    data = [float(args.injectionrate)]
    # append the type of the synthetic traffic that being used
    data.append(args.synthetic)
    data.append(int(args.sim_cycles))

    work_book.save("m5out_stats_traffic.xlsx")
