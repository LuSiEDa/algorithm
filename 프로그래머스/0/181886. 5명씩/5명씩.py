def solution(names):
    ns = [names[i:i+5] for i in range(0,len(names),5)]
    return [fa[0] for fa in ns]
