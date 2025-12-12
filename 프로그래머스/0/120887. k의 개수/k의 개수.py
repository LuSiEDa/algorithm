def solution(i, j, k):
    return sum(str(nn).count(str(k)) for nn in range(i, j+1))