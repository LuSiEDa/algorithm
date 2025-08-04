def solution(num_list):
    return [sum(n % 2 ==0 for n in num_list), sum(n % 2 == 1 for n in num_list)]

