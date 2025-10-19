def solution(my_string, m, c):
    num = []
    for i in range(0, len(my_string), m):
        num.append(my_string[i:i+m])
    result = ""
    for j in num:
        result += j[c-1]
    return result      
