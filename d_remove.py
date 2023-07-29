triBA27_nodes = [
    '111', '112', '113', '121', '122', '123', '131', '132', '133',
    '211', '212', '213', '221', '222', '223', '231', '232', '233',
    '311', '312', '313', '321', '322', '323', '331', '332', '333'
]
triBA27_shortest_path = {
    '111':0, '112':0, '113':0, '121':0, '122':0, '123':0, '131':0, '132':0, '133':0,
    '211':0, '212':0, '213':0, '221':0, '222':0, '223':0, '231':0, '232':0, '233':0,
    '311':0, '312':0, '313':0, '321':0, '322':0, '323':0, '331':0, '332':0, '333':0
}

if __name__ == "__main__":
    m5_file = open("/home/soliman/gem5_dremove/gem5/routing_output.txt")
    for src in triBA27_nodes:
        for dst in triBA27_nodes:
            if src == dst:
                continue
            for line in m5_file:
                path = []
                tmp_line = line.split()
                tmp_src = tmp_line[3]
                tmp_dst = tmp_line[5]
                if tmp_src == src and tmp_dst == dst:
                    index = 7
                    while tmp_line[index] != "-":
                        path.append(tmp_line[index])
                        index += 1
                    if triBA27_shortest_path[]
    m5_file.close()
    # print(f"Count = {count} - count_lines = {count_lines} == {count/count_lines*100}")