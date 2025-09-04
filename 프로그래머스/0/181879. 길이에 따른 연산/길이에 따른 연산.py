def solution(num_list):
    result = 1
    if len(num_list) > 10:
        return sum(num_list)
    else:
        for i in num_list:
            result *= i
        return result