def solution(arr):
    n = len(arr)
    power = 1
    while power < n:
        power *= 2
    zeros_to_add = power - n
    arr += [0] * zeros_to_add
            
    return arr