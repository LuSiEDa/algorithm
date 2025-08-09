def solution(before, after):
    for i in set(before + after):
        if before.count(i) != after.count(i):
            return 0
    return 1