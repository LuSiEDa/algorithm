def solution(order):
    num = 0
    for i in str(order):
        if i in ["3","6","9"]:
            num += 1
    return num