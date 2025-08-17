def solution(start_num, end_num):
    numli = []
    for i in range(start_num,end_num-1, -1):
        if i < end_num:
            break
        numli.append(i)
    return numli