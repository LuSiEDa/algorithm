def solution(str_list, ex):
    for i in range(len(str_list)-1,-1,-1):
        if ex in str_list[i]:
            del str_list[i]
    return "".join(str_list)
