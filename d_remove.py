if __name__ == "__main__":
    m5_file = open("/home/soliman/gem5_dremove/gem5/routing_output.txt")
    count = 0
    count_lines = 0
    for line in m5_file:
        count_lines += 1
        tmp_line = line.split()
        src = tmp_line[3]
        dst = tmp_line[5]
        path = []
        if src != dst:
            count += 1
            index = 7
            while tmp_line[index] != "-":
                path.append(tmp_line[index])
                index += 1
            
    m5_file.close()
    print(f"Count = {count} - count_lines = {count_lines} == {count/count_lines*100}")