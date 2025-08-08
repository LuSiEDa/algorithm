def solution(my_string):
    숫자 = []
    for i in my_string:
        if i in ["0","1","2","3","4","5","6","7","8","9"]:
            숫자 += i
            숫자 = list(map(int,숫자))
    return sorted(숫자)