def solution(n, control):
    move = {'w':1, 's':-1, "d":10, "a":-10}
    return n + sum(move[i] for i in control)
