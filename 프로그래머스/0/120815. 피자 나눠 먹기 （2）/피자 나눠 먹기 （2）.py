def solution(n):
    m = 1
    while 6 * m % n !=0:
        m = m + 1
    return m 