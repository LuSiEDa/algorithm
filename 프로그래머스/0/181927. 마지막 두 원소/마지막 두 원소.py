def solution(num_list):
    lastn = num_list[::-1][0]
    lastnn = num_list[::-1][1]
    if lastn > lastnn:
        num_list.append(lastn - lastnn)
        return num_list
    else:
        num_list.append(lastn * 2)
        return num_list