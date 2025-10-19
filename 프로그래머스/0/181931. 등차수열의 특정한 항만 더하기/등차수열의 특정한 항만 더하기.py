def solution(a, d, included):
    numsum = 0
    for i in range(len(included)):
        if included[i]:
            numsum += a
        a += d
    return numsum
