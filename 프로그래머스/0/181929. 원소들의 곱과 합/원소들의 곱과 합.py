def solution(num_list):
    a = sum(num_list)**2
    b = 1
    for i in num_list:
        b *= i
    if a > b:
        return 1
    else:
        return 0
