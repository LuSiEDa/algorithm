def solution(n):
    answer = 0
    for i in range(2, n+1):
        countn = 0
        for j in range(2, i+1):
            if i % j == 0:
                countn += 1
        if countn >=2:
            answer += 1
    return answer
