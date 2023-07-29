triBA27_nodes = [
    '111', '112', '113', '121', '122', '123', '131', '132', '133',
    '211', '212', '213', '221', '222', '223', '231', '232', '233',
    '311', '312', '313', '321', '322', '323', '331', '332', '333'
]
triBA27_shortest_path = dict()

def construct_triba_dictionary():
    for src in triBA27_nodes:
        triBA27_shortest_path[src] = dict()
        for dst in triBA27_nodes:
            if src == dst:
                continue
            triBA27_shortest_path[src][dst] = 0

def print_triba_dictionary():
    for src in triBA27_nodes:
        for dst in triBA27_nodes:
            if src == dst:
                continue
            print(f"{src} ==> {dst} = {triBA27_shortest_path[src][dst]}")

def initialize_shortest_path_dictionary(m5_file):
     for line in m5_file:
        tmp_line = line.split()
        src = tmp_line[3]
        dst = tmp_line[5]
        if src == dst:
            continue
        path = []
        index = 7
        while tmp_line[index] != "-":
            path.append(tmp_line[index])
            index += 1
        if triBA27_shortest_path[src][dst] == 0:
            triBA27_shortest_path[src][dst] = len(path) - 1
        elif triBA27_shortest_path[src][dst] > len(path):
            triBA27_shortest_path[src][dst] = len(path) - 1

if __name__ == "__main__":
    m5_file = open("/home/soliman/gem5_dremove/gem5/routing_output.txt")
    construct_triba_dictionary()
    initialize_shortest_path_dictionary(m5_file=m5_file)
    count_all, count_long = 0, 0
    m5_file.seek(0)
    # print_triba_dictionary()
    for line in m5_file:
        tmp_line = line.split()
        src = tmp_line[3]
        dst = tmp_line[5]
        if src == dst:
            continue
        count_all += 1
        path = []
        index = 7
        while tmp_line[index] != "-":
            path.append(tmp_line[index])
            index += 1
        shortest_path = triBA27_shortest_path[src][dst]
        if shortest_path < len(path) - 1:
            print(f"Long {src} ==> {dst} : hops {len(path) - shortest_path - 1}")
            count_long += 1
    print(f"All = {count_all} - long = {count_long} - Perc = {count_long/count_all*100}") 
    m5_file.close()
