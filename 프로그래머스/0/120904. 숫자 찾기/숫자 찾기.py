def solution(num, k):
    for i, j in enumerate(str(num)):
        if int(j) == k:
            return i + 1
    return -1

