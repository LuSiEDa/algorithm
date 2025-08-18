def solution(n, k):
    numlist = []
    for i in range(n+1):
        if i > 0 and i % k == 0:
            numlist.append(i)
    return numlist