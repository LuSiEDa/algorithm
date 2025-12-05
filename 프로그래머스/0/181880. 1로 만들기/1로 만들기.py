def solution(num_list):
    numb = 0
    for i in num_list:
        while i != 1:
            if i % 2 == 0:
                numb += 1
                i = i / 2
            else:
                numb += 1
                i = (i-1) / 2
    return numb