def solution(my_string, is_suffix):
    # 무식한 방법:
    # strlist = []
    # for i in range(len(my_string)):
    #     strlist.append(my_string[i:])
    # print(strlist)
    # if is_suffix in strlist: 
    #     return 1
    # else:
    #     return 0 
    return 1 if my_string.endswith(is_suffix) else 0