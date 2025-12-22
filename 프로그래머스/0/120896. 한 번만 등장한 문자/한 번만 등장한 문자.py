def solution(s):
    s = s.lower()
    result = []
    for i in sorted(s):
        if s.count(i) == 1:
            result.append(i)
    return "".join(result)