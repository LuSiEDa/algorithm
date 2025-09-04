def solution(binomial):
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
    }
    bino = binomial.split(" ")
    return ops[bino[1]](int(bino[0]), int(bino[2]))
