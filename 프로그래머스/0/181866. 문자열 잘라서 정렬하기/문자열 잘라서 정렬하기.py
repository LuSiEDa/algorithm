def solution(myString):
    parts = [s for s in myString.split("x") if s]
    return sorted(parts)