def solution(arr, flag):
    x = []
    for i in range(len(flag)):
        if flag[i] == True:
            x.extend([arr[i]] * (arr[i] * 2))
        else:
            x = x[:-arr[i]]
    return x
