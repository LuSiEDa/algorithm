def solution(strArr):
    lengths = [len(s) for s in strArr]
    return max(lengths.count(L) for L in set(lengths))